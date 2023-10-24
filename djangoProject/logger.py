import logging
import datetime
import os
import sys
import random




#
# class logger():
#     def __init__(self):
#         return
#
#     def Getnum(self):
#         char = ''
#         str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#         for i in range(32):
#             char += random.choice(str)
#         return char
#
#
#     def info(self,info):
#         # num = getnum.get_random_num().Getnum()
#         Logger = logging.getLogger(self.Getnum())
#         Logger.setLevel(logging.DEBUG)
#
#         handler = logging.StreamHandler(sys.stdout)
#         handler.setLevel(logging.DEBUG)
#
#         # formatter = logging.Formatter("%(asctime)s [%(levelname)s]    %(filename)s.%(funcName)s [%(lineno)d] -- %(message)s")
#         formatter = logging.Formatter(
#             # "%(asctime)s  [%(levelname)-5s]  %(filename)-10s.%(funcName)-20s   [%(lineno)-4d] :%(message)-s"
#             '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] '
#                                            '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s')
#
#         handler.setFormatter(formatter)
#
#         Logger.addHandler(handler)
#         Logger.info(info)
#
#     def error(self,info):
#         num = self.Getnum()
#         Logger = logging.getLogger(num)
#         Logger.setLevel(logging.DEBUG)
#
#         handler = logging.StreamHandler(sys.stdout)
#         handler.setLevel(logging.DEBUG)
#
#         # formatter = logging.Formatter("%(asctime)s [%(levelname)s]    %(filename)s.%(funcName)s [%(lineno)d] -- %(message)s")
#         formatter = logging.Formatter(
#             # "%(asctime)s  [%(levelname)-5s]  %(filename)-10s.%(funcName)-20s   [%(lineno)-4d] :%(message)-s")
#             '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] '
#             '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s')
#         handler.setFormatter(formatter)
#
#         Logger.addHandler(handler)
#         Logger.error(info)
#
#
#     def debug(self,info):
#         num = self.Getnum()
#         Logger = logging.getLogger(num)
#         Logger.setLevel(logging.DEBUG)
#
#         handler = logging.StreamHandler(sys.stdout)
#         handler.setLevel(logging.DEBUG)
#
#         formatter = logging.Formatter(
#             # "%(asctime)s [%(levelname)s]    %(filename)s.%(funcName)s [%(lineno)d] -- %(message)s")
#             # "%(asctime)s  [%(levelname)-5s]  %(filename)-10s.%(funcName)-20s   [%(lineno)-4d] :%(message)-s")
#             '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] '
#             '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s')
#         handler.setFormatter(formatter)
#
#         Logger.addHandler(handler)
#         Logger.debug(info)

import logging
import datetime
import sys
import random


class logger():
    def __init__(self):
        self.name ='log'
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s  [%(name)s:%(lineno)d] '
            '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    @staticmethod
    def Getnum():
        char = ''
        str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(32):
            char += random.choice(str)
        return char

    def info(self, info):
        self.logger.info(info)

    def error(self,error):
        self.logger.error(error)

