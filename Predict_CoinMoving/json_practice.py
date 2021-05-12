import json
import requests
import urllib.request
import time
import pandas as pd

df = pd.DataFrame()
index = 2
last_date = ''

def get_coin_data_url(coinName, type, scale, cnt=400) :
    addr = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/'
    if type == 'minutes' :
        basic_url = addr + type + '/' + scale + '?code=CRIX.UPBIT.KRW-' + coinName +'&count='+str(cnt)
    else :
        basic_url = addr + type + '/' + '?code=CRIX.UPBIT.KRW-' + coinName +'&count='+str(cnt)

    return basic_url

# 수정 변수들
coinName = "XRP"
to_date = '2021-05-01'
num = 30
scale = '1'
if num == 0:
    type = 'days'
else:
    type = 'minutes/{}'.format(num)

basic_url = get_coin_data_url(coinName,type,scale)
url = basic_url

# get_coin_data_url(coinName,type,scale)

# respone = requests.get(url)

# data = respone.json()
# print(data)

    
# df_for = pd.DataFrame(data)
# df.append(df_for,ignore_index=True)
# print(data[0])


def get_upbit_data(url, last_date, to_date) :
    global df

    fail2GetData = False
    response = ''
    while True:
        try :
            response = requests.get(url)
        except Exception as e:
            print(e)
            time.sleep(20)
            continue
        if str(response) == '<Response [200]>':
            break
        time.sleep(10)
    if ( fail2GetData )  :
        print("Fail to access url")
        exit()

    data = response.json()
    df_for = pd.DataFrame(data)
    df.append(df_for,ignore_index=True)
    date = ''
    # print(data[0]['candleDateTime'])
    date = data[len(data)-1]['candleDateTime']
    print('Doing well...')

    return date


while (1) :
    last_date = get_upbit_data(url, last_date, to_date)
    tmp1 = last_date.split('T')
    if tmp1[0]  < to_date :
        break
    tmp2 = tmp1[1].split('+')
    target_date = tmp1[0] + ' ' + tmp2[0]
    url = basic_url + '&to=' + target_date    #to=2019-11-27 04:01:00
    time.sleep(2)


print(df)