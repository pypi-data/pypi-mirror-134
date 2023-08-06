# #!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/16 18:56
# @Author : BruceLong
# @FileName: x_sqlserver.py
# @Email   : 18656170559@163.com
# @Software: PyCharm
# @Blog ：http://www.cnblogs.com/yunlongaimeng/
import threading

import pymysql

from .config import MYSQL_HOST, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DB


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class MySQLPipeline(metaclass=SingletonType):
    '''
    SqlServer存储管道
    '''

    def __init__(self):
        '''
        初始化操作
        '''
        self.host = MYSQL_HOST
        self.username = MYSQL_USERNAME
        self.password = MYSQL_PASSWORD
        self.db = MYSQL_DB

    def __get_connect(self):
        '''
        创建连接信息
        :return:
        '''
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.connect = pymysql.connect(
            host=self.host,
            user=self.username,
            passwd=self.password,
            db=self.db,
            charset="utf8"
        )
        cursor = self.connect.cursor()
        if not cursor:
            raise (NameError, "连接数据库失败")
        else:
            return cursor

    def get_connect_test(self):
        return self.__get_connect()

    def __create_table(self, cur, item: dict, table: str):
        '''
        合建表相关的信息
        :param item: 数据
        :param table: 表名
        :return:
        '''
        # cur = self.__get_connect()
        # 判断是否存在该表
        sql = f'''select * from information_schema.tables where table_name ='{table}';'''
        cur.execute(sql)
        if not cur.fetchone():
            # 生成创建字段信息
            # ------------目前只支持两种整型及字符串----------------------
            field_info = ',\n'.join(
                [
                    # f'{field} bigint' if isinstance(values, int) else f'{field} nvarchar(max)'
                    f'{field} text'
                    for field, values in item.items()
                ]
            )
            end_field = list(item.keys())[-1]
            cur.execute('select version()')
            mysql_version = cur.fetchone()[0]
            # 解决版本不同创建语句差异问题
            if mysql_version[:3] <= '5.5':
                # 数据库版本小于等于5.5版本
                sql_table = f'''create table {table}(
                        x_id bigint NOT NULL AUTO_INCREMENT,
                        x_inserttime timestamp NULL DEFAULT CURRENT_TIMESTAMP,
--                         x_updatetime timestamp NULL DEFAULT '0000-00-00 00:00:00',
                        {field_info},
                        PRIMARY KEY (`x_id`)
                        )ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;'''
                # --创建update触发器
                # sql_trigger = f'''CREATE TRIGGER trig_{table}_updatetime
                #                   BEFORE UPDATE ON {table} FOR EACH ROW
                #                   SET NEW.x_updatetime = NOW();
                #                   FLUSH'''
                try:
                    # print(sql_table)
                    cur.execute(sql_table)
                    # cur.execute(sql_trigger)
                    self.connect.commit()
                    print(f'Mysql Version is :{mysql_version}', '*' * 15, 'Create Table Successful')
                except Exception as e:
                    print(f'Mysql Version is :{mysql_version}', '*' * 15, 'Create Table Failed', e)
            else:
                sql_table = f'''create table {table}(
                                x_id bigint NOT NULL AUTO_INCREMENT,
                                x_inserttime timestamp NULL DEFAULT CURRENT_TIMESTAMP,
                                x_updatetime timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                                {field_info},
                                PRIMARY KEY (`x_id`)
                                )ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;'''
                try:
                    # print(sql_table)
                    cur.execute(sql_table)
                    self.connect.commit()
                    print(f'Mysql Version is :{mysql_version}', '*' * 15, 'Create Table Successful')
                except Exception as e:
                    print(f'Mysql Version is :{mysql_version}', '*' * 15, 'Create Table Failed', e)
        else:
            # 查询表字段
            select_fields_sql = f'''desc {table}'''
            cur.execute(select_fields_sql)
            # 获取已经存在的表字段
            allready_exists_fields = {i[0].lower() for i in cur.fetchall()}
            # 目前新的字段名
            new_fields = {i.lower() for i in item.keys()}
            # 差集算出需要添加的字段名
            not_exists_fields = new_fields - allready_exists_fields
            if list(not_exists_fields):
                # 构造字段信息
                not_exists_fields_info = ','.join(
                    [
                        # f'{field} bigint' if isinstance(values, int) else f'{field} nvarchar(max)'
                        f'{field} text'
                        for field, values in item.items() if field.lower() in not_exists_fields
                    ]
                )
                add_fields_sql = f'''alter table {table} add {not_exists_fields_info}'''
                try:
                    # print(add_fields_sql)
                    cur.execute(add_fields_sql)
                    self.connect.commit()
                    print('Create Field Successful')
                except Exception as e:
                    print('Create Field Failed', e)

    def insert_one(self, item: dict, table: str):
        '''
        插入一条数据
        :param item:
        :param table:
        :return:
        '''
        cur = self.__get_connect()
        self.__create_table(cur=cur, item=item, table=table)
        # 获取到一个以键且为逗号分隔的字符串，返回一个字符串
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        # print(sql)
        try:
            # 这里的第二个参数传入的要是一个元组
            # data = [v if isinstance(v, int) else str(v) for v in item.values()]
            data = [str(v) for v in item.values()]
            # print(data)
            cur.execute(sql, tuple(data))
            print('Insert One Successful')
            self.connect.commit()
        except:
            print('Insert One Failed')
            self.connect.rollback()
        finally:
            cur.close()
            self.connect.close()
        pass

    def insert_many(self, items: list, table: str):
        '''
        批量插入数据
        :param items:
        :param table:
        :return:
        '''
        if not isinstance(items, list):
            raise (TypeError, 'please input items for list type')
        cur = self.__get_connect()
        k_temp = {k for ite in items for k in ite.keys()}
        v_temp = ['' for _ in range(len(k_temp))]
        data = dict(zip(k_temp, v_temp))
        self.__create_table(cur=cur, item=data, table=table)
        values = ', '.join(['%s'] * len(data))
        # [[item.update({k: str(v)}) for k, v in item.items() if not isinstance(v, (int, str))] for item in items]
        result_data = [{k: str(item.get(k)) if item.get(k) else '' for k in data.keys()} for item in items]
        # print(result_data)
        keys = ', '.join(result_data[0].keys())
        datas = [tuple(i.values()) for i in result_data]
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            cur.executemany(sql, datas)
            self.connect.commit()
            print('Insert Many Successful')
        except Exception as e:
            self.connect.rollback()
            print('Insert Many Failed:', e)
        finally:
            cur.close()
            self.connect.close()

    def find(self, sql: str):
        '''
        通过sql查询对应的数据结果
        :param sql: sql语句
        :return:
        '''
        cur = self.__get_connect()
        try:
            cur.execute(sql)
            desc = cur.description
            result = (dict(zip((d[0] for d in desc), data)) for data in cur.fetchall())
            return result
        except Exception as e:
            print('Find Data Failed:', e)
        finally:
            cur.close()
            self.connect.close()


x_mysql = MySQLPipeline()
