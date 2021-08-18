import datetime
import os
import sys
from tkinter import*
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

import pyupbit

access = 'ACCESS' ###  '' 안에 ACCESS 키를
secret = 'SECRET' ###  '' 안에 SECRET 키를 넣어주세요!
server_url = 'https://upbit.com/home'

upbit = pyupbit.Upbit(access,secret)

########################################################################################################
########################################################################################################
########################################################################################################

pwr_button = [[1,1,1],[1,1,1],[1,1,1]]
balance = 'BALANCE'
tickers = pyupbit.get_tickers()

########################################################################################################
########################################################################################################
########################################################################################################

def resource_path(realative_path): # 현재 파이썬 파일의 절대경로를 받기위한 함수
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

def update_balance(var): ## 바뀔 var 위치를 넣어주어야함
    balance = upbit.get_balance('KRW')
    int_bal = format(balance,',.0f') ## upbit.get_balance 를 통해 나오는 상수값을 정수화시키고, 세미콜론을 찍어줌
    str_bal = ('BALANCE  :' +str(int_bal)+' \\')
    var.set(str_bal)

def time_tick(clock): ## 변화할 clock 위치를 넣어주어야함
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # now = time.ctime(time.time())
    clock.config(text=now)
    clock.after(1000,time_tick) ## after 는 1000ms 이후에 time_tick 을 실행시키겠다는 소리임 (1초마다 시간을 갱신한다는소리)

def focus_out_entry_box(widget, widget_text): ## 버튼을 누르면 해당 버튼 비활성화를 위해
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)

def focus_in_entry_box(widget): ## focus out 과 반대로 stop 버튼을 누르면 다시 재활성화를 위해
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)

def sorting_thread(num):
    if num == 1:
        pass



########################################################################################################
###############################################  함수부  ###############################################
########################################################################################################

# def btn_const_1(thread,text):
#     global const_num_1
#     global pwr_button
#     b1_1 = 0
#     const_num_1 = const_num_entry_1.get()
#     if isNumber(const_num_1) is False:
#         msgbox.showwarning('아이쿠!!!','숫자가 아닌 값이 입력되었습니다. \nCONST NUM 값을 기본값인 [ 1.0 ]로 입력합니다!')
#         const_num_1 = 1
#     float(const_num_1)
#     text.insert(END,'[[  '+str(const_num_1)+'  ]] 변동성 상수 SET\n')
#     text.see(END)
#     btn_const_num_set_1.config(state='disable')
#     if b1_1+b2_1+b3_1 ==0:
#         btn_start_1.config(state='normal')



########################################################################################################
##############################################   GUI  ##################################################
########################################################################################################

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