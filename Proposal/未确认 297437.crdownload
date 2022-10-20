#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('2014_jan.csv')


# In[3]:


gb_hourday = df.groupby(['day','hour'])
gb_hourday.sum()


# In[4]:


df1 = gb_hourday.sum()
df1.reset_index(inplace=True)
df1


# In[5]:


for a in range(0,31):
    for i in range(0+a*24,24+a*24):
        df1.loc[i,'trip_distance'] = df1.loc[i,'trip_distance']/gb_hourday.get_group((df1.loc[i,'day'],df1.loc[i,'hour']))['trip_distance'].size
df1


# In[6]:


average_1 = []
for i in range(0,24):
    df_1 = gb_hourday.get_group((11,i))
    average_1.append(df_1['trip_distance'].sum()/df_1['trip_distance'].size)


# In[7]:


for i in range(0,32):
    exec("average_%s=[]"%i)
for j in range(1,32):
    for i in range(0,24):
        exec("df_%s=gb_hourday.get_group((j,i))" %j)
        exec("average_%s.append(df_%s['trip_distance'].sum()/df_%s['trip_distance'].size)" % (j,j,j))


# In[13]:


fig = plt.figure(figsize=(24, 30))
gs = fig.add_gridspec(nrows=5, ncols=2)
#
ax = fig.add_subplot(gs[0,0])
x = range(0,24)
ax.plot(x,average_1,label='Jan 1')
ax.plot(x,average_2,label='Jan 2')
ax.plot(x,average_3,label='Jan 3')
ax.set_title('Average trip distance in weekday by hour in the first week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend()
#
ax = fig.add_subplot(gs[0,1])
x = range(0,24)
ax.plot(x,average_4,label='Jan 4')
ax.plot(x,average_5,label='Jan 5')
ax.set_title('Average trip distance in weekend by hour in the first week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend()
#
ax = fig.add_subplot(gs[1,0])
x = range(0,24)
ax.plot(x,average_6,label='Jan 6')
ax.plot(x,average_7,label='Jan 7')
ax.plot(x,average_8,label='Jan 8')
ax.plot(x,average_9,label='Jan 9')
ax.plot(x,average_10,label='Jan 10')
ax.set_title('Average trip distance in weekday by hour in the second week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend(loc='upper right')
#
ax = fig.add_subplot(gs[1,1])
x = range(0,24)
ax.plot(x,average_11,label='Jan 11')
ax.plot(x,average_12,label='Jan 12')
ax.set_title('Average trip distance in weekend by hour in the second week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend()
#
ax = fig.add_subplot(gs[2,0])
x = range(0,24)
ax.plot(x,average_13,label='Jan 13')
ax.plot(x,average_14,label='Jan 14')
ax.plot(x,average_15,label='Jan 15')
ax.plot(x,average_16,label='Jan 16')
ax.plot(x,average_17,label='Jan 17')
ax.set_title('Average trip distance in weekday by hour in the third week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend(loc='upper right')
#
ax = fig.add_subplot(gs[2,1])
x = range(0,24)
ax.plot(x,average_18,label='Jan 18')
ax.plot(x,average_19,label='Jan 19')
ax.set_title('Average trip distance in weekend by hour in the third week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend()
#
ax = fig.add_subplot(gs[3,0])
x = range(0,24)
ax.plot(x,average_20,label='Jan 20')
ax.plot(x,average_21,label='Jan 21')
ax.plot(x,average_22,label='Jan 22')
ax.plot(x,average_23,label='Jan 23')
ax.plot(x,average_24,label='Jan 24')
ax.set_title('Average trip distance in weekday by hour in the fourth week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend(loc='upper right')
#
ax = fig.add_subplot(gs[3,1])
x = range(0,24)
ax.plot(x,average_25,label='Jan 25')
ax.plot(x,average_26,label='Jan 26')
ax.set_title('Average trip distance in weekend by hour in the fourth week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend()
#
ax = fig.add_subplot(gs[4,0])
x = range(0,24)
ax.plot(x,average_27,label='Jan 27')
ax.plot(x,average_28,label='Jan 28')
ax.plot(x,average_29,label='Jan 29')
ax.plot(x,average_30,label='Jan 30')
ax.plot(x,average_31,label='Jan 31')
ax.set_title('Average trip distance in weekday by hour in the fifth week')
ax.set_xlabel('Hour')
ax.set_ylabel('Distance (km)')
plt.legend(loc='upper right')

#
plt.show()


# In[10]:


fig = px.line(df1, x="hour", y=df1["trip_distance"], animation_frame="day",range_y=[1.5,5.5])
fig.update_layout(title_text='Average trip distance by hour in different days')
fig.show()


# In[ ]:




