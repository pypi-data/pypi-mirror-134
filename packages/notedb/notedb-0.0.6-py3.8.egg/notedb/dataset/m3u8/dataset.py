import os

from notedrive.tables import SqliteTable
from notetool.secret import read_secret


class M3U8DataSet(SqliteTable):
    def __init__(self, table_name='m3u8_detail', db_path=None, *args, **kwargs):
        if db_path is None:
            db_path = read_secret(cate1="local", cate2="path", cate3="db", cate4="m3u8_db")
        if db_path is None:
            db_path = os.path.abspath(os.path.dirname(__file__)) + '/db/m3u8.db'
        super(M3U8DataSet, self).__init__(db_path=db_path, table_name=table_name, *args, **kwargs)
        self.columns = ['id', 'name', 'size', 'dateline', 'source_url', 'm3u8_url', 'ext_json',
                        'cate1', 'cate2', 'cate3', 'cate4', 'cate5']
        self.create()

    def create(self):
        self.execute("""
                create table if not exists {} (
                    id                 integer primary key AUTOINCREMENT
                   ,name               varchar(200)    DEFAULT ('')     -- 资源的名称
                   ,size               integer         DEFAULT (0)      -- 大小 
                   ,dateline           integer         DEFAULT (0)      -- 时间戳
                   ,source_url         varchar(200)    DEFAULT ('')     -- 资源的源网址
                   ,m3u8_url           varchar(200)    DEFAULT ('')     -- 资源地址
                   ,ext_json           varchar(10000)  DEFAULT ('')
                   ,cate1              varchar(20)     DEFAULT ('')
                   ,cate2              varchar(20)     DEFAULT ('')
                   ,cate3              varchar(20)     DEFAULT ('')
                   ,cate4              varchar(20)     DEFAULT ('')
                   ,cate5              varchar(20)     DEFAULT ('')
                )
                """.format(self.table_name))
