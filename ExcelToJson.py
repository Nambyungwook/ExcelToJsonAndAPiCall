import xlrd
from collections import OrderedDict
import json
import requests

excel_file_path = '엑셀파일 위치'

wb = xlrd.open_workbook(excel_file_path)
sh = wb.sheet_by_index(0)

data_list = []

for rownum in range(1, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    data['siteName'] = row_values[0]
    data['targetMain'] = row_values[1]
    data['targetDetail'] = row_values[2]
    data['local'] = row_values[3]
    data['income'] = row_values[4]
    data['age'] = row_values[5]
    data['gender'] = row_values[6]
    data['siteUrl'] = row_values[7]
    data['siteDetail'] = row_values[8]

    data_list.append(data)


j = json.dumps(data_list, ensure_ascii=False)

with open('data.json', 'w+') as f:
    f.write(j)

json_file_path = './data.json'

json_data = None

with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)

for i in range(0, len(json_data)):
    url = 'apiurl'
    site = json_data[i]
    response = requests.post(url, json=site)