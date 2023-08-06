#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 14:03
# @Author  : Adyan
# @File    : redis_connect.py


import redis


class ClientReids(object):
    """
    ReidsClient('proxy', config )
    ree.get(2)
    """

    def __init__(self, config, name=None):
        """
        创建连接
        :param config:  { "HOST": "ip", "PORT": 6379, "DB": 11 }
        :param name:  "库名称"
        """
        host = config.get('HOST', 'localhost')
        port = config.get('PORT', 6379)
        db = config.get('DB', 0)
        password = config.get('PAW', None)
        if password:
            self.redis_conn = redis.Redis(host=host, port=port, password=password)
        else:
            self.redis_conn = redis.Redis(host=host, port=port, db=db)
        self.name = name

    def get(self, count):
        """
        获取count个数据，同时将这些数据删除
        :param count:
        :return:
        """
        lst = self.redis_conn.lrange(self.name, 0, count - 1)
        self.redis_conn.ltrim(self.name, count, -1)
        return lst

    def sput(self, param):
        """
        :param param:
        :return:
        """
        self.redis_conn.sadd(self.name, param)

    @property
    def queue_len(self):
        """
        获取当前数据库长度
        :return:
        """
        try:
            return self.redis_conn.llen(self.name)
        except:
            return self.redis_conn.scard(self.name)
