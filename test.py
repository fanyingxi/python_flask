#!/usr/bin/env python3
# coding=UTF-8
'''
@Date: 2020-01-04 23:30:27
@LastEditTime : 2020-01-04 23:43:51
@Description: file content
'''
import pandas as pd
import plotly.offline as py
import cufflinks as cf
from pandas import DataFrame
# 导入数据


def get_data_view(limit):

    data = pd.read_csv('forbes.csv')
    regions_available = list(data.values)
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    N = pd.read_csv('forbes.csv', encoding="utf8",
                    keep_default_na=False, na_values='na_rep')
    N.head()

    # Count crime numbers in each neighborhood
    limit = 100
    data5 = N.iloc[0:limit, :]
    print(data5)
    input()

    # disdata5 = pd.DataFrame(data['行业'].value_counts())
    # disdata5.reset_index(inplace=True)
    # disdata5.rename(
    #     columns={'index': '分类', 'PdDistrict': 'Count'}, inplace=True)
    # print(disdata5)
    # input()

    limit = 20
    data4 = N.iloc[0:limit, :]
    print(data4)
    input()

    # disdata4 = pd.DataFrame(data['行业'].value_counts())
    # disdata4.reset_index(inplace=True)
    # disdata4.rename(
    #     columns={'index': '分类', 'PdDistrict': 'Count'}, inplace=True)
    # print(disdata4)
    # input()


if __name__ == '__main__':
    get_data_view(10)
