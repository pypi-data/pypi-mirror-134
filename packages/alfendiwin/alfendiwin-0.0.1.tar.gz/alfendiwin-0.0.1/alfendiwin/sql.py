import util
def query_uni_rowcount(conn,tbl,col,where_col,filter):
    ds = conn.execute("select distinct {} from {} where {} = %s".format(col,tbl,where_col),filter)
    return ds.rowcount

def query_rowcount(conn,tbl,col,where_col,filter):
   
    ds = conn.execute("select {} from {} where {} = %s".format(col,tbl,where_col),filter)
    return ds.rowcount

def last_trade_date(conn,tbl):
    ds = conn.execute("select distinct trade_date from {} order by trade_date desc limit 1".format(tbl))
    for i in ds:
       return_val = i['trade_date']
    return return_val
def first_trade_date(conn,tbl):
    ds = conn.execute("select trade_date from {} order by trade_date limit 1".format(tbl))
    for i in ds:
       return_val = i['trade_date']
    return return_val
    

def insert_diff(conn,src_tbl,dest_tbl,join_col):
    return_val = -1
    try:

        conn.execute("insert into {} select * from {} t1 where not exists \
        (select {} from {} t2 where t1.{} = t2.{})".format(dest_tbl,src_tbl,join_col,dest_tbl,join_col,join_col))
        return_val = 1
    except (Exception,util.exc.SQLAlchemyError) as e:
        print(e)
        print("insert error....")
    return return_val

def insert_2col_diff(conn,src_tbl,dest_tbl,col1,col2):
    return_val = -1
    try:
        conn.execute("insert into {} select l.* from {} l left join {} r using ({},{}) \
            where r.{} is null".format(dest_tbl,src_tbl,dest_tbl,col1,col2,col1))
        return_val = 1
    except (Exception,util.exc.SQLAlchemyError) as insert_err:
        print(insert_err)
        print("insert error....")
    return return_val
        
     