#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   data_process.py
@Time    :   2022/01/14 16:00:06
@Author  :   DingWenjie
@Contact :   359582058@qq.com
@Desc    :   None
'''

import pandas as pd

class BackTest(object):
    '''process etf option data from Wind
    TODO
    '''
    def __init__(self, option_data, etf_data) -> None:
        self.date = list(option_data['date'])
        self.df = option_data
        self.etf = list(etf_data['CLOSE'])