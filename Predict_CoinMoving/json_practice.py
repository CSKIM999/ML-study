import json
import requests
import urllib.request



def get_coin_data_url(coinName, type, scale, cnt=400) :
    addr = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/'
    if type == 'minutes' :
        basic_url = addr + type + '/' + scale + '?code=CRIX.UPBIT.KRW-' + coinName +'&count='+str(cnt)
    else :
        basic_url = addr + type + '/' + '?code=CRIX.UPBIT.KRW-' + coinName +'&count='+str(cnt)

    return basic_url

# 수정 변수들
coinName = "XRP"
to_date = '2021-05-09'
num = 30
scale = '1'

# get_coin_data_url(coinName,type,scale)

addr = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/30/?code=CRIX.UPBIT.KRW-SSX&count='+str(400)


respone = requests.get(addr)

data = respone.json()
# print(data)
for i in range(len(data)):
    # dateKst = data[i]['candleDateTime']
    print("%.2f"%data[i]['openingPrice'])
    # print(dateKst)
    




# def get_upbit_data(url, last_date, to_date) :
#     global show_title
#     global index
    
#     fail2GetData = False
#     failCnt = 0
#     response = ''
#     while True:
#         try :
#             response = requests.get(url)
#         except Exception as e:
#             print(e)
#             time.sleep(20)
#             continue
#         if str(response) == '<Response [200]>':
#             break
#         time.sleep(10)
#     if ( fail2GetData )  :
#         print("Fail to access url")
#         exit()

#     data = response.json()

#     code = data[0]['code']
#     date = ''
#     dateKst = ''

#     for i in range(len(data))  :
#         dateKst = data[i]['candleDateTimeKst']
#         date = data[i]['candleDateTime']
#         if (last_date == '' or last_date > date) :
#             if (dateKst >= to_date) :
#                 simpleDate = dateKst.split('+')
#                 print(simpleDate[0], "%6d"%data[i]['openingPrice'], "%6d"%data[i]['highPrice'], "%6d"%data[i]['lowPrice'], "%6d"%data[i]['tradePrice'], "%9d"%(data[i]['candleAccTradeVolume']));
#                 datas = (simpleDate[0], "%6f"%data[i]['openingPrice'], "%6f"%data[i]['highPrice'], "%6f"%data[i]['lowPrice'], "%6f"%data[i]['tradePrice'], "%9f"%(data[i]['candleAccTradeVolume']))
#                 for seq, name in enumerate(datas):
#                     sheet.cell(row=index, column=seq+1, value=name)

#             else :
#                 break
#         index+=1
#         # print('still working...')

#     return date