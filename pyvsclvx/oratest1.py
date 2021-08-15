#coding=utf-8
import cx_Oracle

conn= cx_Oracle.connect('mymotif/wxwpxh@xe')
cur = conn.cursor() 			
cur.execute("select * from STUDENT")
info = cur.fetchall() 
print(len(info))   	#获得表中有多少条数据
for ii in info:
    print(ii[0]+' '+ii[1]+' '+ii[2]+' '+ii[3].strftime('%Y-%m-%d')+' '+ii[4])	
cur.close()
conn.commit()
conn.close()
