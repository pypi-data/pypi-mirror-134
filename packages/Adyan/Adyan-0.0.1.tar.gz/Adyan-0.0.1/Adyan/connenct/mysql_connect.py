#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 14:03
# @Author  : Adyan
# @File    : mysql_connect.py


from datetime import datetime

from pymongo import MongoClient


class ClientMongo(object):
    def __init__(self, db_name, config):
        """
        创建连接
        :param db_name:数据库名称
        :param config: {
            "host": "192.168.20.211",
            "port": 27017
            }
        """
        self.db = MongoClient(**config, connect=True)[db_name]


class MongoBase(object):

    def __init__(self, sheet, db_name, config):
        self.mg = ClientMongo(db_name, config)
        self.mongo_conn = self.mg.db[sheet]

    def exist_list(self, data: list, key, get_id: callable, path):
        """
        mongo去重查询
        :param data: 数据数组
        :param key: 唯一的key
        :param get_id: 获取key的lambda表达式
        :param path: 废弃的数据存储文件位置
        :return:
        """
        lst = [get_id(obj) for obj in data]
        set_list = set([
            i.get(key)
            for i in list(
                self.mongo_conn.find({key: {"$in": lst}})
            )
        ])
        set_li = set(lst) - set_list
        with open(path, "rt", encoding="utf-8") as f:
            _ignore = [int(line.split(",")[0]) for line in f.readlines()]
        exist = list(set_li - set(_ignore))
        for obj in data:
            if get_id(obj) in exist:
                yield obj

    def exist(self, dic):
        """
        单条查询
        :param dic:
        :return:1,0
        """
        return self.mongo_conn.find(dic).count()

    def update_one(self, dic, item=None):
        """
        单条数据更新
        :param dic:
        :param item:
        :return:
        """
        result = self.exist(dic)
        if item and result == 1:
            item['updateTime'] = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
            self.mongo_conn.update(dic, {"$set": item})
        elif item:
            self.mongo_conn.update(dic, {"$set": item}, upsert=True)

    def insert_one(self, param):
        """
        :param param: 多条list 或者 单条dict储存
        :return:
        """
        self.mongo_conn.insert(param)

    def find_len(self, dic):
        """
        查询数量
        :param dic: 查询条件
        :return:
        """
        return self.mongo_conn.find(dic).count()

    def find_one(self):
        return self.mongo_conn.find_one()

    def find_list(self, count, dic=None, page=None, ):
        """
        查询数据
        :param count:查询量
        :param dic:{'city': ''} 条件查询
        :param page:分页查询
        :return:
        """
        if dic:
            return list(self.mongo_conn.find(dic).limit(count))
        if page:
            return list(self.mongo_conn.find().skip(page * count - count).limit(count))

    def conn(self):
        return self.mongo_conn


class MongoPerson(MongoBase):
    """
    MongoPerson('shop_list_info', 'update_bsr', config=mongo_config).collection
    """

    def __init__(self, sheet, db_name, config):
        super(MongoPerson, self).__init__(sheet, db_name, config)
