
# coding: utf-8

# In[242]:

import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
def namechange(row):  
    if row['destination'].endswith('DTL') or row['destination'].endswith('CCL') or row['destination'].endswith('NEL') :
        row['destination'] = row['destination'][:-4]
        
    if row['destination'].endswith('NSEW'):
        row['destination'] = row['destination'][:-5]
        
    if row['origin'].endswith('DTL') or row['origin'].endswith('CCL') or row['origin'].endswith('NEL') :
        row['origin']=row['origin'][:-4]
        
    if row['origin'].endswith('NSEW'):
        row['origin'] = row['origin'][:-5] 
    return row

c
df=df[df.destination!=df.origin] # removing entries such that origin = destination
df=df.apply(namechange,axis=1) # clearing up CCL, NSEW, NEL from the MRT Names
df['duration']= pd.to_datetime(df['destination_tm'], format='%H:%M:%S') - pd.to_datetime(df['origin_tm'], format= '%H:%M:%S' )
df['duration']=pd.to_timedelta(df['duration'])
df['duration']=df['duration']/np.timedelta64(1, 's')
# df.sort_values(by=['destination','origin'],axis=0) # sorting entries by the destination and origin



# In[289]:

df= pd.read_csv('mrt_trips_sampled.csv', header=0, quoting = 3)
df


# In[277]:

df_av=pd.DataFrame({'Averaged_duration':df.groupby(['destination','origin'])['duration'].mean()})
df_av
# df_avg[df_avg['destination']=='Admiralty'].sort('Averaged_duration')


# In[290]:

small = df_av['Averaged_duration'].groupby(level=0, group_keys=False)
small.nsmallest(2)
dfsmall=pd.DataFrame({'Smallest 2':small.nsmallest(2)})
dfsmall


# In[279]:

print("Mean travelling times shortest to every station = ",small.nsmallest(2).mean())
print("Standard Deviation=",small.nsmallest(2).std())


# In[280]:

get_ipython().magic('matplotlib inline')
plt.figure(figsize=(25,10))
small.nsmallest(2).plot(kind='bar')


# In[287]:

mean=small.nsmallest(2).mean()
std=small.nsmallest(2).std()
mins= mean-2*std
maxs=mean+2*std
df_avg=df_av.reset_index()
listofstations=[]
for i in df_avg['destination'].unique():
    if i not in listofstations:
        listofstations.append(i)
for i in df_avg['origin'].unique():
    if i not in listofstations:
        listofstations.append(i)
df_avg[df_avg['destination']=='Admiralty'].sort('Averaged_duration')

#initialising
i=1
station='Admiralty'
df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values
dictofline={}
dictofline[i]=[]
dictofline[i].append(station)
dictofline[i].append(df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[0]])

station=df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[0]]
# Generate the map
# for j in dictofline:
    
#         listof4=df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values
#         if listof4[3]>mins and listof4[3]<maxs and listof4[2]>mins and listof4[2]<maxs:
#             if df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[0]] in dictofline[i]:
#                 j.append(df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[1]])
#                 station=df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[1]]
#             else:
#                 j.append(df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[0]])
#                 station=df_avg.origin[df_avg[df_avg['destination']==station].Averaged_duration.nsmallest(4).index.values[0]]



   


# In[ ]:



