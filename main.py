import pandas as py
import csv


import plotly.express as go
df=py.read_csv('data.csv')
mean=df.groupby(['student_id','level'],as_index=False)['attempt'].mean()

fig=go.scatter(mean,x='student_id',y='level',size='attempt',color='attempt')

fig.show()