# -*- coding: utf-8 -*-


import pandas


url= "https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt"
names = ["edad","genero","bmi","bp","s1","s2","s3","s4","s5","s6","Y"]
df = pandas.read_csv(url, names=names, sep='\t')
 
print(df.shape)
 
#head
print(df.head(5))
for index, row in df.iterrows():
    #print(row)
    age = row['edad']
    bmi = row['bmi']
    print(index, age, bmi)
