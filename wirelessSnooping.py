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
    #removes cisco equipment
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
    #eliminates most xerox mac addresses
    data = data[~data.Source.str.startswith('00:00')]
    data = data[~data.Source.str.startswith('08:00')]
    return data
    
def before_and_after(data):
    print("Before preprocessing:",len(data))
    data = preprocess(data)
    print("After preprocessing:",len(data))
    print("")
    data = data.sort_values(by=['Length','Source'])
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
    
#read the file into pandas array
fab461 = pd.read_csv("FAB_46_052418_1155_1255.csv")
fab462 = pd.read_csv("FAB_46_052918_1155_1255.csv")
fab463 = pd.read_csv("FAB_46_060218_1155_1255.csv")
lib1 = pd.read_csv("LIB_052918_830_930.csv")
lib2 = pd.read_csv("LIB_053118_830_930.csv")
ut1 = pd.read_csv("UT_052918_958_1058.csv")
ut2 = pd.read_csv("UT_053118_958_1058.csv")
smu1 = pd.read_csv("SMU_052418_150_250.csv")
#smu2 = pd.read_csv("")

#initilize user population arrays for each location
fabPop = []
utPop = []
smuPop =[]
libPop = []

#preprocess fab data and collect number of users in a population array
print("Fab 46 on 5/24/2018 from 1155-1255")
fab461 = before_and_after(fab461)
fabPop.append(len(fab461))
print("Fab 46 on 5/29/2018 from 1155-1255")
fab462 = before_and_after(fab462)
fabPop.append(len(fab462))
print("Fab 46 on 6/2/2018 from 1155-1255")
fab463 = before_and_after(fab463)
fabPop.append(len(fab463))
#print average # users at FAB
print("Average Users at FAB:",sum(fabPop)/len(fabPop))
print("")

#preprocess Lib data and collect number of users in a population array
print("Library on 5/29/2018 from 0830-0930")
lib1 = before_and_after(lib1)
libPop.append(len(lib1))
print("Library on 5/29/2018 from 0830-0930")
lib2 = before_and_after(lib2)
libPop.append(len(lib2))
print("Average users at Lib:",sum(libPop)/len(libPop))
#print average # users at Lib
print("Average Users at Lib:",sum(libPop)/len(libPop))
print("")

#preprocess UT data and collect number of users in a population array
print("UT on 5/29/2018 from 0958-1058")
ut1 = before_and_after(ut1)
utPop.append(len(ut1))
print("UT on 5/31/2018 from 0958-1058")
ut2 = before_and_after(ut2)
utPop.append(len(ut2))
#print average # users at UT
print("Average Users at UT:",sum(utPop)/len(utPop))
print("")

#preprocess SMU data and collect number of users in a population array
print("SMU on 5/24/2018 from 1350-1450")
smu1 = before_and_after(smu1)
smuPop.append(len(smu1))
#print average # users at SMU
print("Average Users at SMU:",sum(smuPop)/len(smuPop))
print("")

#commented out histogram print
'''
#collect all the data rates for each sample
dataRate1 = fab461['DataRate'].values
dataRate2 = fab462['DataRate'].values
dataRate3 = fab463['DataRate'].values
dataRate4 = lib1['DataRate'].values
dataRate5 = lib2['DataRate'].values
dataRate6 = smu1['DataRate'].values
dataRate7 = ut1['DataRate'].values
dataRate8 = ut2['DataRate'].values
#concatenate data rates into a singular list for plotting
dataRates = np.concatenate((dataRate1,dataRate2,dataRate3,dataRate4,dataRate5,
                            dataRate6,dataRate7,dataRate8)).tolist()
histogram = pd.DataFrame(dataRates) #convert to pandas dataframe
pd.DataFrame.hist(histogram,bins=40) #plot histogram'''

#create arrays of source users from each collection
users1 = fab461["Source"]
users2 = fab462["Source"]
users3 = fab463["Source"]
users4 = lib1["Source"]
users5 = lib2["Source"]
users6 = ut1["Source"]
users7 = ut2["Source"]
users8 = smu1["Source"]

#inialize an array for users in multiple collections
match = []

#search for user matches at all collections for collection 1
if find(users1,users2,match):
    print("Found at Fab")
if find(users1,users3,match):
    print("Found at Fab")
if find(users1,users4,match):
    print("Found at Lib")
if find(users1,users5,match):
    print("Found at Lib")
if find(users1,users6,match):
    print("Found at UT")
if find(users1,users7,match):
    print("Found at UT")
if find(users1,users8,match):
    print("Found at SMU")
    
#search for user matches at all collections for collection 2
if find(users2,users3,match):
    print("Found at Fab")
if find(users2,users4,match):
    print("Found at Lib")
if find(users2,users5,match):
    print("Found at Lib")
if find(users2,users6,match):
    print("Found at UT")
if find(users2,users7,match):
    print("Found at UT")
if find(users2,users8,match):
    print("Found at SMU")
    
#search for user matches at all collections for collection 3  
if find(users3,users4,match):
    print("Found at Lib")
if find(users3,users5,match):
    print("Found at Lib")
if find(users3,users6,match):
    print("Found at UT")
if find(users3,users7,match):
    print("Found at UT")
if find(users3,users8,match):
    print("Found at SMU")
    
#search for user matches at all collections for collection 4
if find(users4,users5,match):
    print("Found at Lib")
if find(users4,users6,match):
    print("Found at UT")
if find(users4,users7,match):
    print("Found at UT")
if find(users4,users8,match):
    print("Found at SMU")
    

    

print(match)