import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot


data_naren=pd.read_csv("sunilsir.csv",usecols=[0,1,7,8,11,12,13,14])

data_naren1=data_naren[(data_naren['Organization']=='AKAMAI PVT LTD')]
data_naren2=data_naren[(data_naren['Organization']=='ATOS Worldline India Pvt. Ltd.')]
data_naren3=data_naren[(data_naren['Organization']=='Betterworld')]
data_naren4=data_naren[(data_naren['Organization']=='BLUE LOTUS')]
data_naren5=data_naren[(data_naren['Organization']=='CoreIT')]
data_naren6=data_naren[(data_naren['Organization']=='Diadem Technologies Pvt. Ltd.')]
data_naren7=data_naren[(data_naren['Organization']=='DIRECT i')]
data_naren8=data_naren[(data_naren['Organization']=='FedEX')]
data_naren9=data_naren[(data_naren['Organization']=='IFTAS')]
data_naren10=data_naren[(data_naren['Organization']=='ISHAN INTECH')]
data_naren11=data_naren[(data_naren['Organization']=='Mahanagar Gas Limited')]
data_naren12=data_naren[(data_naren['Organization']=='NxtGen')]
data_naren13=data_naren[(data_naren['Organization']=='Nirmal Bang')]
data_naren14=data_naren[(data_naren['Organization']=='Nxtradata Limited')]
data_naren15=data_naren[(data_naren['Organization']=='oracle')]
data_naren16=data_naren[(data_naren['Organization']=='Smartlink')]
data_naren17=data_naren[(data_naren['Organization']=='Supreme Petrochem Ltd')]
data_naren18=data_naren[(data_naren['Organization']=='Xcell Host')]


export_csv = data_naren1.to_csv (r'Customer1.csv', index = None, header=True)
export_csv = data_naren2.to_csv (r'Customer2.csv', index = None, header=True)
export_csv = data_naren3.to_csv (r'Customer3', index = None, header=True)
export_csv = data_naren4.to_csv (r'Customer4.csv', index = None, header=True)
export_csv = data_naren5.to_csv (r'Customer5.csv', index = None, header=True)
export_csv = data_naren6.to_csv (r'Customer6.csv', index = None, header=True)
export_csv = data_naren7.to_csv (r'Customer7.csv', index = None, header=True)
export_csv = data_naren8.to_csv (r'Customer8.csv', index = None, header=True)
export_csv = data_naren9.to_csv (r'Customer9.csv', index = None, header=True)
export_csv = data_naren10.to_csv (r'Customer10.csv', index = None, header=True)
export_csv = data_naren11.to_csv (r'Customer11.csv', index = None, header=True)
export_csv = data_naren12.to_csv (r'Customer12.csv', index = None, header=True)
export_csv = data_naren13.to_csv (r'Customer13.csv', index = None, header=True)
export_csv = data_naren14.to_csv (r'Customer14.csv', index = None, header=True)
export_csv = data_naren15.to_csv (r'Customer15.csv', index = None, header=True)
export_csv = data_naren16.to_csv (r'Customer16.csv', index = None, header=True)
export_csv = data_naren17.to_csv (r'Customer17.csv', index = None, header=True)
export_csv = data_naren18.to_csv (r'Customer18.csv', index = None, header=True)
