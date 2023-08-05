import os

from notedrive.tables import SqliteTable
from notetool.secret import read_secret


class YYetsDataSet(SqliteTable):
    def __init__(self, table_name='yyets', db_path=None, *args, **kwargs):
        if db_path is None:
            db_path = read_secret(cate1="local", cate2="path", cate3="db", cate4="yyets")
        if db_path is None:
            db_path = os.path.abspath(os.path.dirname(__file__)) + '/db/yyets.sqlite'
        super(YYetsDataSet, self).__init__(db_path=db_path, table_name=table_name, *args, **kwargs)
        self.columns = ['id', 'cnname', 'enname', 'aliasname', 'views', 'data']
        self.create()

    def create(self):
        self.execute("""
                create table if not exists {} (
                    id              integer primary key AUTOINCREMENT
                   ,cnname          varchar(200)
                   ,enname          varchar(200)  
                   ,aliasname       varchar(200)
                   ,views           integer
                   ,data            varchar(2000)  
                )
                """.format(self.table_name))
