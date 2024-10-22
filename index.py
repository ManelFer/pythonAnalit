import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados
data_pas = pd.read_csv("https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv", 
                        names=['ano','sigla_uf','nome_uf','id_municipio','nome_municipio','nome_regiao','nome_empresa','porte_empresa','tecnologia','transmissao','acessos'], 
                        low_memory=False)

# Visualização
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(10,10))

# Exemplo de boxplot com colunas existentes
sns.boxplot(data=data_pas, x="porte_empresa", y="acessos", ax=axs[0][0])
axs[0][0].set_title('Acessos por Porte da Empresa')

sns.boxplot(data=data_pas, x="tecnologia", y="acessos", ax=axs[0][1])
axs[0][1].set_title('Acessos por Tecnologia')

# Adicione mais visualizações conforme necessário
sns.boxplot(data=data_pas, x="nome_uf", y="acesso", ax=axs[1][0])
axs[1][0].set_title('Acessos por regiao')

plt.tight_layout()
plt.show()