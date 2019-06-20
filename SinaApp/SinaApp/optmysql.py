import pymysql
from pymysql import cursors
from SinaApp import settings
sqlConnect = pymysql.connect(
    host = settings.Mysql_host,
    user = settings.Mysql_user,
    passwd = settings.Mysql_pwd,
    db =settings.Mysql_db
)
cur = sqlConnect.cursor()
class Sql:
    @staticmethod
    def inster_table(data):
        str = 'insert into sina(a,b,c,d,e,f,g,h,i,j,k,l,m) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(data['a'],data['b'],data['c'],data['d'],data['e'],data['f'],data['g'],data['h'],data['i'],data['j'],data['k'],data['l'],data['m'])
        cur.execute(str)
        sqlConnect.commit()
        pass

    @staticmethod
    def closemysql():
        cur.close()
        sqlConnect.close()

    pass
