# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     db_sqlit3
   Description :
   Author :       jpl
   date：          2021/10/11
-------------------------------------------------
   Change Activity:
                   2021/10/11:
-------------------------------------------------
"""
__author__ = 'Asdil'
import sqlite3


class Sqlit3:
    """
    Sqlit3类用于存储临时数据
    """
    def __init__(self, path):
        """__init__(self):方法用于初始化

        Parameters
        ----------
        path : str
            db文件地址(绝对路径)

        Returns
        ----------
        """
        self.drive = sqlite3.connect(path)

    def cursor(self):
        """new_cour方法用于创建新的游标
        """
        return self.drive.cursor()

    def select_all(self, sql, args=()):
        """select_all方法用于选择所有数据

        Parameters
        ----------
        sql : str
            sql查询语句
        args : tuple
            参数

        Returns
        ----------
        """
        if type(args) is list:
            args = tuple(args)
        cursor = self.cursor()
        ret = cursor.execute(sql, args)
        ret = ret.fetchall()
        cursor.close()
        return ret

    def select_one(self, sql, args=()):
        """select_one方法用于选择所有数据

        Parameters
        ----------
        sql : str
            sql查询语句
        args : tuple
            参数

        Returns
        ----------
        """
        if type(args) is list:
            args = tuple(args)
        cursor = self.cursor()
        ret = cursor.execute(sql, args)
        ret = ret.fetchone()
        cursor.close()
        return ret

    def excute(self, sql, args=()):
        """excute方法用于

        Parameters
        ----------
        sql: str
            sql语句
        args : tuple
            参数

        Returns
        ----------
        """
        if type(args) is list:
            args = tuple(args)
        cursor = self.cursor()
        cursor.execute(sql, args)
        cursor.close()