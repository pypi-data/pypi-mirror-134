#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE            : PyCharm
@Time           : 2022/1/13 9:43 PM
@Author         : JQS
@File           : main.py
@Introduction   : 简单说明
"""

import gradio as gr
import hocv.img_operate as img

import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.split(os.path.realpath(__file__))[0] + "/config.ini")

def index():
    gr.Interface(fn=[img.blur, img.get_gray, img.pixelated], inputs='image', outputs='image').launch()
