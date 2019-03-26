# Heatmaps as timetables for datathon CRE,ARAFER

import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
import cufflinks as cf
cf.go_offline()
import plotly

import plotly.plotly as py
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

os.chdir('/home/celine/Data/Datathon_Energy')

df_initial = pd.read_csv('initial.csv', names= ['index', 'heure_debut', 'machine'],
                                 header=None, skiprows=1)
D = 500  # nombre de demandes
hours = 24
np.random.seed(42)

# DICO machines
dico_machine_conso = {1: [4, 4], 2: [1, 3]} #1 lave vaisselle / 2 lave linge

# Simule le type de machine : 1 ou 2 (lave à vaisselle ou machine à laver)
type_machine_simul = df_initial['machine'] # Simulation du type de machine

# Simule l'heure de démarrage de la machine
heure_demarrage_simul = df_initial['heure_debut']

# Initialise la matrice de résultat
df_results = pd.DataFrame(np.zeros((D,24)))

# Rajoute des 1 pour le début de la tâche
for i,j,h in zip(range(df_results.shape[0]), heure_demarrage_simul, type_machine_simul):
    if h == 1:
        df_results.loc[i, j:j + dico_machine_conso[h][0]] = 1
    else: 
        df_results.loc[i, j:j + dico_machine_conso[h][0]] = 1

df_predict = pd.read_csv('prediction.csv', names= ['index', 'heure_debut', 'machine'],
                                 header=None, skiprows=1)

D = 500  # nombre de demandes
hours = 24
np.random.seed(42)

# DICO machines
dico_machine_conso = {1: [2.5, 4], 2: [2, 3]} #1 lave vaisselle / 2 lave linge

# Simule le type de machine : 1 ou 2 (lave à vaisselle ou machine à laver)
type_machine_simul = df_predict['machine'] # Simulation du type de machine

# Simule l'heure de démarrage de la machine
heure_demarrage_simul = df_predict['heure_debut']

# Initialise la matrice de résultat
df_results_ = pd.DataFrame(np.zeros((D,24)))

# Rajoute des 1 pour le début de la tâche
for i,j,h in zip(range(df_results_.shape[0]), heure_demarrage_simul, type_machine_simul):
    if h == 1:
        df_results_.loc[i, j:j + dico_machine_conso[h][0]] = 1
    else: 
        df_results_.loc[i, j:j + dico_machine_conso[h][0]] = 1


df_results_.to_csv('df_results_.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Watt\'y'),

    html.Div(children='''
       Nos résultats Watt\'y'
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'z': np.array(df_results),
                 'x': list(range(hours)),
                 'y': ['Tâche_%s'%(str(i)) for i in range(D)], 
                 'type': 'heatmap', 
                 'colorscale': 'Blues',
                 'name': 'Aléatoire'},
                {'z': np.array(df_results_),
                 'x': list(range(hours)),
                 'y': ['Tâche_%s'%(str(i)) for i in range(D)], 
                 'type': 'heatmap', 
                 'colorscale': 'rainbow',
                 'name': 'Q_learning'},
            ],
            'layout': {
                'title': 'Watt\'y application'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)



