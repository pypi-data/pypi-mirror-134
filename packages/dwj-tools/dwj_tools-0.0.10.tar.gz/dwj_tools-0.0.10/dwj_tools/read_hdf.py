from email import header


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_hdf.py
@Time    :   2022/01/15 15:46:05
@Author  :   DingWenjie
@Contact :   359582058@qq.com
@Desc    :   None
'''

import pandas as pd

def read_data():
    option_data = pd.read_hdf('get_data_from_wind/option_50_data_wind.h5')
    etf_data = pd.read_hdf('get_data_from_wind/etf_50_data_wind.h5')
    return option_data, etf_data

if __name__ == '__main__':
    pass