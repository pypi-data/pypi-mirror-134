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

class BackTest_Daily(object):
    '''process daily etf option data from Wind
    TODO
    Attributes:
        date: list of date
        df: corresponding input dataframe of the option
        etf: list of etf close
    '''
    def __init__(self, option_data, etf_data) -> None:
        self.date = list(option_data['date'])
        self.df = option_data
        self.etf = list(etf_data['CLOSE'])

    def crt_option(self,crt_date, maturity_level):
        '''get the options of the given maturity on given date
        Args:
            crt_date: the considered date
            maturity_level: an int in [0,1,2,3]
        Returns:
            true_option: all option
            true_option_call: sorted by 'strike'
            true_option_put: sorted by 'strike'
        '''
        option = self.df.loc[(self.df.index == crt_date)]
        maturity = option['maturity'].drop_duplicates(
                keep='first').tolist()
        maturity.sort()
        maturity = [int(str(maturity[i])[-2:]) for i in range(4)]
        crt_maturity = maturity[maturity_level]
        crt_bool = option['option_name'].str.contains(
                "{0}月".format(crt_maturity))
        true_option = option[crt_bool].sort_values(by='exerciseprice')
        crt_bool = true_option['option_name'].str.contains("购")
        true_option_call = true_option[crt_bool]
        crt_bool_put = true_option['option_name'].str.contains("沽")
        true_option_put = true_option[crt_bool_put]
        K = true_option_call['exerciseprice']
        return true_option, true_option_call, true_option_put

    def cpt_cost(option, csdtrade_list):
        '''compute the cost of the given trade_list
        Args:
            option: considered options on the current date
            trade_list: a list with type of [ ['option_name', size, flag], ... ]
            flag is str:'long' or 'short'
        Return
            cost: float
        '''

if __name__ == '__main__':
    pass