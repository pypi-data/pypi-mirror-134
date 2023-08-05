from datetime import datetime
from datetime import timedelta
import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
from io import StringIO
from sqlalchemy import create_engine
from sqlalchemy import exc
import numpy as np
from io import BytesIO
from zipfile import ZipFile
import util
import sql



def twse_parser(in_text,sepnum,sep='",',filter_str='='):
    df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                     for i in in_text.split('\n') 
                                     if len(i.split(sep)) == sepnum and i[0] != filter_str])), header=0)
    return df

def twse_fund_parser(in_text,sepnum,sep='",',filter_str='"',first_header_str='證'):
    df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                    for i in in_text.split('\n') 
                    if len(i.split('",')) == sepnum and (i[0] != filter_str or i[1]== first_header_str)])), header=0)
    return df
def tradingday_check_by_history(cfg_obj,datestr):
    datestr = datestr
    datestr = util.regular_datestr(datestr)
    if datestr > '2019/01/30':
        trading = tradeday_check_by_datestr(datestr)
    else:
        #conn = util.engine_conn(cfg_obj)[1]
        conn = cfg_obj.conn
        rows = conn.execute("select trade_date from twse_stock_ohlc where stockid = '1101' and \
            trade_date = %s ",datestr).rowcount
        if rows == 0:
            trading = -1
        else:
            trading = 1
    
    return trading
def tradeday_check_by_datestr(date):
    last_release_date = last_release_date_by_soup()
    datestr = util.regular_datestr(date)
    if datestr > last_release_date:
        trade_day = -1
    else:
    
    #print(datestr)
        url = "https://www.taifex.com.tw/cht/3/optDailyMarketReport?queryType=2&marketCode=0&dateaddcnt=-1&commodity_id=TXO&queryDate=" + datestr
        headers = util.http_headers()
        checkres = requests.get(url,"lxml",headers=headers)
        check_result= re.findall(r'查無資料',checkres.text)
        if len(check_result) >=1:
            #當天無交易
            trade_day = -1
        else:
            #當天有交易
            trade_day = 1
    return trade_day

#最新公佈三大法人進出資料日期, 因為大額交易日資料較晚公佈, 所以以大額交易日公佈日期為主
def last_release_date():
    url = "https://www.taifex.com.tw/cht/3/largeTraderFutQry"
    headers=util.http_headers()
    res = requests.get(url,"lxml",headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    datestr = soup.find_all(id="queryDate")[0].get('value')
    #datestr = re.findall(r"\d{4}/\d{1,2}/\d{1,2}",res.text)[1]
    return util.regular_datestr(datestr)
    
def last_release_date_by_soup():
    url = "https://www.taifex.com.tw/cht/3/largeTraderFutQry"
    headers=util.http_headers()
    #2019/01/29 測試OK可以使用
    try:
        res = requests.get(url,'lxml',headers=headers)
        soup = BeautifulSoup(res.content,'lxml')
        datestr = re.findall(r'\d{4}/\d{1,2}/\d{1,2}',soup.find_all('p','12redbbb')[0].text)[0]
        return util.regular_datestr(datestr)
    except Exception as e:
        print("last_release_date_by_soup function error")
        print(e)



#根據指定日期 去證交所把指定日期的三大法人進去資料抓回來
def load_twse_big3(cfg_obj,datestr,maxtry=10,timer=30):
    return_val = -1
    datestr = util.regular_datestr(datestr,"")
    url="https://www.twse.com.tw/fund/T86?response=csv&selectType=ALL&date=" + datestr
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    flow = 1
    while flow <= maxtry:
        try:
            res = util.requests_get_wrapper(url)
            if datestr > '20171214':
                df = twse_parser(res.text,20)
            elif datestr > '20141128':
               df = twse_parser(res.text,17)
            else:
                df = twse_parser(res.text,13)
            flow = maxtry + 1
            parser_error = 0
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            print(e)
            print("%s Has block by 證交所"%datestr)
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  

    if parser_error == 1:
        return return_val
    #columns'證券代號','證券名稱','外陸資買進股數(不含外資自營商)','外陸資賣出股數(不含外資自營商)','外陸資買賣超股數(不含外資自營商)',
    #'自營商買進股數' '資自營商賣出股數' '資自營商買賣超股數'    '信買進股數'     '信賣出股數'     '信買賣超股數'
    #'自商買賣超股數''營商買進股數(自行買賣)''自營商賣出股數(自行買賣)'' 自營商買賣超股數(自行買賣)'' 自營商買進股數(避險)'
    #'自營商賣出股數(避險)'' 自營商買賣超股數(避險)''   三大法人買賣超股數'
    if datestr > '20171214':
        df = df.iloc[:,0:19]
    elif datestr > '20141128':
        df = df.iloc[:,0:16]
    else:
        df = df.iloc[:,0:12]
    
    df.reset_index(drop=True, inplace=True)
    if datestr > '20171214':
        col_header=["stockid","cname","fini_in","fini_out","fini_net","fdealer_in","fdealer_out","fdealer_net","inv_in","inv_out","inv_net",\
                "dealer_net","dealer_sin","dealer_sout","dealer_snet","dealer_hin","dealer_hout","dealer_hnet","big3_net"]
    elif datestr > '20141128':
        col_header=["stockid","cname","fini_in","fini_out","fini_net","inv_in","inv_out","inv_net",\
                "dealer_net","dealer_sin","dealer_sout","dealer_snet","dealer_hin","dealer_hout","dealer_hnet","big3_net"]
    else:
        col_header=["stockid","cname","fini_in","fini_out","fini_net","inv_in","inv_out","inv_net",\
                "dealer_net","dealer_sin","dealer_sout","big3_net"]
    df.columns= col_header
   
    df = df.applymap(lambda x: util.remove_extra_char(x,","))

    df = df.apply(pd.to_numeric, errors='ignore')
    df['trade_date'] = datestr
    print("%s準備寫入資料庫"%datestr)
    trans = conn.begin()
    try:
        #conn.execute('delete from twse_stock_big3_temp')
        df.to_sql('twse_stock_big3',engine,index=False,if_exists='append')
        #sql.insert_2col_diff(conn,"twse_stock_big3_temp","twse_stock_big3","trade_date","stockid")
        #sql.insert_diff(conn,'twse_stock_big3_temp','twse_stock_big3','trade_date')
        #conn.execute('delete from twse_stock_big3_temp')
        trans.commit()
        print("%s is done!"%datestr) 
        return_val = 1
    except(Exception, exc.SQLAlchemyError) as error:
        print(error)
        trans.rollback()
        print("%s is fail...!"%datestr) 
    
    return return_val

def load_bigtrader_oi_by_date(cfg_obj,datestr,maxtry=10,timer=60):
    datestr = datestr
    return_value = -1
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    url = "https://www.taifex.com.tw/enl/eng3/largeTraderFutDown"
    headers = cfg_obj.headers
    payload = {"queryStartDate": datestr,"queryEndDate": datestr}
    flow = 1
    while flow <= maxtry:
        print('準備抓%s十大交易人資料'%datestr)
        try:
            res = requests.post(url,headers=headers,data=payload,stream=True)
            names=['trade_date','commodityid','settlement','category','top5_buy','top5_sell','top10_buy','top10_sell','oi']
            df = pd.read_csv(StringIO(res.text),dtype=object,names=names)
            df = df.iloc[1:-4,:]
            df.reset_index(drop=True, inplace=True)
            for i in range(0,df.shape[0],1):
                for j in range(0,df.shape[1],1):
                    df.iloc[i,j] = util.to_str(df.iloc[i,j]).replace(" ",'')
            df2 = df[(~df['top5_buy'].isin(['-']))]
            df2.apply(pd.to_numeric, errors='ignore')
            parser_error = 0 
            flow = 1
            break
        except Exception as e:

            print(e)
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    if parser_error == 1:
        return return_value
    trans = conn.begin()
    try:
        df2.to_sql('bigtrader',engine,index=False,if_exists='append')
        trans.commit()
        return_value = 1
    except(Exception, exc.SQLAlchemyError)as error:
        trans.rollback()
        return_value = -1
        print(error)
    print("%s is done!"%datestr)
    return return_value

def load_taifex_future_ticks_by_date(cfg_obj,datestr):
    datestr = datestr
    return_val = -1
    #cfg = util.cfg_obj('D:/Tools/momentum.ini')
    #engine,conn = util.engine_conn(cfg_obj)
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    datestr = util.regular_datestr(datestr)
    datestr_underscore = util.regular_datestr(datestr,"_")
    headers= util.http_headers()
    

    baseurl = "https://www.taifex.com.tw/cht/3/futPrevious30DaysSalesData"
    res = util.requests.get(baseurl,'lxml',headers=headers)
    res_find = re.findall(datestr,res.text)
    if len(res_find) == 2:
       # re.findall(datestr,res.text)[0]
        url = "https://www.taifex.com.tw/file/taifex/Dailydownload/Dailydownload_eng/Daily_" +datestr_underscore +".zip"
        res = util.requests.get(url,'lxml',headers=headers)
        f = ZipFile(BytesIO(res.content))
        data = f.read(f.namelist()[0])
        text_obj = data.decode('UTF-8')
        df = util.pd.read_csv(StringIO(text_obj),dtype=object)
        df1 = df.iloc[:,0:6].copy()
        df1.columns=['trade_date','commodityid','settlement','trade_time','price','vol']
        df1['commodityid']=df1.commodityid.str.replace(' ','',regex=True)
        df1['settlement']=df1.settlement.str.replace(' ','',regex=True)
        df1[['price','vol']] = df1[['price','vol']].apply(util.pd.to_numeric)
        trans = conn.begin()
        
        try:
            df1.to_sql('taifex_future_ticks',engine,index=False,if_exists='append')
            trans.commit()
            
            return_val = 1
        except Exception as e:
            trans.rollback()
            
            print(e)
    else:
        print("日期錯誤")
        

    #conn.close()
    print("-- Process End--")
    return return_val

def taifex_contract(datestr):
    datestr = datestr
    datestr = util.regular_datestr(datestr)
    #datestr在月3rd 週三前後關係
    this_settlement_date = util.nthweekday(datestr,3,2)
    if datetime.strptime(datestr,'%Y%m%d') <= this_settlement_date:
        return util.to_str(this_settlement_date.year)+util.to_str(this_settlement_date.month)
    else:
        nextmonth = this_settlement_date + timedelta(months=1)
        return util.to_str(nextmonth.year)+util.to_str(nextmonth.month)

def load_twse_margin_transaction(cfg_obj,datestr,maxtry=10,timer=60):
    return_val = -1
    datestr = datestr
    datestr = util.regular_datestr(datestr,"")
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    url = "https://www.twse.com.tw/en/exchangeReport/MI_MARGN?response=csv&selectType=ALL&date=" + datestr
    flow = 1
    while flow <= maxtry:
        try:
            res=util.requests_get_wrapper(url)    
            df = twse_parser(res.text,14)
            df = df.iloc[:,0:13]
            df.reset_index(drop=True, inplace=True)
            col_header = ["stockid","new_long","redemption_long","outstanding_long","preremain_long","remain_long",\
               "limit_long","redemption_short","new_short","outstanding_short","preremain_short","remain_short",\
               "limit_short"]
            col_to_num = ["new_long","redemption_long","outstanding_long","preremain_long","remain_long",\
               "limit_long","redemption_short","new_short","outstanding_short","preremain_short","remain_short",\
               "limit_short"]
            df.columns= col_header
            df = df.applymap(util.df_remove_comma)
            df[col_to_num] = df[col_to_num].apply(util.pd.to_numeric)
            df['trade_date']=datestr
            flow = maxtry + 1
            parser_error = 0
            print(df)
            break
        except Exception as e:
            print("is blocked by TWSE %d times"%flow)
            
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
            
    if parser_error == 1:
        return return_val
    trans = conn.begin()
    try:
        #conn.execute("delete from twse_margin_transaction_temp")
        df.to_sql('twse_margin_transaction',engine,index=False,if_exists='append')
        #sql.insert_diff(conn,'twse_margin_transaction_temp','twse_margin_transaction','trade_date')
        #conn.execute("delete from twse_margin_transaction_temp")
        trans.commit()
        print("%s twse_margin_transaction update done..."%datestr)
        return_val  = 1
    except (Exception,exc.SQLAlchemyError) as e:
        print(e)
        trans.rollback()
        print("%s twse_margin_transaction update fail..."%datestr)
    
    return return_val

def twse_bad_code_removal(val):
    if val:
        mo = re.search(r'\d+',val)
        if mo:
            return True
        else:
            return False
    else:
        return False

def load_twse_isin_code(cfg_obj,groupid,maxtry=10,timer=30):
    return_val = -1
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    url = 'https://isin.twse.com.tw/isin/C_public.jsp?strMode=' + groupid
    flow = 1
    while flow <= maxtry:
        try:
            res = util.requests_get_wrapper(url)
            
            df = util.pd.read_html(res.text,header=0)[0]
            if groupid == '2' or groupid == '4' or groupid == '5' or groupid == '6':
                col_headers =["stockid","isin","date_listed","market","stock_group","cfi","remarks"]
                cols = 7
            elif groupid == '1':
                col_headers =["stockid","isin","date_listed","stock_group","cfi","remarks"]
                cols = 6
            elif groupid == '3':
                col_headers =["stockid","isin","date_listed","settlement_date","interest","market","stock_group","cfi","remarks"]
                cols = 9
            elif groupid == '7' or groupid == '9' or groupid == '10':
                col_headers =["stockid","isin","date_listed","cfi","remarks"]
                cols = 5
            elif groupid == '8':
                col_headers =["stockid","isin","date_listed","market","cfi","remarks"]
                cols = 6
                df = df.iloc[:,0:cols]

            df.columns = col_headers
            df = df[df['isin'].apply(twse_bad_code_removal)]
            df.reset_index(drop=True, inplace=True)
            df1 = util.pd.merge(df['stockid'].str.split('　',expand=True),df.iloc[:,1:cols],how='left',left_index=True,right_index=True)
            #col_headers =["stockid","cname","isin","date_listed","market","group","cfi","remarks"]
            col_headers.insert(1,'cname')
            df1.columns=col_headers
            df1 = df1.iloc[0:,:]
            parser_error = 0
            flow = maxtry + 1
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    if parser_error == 1:
        return return_val

    trans = conn.begin()
    
    try:
        conn.execute("delete from twse_stockid_temp")
        df.to_sql('twse_stockid_temp',engine,index=False,if_exists='append')
        sql.insert_diff(conn,'twse_stockid_temp','twse_stockid','stockid')
        conn.execute("delete from twse_stockid_temp")
        trans.commit()
        return_val = 1
    except (Exception,exc.SQLAlchemyError) as e:
        trans.rollback()
        print("DB insert Error")
        print(e)
        
    
    print('--%s Process End---'%groupid)
    return return_val

def load_twse_sbl_short(cfg,datestr,maxtry=10,timer=30):
    return_val = -1
    engine=cfg.engine
    conn = cfg.conn
    datestr = util.regular_datestr(datestr,"")
    url = "https://www.twse.com.tw/exchangeReport/TWTASU?response=csv&lang=en&date=" + datestr
    flow = 1
    while flow <= maxtry:
        
        try:
            res = util.requests_get_wrapper(url)
            df = twse_parser(res.text,6)
            df = df.iloc[:,0:5]
            df.reset_index(drop=True, inplace=True)
            col_header = ["stockid","margin_short","margin_short_vol","sbl_short","sbl_short_vol"]
            df.columns= col_header
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                        df.iloc[i,j] = util.to_str(df.iloc[i,j]).replace(',','')
            del col_header[0]
            df[col_header]= df[col_header].apply(util.pd.to_numeric)
            df['trade_date']=datestr
            
            flow = maxtry + 1
            parser_error = 0
            break
        except Exception as e:
            print("%sHas block by 證交所"%datestr)
            print(e)
            parser_error = 1
            flow = flow + 1
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    
    if parser_error == 1:
        return return_val       
    print("%s準備寫入資料庫"%datestr)
    trans = conn.begin()
    try:
        #conn.execute("delete from twse_sbl_short_temp")
        df.iloc[:-1,:].to_sql('twse_sbl_short',engine,index=False,if_exists='append')
        #sql.insert_2col_diff(conn,'twse_sbl_short_temp','twse_sbl_short','trade_date','stockid')
        #conn.execute("delete from twse_sbl_short_temp")
        trans.commit()
        print("%s TWSE SBL-Short update done!"%datestr)
        return_val = 1

    except (Exception,exc.SQLAlchemyError) as e:
        trans.rollback()
        print("%s TWSE SBL-Short update Fail!"%datestr)
        print(e)
        return_val = -1

    return return_val


def load_taifex_future_bigtrader(cfg_obj,datestr,maxtry=10,timer=60):
    datestr = util.regular_datestr(datestr)
    return_val = -1
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    url = "https://www.taifex.com.tw/enl/eng3/largeTraderFutDown"
    payload = {"queryStartDate": datestr,"queryEndDate": datestr}
    
    flow = 1
    while flow <= maxtry:
        try:
            res = util.requests_post_wrapper(url,payload)
            df = twse_parser(res.text,9,",","*")
            col=["trade_date","commodityid","settlement","category","top5_buy","top5_sell","top10_buy","top10_sell","oi"]
            df.columns = col
            df = df[(~df['oi'].isin(['-']))]
            df = df.dropna()
            parser_error = 0
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"ConnectionRefusedError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    if parser_error == 1:
        return return_val        
    trans = conn.begin()
    try:
        #conn.execute("delete from taifex_future_bigtrader_temp")
        df.to_sql('taifex_future_bigtrader',engine,index=False,if_exists='append')
        #sql.insert_diff(conn,'taifex_future_bigtrader_temp','taifex_future_bigtrader','trade_date')
        #conn.execute("delete from taifex_future_bigtrader_temp")
        trans.commit()
        return_val= 1
        print("%s is done!"%datestr)
    except (Exception,exc.SQLAlchemyError) as e:
        trans.rollback()
        print(e)
    
    return return_val

def twse_ohlc_bad_character_removal(value):
    value_as_string = str(value)
    return value_as_string.replace(',', '').replace('+','').replace('--','').replace('X','')

def load_twse_ohlc(cfg,date,stockid,maxtry=10,timer=30):
    return_val = -1
    engine = cfg.engine
    conn = cfg.conn
    datestr = util.regular_datestr(date)
    thisday = datetime.strptime(datestr,"%Y/%m/%d")
    thisday_str = str(thisday.year)+str(thisday.month).zfill(2)+"01"
    url = "https://www.twse.com.tw/en/exchangeReport/STOCK_DAY?response=csv&stockNo=" \
             +stockid +"&date=" + thisday_str
    flow = 1
    while flow <= maxtry:
        try:
            res = util.requests_get_wrapper(url)
            df = twse_parser(res.text,10)
            df = df.iloc[:,0:9]
            col_headers= ["trade_date","vol","amount","oprice","hprice","lprice","cprice","price_change","transaction"]
            col_to_num=["vol","amount","oprice","hprice","lprice","cprice","price_change","transaction"]
            df.columns = col_headers
            df = df.applymap(twse_ohlc_bad_character_removal)
            del col_headers[0]
            df[col_to_num] = df[col_to_num].apply(util.pd.to_numeric)
            df['stockid'] = stockid
            flow = maxtry + 1
            parser_error = 0
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            print("%s parse error"%thisday_str)
            print(e)
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
            
    if parser_error == 1:
        return -1
    #print("%s準備寫入資料庫"%thisday_str)
    trans = conn.begin()
    try:
        conn.execute("delete from twse_stock_ohlc_temp")
        
        df.to_sql('twse_stock_ohlc_temp',engine,index=False,if_exists='append')
        
        sql.insert_2col_diff(conn,'twse_stock_ohlc_temp','twse_stock_ohlc','trade_date','stockid')
        #conn.execute("insert into twse_stock_ohlc select * from twse_stock_ohlc_temp t1 where \
         #    not exists (select trade_date from twse_stock_ohlc t2 where t1.trade_date = t2.trade_date)")
       
        conn.execute("delete from twse_stock_ohlc_temp")
       
        trans.commit()
        return_val = 1
    except (Exception,exc.SQLAlchemyError) as sql_error:
        print(sql_error)
        trans.rollback()
        

    return return_val

def load_taifex_bigtrader(cfg,date,maxtry=10,timer=30):
    return_val = -1
    engine = cfg.engine
    conn = cfg.conn
    headers = cfg.headers
    datestr = util.regular_datestr(date)
    url = "https://www.taifex.com.tw/enl/eng3/largeTraderFutDown"
    payload = {"queryStartDate": datestr,"queryEndDate": datestr}
    flow = 1
    while flow <= maxtry:
        try:
            res = requests.post(url,headers=headers,data=payload,stream=True)
            names=['trade_date','commodityid','settlement','category','top5_buy',\
                    'top5_sell','top10_buy','top10_sell','oi']
            df = pd.read_csv(StringIO(res.text),dtype=object,names=names)
            df = df.iloc[1:-4,:]
            df2 = df[(~df['top5_buy'].isin(['-']))]
            df2.apply(pd.to_numeric, errors='ignore')
            parser_error = 0
            break
        except Exception as e:
            parser_error = 1
            flow = flow + 1
            print("%s parse error!"%datestr)
            print(e)
            if len(re.findall(r"ConnectionRefusedError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    if parser_error == 1:
        return -1       
    trans = conn.begin()
    try:
        print("%s is ready to insert into taifex_bigtrader"%datestr)
        conn.execute("delete from taifex_bigtrader_temp")
        df2.to_sql('taifex_bigtrader_temp',engine,index=False,if_exists='append')
        sql.insert_diff(conn,'taifex_bigtrader_temp','taifex_bigtrader','trade_date')
        conn.execute("delete from taifex_bigtrader_temp")
        trans.commit()
        return_val  = 1
    except (Exception,exc.SQLAlchemyError) as e:
        trans.rollback()
        print(e)
    return return_val

def load_twse_daily_stock_ohlc(cfg,datestr,maxtry=10,timer=30):
    return_val = -1
    datestr = util.regular_datestr(datestr,"")
    engine = cfg.engine
    conn = cfg.conn

    url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&type=ALL&date=" + datestr

    flow = 1
    while flow <= maxtry:
        
        try:
            
            res = util.requests_get_wrapper(url)
            df = twse_parser(res.text,17,'",','*')
            df = df.applymap(lambda x: util.remove_extra_char(x,',="') )
            col_headers = util.alphabet_list(17)
            df.columns = col_headers
            df = df[['A','C','D','E','F','G','H','I','J','K','P']]
            col_headers= ["stockid","vol","transaction","amount","oprice","hprice","lprice","cprice","updn","price_change","pe"]
            df.columns = col_headers
            df = df[(~df['oprice'].isin(['--']))]
            col_headers = ['vol','transaction','amount','oprice','hprice','lprice','cprice',"price_change",'pe']
            col_headers = ['vol','transaction','amount','oprice','hprice','lprice','cprice',"price_change"]

            df['updn'] = df['updn'].apply(lambda x:util.remove_extra_char(x,'X+nan'))
            df['price_change'] = df[['updn','price_change']].apply(lambda x: ''.join(x),axis=1)
            

            df['trade_date']=util.regular_datestr(datestr)
            df = df.iloc[:,np.r_[0:8,9:12]]
            parser_error = 0
            break
        except Exception as e:
            print("%s is block by 證交所"%datestr)    
            print(e)
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"NewConnectionError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)    
    if parser_error == 1:
        return return_val
    trans = conn.begin()
    try:
        
        #conn.execute("delete from twse_stock_ohlc_temp")
        #df.to_sql("twse_stock_ohlc_temp",engine,index=False,if_exists='append')
        #sql.insert_2col_diff(conn,"twse_stock_ohlc_temp","twse_stock_ohlc","trade_date","stockid")
        #conn.execute("delete from twse_stock_ohlc_temp")
        df.to_sql("twse_stock_ohlc",engine,index=False,if_exists='append')
        trans.commit()
        print("%s is done!"%datestr) 
        return_val = 1
    except (Exception,exc.SQLAlchemyError) as sql_error:
        trans.rollback()
        print(sql_error)
    
    return return_val

def load_taifex_future_big3(cfg,datestr,maxtry=10,timer=30):
    return_val = -1
    engine = cfg.engine
    conn = cfg.conn
    datestr = util.regular_datestr(datestr)
    date = util.to_date(datestr)
    year = date.year
    month = date.month
    day = date.day
    firstDate = util.regular_datestr(str(int(year-3)) + str(month)+str(day)) + " 00:00"
    lastDate = datestr + " 00:00"
    url = "https://www.taifex.com.tw/enl/eng3/futContractsDateDown"
    payload = {"firstDate": firstDate,"lastDate":lastDate,\
                "queryStartDate": datestr,"queryEndDate": datestr,"commodityId":""}
    flow = 1
    while flow <= maxtry:
        try:
            res = util.requests_post_wrapper(url,payload)
            #res = util.requests.post(url,headers=headers,data=payload,stream=True)
            df = twse_parser(res.text,15,",","*")
            #df = df.iloc[:,0:15]
            col = ["trade_date","commodityid","category",\
                    "long_vol","long_amt","short_vol","short_amt","net_vol","net_amt",\
                    "long_oi","long_oi_amt","short_oi","short_oi_amt","net_oi","net_oi_amt"]

            df.columns = col
            #df = df[(~df['net_vol'].isin(['-']))]
            dicts = {"Dealers":"dealer","InvestmentTrustCompanies":"investment_trust","FINI":"fini"}
            df['category'] = df['category'].apply(lambda x: dicts[x])
            df = df.query('long_vol + short_vol + net_vol + long_oi + short_oi + net_oi >0 ')
            parser_error = 0
            flow = maxtry + 1
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            print(e)
            if len(re.findall(r"ConnectionRefusedError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)
    if parser_error == 1:
        return return_val
    trans = conn.begin()
    try:
        #conn.execute("delete from taifex_future_big3_temp")
        df.to_sql('taifex_future_big3',engine,index=False,if_exists='append')
        #sql.insert_diff(conn,'taifex_future_big3_temp','taifex_future_big3','trade_date')
        #conn.execute("delete from taifex_future_big3_temp")
        trans.commit()
        return_val = 1
        print("%s TAIFEX Future Big3 update done"%datestr)
    except (Exception, util.exc.SQLAlchemyError) as e:
        trans.rollback()
        print(e)
        print("%s SQL Future Big3 update error"%datestr)

    return return_val

def load_taifex_opt_bigtrader(cfg_obj,datestr,maxtry=10,timer=60):
    datestr = util.regular_datestr(datestr)
    return_val = -1
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    url = "https://www.taifex.com.tw/enl/eng3/largeTraderOptDown"
    payload = {"queryStartDate": datestr,"queryEndDate": datestr}
    
    flow = 1
    while flow <= maxtry:
        try:

            res = util.requests_post_wrapper(url,payload)
            df = twse_parser(res.text,10,",","*")
            col=["trade_date","commodityid","call_put","settlement","category","top5_buy","top5_sell","top10_buy","top10_sell","oi"]
            df.columns = col
            df['call_put'] = df['call_put'].apply(lambda x: str.upper(x))
            df = df[(~df['settlement'].isin(['-']))]
            parser_error = 0
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"ConnectionRefusedError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    if parser_error == 1:
        return return_val        
    trans = conn.begin()
    try:
        #conn.execute("delete from taifex_opt_bigtrader_temp")
        df.to_sql('taifex_opt_bigtrader',engine,index=False,if_exists='append')
        #sql.insert_diff(conn,'taifex_opt_bigtrader_temp','taifex_opt_bigtrader','trade_date')
        #conn.execute("delete from taifex_opt_bigtrader_temp")
        trans.commit()
        return_val= 1
        print("%s is done!"%datestr)
    except (Exception,exc.SQLAlchemyError) as e:
        trans.rollback()
        print(e)
    
    return return_val

def load_taifex_opt_big3(cfg_obj,datestr,maxtry=10,timer=60):
    datestr = util.regular_datestr(datestr)
    return_val = -1
    engine = cfg_obj.engine
    conn = cfg_obj.conn
    url = "https://www.taifex.com.tw/enl/eng3/callsAndPutsDateDown"
    date = util.to_date(datestr)
    year = date.year
    month = date.month
    day = date.day
    firstDate = util.regular_datestr(str(int(year-3)) + str(month)+str(day)) + " 00:00"
    lastDate = datestr + " 00:00"
    payload = {"firstDate": firstDate,"lastDate":lastDate,\
           "queryStartDate": datestr,"queryEndDate": datestr}

    
    flow = 1
    while flow <= maxtry:
        try:

            res = util.requests_post_wrapper(url,payload)
            df = twse_parser(res.text,16,",","*")

            col = ["trade_date","commodityid","call_put","category",\
            "long_vol","long_amt","short_vol","short_amt","net_vol","net_amt",\
            "long_oi","long_oi_amt","short_oi","short_oi_amt","net_oi","net_oi_amt"]

            df.columns = col
            dicts = {"Dealers":"dealer","InvestmentTrustCompanies":"investment_trust","FINI":"fini"}
            df['category'] = df['category'].apply(lambda x: dicts[x])
            parser_error = 0
            break
        except Exception as e:
            flow = flow + 1
            parser_error = 1
            if len(re.findall(r"ConnectionRefusedError",str(e)))> 0:
                util.renew_ip()
            else:
                time.sleep(timer)  
    if parser_error == 1:
        return return_val        
    trans = conn.begin()
    try:
        #conn.execute("delete from taifex_opt_big3_temp")
        df.to_sql('taifex_opt_big3',engine,index=False,if_exists='append')
        #sql.insert_diff(conn,'taifex_opt_big3_temp','taifex_opt_big3','trade_date')
        #conn.execute("delete from taifex_opt_big3_temp")
        trans.commit()
        return_val= 1
        print("%s is done!"%datestr)
    except (Exception,exc.SQLAlchemyError) as e:
        trans.rollback()
        print(e)
    
    return return_val

    
        
    







        







    




    
    
    

    




    





