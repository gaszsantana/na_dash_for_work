#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:34:39 2020

@author: gasz
"""
import pandas as pd
import numpy as np
import plotly.graph_objects as go


#--- Datos extraidos de Twitter
dia= pd.read_csv('datos/day.csv')
hora= pd.read_csv('datos/hour.csv')
mes= pd.read_csv('datos/mes.csv')
prueba= pd.read_csv('datos/prueba.csv')
semana= pd.read_csv('datos/semana.csv')

x=dia['day_of_week']
fig = go.Figure(go.Bar(x=x, y=dia['tweets_count'], name='Numero de Tweets'))
fig.add_trace(go.Bar(x=x, y=dia['interactions_count'], name='Interacciones'))
fig.add_trace(go.Bar(x=x, y=dia['retweet_count'], name='Numero de Retweets'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':[x[1],x[5],x[6],x[4],x[0],x[2],x[3]]
})
fig.show()