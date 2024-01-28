import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_usa = pd.read_csv('USvideos.csv')
df_usa[df_usa['description'].apply(lambda x: pd.isna(x))].head()
df_usa['trending_date'] = pd.to_datetime(df_usa['trending_date'], format='%y.%d.%m').dt.date
publish_time = pd.to_datetime(df_usa['publish_time'], format='%Y-%m-%dT%H:%M:%S.%fZ')
df_usa['publish_date'] = publish_time.dt.date
df_usa['publish_time'] = publish_time.dt.time
df_usa['publish_hour'] = publish_time.dt.hour

df_usa['publish_date']
df_usa['publish_time'] 
df_usa['publish_hour']

columns_show = ['views', 'likes', 'dislikes', 'comment_count' ]
f, ax = plt.subplots(figsize = (8, 8))
corr = df_usa[columns_show].corr()
sns.heatmap(corr, cmap = sns.diverging_palette(220, 10, as_cmap = True), square = True, ax = ax, annot = True)

usa_video_views = df_usa.groupby(['video_id'])['views'].agg('sum')
usa_video_likes = df_usa.groupby(['video_id'])['likes'].agg('sum')
usa_video_dislikes = df_usa.groupby(['video_id'])['dislikes'].agg('sum')
usa_video_comment_count = df_usa.groupby(['video_id'])['comment_count'].agg('sum')

df_usa_single_day_trend = df_usa.drop_duplicates(subset = 'video_id', keep = False, inplace = False)
df_usa_multiple_day_trend = df_usa.drop_duplicates(subset = 'video_id', keep = 'first', inplace = False)

frames = [df_usa_single_day_trend, df_usa_multiple_day_trend]
df_usa_without_duplicates = pd.concat(frames)

df_usa_comment_disabled = df_usa_without_duplicates[df_usa_without_duplicates['comments_disabled'] == True].describe()
df_usa_rating_disabled = df_usa_without_duplicates[df_usa_without_duplicates['ratings_disabled'] == True].describe()
df_usa_video_error = df_usa_without_duplicates[df_usa_without_duplicates['video_error_or_removed'] == True].describe()

df_usa_single_day_trend.head()
df_usa_multiple_day_trend.head()

df_usa_which_video_trended_maximum_days = df_usa.groupby(by=['video_id'],as_index = False).count().sort_values(by = 'title',ascending = False).head()
df_usa_which_video_trended_maximum_days

df_usa_which_video_trended_maximum_days=df_usa.groupby(by = ['video_id'],as_index = False).count().sort_values(by = 'title',ascending = False).head()

plt.figure(figsize = (10,10))
sns.set_style("darkgrid")

ax = sns.barplot(x = df_usa_which_video_trended_maximum_days['video_id'],y = df_usa_which_video_trended_maximum_days['trending_date'], data = df_usa_which_video_trended_maximum_days)
plt.xlabel("Video Id")
plt.ylabel("Count")
plt.title("Top 5 Videos that trended maximum days in USA")

df_usa_maximum_views = usa_video_views['sXP6vliZIHI']
df_usa_maximum_likes = usa_video_likes['sXP6vliZIHI']
df_usa_maximum_dislikes = usa_video_dislikes['sXP6vliZIHI']
df_usa_maximum_comment = usa_video_comment_count['sXP6vliZIHI']


