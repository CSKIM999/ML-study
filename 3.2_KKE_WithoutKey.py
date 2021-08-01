import os
from math import exp
from pandas._libs.tslibs import *
from pandas.core import frame
import pyupbit
import time
from urllib.parse import urlencode
from pyupbit.exchange_api import Upbit
from pyupbit.quotation_api import get_current_price, get_tickers
import datetime
from tkinter import *
import threading
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import tkinter as tk
import sys
from urllib3.packages.six import ensure_text
##################################################################
#############   팡-숀   ##########################################
##################################################################
access = 'ACCESS'
secret = 'SECRET'
server_url = 'https://upbit.com/home'

upbit = pyupbit.Upbit(access,secret)
path = os.path.dirname(os.path.realpath(__file__))

################# 하나로 묶기

b1_1 = 1
b2_1 = 1
b3_1 = 1
b1_2 = 1
b2_2 = 1
b3_2 = 1
b1_3 = 1
b2_3 = 1
b3_3 = 1
balance ='BALANCE'
tickers = get_tickers()
################# ################# 


################# 하나로 묶기
#상수값
const_num_1 = 1
coin_ticker_1 = 'BTC'
want2tradetime_1=30
op_mode_1 = False
hold_1 = False
pwr_btn_1 = 0

const_num_2 = 1
coin_ticker_2 = 'BTC'
want2tradetime_2=30
op_mode_2 = False
hold_2 = False
pwr_btn_2 = 0

const_num_3 = 1
coin_ticker_3 = 'BTC'
want2tradetime_3=30
op_mode_3 = False
hold_3 = False
pwr_btn_3 = 0

################# ################# 

def resource_path(realative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path,realative_path)


def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

def so_cute():
    msgbox.showinfo('고양이', '정말귀여워')

def update_balance():
    balance = upbit.get_balance('KRW')
    int_bal = format(balance,',.0f')
    str_bal = ('BALANCE  :' +str(int_bal)+' \\')
    var_balance.set(str_bal)
    
def warn_stoploss():
    msgbox.showwarning('아이쿠!','STOP LOSS 기능은 아직 구현되지 않았습니당.')

def time_tick():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # now = time.ctime(time.time())
    clock.config(text=now)
    clock.after(1000,time_tick)


def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)

def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)


########################################################################################################
########################################################################################################
########################################################################################################


################# ################# ################# 

def btn_const_1():
    global const_num_1
    global b1_1
    b1_1 = 0
    const_num_1 = const_num_entry_1.get()
    if isNumber(const_num_1) is False:
        msgbox.showwarning('아이쿠!!!','숫자가 아닌 값이 입력되었습니다. \nCONST NUM 값을 기본값인 [ 1.0 ]로 입력합니다!')
        const_num_1 = 1
    float(const_num_1)
    text_1.insert(END,'[[  '+str(const_num_1)+'  ]] 변동성 상수 SET\n')
    text_1.see(END)
    btn_const_num_set_1.config(state='disable')
    if b1_1+b2_1+b3_1 ==0:
        btn_start_1.config(state='normal')

def btn_const_2():
    global const_num_2
    global b1_2
    b1_2 = 0
    const_num_2 = const_num_entry_2.get()
    if isNumber(const_num_2) is False:
        msgbox.showwarning('아이쿠!!!','숫자가 아닌 값이 입력되었습니다. \nCONST NUM 값을 기본값인 [ 1.0 ]로 입력합니다!')
        const_num_2 = 1
    float(const_num_2)
    text_2.insert(END,'[[  '+str(const_num_2)+'  ]] 변동성 상수 SET\n')
    text_2.see(END)
    btn_const_num_set_2.config(state='disable')
    if b1_2+b2_2+b3_2 ==0:
        btn_start_2.config(state='normal')

def btn_const_3():
    global const_num_3
    global b1_3
    b1_3 = 0
    const_num_3 = const_num_entry_3.get()
    if isNumber(const_num_3) is False:
        msgbox.showwarning('아이쿠!!!','숫자가 아닌 값이 입력되었습니다. \nCONST NUM 값을 기본값인 [ 1.0 ]로 입력합니다!')
        const_num_3 = 1
    float(const_num_3)
    text_3.insert(END,'[[  '+str(const_num_3)+'  ]] 변동성 상수 SET\n')
    text_3.see(END)
    btn_const_num_set_3.config(state='disable')
    if b1_3+b2_3+b3_3 ==0:
        btn_start_3.config(state='normal')

################# ################# ################# 

def btn_coin_ticker_1():
    global coin_ticker_1
    global b2_1
    b2_1 = 0
    coin_ticker_data_1 = coin_name_entry_1.get()
    btn_coin_name_set_1.config(state='disable')
    if tickers.count('KRW-'+coin_ticker_data_1.upper()) == 1:
        coin_ticker_1 = coin_ticker_data_1.upper()
    else:
        msgbox.showwarning('아이쿠!!!!','KRW마켓에 없거나 잘못된 TICKER 를 입력하셨습니다.\n 기본값인 BTC 가 입력됩니다.')
        coin_ticker_1 = 'BTC'
    text_1.insert(END,'[[  '+str(coin_ticker_1)+'  ]] COIN TICKER SET\n')
    text_1.see(END)
    if b1_1+b2_1+b3_1 ==0:
        btn_start_1.config(state='normal')
    
def btn_coin_ticker_2():
    global coin_ticker_2
    global b2_2
    b2_2 = 0
    coin_ticker_data_2 = coin_name_entry_2.get()
    btn_coin_name_set_2.config(state='disable')
    if tickers.count('KRW-'+coin_ticker_data_2.upper()) == 1:
        coin_ticker_2 = coin_ticker_data_2.upper()
    else:
        msgbox.showwarning('아이쿠!!!!','KRW마켓에 없거나 잘못된 TICKER 를 입력하셨습니다.\n 기본값인 BTC 가 입력됩니다.')
        coin_ticker_2 = 'BTC'
    text_2.insert(END,'[[  '+str(coin_ticker_2)+'  ]] COIN TICKER SET\n')
    text_2.see(END)
    if b1_2+b2_2+b3_2 ==0:
        btn_start_2.config(state='normal')
    
def btn_coin_ticker_3():
    global coin_ticker_3
    global b2_3
    b2_3 = 0
    coin_ticker_data_3 = coin_name_entry_3.get()
    btn_coin_name_set_3.config(state='disable')
    if tickers.count('KRW-'+coin_ticker_data_3.upper()) == 1:
        coin_ticker_3 = coin_ticker_data_3.upper()
    else:
        msgbox.showwarning('아이쿠!!!!','KRW마켓에 없거나 잘못된 TICKER 를 입력하셨습니다.\n 기본값인 BTC 가 입력됩니다.')
        coin_ticker_3 = 'BTC'
    text_3.insert(END,'[[  '+str(coin_ticker_3)+'  ]] COIN TICKER SET\n')
    text_3.see(END)
    if b1_3+b2_3+b3_3 ==0:
        btn_start_3.config(state='normal')

################# ################# ################# 

def btn_w2tmin_1():
    global want2tradetime_1
    global b3_1
    b3_1 = 0
    btn_combobox_1.config(state='disable')
    w2t = Combobox_min_1.get()
    if w2t == '거래기준봉':
        msgbox.showwarning('아이쿠!!!!!','거래 기준봉을 선택해주세요!')
        btn_combobox_1.config(state='normal')
    elif w2t == '10 분':
        want2tradetime_1 = 10
    elif w2t == '60 분':
        want2tradetime_1 = 60
    elif w2t == '240 분':
        want2tradetime_1 = 240
    else:
        want2tradetime_1 = 30
    text_1.insert(END,str(want2tradetime_1)+'분봉 SET\n')
    text_1.see(END)
    if b1_1+b2_1+b3_1 ==0:
        btn_start_1.config(state='normal')

def btn_w2tmin_2():
    global want2tradetime_2
    global b3_2
    b3_2 = 0
    btn_combobox_2.config(state='disable')
    w2t = Combobox_min_2.get()
    if w2t == '거래기준봉':
        msgbox.showwarning('아이쿠!!!!!','거래 기준봉을 선택해주세요!')
        btn_combobox_2.config(state='normal')
    elif w2t == '10 분':
        want2tradetime_2 = 10
    elif w2t == '60 분':
        want2tradetime_2 = 60
    elif w2t == '240 분':
        want2tradetime_2 = 240
    else:
        want2tradetime_2 = 30
    text_2.insert(END,str(want2tradetime_2)+'분봉 SET\n')
    text_2.see(END)
    if b1_2+b2_2+b3_2 ==0:
        btn_start_2.config(state='normal')

def btn_w2tmin_3():
    global want2tradetime_3
    global b3_3
    b3_3 = 0
    btn_combobox_3.config(state='disable')
    w2t = Combobox_min_3.get()
    if w2t == '거래기준봉':
        msgbox.showwarning('아이쿠!!!!!','거래 기준봉을 선택해주세요!')
        btn_combobox_3.config(state='normal')
    elif w2t == '10 분':
        want2tradetime_3 = 10
    elif w2t == '60 분':
        want2tradetime_3 = 60
    elif w2t == '240 분':
        want2tradetime_3 = 240
    else:
        want2tradetime_3 = 30
    text_3.insert(END,str(want2tradetime_3)+'분봉 SET\n')
    text_3.see(END)
    if b1_3+b2_3+b3_3 ==0:
        btn_start_3.config(state='normal')

################# ################# ################# 

def  min_30_trade_1():
    global op_mode_1
    global pwr_btn_1
    global hold_1
    global target_1

    while True:
        now = datetime.datetime.now()

        if (now.minute == 30 or now.minute == 00) and (10<=now.second<=20):
            # print(now.minute)
            # print(now.second)        
            target_1 = cal_target_1()
            text_1.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_1))
            text_1.see(END)
            op_mode_1 = True


        price_1 = pyupbit.get_current_price('KRW-'+coin_ticker_1)

        if (op_mode_1 is True) and (price_1 is not None) and (hold_1 is False) and (price_1 > target_1): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_1,krw_balance*0.9995)
            hold_1 = True
            text_1.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_1.insert(END,'??? : 그가 매수했습니다.\n')
            text_1.see(END)
        
        #매도
        if (now.minute == 29 or now.minute == 59 )and (50<= now.second <=59) and (hold_1 is True):
            print(now.minute)
            print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_1)
            upbit.sell_market_order('KRW-'+coin_ticker_1,btc_balance)
            text_1.insert(END,'시가매도\n')
            text_1.insert(END,'??? : 그가 매도했습니다.\n')
            text_1.see(END)
            hold_1 = False
            op_mode_1 = False


        text_1.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_1)+'\n'))
        text_1.see(END)

        time.sleep(10)

        if pwr_btn_1 == 1:
            text_1.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_1.see(END)
            break

def  min_30_trade_2():
    global op_mode_2
    global pwr_btn_2
    global hold_2
    global target_2

    while True:
        now = datetime.datetime.now()

        if (now.minute == 30 or now.minute == 00) and (10<=now.second<=20):
            # print(now.minute)
            # print(now.second)        
            target_2 = cal_target_2()
            text_2.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_2))
            text_2.see(END)
            op_mode_2 = True


        price_2 = pyupbit.get_current_price('KRW-'+coin_ticker_2)

        if (op_mode_2 is True) and (price_2 is not None) and (hold_2 is False) and (price_2 > target_2): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_2,krw_balance*0.9995)
            hold_2 = True
            text_2.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_2.insert(END,'??? : 그가 매수했습니다.\n')
            text_2.see(END)
        
        #매도
        if (now.minute == 29 or now.minute == 59 )and (50<= now.second <=59) and (hold_2 is True):
            print(now.minute)
            print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_2)
            upbit.sell_market_order('KRW-'+coin_ticker_2,btc_balance)
            text_2.insert(END,'시가매도\n')
            text_2.insert(END,'??? : 그가 매도했습니다.\n')
            text_2.see(END)
            hold_2 = False
            op_mode_2 = False


        text_2.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_2)+'\n'))
        text_2.see(END)

        time.sleep(10)

        if pwr_btn_2 == 1:
            text_2.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_2.see(END)
            break

def  min_30_trade_3():
    global op_mode_3
    global pwr_btn_3
    global hold_3
    global target_3

    while True:
        now = datetime.datetime.now()

        if (now.minute == 30 or now.minute == 00) and (10<=now.second<=20):
            # print(now.minute)
            # print(now.second)        
            target_3 = cal_target_3()
            text_3.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_3))
            text_3.see(END)
            op_mode_3 = True


        price_3 = pyupbit.get_current_price('KRW-'+coin_ticker_3)

        if (op_mode_3 is True) and (price_3 is not None) and (hold_3 is False) and (price_3 > target_3): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_3,krw_balance*0.9995)
            hold_3 = True
            text_3.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_3.insert(END,'??? : 그가 매수했습니다.\n')
            text_3.see(END)
        
        #매도
        if (now.minute == 29 or now.minute == 59 )and (50<= now.second <=59) and (hold_3 is True):
            print(now.minute)
            print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_3)
            upbit.sell_market_order('KRW-'+coin_ticker_3,btc_balance)
            text_3.insert(END,'시가매도\n')
            text_3.insert(END,'??? : 그가 매도했습니다.\n')
            text_3.see(END)
            hold_3 = False
            op_mode_3 = False


        text_3.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_3)+'\n'))
        text_3.see(END)

        time.sleep(10)

        if pwr_btn_3 == 1:
            text_3.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_3.see(END)
            break

################# ################# ################# 

def  min_10_trade_1():
    global op_mode_1
    global pwr_btn_1
    global hold_1
    global target_1

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if (now.minute == 10 or now.minute == 20 or  now.minute == 30 or now.minute == 40 or now.minute == 50  or  now.minute == 00) and (10<=now.second<=20):
            # print(now.minute)
            # print(now.second)        
            target_1 = cal_target_1()
            text_1.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_1))
            text_1.see(END)
            op_mode_1 = True


        price_1 = pyupbit.get_current_price('KRW-'+coin_ticker_1)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_1 is True) and (price_1 is not None) and (hold_1 is False) and (price_1 > target_1): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_1,krw_balance*0.9995)
            hold_1 = True
            text_1.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_1.insert(END,'??? : 그가 매수했습니다.\n')
            text_1.see(END)
        
        #매도기능
        if (now.minute == 9 or now.minute == 19 or now.minute == 29 or now.minute == 39 or now.minute == 49 or now.minute == 59 )and (50<= now.second <=59) and (hold_1 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_1)
            upbit.sell_market_order('KRW-'+coin_ticker_1,btc_balance)
            text_1.insert(END,'시가매도\n')
            text_1.insert(END,'??? : 그가 매도했습니다.\n')
            text_1.see(END)
            hold_1 = False
            op_mode_1 = False

        

        text_1.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_1)+'\n'))
        text_1.see(END)


        time.sleep(10)
        if pwr_btn_1 == 1:
            text_1.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_1.see(END)
            break

def  min_10_trade_2():
    global op_mode_2
    global pwr_btn_2
    global hold_2
    global target_2

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if (now.minute == 10 or now.minute == 20 or  now.minute == 30 or now.minute == 40 or now.minute == 50  or  now.minute == 00) and (10<=now.second<=20):
            # print(now.minute)
            # print(now.second)        
            target_2 = cal_target_2()
            text_2.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_2))
            text_2.see(END)
            op_mode_2 = True


        price_2 = pyupbit.get_current_price('KRW-'+coin_ticker_2)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_2 is True) and (price_2 is not None) and (hold_2 is False) and (price_2 > target_2): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_2,krw_balance*0.9995)
            hold_2 = True
            text_2.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_2.insert(END,'??? : 그가 매수했습니다.\n')
            text_2.see(END)
        
        #매도기능
        if (now.minute == 9 or now.minute == 19 or now.minute == 29 or now.minute == 39 or now.minute == 49 or now.minute == 59 )and (50<= now.second <=59) and (hold_2 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_2)
            upbit.sell_market_order('KRW-'+coin_ticker_2,btc_balance)
            text_2.insert(END,'시가매도\n')
            text_2.insert(END,'??? : 그가 매도했습니다.\n')
            text_2.see(END)
            hold_2 = False
            op_mode_2 = False

        

        text_2.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_2)+'\n'))
        text_2.see(END)


        time.sleep(10)
        if pwr_btn_2 == 1:
            text_2.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_2.see(END)
            break
        
def  min_10_trade_3():
    global op_mode_3
    global pwr_btn_3
    global hold_3
    global target_3

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if (now.minute == 10 or now.minute == 20 or  now.minute == 30 or now.minute == 40 or now.minute == 50  or  now.minute == 00) and (10<=now.second<=20):
            # print(now.minute)
            # print(now.second)        
            target_3 = cal_target_3()
            text_3.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_3))
            text_3.see(END)
            op_mode_3 = True


        price_3 = pyupbit.get_current_price('KRW-'+coin_ticker_3)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_3 is True) and (price_3 is not None) and (hold_3 is False) and (price_3 > target_3): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_3,krw_balance*0.9995)
            hold_3 = True
            text_3.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_3.insert(END,'??? : 그가 매수했습니다.\n')
            text_3.see(END)
        
        #매도기능
        if (now.minute == 9 or now.minute == 19 or now.minute == 29 or now.minute == 39 or now.minute == 49 or now.minute == 59 )and (50<= now.second <=59) and (hold_3 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_3)
            upbit.sell_market_order('KRW-'+coin_ticker_3,btc_balance)
            text_3.insert(END,'시가매도\n')
            text_3.insert(END,'??? : 그가 매도했습니다.\n')
            text_3.see(END)
            hold_3 = False
            op_mode_3 = False

        

        text_3.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_3)+'\n'))
        text_3.see(END)


        time.sleep(10)
        if pwr_btn_3 == 1:
            text_3.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_3.see(END)
            break

################# ################# ################# 

def  min_60_trade_1():
    global op_mode_1
    global pwr_btn_1
    global hold_1
    global target_1

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if now.minute == 00 and  45 <= now.second<= 55 :
            # print(now.minute)
            # print(now.second)        
            target_1 = cal_target_1()
            text_1.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_1))
            text_1.see(END)
            op_mode_1 = True


        price_1 = pyupbit.get_current_price('KRW-'+coin_ticker_1)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_1 is True) and (price_1 is not None) and (hold_1 is False) and (price_1 > target_1): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_1,krw_balance*0.9995)
            hold_1 = True
            text_1.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_1.insert(END,'??? : 그가 매수했습니다.\n')
            text_1.see(END)
        
        #매도기능
        if now.minute == 59 and  45 <= now.second<= 55 and (hold_1 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_1)
            upbit.sell_market_order('KRW-'+coin_ticker_1,btc_balance)
            text_1.insert(END,'시가매도\n')
            text_1.insert(END,'??? : 그가 매도했습니다.\n')
            text_1.see(END)
            hold_1 = False
            op_mode_1 = False

        

        text_1.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_1)+'\n'))
        text_1.see(END)


        time.sleep(10)
        if pwr_btn_1 == 1:
            text_1.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_1.see(END)
            break

def  min_60_trade_2():
    global op_mode_2
    global pwr_btn_2
    global hold_2
    global target_2

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if now.minute == 00 and  45 <= now.second<= 55 :
            # print(now.minute)
            # print(now.second)        
            target_2 = cal_target_2()
            text_2.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_2))
            text_2.see(END)
            op_mode_2 = True


        price_2 = pyupbit.get_current_price('KRW-'+coin_ticker_2)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_2 is True) and (price_2 is not None) and (hold_2 is False) and (price_2 > target_2): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_2,krw_balance*0.9995)
            hold_2 = True
            text_2.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_2.insert(END,'??? : 그가 매수했습니다.\n')
            text_2.see(END)
        
        #매도기능
        if now.minute == 59 and  45 <= now.second<= 55 and (hold_2 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_2)
            upbit.sell_market_order('KRW-'+coin_ticker_2,btc_balance)
            text_2.insert(END,'시가매도\n')
            text_2.insert(END,'??? : 그가 매도했습니다.\n')
            text_2.see(END)
            hold_2 = False
            op_mode_2 = False

        

        text_2.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_2)+'\n'))
        text_2.see(END)


        time.sleep(10)
        if pwr_btn_2 == 1:
            text_2.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_2.see(END)
            break

def  min_60_trade_3():
    global op_mode_3
    global pwr_btn_3
    global hold_3
    global target_3

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if now.minute == 00 and  45 <= now.second<= 55 :
            # print(now.minute)
            # print(now.second)        
            target_3 = cal_target_3()
            text_3.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_3))
            text_3.see(END)
            op_mode_3 = True


        price_3 = pyupbit.get_current_price('KRW-'+coin_ticker_3)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_3 is True) and (price_3 is not None) and (hold_3 is False) and (price_3 > target_3): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_3,krw_balance*0.9995)
            hold_3 = True
            text_3.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_3.insert(END,'??? : 그가 매수했습니다.\n')
            text_3.see(END)
        
        #매도기능
        if now.minute == 59 and  45 <= now.second<= 55 and (hold_3 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_3)
            upbit.sell_market_order('KRW-'+coin_ticker_3,btc_balance)
            text_3.insert(END,'시가매도\n')
            text_3.insert(END,'??? : 그가 매도했습니다.\n')
            text_3.see(END)
            hold_3 = False
            op_mode_3 = False

        

        text_3.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_3)+'\n'))
        text_3.see(END)


        time.sleep(10)
        if pwr_btn_3 == 1:
            text_3.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_3.see(END)
            break

################# ################# ################# 

def  min_240_trade_1():
    global op_mode_1
    global pwr_btn_1
    global hold_1
    global target_1

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if (now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21) and now.minute == 00 and  45 <= now.second<= 55 :
            # print(now.minute)
            # print(now.second)        
            target_1 = cal_target_1()
            text_1.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_1))
            text_1.see(END)
            op_mode_1 = True


        price_1 = pyupbit.get_current_price('KRW-'+coin_ticker_1)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_1 is True) and (price_1 is not None) and (hold_1 is False) and (price_1 > target_1): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_1,krw_balance*0.9995)
            hold_1 = True
            text_1.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_1.insert(END,'??? : 그가 매수했습니다.\n')
            text_1.see(END)
        
        #매도기능
        if (now.hour == 00 or now.hour == 4 or now.hour == 8 or now.hour == 12 or now.hour == 16 or now.hour == 20) and now.minute == 59 and  45 <= now.second<= 55 and (hold_1 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_1)
            upbit.sell_market_order('KRW-'+coin_ticker_1,btc_balance)
            text_1.insert(END,'시가매도\n')
            text_1.insert(END,'??? : 그가 매도했습니다.\n')
            text_1.see(END)
            hold_1 = False
            op_mode_1 = False

        

        text_1.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_1)+'\n'))
        text_1.see(END)


        time.sleep(10)
        if pwr_btn_1 == 1:
            text_1.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_1.see(END)
            break

def  min_240_trade_2():
    global op_mode_2
    global pwr_btn_2
    global hold_2
    global target_2

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if (now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21) and now.minute == 00 and  45 <= now.second<= 55 :
            # print(now.minute)
            # print(now.second)        
            target_2 = cal_target_2()
            text_2.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_2))
            text_2.see(END)
            op_mode_2 = True


        price_2 = pyupbit.get_current_price('KRW-'+coin_ticker_2)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_2 is True) and (price_2 is not None) and (hold_2 is False) and (price_2 > target_2): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_2,krw_balance*0.9995)
            hold_2 = True
            text_2.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_2.insert(END,'??? : 그가 매수했습니다.\n')
            text_2.see(END)
        
        #매도기능
        if (now.hour == 00 or now.hour == 4 or now.hour == 8 or now.hour == 12 or now.hour == 16 or now.hour == 20) and now.minute == 59 and  45 <= now.second<= 55 and (hold_2 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_2)
            upbit.sell_market_order('KRW-'+coin_ticker_2,btc_balance)
            text_2.insert(END,'시가매도\n')
            text_2.insert(END,'??? : 그가 매도했습니다.\n')
            text_2.see(END)
            hold_2 = False
            op_mode_2 = False

        

        text_2.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_2)+'\n'))
        text_2.see(END)


        time.sleep(10)
        if pwr_btn_2 == 1:
            text_2.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_2.see(END)
            break

def  min_240_trade_3():
    global op_mode_3
    global pwr_btn_3
    global hold_3
    global target_3

    while True:
        now = datetime.datetime.now()
        
        # 목표가 갱신 프로세스
        if (now.hour == 1 or now.hour == 5 or now.hour == 9 or now.hour == 13 or now.hour == 17 or now.hour == 21) and now.minute == 00 and  45 <= now.second<= 55 :
            # print(now.minute)
            # print(now.second)        
            target_3 = cal_target_3()
            text_3.insert(END,'[[[ 목표가 갱신 : {} ]]]\n'.format(target_3))
            text_3.see(END)
            op_mode_3 = True


        price_3 = pyupbit.get_current_price('KRW-'+coin_ticker_3)

        #매 초마다 조건 확인 후 매수 시도
        ### upbit 은 에러의 경우 None 을 return 해주므로 None 을 이용한 예외처리를 하면 좋음.
        if (op_mode_3 is True) and (price_3 is not None) and (hold_3 is False) and (price_3 > target_3): 
            #매수
            krw_balance = upbit.get_balance('KRW')
            upbit.buy_market_order("KRW-"+coin_ticker_3,krw_balance*0.9995)
            hold_3 = True
            text_3.insert(END,'[[ 목표가 도달 매수합니다 ]]\n')
            text_3.insert(END,'??? : 그가 매수했습니다.\n')
            text_3.see(END)
        
        #매도기능
        if (now.hour == 00 or now.hour == 4 or now.hour == 8 or now.hour == 12 or now.hour == 16 or now.hour == 20) and now.minute == 59 and  45 <= now.second<= 55 and (hold_3 is True):
            # print(now.minute)
            # print(now.second)        
            btc_balance = upbit.get_balance("KRW-"+coin_ticker_3)
            upbit.sell_market_order('KRW-'+coin_ticker_3,btc_balance)
            text_3.insert(END,'시가매도\n')
            text_3.insert(END,'??? : 그가 매도했습니다.\n')
            text_3.see(END)
            hold_3 = False
            op_mode_3 = False

        

        text_3.insert(END,(str(now.strftime("%Y-%m-%d %H:%M:%S")) +' \\'+ str(price_3)+'\n'))
        text_3.see(END)


        time.sleep(10)
        if pwr_btn_3 == 1:
            text_3.insert(END,'[[[ 거래 중지 완료 ]]]\n')
            text_3.see(END)
            break

################# ################# ################# 

def cal_target_1():
    global target_1
    global const_num_1
    global want2tradetime_1

    df = pyupbit.get_ohlcv('KRW-'+coin_ticker_1,'minute{}'.format(want2tradetime_1)) # minute10 5 3 1
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_high = float(yesterday['high'])
    yesterday_low = float(yesterday['low'])
    yesterday_range= yesterday_high-yesterday_low
    today_open = (today['open'])
    target_1 = today_open + yesterday_range*float(const_num_1)
    return target_1

target_1 = cal_target_1()
# print('target_1 price_1 : {} '.format(target_1))

def cal_target_2():
    global target_2
    global const_num_2
    global want2tradetime_2

    df = pyupbit.get_ohlcv('KRW-'+coin_ticker_2,'minute{}'.format(want2tradetime_2)) # minute10 5 3 1
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_high = float(yesterday['high'])
    yesterday_low = float(yesterday['low'])
    yesterday_range= yesterday_high-yesterday_low
    today_open = (today['open'])
    target_2 = today_open + yesterday_range*float(const_num_2)
    return target_2

target_2 = cal_target_2()

def cal_target_3():
    global target_3
    global const_num_3
    global want2tradetime_3

    df = pyupbit.get_ohlcv('KRW-'+coin_ticker_3,'minute{}'.format(want2tradetime_3)) # minute10 5 3 1
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_high = float(yesterday['high'])
    yesterday_low = float(yesterday['low'])
    yesterday_range= yesterday_high-yesterday_low
    today_open = (today['open'])
    target_3 = today_open + yesterday_range*float(const_num_3)
    return target_3

target_3 = cal_target_3()


################# ################# ################# 

class BackThread_start1(threading.Thread):   
    global want2tradetime_1
    global const_num_1
    global coin_ticker_1

     
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True  
    
    def run (self):
        # print('start')
        
        progressbar_1.start(10)
        if want2tradetime_1 == 10:
            text_1.insert(END,'[[  상수 ['+const_num_1+'] ['+coin_ticker_1+'] 10분 매매 시작  ]] \n')
            text_1.insert(END,'Target Price : '+str(cal_target_1()) +'\n')
            text_1.see(END)
            btn_start_1.config('disable')
            min_10_trade_1()

        if want2tradetime_1 == 30:
            text_1.insert(END,'[[  상수 ['+const_num_1+'] ['+coin_ticker_1+'] 30분 매매 시작  ]] \n')
            text_1.insert(END,'Target Price : '+str(cal_target_1()) +'\n')
            text_1.see(END)
            btn_start_1.config('disable')
            min_30_trade_1()

        if want2tradetime_1 == 60:
            text_1.insert(END,'[[  상수 ['+const_num_1+'] ['+coin_ticker_1+'] 60분 매매 시작  ]] \n')
            text_1.insert(END,'Target Price : '+str(cal_target_1()) +'\n')
            text_1.see(END)
            btn_start_1.config('disable')
            min_60_trade_1()
        
        if want2tradetime_1 == 240:
            text_1.insert(END,'[[  상수 ['+const_num_1+'] ['+coin_ticker_1+'] 4시간 매매 시작  ]] \n')
            text_1.insert(END,'Target Price : '+str(cal_target_1()) +'\n')
            text_1.see(END)
            btn_start_1.config('disable')
            min_240_trade_1()
    
class BackThread_start_2(threading.Thread):   
    global want2tradetime_2
    global const_num_2
    global coin_ticker_2

     
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True  
    
    def run (self):
        # print('start')
        
        progressbar_2.start(10)
        if want2tradetime_2 == 10:
            text_2.insert(END,'[[  상수 ['+const_num_2+'] ['+coin_ticker_2+'] 10분 매매 시작  ]] \n')
            text_2.insert(END,'Target Price : '+str(cal_target_2()) +'\n')
            text_2.see(END)
            btn_start_2.config('disable')
            min_10_trade_2()

        if want2tradetime_2 == 30:
            text_2.insert(END,'[[  상수 ['+const_num_2+'] ['+coin_ticker_2+'] 30분 매매 시작  ]] \n')
            text_2.insert(END,'Target Price : '+str(cal_target_2()) +'\n')
            text_2.see(END)
            btn_start_2.config('disable')
            min_30_trade_2()

        if want2tradetime_2 == 60:
            text_2.insert(END,'[[  상수 ['+const_num_2+'] ['+coin_ticker_2+'] 60분 매매 시작  ]] \n')
            text_2.insert(END,'Target Price : '+str(cal_target_2()) +'\n')
            text_2.see(END)
            btn_start_2.config('disable')
            min_60_trade_2()

        if want2tradetime_2 == 240:
            text_2.insert(END,'[[  상수 ['+const_num_2+'] ['+coin_ticker_2+'] 4시간 매매 시작  ]] \n')
            text_2.insert(END,'Target Price : '+str(cal_target_2()) +'\n')
            text_2.see(END)
            btn_start_2.config('disable')
            min_240_trade_2()

class BackThread_start_3(threading.Thread):   
    global want2tradetime_3
    global const_num_3
    global coin_ticker_3

     
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True  
    
    def run (self):
        # print('start')
        
        progressbar_3.start(10)
        if want2tradetime_3 == 10:
            text_3.insert(END,'[[  상수 ['+const_num_3+'] ['+coin_ticker_3+'] 10분 매매 시작  ]] \n')
            text_3.insert(END,'Target Price : '+str(cal_target_3()) +'\n')
            text_3.see(END)
            btn_start_3.config('disable')
            min_10_trade_3()

        if want2tradetime_3 == 30:
            text_3.insert(END,'[[  상수 ['+const_num_3+'] ['+coin_ticker_3+'] 30분 매매 시작  ]] \n')
            text_3.insert(END,'Target Price : '+str(cal_target_3()) +'\n')
            text_3.see(END)
            btn_start_3.config('disable')
            min_30_trade_3()

        if want2tradetime_3 == 60:
            text_3.insert(END,'[[  상수 ['+const_num_3+'] ['+coin_ticker_3+'] 60분 매매 시작  ]] \n')
            text_3.insert(END,'Target Price : '+str(cal_target_3()) +'\n')
            text_3.see(END)
            btn_start_3.config('disable')
            min_60_trade_3()

        if want2tradetime_3 == 240:
                    text_3.insert(END,'[[  상수 ['+const_num_3+'] ['+coin_ticker_3+'] 4시간 매매 시작  ]] \n')
                    text_3.insert(END,'Target Price : '+str(cal_target_3()) +'\n')
                    text_3.see(END)
                    btn_start_3.config('disable')
                    min_240_trade_3()

################# ################# ################# 

class BackThread_stop_1(threading.Thread):    
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True  
    
    def run (self):
        trade_off_1

class BackThread_stop_2(threading.Thread):    
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True  
    
    def run (self):
        trade_off_2

class BackThread_stop_3(threading.Thread):    
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True  
    
    def run (self):
        trade_off_3

################# ################# ################# 

def trade_off_1():
    global pwr_btn_1
    btn_start_1.config(state='normal')
    btn_combobox_1.config(state='normal')
    btn_const_num_set_1.config(state='normal')
    btn_coin_name_set_1.config(state='normal')
    btn_start_1.config(state='disable')
    text_1.insert(END,'[[[ 거래 중지 요청 ]]]\n')
    text_1.see(END)
    pwr_btn_1 = 1
    progressbar_1.stop()

def trade_off_2():
    global pwr_btn_2
    btn_start_2.config(state='normal')
    btn_combobox_2.config(state='normal')
    btn_const_num_set_2.config(state='normal')
    btn_coin_name_set_2.config(state='normal')
    btn_start_2.config(state='disable')
    text_2.insert(END,'[[[ 거래 중지 요청 ]]]\n')
    text_2.see(END)
    pwr_btn_2 = 1
    progressbar_2.stop()

def trade_off_3():
    global pwr_btn_3
    btn_start_3.config(state='normal')
    btn_combobox_3.config(state='normal')
    btn_const_num_set_3.config(state='normal')
    btn_coin_name_set_3.config(state='normal')
    btn_start_3.config(state='disable')
    text_3.insert(END,'[[[ 거래 중지 요청 ]]]\n')
    text_3.see(END)
    pwr_btn_3 = 1
    progressbar_3.stop()

################# ################# ################# 

'''
>>> 함수부가 초창기에 세부분으로 나눈다고 상당히 복잡하다 간단하게 만들자
'''


##################################################################
#############   GUI   ############################################
##################################################################



root = Tk()
root.title('CSKIM GUI')
root.geometry('1150x750')

var_balance = StringVar()
var_balance.set(balance)
photo = PhotoImage(file= resource_path('KKE.png'))

#frame pack
title_frame = LabelFrame(root,bd=4)
title_frame.pack(fill='x', padx=5,pady=5)

value_frame = Frame(root)
value_frame.pack(fill='x', padx=5 , pady=5)
value_frame_left = LabelFrame(value_frame,text='Thread-1 Values',relief='solid',bd=2)
value_frame_left.pack(side='left',padx=25)
value_frame_center = LabelFrame(value_frame,text='Thread-2 Values',relief='solid',bd=2)
value_frame_center.pack(side='left',padx=25)
value_frame_right = LabelFrame(value_frame,text='Thread-3 Values',relief='solid',bd=2)
value_frame_right.pack(side='left',padx=25)
value_frame_cat_n_balance = Frame(value_frame)
value_frame_cat_n_balance.pack(side='right')

text_frame =LabelFrame(root,text = 'TERMINAL')
text_frame.pack(fill='x',padx=5 , pady=5)
text_frame_left =LabelFrame(text_frame,text = 'Thread 1')
text_frame_left.pack(side='left',padx=5 , pady=5)
text_frame_center =LabelFrame(text_frame,text = 'Thread 2')
text_frame_center.pack(side='left',padx=5 , pady=5)
text_frame_right =LabelFrame(text_frame,text = 'Thread 3')
text_frame_right.pack(side='left',padx=5 , pady=5)
scrollbar_1 = Scrollbar(text_frame_left)
scrollbar_1.pack(side='right',fill='y')
scrollbar_2 = Scrollbar(text_frame_center)
scrollbar_2.pack(side='right',fill='y')
scrollbar_3 = Scrollbar(text_frame_right)
scrollbar_3.pack(side='right',fill='y')

Bottom_Frame = Frame(root)
Bottom_Frame.pack()
Bottom_Frame_left = LabelFrame(Bottom_Frame,text = 'THREAD 1')
Bottom_Frame_left.pack(fill='both',side='left', padx=9,pady=5)
Bottom_Frame_center = LabelFrame(Bottom_Frame,text = 'THREAD 2')
Bottom_Frame_center.pack(fill='both',side='left', padx=9,pady=5)
Bottom_Frame_right = LabelFrame(Bottom_Frame,text = 'THREAD 3')
Bottom_Frame_right.pack(fill='both',side='right', padx=9,pady=5)
Bottom_Frame_left_progress =  LabelFrame(Bottom_Frame_left,text='Loading bar...')
Bottom_Frame_left_progress.pack(side='left', padx=5,pady=5)
Bottom_Frame_left_action = LabelFrame(Bottom_Frame_left,text='실행')
Bottom_Frame_left_action.pack(side='right', padx=5,pady=5)
Bottom_Frame_center_progress =  LabelFrame(Bottom_Frame_center,text='Loading bar...')
Bottom_Frame_center_progress.pack(side='left', padx=5,pady=5)
Bottom_Frame_center_action = LabelFrame(Bottom_Frame_center,text='실행')
Bottom_Frame_center_action.pack(side='right', padx=5,pady=5)
Bottom_Frame_right_progress =  LabelFrame(Bottom_Frame_right,text='Loading bar...')
Bottom_Frame_right_progress.pack(side='left', padx=5,pady=5)
Bottom_Frame_right_action = LabelFrame(Bottom_Frame_right,text='실행')
Bottom_Frame_right_action.pack(side='right', padx=5,pady=5)
#title frame
clock = tk.Label(title_frame, font =('Hack',10,'bold'), text="text")
clock.pack(side='right')
time_tick()

Label(title_frame,text='                       CSKIM의 변동성돌파   A.K.A 까꿍이 3.0',font=('Hack',15,'bold')).pack()


#value frame left
values = ['10 분','30 분', '60 분','240 분']
Combobox_min_1 = ttk.Combobox(value_frame_left,height=4,justify='center',state='readonly',values=values)
Combobox_min_1.set('거래기준봉')
btn_combobox_1 = Button(value_frame_left,text='SET',command=btn_w2tmin_1)

const_entry_text = 'CONST NUM'
coin_name_entry_text = 'COIN NAME'
stop_loss_entry_text = 'STOP LOSS'
const_num_entry_1 = Entry(value_frame_left,width=20,justify='center',fg='Grey')
const_num_entry_1.insert(0,const_entry_text)
btn_const_num_set_1 = Button(value_frame_left, text='SET',command=btn_const_1)
coin_name_entry_1 = Entry(value_frame_left,width=20,justify='center',fg='Grey')
coin_name_entry_1.insert(0,coin_name_entry_text)
btn_coin_name_set_1 = Button(value_frame_left, text='SET',command=btn_coin_ticker_1)
stop_loss_entry = Entry(value_frame_left,width=20,justify='center',fg='Grey')
stop_loss_entry.insert(0,'STOP LOSS')
btn_stop_loss_set = Button(value_frame_left, text='SET',command=warn_stoploss)
const_num_entry_1.bind("<FocusIn>", lambda args: focus_in_entry_box(const_num_entry_1))
const_num_entry_1.bind("<FocusOut>", lambda args: focus_out_entry_box(const_num_entry_1,const_entry_text))
coin_name_entry_1.bind("<FocusIn>", lambda args: focus_in_entry_box(coin_name_entry_1))
coin_name_entry_1.bind("<FocusOut>", lambda args: focus_out_entry_box(coin_name_entry_1,coin_name_entry_text))
stop_loss_entry.bind("<FocusIn>", lambda args: focus_in_entry_box(stop_loss_entry))
stop_loss_entry.bind("<FocusOut>", lambda args: focus_out_entry_box(stop_loss_entry,stop_loss_entry_text))

Combobox_min_2 = ttk.Combobox(value_frame_center,height=4,justify='center',state='readonly',values=values)
Combobox_min_2.set('거래기준봉')
btn_combobox_2 = Button(value_frame_center,text='SET',command=btn_w2tmin_2)

const_num_entry_2 = Entry(value_frame_center,width=20,justify='center',fg='Grey')
const_num_entry_2.insert(0,'CONST NUM')
btn_const_num_set_2 = Button(value_frame_center, text='SET',command=btn_const_2)
coin_name_entry_2 = Entry(value_frame_center,width=20,justify='center',fg='Grey')
coin_name_entry_2.insert(0,'COIN NAME')
btn_coin_name_set_2 = Button(value_frame_center, text='SET',command=btn_coin_ticker_2)
stop_loss_entry_2 = Entry(value_frame_center,width=20,justify='center',fg='Grey')
stop_loss_entry_2.insert(0,'STOP LOSS')
btn_stop_loss_set_2 = Button(value_frame_center, text='SET',command=warn_stoploss)
const_num_entry_2.bind("<FocusIn>", lambda args: focus_in_entry_box(const_num_entry_2))
const_num_entry_2.bind("<FocusOut>", lambda args: focus_out_entry_box(const_num_entry_2,const_entry_text))
coin_name_entry_2.bind("<FocusIn>", lambda args: focus_in_entry_box(coin_name_entry_2))
coin_name_entry_2.bind("<FocusOut>", lambda args: focus_out_entry_box(coin_name_entry_2,coin_name_entry_text))
stop_loss_entry_2.bind("<FocusIn>", lambda args: focus_in_entry_box(stop_loss_entry_2))
stop_loss_entry_2.bind("<FocusOut>", lambda args: focus_out_entry_box(stop_loss_entry_2,stop_loss_entry_text))

Combobox_min_3 = ttk.Combobox(value_frame_right,height=4,justify='center',state='readonly',values=values)
Combobox_min_3.set('거래기준봉')
btn_combobox_3 = Button(value_frame_right,text='SET',command=btn_w2tmin_3)

const_num_entry_3 = Entry(value_frame_right,width=20,justify='center',fg='Grey')
const_num_entry_3.insert(0,'CONST NUM')
btn_const_num_set_3 = Button(value_frame_right, text='SET',command=btn_const_3)
coin_name_entry_3 = Entry(value_frame_right,width=20,justify='center',fg='Grey')
coin_name_entry_3.insert(0,'COIN NAME')
btn_coin_name_set_3 = Button(value_frame_right, text='SET',command=btn_coin_ticker_3)
stop_loss_entry_3 = Entry(value_frame_right,width=20,justify='center',fg='Grey')
stop_loss_entry_3.insert(0,'STOP LOSS')
btn_stop_loss_set_3 = Button(value_frame_right, text='SET',command=warn_stoploss)
const_num_entry_3.bind("<FocusIn>", lambda args: focus_in_entry_box(const_num_entry_3))
const_num_entry_3.bind("<FocusOut>", lambda args: focus_out_entry_box(const_num_entry_3,const_entry_text))
coin_name_entry_3.bind("<FocusIn>", lambda args: focus_in_entry_box(coin_name_entry_3))
coin_name_entry_3.bind("<FocusOut>", lambda args: focus_out_entry_box(coin_name_entry_3,coin_name_entry_text))
stop_loss_entry_3.bind("<FocusIn>", lambda args: focus_in_entry_box(stop_loss_entry_3))
stop_loss_entry_3.bind("<FocusOut>", lambda args: focus_out_entry_box(stop_loss_entry_3,stop_loss_entry_text))

#value frame left grid
Combobox_min_1.grid(row=0,column=0,padx=7,pady=11)
btn_combobox_1.grid(row=0,column=1,padx=7,pady=11)
const_num_entry_1.grid(row=1,column=0,padx=7,pady=11)
btn_const_num_set_1.grid(row=1,column=1,padx=7,pady=11)
coin_name_entry_1.grid(row=2,column=0,padx=7,pady=11)
btn_coin_name_set_1.grid(row=2,column=1,padx=7,pady=11)
stop_loss_entry.grid(row=3,column=0,padx=7,pady=11)
btn_stop_loss_set.grid(row=3,column=1,padx=7,pady=11)

Combobox_min_2.grid(row=0,column=0,padx=7,pady=11)
btn_combobox_2.grid(row=0,column=1,padx=7,pady=11)
const_num_entry_2.grid(row=1,column=0,padx=7,pady=11)
btn_const_num_set_2.grid(row=1,column=1,padx=7,pady=11)
coin_name_entry_2.grid(row=2,column=0,padx=7,pady=11)
btn_coin_name_set_2.grid(row=2,column=1,padx=7,pady=11)
stop_loss_entry_2.grid(row=3,column=0,padx=7,pady=11)
btn_stop_loss_set_2.grid(row=3,column=1,padx=7,pady=11)

Combobox_min_3.grid(row=0,column=0,padx=7,pady=11)
btn_combobox_3.grid(row=0,column=1,padx=7,pady=11)
const_num_entry_3.grid(row=1,column=0,padx=7,pady=11)
btn_const_num_set_3.grid(row=1,column=1,padx=7,pady=11)
coin_name_entry_3.grid(row=2,column=0,padx=7,pady=11)
btn_coin_name_set_3.grid(row=2,column=1,padx=7,pady=11)
stop_loss_entry_3.grid(row=3,column=0,padx=7,pady=11)
btn_stop_loss_set_3.grid(row=3,column=1,padx=7,pady=11)


#value frame right ....aka_cat_frame
btn_cat = Button(value_frame_cat_n_balance,image=photo,command=so_cute)
btn_cat.pack(fill='both',side='top',expand=True)
balance_entry = Label(value_frame_cat_n_balance,textvariable=var_balance,width=20)
btn_reset = Button(value_frame_cat_n_balance, text='RESET',command=update_balance)
btn_reset.pack(side='right',padx=7,pady=11)
balance_entry.pack(side='right',padx=7,pady=11)

#text frame
text_1 = Text(text_frame_left,pady=0,padx=0,width=50,yscrollcommand=scrollbar_1.set)
text_1.pack(side='left',expand=True)
text_2 = Text(text_frame_center,pady=0,padx=0,width=50,yscrollcommand=scrollbar_2.set)
text_2.pack(side='left',expand=True)
text_3 = Text(text_frame_right,pady=0,padx=0,width=50,yscrollcommand=scrollbar_3.set)
text_3.pack(side='left',expand=True)


#Bottom Frame
progressbar_1 = ttk.Progressbar(Bottom_Frame_left_progress,maximum=100,mode='indeterminate',length=190)
progressbar_1.pack(side='left', padx=5,pady=5)
btn_reset_1 = Button(Bottom_Frame_left_action, text='RESET-ALL',command=trade_off_1)
btn_reset_1.pack(side='right', padx=5,pady=5)
btn_start_1 = Button(Bottom_Frame_left_action,state='disable', text='START',command=BackThread_start1().start)
btn_start_1.pack(side='right', padx=5,pady=5)
progressbar_2 = ttk.Progressbar(Bottom_Frame_center_progress,maximum=100,mode='indeterminate',length=190)
progressbar_2.pack(side='left', padx=5,pady=5)
btn_reset_2 = Button(Bottom_Frame_center_action, text='RESET-ALL',command=trade_off_2)
btn_reset_2.pack(side='right', padx=5,pady=5)
btn_start_2 = Button(Bottom_Frame_center_action,state='disable', text='START',command=BackThread_start_2().start)
btn_start_2.pack(side='right', padx=5,pady=5)
progressbar_3 = ttk.Progressbar(Bottom_Frame_right_progress,maximum=100,mode='indeterminate',length=190)
progressbar_3.pack(side='left', padx=5,pady=5)
btn_reset_3 = Button(Bottom_Frame_right_action, text='RESET-ALL',command=trade_off_3)
btn_reset_3.pack(side='right', padx=5,pady=5)
btn_start_3 = Button(Bottom_Frame_right_action,state='disable', text='START',command=BackThread_start_3().start)
btn_start_3.pack(side='right', padx=5,pady=5)


root.resizable(False,False)
root.mainloop()

#end by py3.8.8 