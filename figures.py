#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 03:41:14 2020

@author: gasz
"""
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from data1 import *
import pandas as pd
from datos.test import *

colors = {
    'background': '#0A1B2A',
    'text': '#CEE3F6'
}

#----------------Figure 2------------------
grupo_ordenes_pagadas["ORDENES PAGADAS"] = "ORDENES PAGADAS"
fig2 = px.treemap(grupo_ordenes_pagadas, path=['ORDENES PAGADAS', 'RUBRO','NOMBRE_PROVEEDOR','ORDEN_DE_COMPRA','VOL_PLANIFICADO'], values='CANT_PLANIFICADO', color='MONTO', color_continuous_scale='Viridis')
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])


#------------Figure 3-----------------------------
fig3 = px.scatter(monto_dias, x="Monto en Bolivares", y="Dias de pago",
                 size="Monto en Bolivares", color="Rubro",
                 log_x=True, opacity=0.9, size_max=100)


fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])

#------------Figure 4-------------------
fig4 = go.Figure(data=[go.Table(
    header=dict(values=list(af.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[af['Proveedor'], af['Frecuencia']],
               fill_color='lavender',
               align='left'))
])


fig4.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color='black')

#----------Figure 5--------------------
labels = ["Ordenes no planificadas", "Ordenes planificadas"]
fig5 = go.Figure(data=[go.Pie(labels=labels, values=[100-KPI,KPI], hole = .65)])

fig5.update_layout(plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    annotations=[dict(text= KPI1 , x=0.5, y=0.5, font_size=50,  showarrow=False)]
    )

#------------Figura 6---------------------
fig6 = px.scatter(grupo_ordenes_dif_fecha, x="INTERVALO DE TIEMPO", y="ORDEN DE COMPRA",
                 size="CANTIDAD DE PLANIFICACIONES", color="PROVEEDOR",
                 log_x=True, opacity=0.9, size_max=40)

fig6.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])


#-------------------Figura 7-------------
fig7 = ff.create_table(cxp, height_constant=60)
teams = cxp["FECHA_ORDEN"]
GFPG = cxp["MONTO"]
trace1 = go.Bar(x=teams, y=GFPG, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Bolívares ')
fig7.add_traces(trace1)

# initialize xaxis2 and yaxis2
fig7['layout']['xaxis2'] = {}
fig7['layout']['yaxis2'] = {}

# Edit layout for subplots
fig7.layout.yaxis.update({'domain': [0, .45]})
fig7.layout.yaxis2.update({'domain': [.6, 1]})

# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
fig7.layout.yaxis2.update({'anchor': 'x2'})
fig7.layout.xaxis2.update({'anchor': 'y2'})
fig7.layout.yaxis2.update({'title': 'Bolívares '})

# Update the margins to add a title and see graph x-labels.
fig7.layout.margin.update({'t':35, 'l':25})
#fig7.layout.update({'title': '2016 Hockey Stats'})

# Update the height because adding a graph vertically will interact with
# the plot height calculated for the table
fig7.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])




#----Figure8


fig_bs = px.treemap(df_bs, path=['Bolivares', 'rubro', 'proveedor'], values='monto')

fig_bs.update_layout(plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    )

fig_e = px.treemap(df_e, path=['Euros', 'rubro', 'proveedor'], values='monto')

fig_e.update_layout(plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    )

fig_p = px.treemap(df_p, path=['Petro', 'rubro', 'proveedor'], values='monto')

fig_p.update_layout(plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    )

#--- Figure twitter 1-------
fig_t1 = go.Figure(go.Bar(x=x, y=dia['tweets_count'], name='Numero de Tweets'))
fig_t1.add_trace(go.Bar(x=x, y=dia['interactions_count'], name='Interacciones'))
fig_t1.add_trace(go.Bar(x=x, y=dia['retweet_count'], name='Numero de Retweets'))

fig_t1.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':[x[1],x[5],x[6],x[4],x[0],x[2],x[3]]})
