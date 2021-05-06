import json

def get_coin_data_url(coinName, type, scale, cnt=400) :
    addr = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/'
    if type == 'minutes' :
        basic_url = addr + type + '/' + scale + '?code=CRIX.UPBIT.KRW-' + coinName +'&count='+str(cnt)
    else :
        basic_url = addr + type + '/' + '?code=CRIX.UPBIT.KRW-' + coinName +'&count='+str(cnt)

    return basic_url

# 수정 변수들
coinName = "XRP"
to_date = '2021-05-0'
num = 30
scale = '1'

# get_coin_data_url(coinName,type,scale)

addr = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1/?code=CRIX.UPBIT.KRW-XRP&count='+str(400)


print(addr)