####################################################################################################################

# Program Name : code_style.py 
# Description  : Python code for Temporal Graph Visualisation
# Author       : Mohamed Feroz Khan and Ramaguru sir
# Created Date : 27-Nov-2022
# Last Updated : 13-April-2023
# Execution    : Python code_style.py
####################################################################################################################


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import pathpy as pp

df=pd.read_excel('Backup_BCT_BTC_500.xlsx')
t = pp.TemporalNetwork()

[t.add_edge(df['address'][i],df['balance'][i],int(df['time'][i])) for i in range(len(df))]

# style for first node

style1 = {    
  'ts_per_frame': 1, 
  'ms_per_frame': 2000,
  'look_ahead': 2, 
  'look_behind': 2, 
  'node_size': 15, 
  'inactive_edge_width': 2,
  'active_edge_width': 4, 
  'label_color' : '#ffffff',
  'label_size' : '24px',
  'label_offset': [0,5],
  'active_node_color' : '#003800'
  }

# style for second node

style2 = {    
  'ts_per_frame': 1, 
  'ms_per_frame': 2000,
  'look_ahead': 2, 
  'look_behind': 2, 
  'node_size': 15, 
  'inactive_edge_width': 2,
  'active_edge_width': 4, 
  'label_color' : '#ffffff',
  'label_size' : '24px',
  'label_offset': [0,5],
  }

stylenode = { 
	'ts_per_frame': 1, 
  	'ms_per_frame': 2000,
  	'look_ahead': 2, 
  	'look_behind': 2, 
  	'node_size': 15, 
  	'inactive_edge_width': 2,
  	'active_edge_width': 4
} 

# loop and style for the node

i=0
for i in range(len(df)):
	if df['time'][i] == 1:
    		pp.visualisation.plot(t, **style1)
	elif df['time'][i] == 2:
    		pp.visualisation.plot(t, **style2)
	else:
    		pp.visualisation.plot(t, **style1)

# visualisation for the given dataset

pp.visualisation.export_html(t, 'my_temporal_network_sample.html')