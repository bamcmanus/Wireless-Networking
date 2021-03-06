# -*- coding: utf-8 -*-
"""
Created on Fri May 25 19:58:13 2018

@author: brent
"""
import pandas as pd
import numpy as np

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None)

def preprocess(data):
    #keep only data transmissions
    data = data[data.Type == "Data"]
    data = data.drop('Type',axis=1)
    #data = data.drop(['Abs time'],axis=1)
    #remove null datum
    data = data[~data.Source.isnull()]
    data = data[~data.Destination.isnull()]
    #scrub IP addresses 
    data = data[data.Source.str.contains(":")]
    #eliminates broadcasts
    data = data[data.Source != 'ff:ff:ff:ff:ff:ff']
    data = data[data.Destination != 'ff:ff:ff:ff:ff:ff']
    #removes peripherals?
    data = data[data.Length != 63]
    #removes all source data that isnt the length of a mac address
    data = data[data['Source'].map(len) == 17]
    #removes cisco equipment
    data = data[~data.Source.str.startswith("2c:5a:0f")]
    data = data[~data.Source.str.startswith("7c:95:f3")]
    data = data[~data.Source.str.startswith("74:26:ac")]
    data = data[~data.Source.str.startswith("f4:1f:c2")]
    data = data[~data.Source.str.startswith("44:ad:d9")]
    data = data[~data.Source.str.startswith("c0:25:5c")]
    data = data[~data.Source.str.startswith("00:f2:8b")]
    data = data[~data.Source.str.startswith("08:1f:f3")]
    data = data[~data.Source.str.startswith("30:37:a6")]
    data = data[~data.Source.str.startswith("3c:ce:73")]
    data = data[~data.Source.str.startswith("b0:aa:77")]
    data = data[~data.Source.str.startswith("00:08:e3")]
    data = data[~data.Source.str.startswith("00:3a:7d")]
    data = data[~data.Source.str.startswith("00:fe:c8")]
    data = data[~data.Source.str.startswith("04:c5:a4")]
    data = data[~data.Source.str.startswith("0c:27:24")]
    data = data[~data.Source.str.startswith("40:ce:24")]
    data = data[~data.Source.str.startswith("40:f4:ec")]
    data = data[~data.Source.str.startswith("44:e4:d9")]
    data = data[~data.Source.str.startswith("50:17:ff")]
    data = data[~data.Source.str.startswith("58:bc:27")]
    data = data[~data.Source.str.startswith("70:df:2f")]
    data = data[~data.Source.str.startswith("c0:62:6b")]
    data = data[~data.Source.str.startswith("d0:57:4c")]
    data = data[~data.Source.str.startswith("e4:aa:5d")]
    data = data[~data.Source.str.startswith("10:05:ca")]
    data = data[~data.Source.str.startswith("dc:a5:f4")]
    data = data[~data.Source.str.startswith("08:cc:68")]
    data = data[~data.Source.str.startswith("18:80:90")]
    data = data[~data.Source.str.startswith("f0:29:29")]
    data = data[~data.Source.str.startswith("2c:5a:0f")]
    #removes netgear equipment
    data = data[~data.Source.str.startswith("10:da:43")]
    data = data[~data.Source.str.startswith("10:da:43")]
    data = data[~data.Source.str.startswith("28:c6:8e")]
    #removes arris equipment
    data = data[~data.Source.str.startswith("9c:34:26")]
    #removes atheros equipment
    data = data[~data.Source.str.startswith("00:03:7f")]
    #removes intel equipment
    data = data[~data.Source.str.startswith("00:24:d6")]
    data = data[~data.Source.str.startswith("34:f3:9a")]
    data = data[~data.Source.str.startswith("44:85:00")]
    data = data[~data.Source.str.startswith("f8:34:41")]
    data = data[~data.Source.str.startswith("f8:63:3f")]
    data = data[~data.Source.str.startswith("b8:08:cf")]
    data = data[~data.Source.str.startswith("68:ec:c5")]
    data = data[~data.Source.str.startswith("88:b1:11")]
    data = data[~data.Source.str.startswith("d4:25:8b")]
    data = data[~data.Source.str.startswith("00:50:f1")]
    data = data[~data.Source.str.startswith("9c:da:3e")]
    data = data[~data.Source.str.startswith("34:e6:ad")]
    #eliminates most xerox mac addresses
    data = data[~data.Source.str.startswith('00:00')]
    data = data[~data.Source.str.startswith('08:00')]
    #removes murata equipment
    data = data[~data.Source.str.startswith("44:91:60")]
    return data
    

def before_and_after(data):
    #print("Before preprocessing:",len(data))
    data = preprocess(data)
    #print("After preprocessing:",len(data))
    #print("")
    data = data.sort_values(by=['Source','Time'])
    data = data.reset_index()
    data = data.drop('index',axis=1)
    return data


#find users in both data frames
def find(list1,list2,matchList):
    found = False
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                found = True
                print(list1[i],list2[j])
                matchList.append(list1[i]) 
    return found


#print information about users who have been located in multiple locations
def printUser(user,data):
    data = data[data.Source == user]
    print(data)
    
    
def printAll(user):
    printUser(user,fab1)
    printUser(user,fab2)
    printUser(user,fab3)
    printUser(user,lib1)
    printUser(user,lib2)
    printUser(user,lib3)
    printUser(user,ut1)
    printUser(user,ut2)
    printUser(user,ut3)
    printUser(user,smu1)
    printUser(user,smu2)
    printUser(user,smu3)
    

if __name__ == "__main__":  
    #read the file into pandas array
    fab1 = pd.read_csv("FAB_46_052418_1155_1255.csv")
    fab2 = pd.read_csv("FAB_46_052918_1155_1255.csv")
    fab3 = pd.read_csv("FAB_46_060218_1155_1255.csv")
    lib1 = pd.read_csv("LIB_052918_830_930.csv")
    lib2 = pd.read_csv("LIB_053118_830_930.csv")
    lib3 = pd.read_csv("LIB_060418_830_930.csv")
    ut1 = pd.read_csv("UT_052918_958_1058.csv")
    ut2 = pd.read_csv("UT_053118_958_1058.csv")
    ut3 = pd.read_csv("UT_060418_958_1058.csv")
    smu1 = pd.read_csv("SMU_052418_150_250.csv")
    smu2 = pd.read_csv("SMU_060218_151_251.csv")
    smu3 = pd.read_csv("SMU_060318_150_250.csv")

    #initilize user population arrays for each location
    fabPop = []
    utPop = []
    smuPop =[]
    libPop = []

    #preprocess fab data and collect number of users in a population array
    #print("Fab on 5/24/2018 from 1155-1255")
    fab1 = before_and_after(fab1)
    fabPop.append(len(fab1))
    #print("Fab on 5/29/2018 from 1155-1255")
    fab2 = before_and_after(fab2)
    fabPop.append(len(fab2))
    #print("Fab on 6/2/2018 from 1155-1255")
    fab3 = before_and_after(fab3)
    fabPop.append(len(fab3))
    #print average # users at FAB
    print("Average Users at FAB:",sum(fabPop)/len(fabPop),'\n')
    
    #preprocess Lib data and collect number of users in a population array
    #print("Library on 5/29/2018 from 0830-0930")
    lib1 = before_and_after(lib1)
    libPop.append(len(lib1))
    #print("Library on 5/29/2018 from 0830-0930")
    lib2 = before_and_after(lib2)
    libPop.append(len(lib2))
    #print("Library on 6/4/2018 from 0830-0930")
    lib3 = before_and_after(lib3)
    libPop.append(len(lib3))
    #print average # users at Lib
    print("Average Users at Lib:",sum(libPop)/len(libPop),'\n')
    
    #preprocess UT data and collect number of users in a population array
    #print("UT on 5/29/2018 from 0958-1058")
    ut1 = before_and_after(ut1)
    utPop.append(len(ut1))
    #print("UT on 5/31/2018 from 0958-1058")
    ut2 = before_and_after(ut2)
    utPop.append(len(ut2))
    #print("UT on 6/4/2018 from 0958-1058")
    ut3 = before_and_after(ut3)
    utPop.append(len(ut3))
    #print average # users at UT
    print("Average Users at UT:",sum(utPop)/len(utPop),'\n')
    
    #preprocess SMU data and collect number of users in a population array
    #print("SMU on 5/24/2018 from 1350-1450")
    smu1 = before_and_after(smu1)
    smuPop.append(len(smu1))
    #print("SMU on 6/2/2018 from 1350-1450")
    smu2 = before_and_after(smu2)
    smuPop.append(len(smu2))
    #print("SMU on 6/3/2018 from 1350-1450")
    smu3 = before_and_after(smu3)
    smuPop.append(len(smu3))
    #print average # users at SMU
    print("Average Users at SMU:",sum(smuPop)/len(smuPop),'\n')
    
    ut2.to_html("ut2.html")
    ut3.to_html("ut3.html")
    
    #collect all the data rates for each sample
    dataRate1 = fab1['DataRate'].values
    dataRate2 = fab2['DataRate'].values
    dataRate3 = fab3['DataRate'].values
    dataRate4 = lib1['DataRate'].values
    dataRate5 = lib2['DataRate'].values
    dataRate6 = lib3['DataRate'].values
    dataRate7 = smu1['DataRate'].values
    dataRate8 = smu2['DataRate'].values
    dataRate9 = smu3['DataRate'].values
    dataRate10 = ut1['DataRate'].values
    dataRate11 = ut2['DataRate'].values
    dataRate12 = ut3['DataRate'].values
    #concatenate data rates into a singular list for plotting
    dataRates = np.concatenate((dataRate1,dataRate2,dataRate3,dataRate4,dataRate5,
                dataRate6,dataRate7,dataRate8,dataRate9,dataRate10,dataRate11,
                dataRate12)).tolist()
    histogram = pd.DataFrame(dataRates) #convert to pandas dataframe
    pd.DataFrame.hist(histogram,bins=40) #plot histogram

    print("User from LIB on 5/29 at UT on 5/31")    
    printUser("24:00:aa:aa:03:00",lib1)
    printUser("24:00:aa:aa:03:00",ut2)
    print('\n','\n')
    
    print("User from LIB on 5/31 at LIB on 6/4")
    printUser("9c:50:57:d4:24:02",lib2)
    printUser("9c:50:57:d4:24:02",lib3)
    print('\n','\n')
    
    print("User from UT on 5/29 at UT on 5/31 and 6/4")
    printUser("01:00:aa:aa:03:00",ut1)
    printUser("01:00:aa:aa:03:00",ut2)
    printUser("01:00:aa:aa:03:00",ut3)
    print('\n','\n')
    
    print("User from UT on 5/29 at UT on 6/4")
    printUser("14:4e:00:00:14:4e",ut1)
    printUser("14:4e:00:00:14:4e",ut3)
    print('\n','\n')
    
    print("User from UT on 5/31 at SMU on 6/2")
    printUser("03:00:aa:aa:03:00",ut2)
    printUser("03:00:aa:aa:03:00",smu2)
    print('\n','\n')
    
    print("User from SMU on 6/2 at SMU on 6/3")
    printUser("e4:00:00:da:c6:b2",smu2)
    printUser("e4:00:00:da:c6:b2",smu3)