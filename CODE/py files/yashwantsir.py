import pandas as pd


data_naren=pd.read_csv("load.csv")
data_naren['Total']= data_naren.iloc[:, 4:8].sum(axis=1)




data_naren1=data_naren[(data_naren['Device No.']=='SH000198')]
data_naren2=data_naren[(data_naren['Device No.']=='SH000269')]
data_naren3=data_naren[(data_naren['Device No.']=='SH000458')]
data_naren4=data_naren[(data_naren['Device No.']=='SH000492')]


export_csv = data_naren1.to_csv (r'Device1.csv', index = None, header=True)
export_csv = data_naren2.to_csv (r'Device2.csv', index = None, header=True)
export_csv = data_naren3.to_csv (r'Device3.csv', index = None, header=True)
export_csv = data_naren4.to_csv (r'Device4.csv', index = None, header=True)





data_naren1=pd.read_csv("Device1.csv")
data_naren2=pd.read_csv("Device2.csv")
data_naren3=pd.read_csv("Device3.csv")
data_naren4=pd.read_csv("Device4.csv")

x1=data_naren1['kVA'].max()
x2=data_naren2['kVA'].max()
x3=data_naren3['kVA'].max()
x4=data_naren4['kVA'].max()

b=x1+x2+x3+x4
print(x1+x2+x3+x4)

data_naren['Total kVa']=data_naren1['kVA']+data_naren2['kVA']+data_naren3['kVA']+data_naren4['kVA']
print(data_naren['Total kVa'].max())
a=data_naren['Total kVa'].max()
print('difference is')
print(b-a)


















































