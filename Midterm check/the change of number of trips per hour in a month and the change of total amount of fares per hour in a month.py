import pandas as pd
import plotly.express as px

td=pd.read_csv('2014_jan.csv')
tf=td.groupby(['day','hour']).count()
tf.reset_index(inplace=True)

fig = px.line(tf, x=tf['hour'], y=tf['pickup_datetime'], animation_frame=tf['day'])
fig["layout"].pop("updatemenus")
fig.update_yaxes(title="number of trips")
fig.show()

tf2=td.groupby(['day','hour']).sum()
tf2.reset_index(inplace=True)

fig = px.line(tf2, x=tf['hour'], y=tf2['total_amount'], animation_frame=tf2['day'])
fig["layout"].pop("updatemenus")
fig.update_yaxes(title="total amount each hour")
fig.show()