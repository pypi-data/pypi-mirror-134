import ctypes
import numpy as np
from sqlalchemy import create_engine
from sqlalchemy import exc
import requests
from random import choice
from datetime import datetime
from datetime import timedelta
from configparser import ConfigParser
import os


class cfg_obj:
    def __init__(self,filename='./alfendiwin.ini'):
        self.now = datetime.now()
        self.filename = filename
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        self.cfg = ConfigParser()
        self.cfg.read(self.filename,encoding='utf8')
        self.db_ip = self.cfg['postgresql']['ip']
        self.db_port = self.cfg['postgresql'].getint('port')
        self.db_uid = self.cfg['postgresql']['uid']
        self.db_pw = self.cfg['postgresql']['password']
        self.db_name = self.cfg['postgresql']['dbName']
        self.linedll_path = self.cfg['linedll']['path']
        self.allee_module_path = self.cfg['allee_module']['path']
        self.momentum_module_path =self.cfg['momentum_module']['path']
        self.fini_file = self.cfg['multicharts']['fini_file']
        self.top10_file = self.cfg['multicharts']['top10_file']
        self.fini_entry_file = self.cfg['multicharts']['fini_entry_file']
        self.engine = None
        self.conn = None
        
    def linkdb(self):
        try:
            self.engine = create_engine('postgresql://%s:%s@%s/%s'%(self.db_uid,self.db_pw,self.db_ip,self.db_name),client_encoding='utf8')
            self.conn = self.engine.connect()
        except (Exception,exc.SQLAlchemyError) as e:
            print(e)
        return self.engine,self.conn

class sql:
    def __init__(self,cfg_obj):
        self.cfg_obj = cfg_obj
        self.engine,self.conn = self.cfg_obj.linkdb()

    def __enter__(self):
        
        self.engine,self.conn = self.cfg_obj.linkdb()
        return self.engine,self.conn
        

    def __exit__(self,type,value,traceback):
        self.engine.dispose()

def prompt_process_end(cfg_obj):
    if cfg_obj.engine != None:
        cfg_obj.engine.dispose()
    print("---Whole Process End, total take %s time to finish--"%str(datetime.now()-cfg_obj.now))

# To Short function call-----------------------
def http_headers():
    return {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}



#String handling-----------------
def to_str(var):
    var=var
    if type(var) is list:
        return str(var)[1:-1] # list
    if type(var) is np.ndarray:
        try:
            return str(list(var[0]))[1:-1] # numpy 1D array
        except TypeError:
            return str(list(var))[1:-1] # numpy sequence
    return str(var) # everything else

def to_date(date):
    if type(date) is datetime or type(date) is date:
        return date
    else:
        datestr = regular_datestr(date)
        return datetime.strptime(datestr,"%Y/%m/%d")

def regular_datestr(date,sep='/'):
    if type(date) is datetime or type(date) is date:
        new_date = date
    else:
        datestr = date.replace("/","")
        datestr = datestr.replace("-","")
        datestr = datestr.replace(" ","")
        try:
            new_date = datetime.strptime(datestr,'%Y%m%d')
        except:
            print("日期格式錯誤")
    return  str(new_date.year) + sep + str(new_date.month).zfill(2) + sep + str(new_date.day).zfill(2)
  
#用來消除爬蟲過程中常會出現comma 
def df_remove_comma(value):
    value_as_string = str(value)
    return value_as_string.replace(',', '')

#用來消除各種不要的字元
#好用函數
def remove_extra_char(val,removal):
    instr = to_str(val)
    transtab = str.maketrans('','',removal)
    return instr.translate(transtab)
#用來消除 $sign    
def df_remove_dollarsign(value):
    value_as_string = str(value)
    return value_as_string.replace(r'\$', '')
#Utility------------------

#發 Line訊息
#20220110 目前只設定在windows 下執行
def sendMessage(msg):
    
    cfg = cfg_obj()
    if os.name =='nt':
        dll = ctypes.windll.LoadLibrary(cfg.linedll_path)
        send_msg=bytes(msg,encoding='big5')
        try:
            dll.SendLineMessage(send_msg)
            return 1
        except:
            return -1
    else:
        return 1
#        engine,conn = cfg.linkdb()
#        line_flag = 1
#        now = datetime.now()
#        conn.execute("insert into line_message (message,msgdate,flag)values (%s,%s,%s)",(msg,now,line_flag))
#        engine.dispose()
       
#輸入1-26間的數字, 返回對應長度的英文字串    
def alphabet_list(num):
    import string
    d = dict.fromkeys(string.ascii_uppercase,0)
    a = [i for i in d.keys()]
    a.sort
    return a[0:num]


def nthweekday(datestr,nth,weeknum):
    #首先要把字串標準化
    datestr = datestr
    datestr = regular_datestr(datestr)
    thisdate = datetime.strptime(datestr,'%Y/%m/%d')
    thisday = thisdate.day
    
    #每月一號
    firstday_of_month = thisdate - timedelta(days=thisday-1)
    #每月一號為星期幾
    weekday_of_month = firstday_of_month.weekday()
    if weekday_of_month <= weeknum:
        days = (weeknum - weekday_of_month) + (nth-1)*7
    else:
        days = (weeknum - weekday_of_month) + nth*7
    return firstday_of_month + timedelta(days=days)


def requests_get_wrapper(url,timeout=5):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    cfg = cfg_obj()
    return requests.get(url,'lxml',headers=headers,timeout=timeout)

def requests_post_wrapper(url,payload,timeout=5):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    cfg = cfg_obj()
    return requests.post(url,headers=headers,data=payload,timeout=timeout)


def remove_empty_lines(filename):
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open(filename) as in_file, open(filename, 'r+') as out_file:
        out_file.writelines(line for line in in_file if line.strip())
        out_file.truncate()
        

   




   