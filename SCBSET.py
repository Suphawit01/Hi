# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 22:02:37 2018

@author: Suphawit
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def readscbsetfile(file):
    df2 = pd.read_excel(file,parse_dates=True,index_col='Date')
    df1 = df2.interpolate('linear').sort_index(ascending = True)
    
    df1['diff'] =df1['SCBSET'] - df1['SCBSET'].shift()
    
#    df.loc['01/05/2017':'23/05/2018','diff'].plot(kind='line',style = 'k.-')
#    plt.savefig('trend.png',dpi=700)
#    plt.show()
    df1 = df1.sort_index()
    return df2,df1


df2,df1=readscbsetfile('SCBSET26-7-2561.xlsx')
df1['diff'] =df1['SCBSET']-df1['SCBSET'].shift(-1)
mse={}
def buildewa(df1,mse):
    for i in [x/10 for x in range(1,10)]:
        text='ewa'+str(i)
        df1[text] =df1.SCBSET.ewm(alpha=i).mean().shift()
        error=np.mean((df1[text]-df1.SCBSET)**2)
        mse[text]=error
    text='naive'
    df1[text]=df1.SCBSET.shift(1)
    error=np.mean((df1[text]-df1.SCBSET)**2)
    mse[text]=error
    return df1,mse
        
#df1,mse=buildewa(df1,mse)        
df2.dropna(subset=['SCBSET'])
#df1['emv1'] =df1.SCBSET.ewm(alpha=0.9).mean()


#dfshow=pd.DataFrame()
##dfshow['r']=df1.loc['01/01/2015':'23/05/2018','SCBSET']
##dfshow['0.1']=df1.loc['01/01/2015':'23/05/2018','emv']
##dfshow['0.9']=df1.loc['01/01/2017':'23/05/2018','emv1']
#dfshow.plot(kind='line',style = ['k.-','r.-'])
#
#plt.savefig('price.png',dpi=1700)
#plt.show()
#df1.loc['01/01/2018':'23/05/2018',['diff']].plot(kind='line',style = 'k.-')
##plt.savefig('trend.png',dpi=1700)
#plt.show()

current_amount = 0
invest_budget = 0
sold_budget = 0


def buy(current_price,current_amount,invest_value,invest_budget):
    current_amount += invest_value/current_price
    invest_budget+=invest_value
    return current_amount

def sell(current_price,current_amount,sell_amount,sold_budget):
    current_amount -= sell_amount
    sold_budget+=sell_amount*current_price
    return current_amount


