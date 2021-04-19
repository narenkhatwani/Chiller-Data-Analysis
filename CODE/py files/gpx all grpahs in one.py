import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd


data_naren=pd.read_csv("chiller.csv")
data_naren.dropna(axis=1)

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['Actual Capacity'], name="COND REF PRESS COMP1",line_color='green'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['Entering Fluid temp'], name="COND REF PRESS COMP1",line_color='yellow'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['Leaving Fluid temp'], name="COND REF PRESS COMP1",line_color='black'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['EVAP PRESS COMP1'], name="EVAPORATIVE PRESSURE COMPRESSOR 1",line_color='purple'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['EVAP PRESS COMP2'], name="EVAPORATIVE PRESSURE COMPRESSOR 1",line_color='deepskyblue'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['COND REF PRESS COMP1'], name="COND REF PRESS COMP1",line_color='orange'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['COND REF PRESS COMP2'], name="COND REF PRESS COMP2",line_color='brown'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['OIL Pressure COMP1'], name="Oil Pressure COMP 1",line_color='grey'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['OIL Pressure COMP2'], name="Oil Pressure COMP2",line_color='pink'))
fig1.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['DP'], name="DP",line_color='deepskyblue'))



fig1.update_layout(title_text='All Parameters 1',xaxis_rangeslider_visible=True)
fig1.show()
plot(fig1)


fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['COND SAT TEMP COMP 1'], name="COND SAT TEMP COMP 1",line_color='deepskyblue'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['COND SAT TEMP COMP 2'], name="COND SAT TEMP COMP 2",line_color='green'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['EVAP SAT TEMP COM1'], name="EVAP SAT TEMP COMP 1",line_color='blue'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['EVAP SAT TEMP COM2'], name="EVAP SAT TEMP COMP 2",line_color='yellow'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['EXPV Position COM 1'], name="EXPV Position COM 1",line_color='grey'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['EXPV Position COM 2'], name="EXPV Position COM 2",line_color='orange'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['SUCTION TEMP COMP 1'], name="SUCTION TEMP COMP 1",line_color='pink'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['SUCTION TEMP COMP 2'], name="SUCTION TEMP COMP 2",line_color='brown'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['DISCHARGE TEMP COMP 1'], name="DISCHARGE TEMP COMP 1",line_color='purple'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['DISCHARGE TEMP COMP 2'], name="DISCHARGE TEMP COMP 2",line_color='magenta'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['SUCTION SH    COMP 1'], name="SUCTION SH COMP 1",line_color='black'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['SUCTION SH    COMP 2'], name="SUCTION SH COMP 2",line_color='red'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['DISCH     SH    COMP 1'], name="DISCH SH COMP 1",line_color='violet'))
fig2.add_trace(go.Scatter(x=data_naren['Time Snap'], y=data_naren['DISCH    SH    COMP 2'], name="DISCH SH COMP 2",line_color='maroon'))
   

fig2.update_layout(title_text='All Parameters 1',xaxis_rangeslider_visible=True)
fig2.show()
plot(fig2)



