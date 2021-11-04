# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:05:12 2021

@author: DaviesJones
"""

from pandas import DataFrame

l1 = [1,2,3,4]
l2 = [1,2,3,4]
df = DataFrame({'Stimulus Time': l1, 'Reaction Time': l2})
df

df.to_excel('test2.xlsx', sheet_name='sheet1', index=False)