import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Carregar os dados
data_pas = pd.read_csv("https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv", 
                        names=['ano','sigla_uf','nome_uf','id_municipio','nome_municipio','nome_regiao','nome_empresa','porte_empresa','tecnologia','transmissao','acessos'], 
                        low_memory=False)

# Gráfico de pizza para estados
estado_acessos = data_pas.groupby('nome_uf')['acessos'].sum().reset_index()
fig_estado = px.pie(estado_acessos, values='acessos', names='nome_uf', title='Acessos por Estado')

# Gráfico de pizza para empresas
empresa_acessos = data_pas.groupby('nome_empresa')['acessos'].sum().reset_index()
fig_empresa = px.pie(empresa_acessos, values='acessos', names='nome_empresa', title='Acessos por Empresa')

# Gráfico de pizza para tecnologia
tecnologia_acessos = data_pas.groupby('tecnologia')['acessos'].sum().reset_index()
fig_tecnologia = px.pie(tecnologia_acessos, values='acessos', names='tecnologia', title='Acessos por Tecnologia')

# Gráfico de pizza para acessos totais
acessos_totais = data_pas['acessos'].sum()
fig_acessos = px.pie(data_pas.groupby('nome_uf')['acessos'].sum().reset_index(), values='acessos', names='nome_uf', title='Acessos Totais')

# Criar o dashboard
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard de Acessos'),
    dcc.Tabs([
        dcc.Tab(label ='Acessos por Estado', children=[
            dcc.Graph(figure=fig_estado)
        ]),
        dcc.Tab(label='Acessos por Empresa', children=[
            dcc.Graph(figure=fig_empresa)
        ]),
        dcc.Tab(label='Acessos por Tecnologia', children=[
            dcc.Graph(figure=fig_tecnologia)
        ]),
        dcc.Tab(label='Acessos Totais', children=[
            dcc.Graph(figure=fig_acessos)
        ])
    ])
])

if __name__ == '__main__':
    app.run_server()