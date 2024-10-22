import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data_pas = pd.read_csv("https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv", names=['ano','sigla_uf','nome_uf','id_municipio','nome_municipio','nome_regiao','nome_empresa','porte_empresa','tecnologia','transmissao','acessos'], low_memory=False)
#print(data_pas)
data_pas.describe()

#calculo da media
data_pas[['ano','sigla_uf','nome_uf','id_municipio','nome_municipio','nome_regiao','nome_empresa','porte_empresa','tecnologia','transmissao','acessos']].mean()

#calculo da mediana
data_pas[['ano','sigla_uf','nome_uf','id_municipio','nome_municipio','nome_regiao','nome_empresa','porte_empresa','tecnologia','transmissao','acessos']].median()