# encoding: UTF-8
import sys
from datetime import datetime
from threading import *
from .EventManager import *
from QUANTAXIS.QASignal import QA_Signal_eventManager,QA_Signal_events


# this is a standard module of writing signal


#事件名称  
Signal = "Signal"

#事件源 
class PublicAccounts:
    def __init__(self,eventManager):
        self.eventManager = eventManager

    def QA_signal_send_market_deal_success(self):
        #事件对象，交易成功
        event = QA_Signal_events(type_=Signal)
        #event.dict["Signal"] = u'如何写出更优雅的代码\n'
        #发送事件
        self.eventManager.SendEvent(event)
        print ('aaa')
    def QA_signal_send_account_change(self):
        #事件对象，账户改变
        event = QA_Signal_events(type_=Signal)
        #event.dict["Signal"] = u'如何写出更优雅的代码\n'
        #发送事件
        self.eventManager.SendEvent(event)
        print ('aaa')
    def QA_signal_send_risk_finish(self):
        #事件对象，风险评估完成
        event = QA_Signal_events(type_=Signal)
       # event.dict["Signal"] = u'如何写出更优雅的代码\n'
        #发送事件
        self.eventManager.SendEvent(event)
        print ('aaa')
    def QA_signal_send_portfolio_finish(self):
        #事件对象，组合控制完成
        event = QA_Signal_events(type_=Signal)
        #event.dict["Signal"] = u'如何写出更优雅的代码\n'
        #发送事件
        self.eventManager.SendEvent(event)
        print ('aaa')
    def QA_signal_send_strategy_update(self):
        #事件对象，策略数据更新
        event = QA_Signal_events(type_=Signal)
        #event.dict["Signal"] = u'如何写出更优雅的代码\n'
        #发送事件
        self.eventManager.SendEvent(event)
        print ('aaa')
    def QA_signal_send_multi_strategy_change(self):
        #事件对象，多策略更新
        event = QA_Signal_events(type_=Signal)
        event.dict["Signal"] = 'change'
        #发送事件
        self.eventManager.SendEvent(event)
        print ('send event')
    def QA_signal_send_event(self):
        event = QA_Signal_events(type_=Signal)
        event.dict["Signal"] = 'change'
        #发送事件
        self.eventManager.SendEvent(event)



#监听器 订阅者
class Listener:
    def __init__(self,username):
        self.username = username

    #监听器的处理函数 

    def QA_signal_receive_market(self,event):
        print('receive deal')
        print(u'%s 收到了这个消息' % self.username)
    def QA_signal_receive_account(self,event):
        print('receive change')
        print(u'%s 收到了这个消息' % self.username)
    def QA_signal_receive_risk(self,event):
        print('receive change')
        print(u'%s 收到了这个消息' % self.username)
    def QA_signal_receive_portfolio(self,event):
        print('receive change')
        print(u'%s 收到了这个消息' % self.username)
    def QA_signal_receive_strategy(self,event):
        print('receive change')
        print(u'%s 收到了这个消息' % self.username)
    def QA_signal_receive_multi(self,event):
        print('receive change')
        print(u'%s 收到了这个消息' % self.username)
    def QA_signal_receive_event(self,event):
        print('receive change')
        print(u'%s 收到了这个消息' % self.username)
"""测试函数"""
#--------------------------------------------------------------------
def QA_signal_usual_model():
    listner1 = Listener("market") #订阅者1
    listner2 = Listener("account")#订阅者2
    listner3 = Listener("strategy")#订阅者2


    eventManager = QA_Signal_eventManager()

    #绑定事件和监听器响应函数
    eventManager.AddEventListener(Signal, listner1.QA_signal_receive_account)
    eventManager.AddEventListener(Signal, listner1.QA_signal_receive_market)
    eventManager.AddEventListener(Signal, listner2.QA_signal_receive_market)
    eventManager.AddEventListener(Signal, listner2.QA_signal_receive_portfolio)
    eventManager.AddEventListener(Signal, listner3.QA_signal_receive_risk)
    eventManager.AddEventListener(Signal, listner3.QA_signal_receive_portfolio)
    eventManager.AddEventListener(Signal, listner3.QA_signal_receive_account)
    eventManager.Start()

    publicAcc = PublicAccounts(eventManager)
    
    for i in range(1,10,1):
        timer = Timer(2, publicAcc.QA_signal_send_account_change)
        timer = Timer(2, publicAcc.QA_signal_send_market_deal_success)
        timer = Timer(2, publicAcc.QA_signal_send_multi_strategy_change)
        timer = Timer(2, publicAcc.QA_signal_send_portfolio_finish)
        timer = Timer(2, publicAcc.QA_signal_send_risk_finish)
        timer = Timer(2, publicAcc.QA_signal_send_strategy_update)
        timer.start()


