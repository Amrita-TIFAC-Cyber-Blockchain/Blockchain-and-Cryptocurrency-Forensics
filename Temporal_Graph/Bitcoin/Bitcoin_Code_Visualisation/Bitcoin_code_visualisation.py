####################################################################################################################

# Program Name : code_visualisation.py 
# Description  : Python code for Temporal Graph Visualisation
# Author       : Mohamed Feroz Khan and Ramaguru sir
# Created Date : 14-Dec-2022
# Last Updated : 13-April-2023
# Execution    : Python code_visualisation.py
####################################################################################################################

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import pathpy as pp

# Given Dataset

df=pd.read_excel('Fraud_BCT_BTC.xlsx')
t = pp.TemporalNetwork()

[t.add_edge(df['Target address'][i],df['receiving address'][i],int(df['time'][i])) for i in range(len(df))]

# style for the node

style = {    
  'ts_per_frame': 1, 
  'ms_per_frame': 2000,
  'look_ahead': 2, 
  'look_behind': 2, 
  'node_size': 15, 
  'inactive_edge_width': 2,
  'active_edge_width': 4, 
  'label_color' : '#706f6f',
  'label_size' : '24px',
  'label_offset': [0,5]
  }

# Visualisation for the given dataset

pp.visualisation.export_html(t, 'my_temporal_network_sample_sicp.html', **style)