#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 06:09:57 2020

@author: gasz
"""
import pandas as pd
import numpy as np

ordenes= pd.read_csv('orden_compra_con_fechas.csv')

df= pd.DataFrame(ordenes)
df['FECHA_ORDEN']= pd.to_datetime(df['FECHA_ORDEN'], format="%d-%m-%Y")
df['FECHA_VENCIMIENTO']= pd.to_datetime(df['FECHA_VENCIMIENTO'], format="%d-%m-%Y")
df['FECHA_ORDEN_PAGADA']= pd.to_datetime(df['FECHA_ORDEN_PAGADA'], format="%d-%m-%Y")
df['DIFERENCIA']= df['FECHA_ORDEN_PAGADA'] - df['FECHA_ORDEN']


rubro= df.groupby('RUBRO')      
monto= rubro['MONTO'].sum()
dias_pago= rubro['DIFERENCIA'].sum()
rubro_pro= rubro['NOMBRE_PROVEEDOR'].sum()

monto_dias= pd.DataFrame({'Rubro': monto.index, 'Monto en Bolivares': np.array(monto), 'Dias de pago': np.array(dias_pago),'Proveedores por rubro':np.array(rubro_pro).T})
monto_dias['Dias de pago']= monto_dias['Dias de pago'].dt.days



a= df['NOMBRE_PROVEEDOR'].value_counts()
af= pd.DataFrame({'Proveedor': a.index, 'Frecuencia': np.array(a)})


# A continuación se incorpora el estudio de la data descargada de la base de datos
pro= pd.read_csv('proveedores_euros.csv')
total_euro= pro['MONTO_EURO'].sum()
grupo_pro= pro.groupby(['PROVEEDOR'])
pro_contar= grupo_pro['PROVEEDOR'].value_counts()
euro= grupo_pro['MONTO_EURO'].sum()
euro_por= (np.array(euro)*100/total_euro)
proveedores= pd.DataFrame({'Proveedores': np.array(euro.index), 'Frecuencia': np.array(pro_contar), 'Monto de la ODC (Euros)': np.array(euro), 'Porcentaje': euro_por})



#------------------------------------------
ordenes1 = pd.read_csv("orden_compra_con_fechas.csv")
ordenes4 = pd.read_csv("ordenes_planificadas_a.csv", sep = ";")

ordenes4["VOL_PLANIFICADO"] = (ordenes4["VOL_PLANIFICADO"].str.split()).apply(lambda x: float(x[0].replace(',', '.')))
ordenes4["CANTOT"] = (ordenes4["CANTOT"].str.split()).apply(lambda x: float(x[0].replace(',', '.')))

grupo_ordenes1 = ordenes1.groupby(["NOMBRE_PROVEEDOR","ORDEN_DE_COMPRA","FECHA_ORDEN","RUBRO",],as_index=False).agg({"MONTO":"sum"})
grupo_ordenes4 = ordenes4.groupby(["ORDCOM","TO_CHAR(O.FECORD,'DD-MM-YYYY')","NOMPRO","CANTOT"],as_index=False).agg({"TO_CHAR(DP.FECHA_PLANIFICACION,'DD-MM-YYYYHH:MM:SS')":"count","VOL_PLANIFICADO":"sum"})

grupo_ordenes4.rename(columns={"ORDCOM": "ORDEN_DE_COMPRA" , "TO_CHAR(O.FECORD,'DD-MM-YYYY')": "FECHA_ORDEN","CANTOT": "CANT_TON","TO_CHAR(DP.FECHA_PLANIFICACION,'DD-MM-YYYYHH:MM:SS')": "CANT_PLANIFICADO", "NOMPRO" : "NOMBRE_PROVEEDOR"}, inplace=True)
grupo_ordenes_pagadas = grupo_ordenes1.merge(grupo_ordenes4, how='inner')


#-----------------------------------------------------------------


# A continuación se incorpora el estudio de la data descargada de la base de datos
ordenes4 = pd.read_csv("ordenes_planificadas_a.csv", sep = ";")
ordenes5 = pd.read_csv('proveedores_euros.csv')


grupo_ordenes5 = ordenes5.groupby(["FECHA","PROVEEDOR"],as_index=False).agg({"MONTO_EURO":"sum", "ORDEN_COMPRA":"count"})
Total = grupo_ordenes5['ORDEN_COMPRA'].sum()


grupo_ordenes4 = ordenes4.groupby(["ORDCOM"],as_index=False).agg({"TO_CHAR(DP.FECHA_PLANIFICACION,'DD-MM-YYYYHH:MM:SS')":"count"})
grupo_ordenes4["CANTIDAD_ORDENES"] = 1

grupo_ordenes4.rename(columns={"TO_CHAR(DP.FECHA_PLANIFICACION,'DD-MM-YYYYHH:MM:SS')": "CANTIDAD DE PLANIFICACIONES", "CANTIDAD_ORDENES" : "CANTIDAD DE ODC"}, inplace=True)
Total_planificaciones = grupo_ordenes4['CANTIDAD DE ODC'].sum()


KPI = (Total_planificaciones/Total)*100
KPI1 = round(KPI,2)

# A continuación se incorpora el estudio de la data descargada de la base de datos


ordenes4["PROVEEDOR"] = ordenes4["NOMPRO"]
ordenes4.drop("NOMPRO", axis = 1, inplace = True)
ordenes4["FECHA DE ORDEN DE COMPRA"] = ordenes4["TO_CHAR(O.FECORD,'DD-MM-YYYY')"]
ordenes4.drop("TO_CHAR(O.FECORD,'DD-MM-YYYY')", axis = 1, inplace = True)
ordenes4["FECHA DE PLANIFICACION"] = ordenes4["TO_CHAR(DP.FECHA_PLANIFICACION,'DD-MM-YYYYHH:MM:SS')"]
ordenes4.drop("TO_CHAR(DP.FECHA_PLANIFICACION,'DD-MM-YYYYHH:MM:SS')", axis = 1, inplace = True)
ordenes4.rename(columns={"ORDCOM":"ORDEN DE COMPRA"}, inplace=True)


ordenes4["FECHA DE ORDEN DE COMPRA"] = pd.to_datetime(ordenes4["FECHA DE ORDEN DE COMPRA"])
ordenes4["FECHA DE PLANIFICACION"] = pd.to_datetime(ordenes4["FECHA DE PLANIFICACION"])


grupo_ordenes = ordenes4[["ORDEN DE COMPRA","PROVEEDOR","FECHA DE ORDEN DE COMPRA","FECHA DE PLANIFICACION"]]


grupo_ordenes["INTERVALO DE TIEMPO (D/H/M/S)"] = grupo_ordenes["FECHA DE PLANIFICACION"]-grupo_ordenes["FECHA DE ORDEN DE COMPRA"]
grupo_ordenes.sort_values('PROVEEDOR', inplace = True)

grupo_ordenes['CANTIDAD DE PLANIFICACIONES']=1
grupo_ordenes['INTERVALO DE TIEMPO'] = (grupo_ordenes['FECHA DE PLANIFICACION'] - grupo_ordenes['FECHA DE ORDEN DE COMPRA'])  / np.timedelta64(1,'D')
grupo_ordenes_dif_fecha = grupo_ordenes.groupby(["PROVEEDOR","ORDEN DE COMPRA"],as_index=False).agg({"INTERVALO DE TIEMPO":"mean","CANTIDAD DE PLANIFICACIONES":"count"})


#-----------------------------------------------------------------

#---cUENTAS POR PAGAR
cxp= pd.read_csv('tabla_cuentas_x_pagar.csv')
cxp=cxp.drop(["FECHA_VENCIMIENTO","TIPO_MONEDA","MONTO_ORDEN"],axis=1)
total_cxp= cxp["MONTO"].sum()


#-------- Agrupacion de ordenes planificadas por Rubro y tipo de moneda
df_ord= pd.read_csv("orden_compra_info.csv") # Aqui leemos el archivo con informacion de ordenes de compra

#--Categorizamos por tipo de moneda
in_bolivar= df_ord['TIPO_MONEDA']== 'BOLIVAR' 
in_euro= df_ord['TIPO_MONEDA']== 'EURO'
in_petro= df_ord['TIPO_MONEDA']== 'PETRO'

# Creamos una tabla con filtro en tipo de moneda
bolivar= df_ord[in_bolivar]
euro= df_ord[in_euro]
petro= df_ord[in_petro]

#---- Separamos por tipo: Bolivares------
rubro_bs= bolivar.groupby(['RUBRO','NOMBRE_PROVEEDOR']).sum()
rubro_bs_a= np.array(rubro_bs)
r_bs= np.array(rubro_bs.index)
pro_bs=[]
rub_bs=[]
rubro_bs_array= []
for i in range(0,len(r_bs)):
    rub_bs= [r_bs[i][0]]+rub_bs
    pro_bs=[r_bs[i][1]]+pro_bs
    rubro_bs_array = [rubro_bs_a[i][0]]+ rubro_bs_array
rub_bs= np.array(rub_bs[::-1])
pro_bs= np.array(pro_bs[::-1])
rubro_bs_array= np.array(rubro_bs_array[::-1])

df_bs= pd.DataFrame({'rubro':rub_bs,'proveedor':pro_bs,'monto':rubro_bs_array})
df_bs['Bolivares']='Bolivares'

#------ EURO-----------
rubro_e= euro.groupby(['RUBRO','NOMBRE_PROVEEDOR']).sum()
rubro_e_a= np.array(rubro_e)
r_e= np.array(rubro_e.index)
pro_e=[]
rub_e=[]
rubro_e_array= []
for i in range(0,len(r_e)):
    rub_e= [r_e[i][0]]+rub_e
    pro_e=[r_e[i][1]]+pro_e
    rubro_e_array = [rubro_e_a[i][0]]+ rubro_e_array
rub_e= np.array(rub_e[::-1])
pro_e= np.array(pro_e[::-1])
rubro_e_array= np.array(rubro_e_array[::-1])

df_e= pd.DataFrame({'rubro':rub_e,'proveedor':pro_e,'monto':rubro_e_array})
df_e['Euros']='Euros'

#---PETRO-----------------------
rubro_p= petro.groupby(['RUBRO','NOMBRE_PROVEEDOR']).sum()
rubro_p_a= np.array(rubro_p)
r_p= np.array(rubro_p.index)
pro_p=[]
rub_p=[]
rubro_p_array= []
for i in range(0,len(r_p)):
    rub_p= [r_p[i][0]]+rub_p
    pro_p=[r_p[i][1]]+pro_p
    rubro_p_array = [rubro_p_a[i][0]]+ rubro_p_array
rub_p= np.array(rub_p[::-1])
pro_p= np.array(pro_p[::-1])
rubro_p_array= np.array(rubro_p_array[::-1])

df_p= pd.DataFrame({'rubro':rub_p,'proveedor':pro_p,'monto':rubro_p_array})
df_p['Petro']='Petro'