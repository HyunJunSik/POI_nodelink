import pandas as pd
import numpy as np
import requests

url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
headers = {"Authorization": "KakaoAK 6112824f8f41680057cfcd60efff8c98"} 
df = pd.DataFrame()

lat = np.linspace(37.422324, 37.706201, 190)
lon = np.linspace(126.763382, 127.185751, 170)
for i in lat:
    for j in lon:
        for k in range(3):
            params = {'query' : '학교', 'page' : k + 1, 'x' : j , 'y' : i, 'radius' : 300, 'category_group_code' : 'SC4'} 
            total = requests.get(url, params=params, headers=headers).json()['documents']
            for l in range(len(total)):
                if "서울" not in total[l]['place_name']:
                    continue 
                df = df.append(pd.DataFrame(total[l], index=[0]), ignore_index=True)
            print('finish in school')
            params = {'query' : '학원', 'page' : k + 1, 'x' : j , 'y' : i, 'radius' : 300, 'category_group_code' : 'AC5'} 
            total = requests.get(url, params=params, headers=headers).json()['documents']
            for l in range(len(total)):
                if "서울" not in total[l]['place_name']:
                    continue 
                df = df.append(pd.DataFrame(total[l], index=[0]), ignore_index=True)
            # print('finish in academy')
            # params = {'query' : '관광명소', 'page' : k + 1, 'x' : j , 'y' : i, 'radius' : 150, 'category_group_code' : 'AT4'} 
            # total = requests.get(url, params=params, headers=headers).json()['documents']
            # for l in range(len(total)):
            #     if "서울" not in total[l]['place_name']:
            #         continue 
            #     df = df.append(pd.DataFrame(total[l], index=[0]), ignore_index=True)
            # print('finish in tourist')
            # params = {'query' : '카페', 'page' : k + 1, 'x' : j , 'y' : i, 'radius' : 150, 'category_group_code' : 'CE7'} 
            # total = requests.get(url, params=params, headers=headers).json()['documents']
            # for l in range(len(total)):
            #     if "서울" not in total[l]['place_name']:
            #         continue 
            #     df = df.append(pd.DataFrame(total[l], index=[0]), ignore_index=True)
            # print('finish in cafe')
            params = {'query' : '공공기관', 'page' : k + 1, 'x' : j , 'y' : i, 'radius' : 300, 'category_group_code' : 'PO3'} 
            total = requests.get(url, params=params, headers=headers).json()['documents']
            for l in range(len(total)):
                if "서울" not in total[l]['place_name']:
                    continue 
                df = df.append(pd.DataFrame(total[l], index=[0]), ignore_index=True)
            print('finish in public')
        print('finished', i, j)
                


df.drop_duplicates(['place_name'], inplace=True, ignore_index=True)
df = df[['place_name','category_group_name', 'x', 'y']]
df['x'] = df['x'].astype(float)
df['y'] = df['y'].astype(float)
df.sort_values('category_group_name', inplace=True)
df.rename(columns={'category_group_name' : 'category'}, inplace=True)
df.rename(columns={'place_name' : 'place'}, inplace=True)
df.to_csv('school.csv', index=False, encoding='utf-8-sig')

