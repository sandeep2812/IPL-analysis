#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


deliveries_data = pd.read_csv(r'/Users/sandeepkumar/Downloads/IPL Ball-by-Ball 2008-2020.csv')
match_data = pd.read_csv(r'/Users/sandeepkumar/Downloads/IPL Matches 2008-2020.csv')


# In[7]:


match_data.head()


# In[8]:


match_data.tail()


# In[10]:


match_data.columns


# In[14]:


match_data.shape


# In[16]:


type(match_data.shape)


# In[17]:


type(match_data)


# In[19]:


match_data.shape[0]


# In[21]:


match_data['city'].unique()


# In[22]:


match_data['team1'].unique()


# In[26]:


match_data['toss_winner'].value_counts()


# In[31]:


match_data['toss_winner'].value_counts().index[0]


# In[34]:


match_data['player_of_match'].value_counts().index[0]


# In[ ]:





# In[35]:


deliveries_data.head()


# In[39]:


deliveries_data['batsman'].unique()


# In[43]:


filt = deliveries_data['batsman']=='V Kohli'


# In[46]:


df_kohli = deliveries_data[filt]


# In[48]:


df_kohli.columns


# In[49]:


df_kohli.head()


# In[50]:


df_kohli['dismissal_kind'].value_counts()


# In[51]:


df_kohli['batsman_runs'].unique()


# In[55]:


df_kohli['fielder'].unique()


# In[56]:


filt3 = df_kohli['fielder'] == 'MS Dhoni'


# In[63]:


df_kohli['batsman_runs'].unique()


# In[62]:


len(df_kohli[df_kohli['batsman_runs'] == 1])


# In[64]:


df_kohli[df_kohli['batsman_runs'] == 1]


# In[65]:


df_kohli[df_kohli['batsman_runs'] == 2]


# In[66]:


df_kohli[df_kohli['batsman_runs'] == 6]


# In[68]:


len(df_kohli[df_kohli['batsman_runs'] == 6])*6


# In[ ]:





# In[ ]:





# In[ ]:





# In[69]:


import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot


# In[70]:


values = [1919 , 692 , 39 , 2016 , 1212]
labels = [1, 2, 3 ,4, 6]

trace = go.Pie(labels= labels , values= values , hole=0.3)

data = [trace]

fig = go.Figure(data = data)


# In[71]:


fig.show()


# In[ ]:





# In[ ]:





# In[72]:


#Toss decision across seasons


# In[74]:


match_data.columns


# In[75]:


match_data['Season'] = pd.to_datetime(match_data['date']).dt.year  ## extract season from "date" feature


# In[76]:


match_data['Season'] = pd.to_datetime(match_data['date']).dt.year


# In[77]:


match_data.columns


# In[78]:


match_data.groupby(['Season' , 'toss_decision']).size()


# In[79]:


type(match_data.groupby(['Season' , 'toss_decision']).size())


# In[86]:


match_data.groupby(['Season' , 'toss_decision']).size().reset_index()


# In[82]:


season_toss_count_df = match_data.groupby(['Season' , 'toss_decision']).size().reset_index()


# In[83]:


season_toss_count_df = match_data.groupby(['Season' , 'toss_decision']).size().reset_index().rename(columns={0:'count'})


# In[84]:


season_toss_count_df


# In[ ]:





# In[89]:


plt.figure(figsize=(7,4))
sns.barplot(x='Season' , y='count' , hue = 'toss_decision' , data = season_toss_count_df)

## plotting barplot of "Season" vs "count" for bat & field both ..
plt.show()


# In[ ]:





# In[ ]:





# In[91]:


match_data.columns


# In[92]:


match_data.head()


# In[96]:


match_data[['team1','team2','toss_winner','winner']].rename(columns={'winner':'Chicken_dinner'})


# In[97]:


match_data[['team1','team2','toss_winner','winner']]


# In[103]:


## if "toss_winner" equals to "match_winner" , then assign "Yes" else assign "No"

match_data['toss_win_game_win'] = np.where(match_data['toss_winner'] == match_data['winner'], 'Yes', 'No')


# In[104]:


match_data.columns


# In[106]:


match_data['toss_win_game_win'].unique()


# In[108]:


match_data['toss_win_game_win'].value_counts()


# In[113]:


match_data['toss_win_game_win'].value_counts().index


# In[115]:


match_data['toss_win_game_win'].value_counts().values


# In[127]:


labels = match_data['toss_win_game_win'].value_counts().index
values = match_data['toss_win_game_win'].value_counts().values

trace = go.Pie(labels= labels , values= values , hole=0.4)

data = [trace]

fig = go.Figure(data = data)

fig.update_traces(hoverinfo='label+percent' , textinfo='label+percent')


# In[ ]:





# In[128]:


#how many times team have won the tournament


# In[129]:


match_data.columns


# In[130]:


match_data['Season'].unique()


# In[137]:


df_2018 = match_data[match_data['Season']==2018]


# In[138]:


df_2018


# In[142]:


df_2018['winner'].tail(1).values[0]


# In[143]:


# winner of every season


# In[144]:


winners_team = {}
for year in sorted(match_data['Season'].unique()):
    current_year_df = match_data[match_data['Season']==year]
    winners_team[year] = current_year_df['winner'].tail(1).values[0]


# In[145]:


winners_team


# In[148]:


winners_team.values()


# In[ ]:





# In[161]:


from collections import Counter


# In[165]:


Counter(winners_team.values())


# In[166]:


match_data.columns


# In[167]:


match_data.head()


# In[168]:


# most number of wins


# In[169]:


match_data[['team1','team2']]


# In[170]:


match_data['team1'].value_counts()


# In[171]:


match_data['team2'].value_counts()


# In[172]:


match_data['team1'].value_counts() + match_data['team2'].value_counts()


# In[173]:


matches_played = match_data['team1'].value_counts() + match_data['team2'].value_counts()


# In[174]:


matches_played


# In[175]:


type(matches_played)


# In[179]:


matches_played.to_frame().reset_index()


# In[180]:


matches_played_df = matches_played.to_frame().reset_index()


# In[184]:


matches_played_df.columns=['Team_name','Matches_played']


# In[190]:


matches_played_df


# In[191]:


# which team wins more matches


# In[194]:


pd.DataFrame(match_data['winner'].value_counts()).reset_index()


# In[195]:


wins = pd.DataFrame(match_data['winner'].value_counts()).reset_index()


# In[196]:


wins.columns = ['Team_name','Wins']


# In[197]:


wins


# In[201]:


played = matches_played_df.merge(wins, on='Team_name',how='inner')    #merged 2 tables 


# In[202]:


played


# In[ ]:





# In[205]:


trace1 = go.Bar(
    x = played['Team_name'] , 
    y = played['Matches_played'] , 
    name = 'Total Matches'
)


trace2 = go.Bar(
    x = played['Team_name'] , 
    y = played['Wins'] , 
    name = 'Matches won'
)


# In[206]:


data = [trace1 , trace2]


# In[208]:


iplot(data)


# In[ ]:




