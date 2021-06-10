# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 07:56:23 2021

@author: DaviesJones
"""

from cs50 import get_float
while True:
    dollars = get_float("Change Owed: ")
    if dollars > 0:
        cents = round(dollars*100)
        quarter = int(cents / 25)
        rquarter = int(cents % 25)
        dime = int(rquarter / 10)
        rdime = int(rquarter % 10)
        nickel = int(rdime / 5)
        rnickel = int(rdime % 5)
        penny = int(rnickel)
        coins = 0
        if (rquarter == 0):
            coins = quarter
        elif (rdime == 0):
            coins = quarter + dime
        elif (rnickel == 0):
            coins = quarter + dime + nickel
        else:
            coins = quarter + dime + nickel + penny
        print(coins)
        break