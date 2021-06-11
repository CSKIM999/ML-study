import json
import requests
import urllib.request
import time
import pandas as pd

df = pd.DataFrame()
index = 0
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
# # print(data)

    
# df_for = pd.DataFrame(data)
# df.append(df_for,ignore_index=True)
# print(df.head(5))


def get_upbit_data(url, last_date, to_date) :
    global df
    global index

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

    if index == 0:
        print('plan a')
        df = pd.DataFrame(data)
        date = ''
        date = data[len(data)-1]['candleDateTime']
        index +=1
        print(df)
        print('='*100)
        print('='*100)

    else:
        print('plan b')
        df_for = pd.DataFrame(data)
        print(df_for)
        df = df.append(df_for,ignore_index=True)
        date = ''
        # print(data[0]['candleDateTime'])
        date = data[len(data)-1]['candleDateTime']
        print('Doing well...')
        print('='*100)
        print('='*100)



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


############# PANDAS FRAMEWORK ############

idx_todate = df.index[(df.candleDateTimeKst == '{}T00:00:00+09:00'.format(to_date))].tolist()[0]+1
df = df.drop(df.index[idx_todate:])

print(df)

'''
필요 보조지표 수식
RSI :   전일보다 상승한 날의 상승분 U  // 하락장의 하락분 D
        U 값과 D 값의 평균값을 구해서 AU 와 AD 로 구분 후 AU/ AD = RS
        RSI = RS / (1 + RS)  [[ 이 값은 백분율로 나타나진다 ]]
        일반적으로 14, 15 , 25, 9 일의 기간 사용

CCI :   M = 전일의 ( 고가 + 저가 + 종가 ) / 3
        SM = M 의 n일 합계 / n
        D = ( M - SM ) 의 N 일 합계 / N
        CCI = ( M - SM ) / (0.015 * D)
        일반적으로 N 은 20 사용



MACD:   종가를 이용한 장/단기 지수이동평균 계산
        권장 장/단기 변수 26/12
        신호선의 N 값 9
        MACD = 단기 지수이동평균 - 장기지수이동평균
        MACD 신호선 = N 일의 MACD 지수이동 평균
        MACD Oscillator = MACD - MACD 신호선




EMA :   EMA(price,N)i = alpha*price + ( 1 - alpha) * EMA(price,N)(i-1)
        ex) N = 5 [[ alpha = a = 2/5+1 = 1/3 ]]
            (1/3)(2/3)^0 * A + (1/3)(2/3)^1 * B + (1/3)(2/3)^2 * C + (1/3)(2/3)^4 * D + (1/3)(2/3)^4 * E + (1/3)(2/3)^5 * F
        위는 지수이동평균으로써 나름 추세를 균일하게 반영한다.
        하지만 조금 더 최근 추세를 반영하기 위해 업비트와 같은 거래소에서는 지수가중이동평균 EWMA 를 사용한다
        그 식은 다음과 같다.
        
'''

df['rsi_ud'] = 0

for j in range(2):
    upper = 0
    down = 0
    for i in range(14):
        if df['tradePrice'][i+j] > df['tradePrice'][i+j+1]:
            upper += (df['tradePrice'][i+j] - df['tradePrice'][i+j+1])
            print(upper)
        elif df['tradePrice'][i+j] < df['tradePrice'][i+j+1]:
            down += df['tradePrice'][i+j+1] - df['tradePrice'][i+j]
            print(down)
        else:
            continue
    print(upper,down)
    AU = upper/14
    AD = down/14
    RS = AU / AD
    # print(RS)
    RSI = (RS/(1+RS))
    # print(RSI)

