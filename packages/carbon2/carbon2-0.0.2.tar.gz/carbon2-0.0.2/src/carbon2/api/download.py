import requests
import json
from quick_crawler.page import quick_html_page,quick_html_object,quick_download_file,quick_save_csv
from quick_crawler.browser import get_html_str_with_browser
import os

def download_data_from_server(server_url,page_count,save_rawdata_folder,save_csv_path):
    api_url = f"{server_url}/api/Data"
    list_model = []
    fields = []
    for page_index in range(1,page_count+1):# page count
        parameters = {
            "PageIndex": page_index,
            "PageSize": 100
        }
        r = requests.get(api_url, params=parameters)
        page = json.loads(r.text)
        # print(page)
        print("page index = ",page_index)
        # print("PageCount:", page["PageCount"])

        for row in page["DataTable"]:
            # print(row)
            if len(fields) == 0:
                fields = row.keys()
                print(fields)
            file_id = row["FileId"]
            download_fulltext_url = f"{server_url}/WebData/{file_id}.txt"
            save_path = f"{save_rawdata_folder}/{file_id}.txt"
            if not os.path.exists(save_path):
                try:
                    quick_download_file(download_fulltext_url, save_file_path=save_path)
                except:
                    print("error in downloading file", download_fulltext_url)
            list_model.append(row)
    quick_save_csv(save_csv_path, field_names=fields, list_rows=list_model)
