import hashlib
from quick_crawler.browser import *
import uuid
from carbon2.api.submit import Carbon2Api
from tqdm import tqdm

def get_page_meta(html_str):
    try:
        soup = BeautifulSoup(html_str, features="lxml")

        keywords=""
        description=""

        title = soup.title.string
        print('title = ', title)

        # print(soup.attrs)
        html=soup.find("html")
        if "lang" in html.attrs.keys():
            lang = html["lang"]
        else:
            lang = ""
        print("lang = ",lang)

        meta = soup.find_all('meta')
        # print(html_str)
        for tag in meta:
            if 'name' in tag.attrs.keys():
                name=tag.attrs['name'].strip().lower()
                if name=="description":
                    if 'content' in tag.attrs.keys():
                        description=tag.attrs['content']
                    else:
                        description=""
                if name=="keywords":
                    keywords=tag.attrs['content']
        model = {
            "title":title.replace("\n",""),
            "lang":lang,
            "keywords":keywords.replace("\n",""),
            "description":description.replace("\n","")
        }
    except:
        model = {
            "title": "",
            "lang": "",
            "keywords": "",
            "description":""
        }
    return model

def upload_to_server(server_url,user_id,target_url,driver_path="",save_folder="html_data",use_md5url_as_id=False,tag="",language=""):
    # carbon2system's url
    root_url = f"{server_url}/api"
    c2api = Carbon2Api(root_url)

    # the page url that you want to upload
    # target_url="http://xinhuanet.com/"

    # 1. Generate an unique ID
    page_id=""
    if use_md5url_as_id:
        unique_id=hashlib.md5(target_url.encode())
        page_id=str(unique_id.hexdigest())
    else:
        unique_id = uuid.uuid4()
        page_id=str(unique_id)
    print(page_id)

    # check if exists
    if c2api.exists_url(target_url)==1:
        print("Url exists! ",target_url)
        return

    # 2. quick obtain an HTML page
    if driver_path=="":
        html_str=quick_html_page(target_url)
    else:
        html_str=get_html_str_with_browser(url=target_url,driver_path=driver_path,slient=True)
    f_out=open(f"{save_folder}/{page_id}.txt","w",encoding="utf-8")
    f_out.write(html_str)
    f_out.close()

    # 2.1 get meta info
    meta_model = get_page_meta(html_str)

    # 3. submit the meta data

    r=c2api.submit_metadata(target_url,meta_model["title"],user_id,keywords=meta_model["keywords"],description=meta_model["description"], file_id=page_id,tag=tag,language=language)
    print("r=",r)
    if r==1:
        # 4. submit the file with same unique id
        r=c2api.submit_file(f"{save_folder}/{page_id}.txt")

        # 5. Verify if upload success
        download_url=f"{server_url}/WebData/{page_id}.txt"
        if check_url_ok(download_url):
            print("upload successfully")
    else:
        print("insert error: the url may be repeated!")

# the csv file must contain fields real_url, title.
def submit_page_list(server_url, user_id,csv_file,save_folder, use_md5url_as_id=False, driver_path="browsers/chromedriver.exe",tag="",language=""):
    list_model = quick_read_csv_model(csv_file, encoding='utf-8')
    for model in tqdm(list_model):
        url = model["real_url"]
        try:
            upload_to_server(server_url,user_id, url,use_md5url_as_id=use_md5url_as_id, driver_path=driver_path,tag=tag,language=language)
        except:
            print("Error in calling API!")

def submit_url_list(server_url, user_id,list_url,use_md5url_as_id=False, driver_path="browsers/chromedriver.exe",tag="",language=""):
    for url in tqdm(list_url):
        try:
            upload_to_server(server_url,user_id, url,use_md5url_as_id=use_md5url_as_id, driver_path=driver_path,tag=tag,language=language)
        except:
            print("Error in calling API!")

