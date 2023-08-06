#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE            : PyCharm
@Time           : 2022/1/13 2:18 PM
@Author         : JQS
@File           : img_operate.py
@Introduction   : 图像处理操作
"""

import cv2
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.split(os.path.realpath(__file__))[0] + "/config.ini")


def blur(src):
    """
    均值模糊
    :param src: 输入图片
    """
    return cv2.blur(src, (15, 15))


def get_gray(src):
    """
    提取灰度图
    :param src: 输入图片
    """
    return cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)


def pixelated(src):
    """
    像素化
    :param src: 输入图片
    """
    height, width = src.shape[:2]
    w, h = (16, 16)
    temp = cv2.resize(src, (w, h), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

