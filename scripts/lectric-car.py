# %%
import pandas as pd
import matplotlib as plot
import matplotlib.pyplot as plt
plt.style.use("ggplot")

#Lendo o csv e atribuindo a uma variavel
dfcar = pd.read_csv("./data/ElectricCarData_Clean.csv")
pd.set_option('display.max_rows', dfcar.shape[0]+1)
dfcar.head()

# %%
# Vendo a quantidade de linhas e colunas do banco de dados
dfcar.shape

# %%
dfcar.info()

# %%
# Verificando a existencia de valores nulos
dfcar.isnull().sum()

# %%
# Mostrando as duas primeiras linhas
dfcar.head(2)

# %%
# Pegando aleatoriamente 10 linhas em qualquer posição
dfcar.sample(2)

# %% [markdown]
# RENOMEANDO AS COLUNAS

# %%
# -------------------------------------------------
#  REMOMEANDO AS COLUNAS E PEGANDO A PRIMEIRA LINHA COM O NOME DAS MESMAS
# -------------------------------------------------
dfcar = dfcar.rename(columns =
{
    'Brand': 'Marca', 'Model': 'Modelo','AccelSec': 'Acel/s','TopSpeed_KmH':'Veloc_Max_Kmh',
    'Range_Km':'Autonomia_km','FastCharge_KmH':'Km/Hr_Carga','PowerTrain':'Tracao',
    'PlugType': 'Tipo_Conector','BodyStyle': 'Estilo', 'Segment':'Segmento','Assentos': 'Assentos', 
    'PriceEuro': 'Preco(€)','Efficiency_WhKm':'Eficiencia_WhKm'
}) 
# duas maneiras de ver o nome das colunas
dfcar.head(0)
#dfcar.columns
# -------------------------------------------------

# %%
# -------------------------------------------------
#  OBTENDO UMA DESCRIÇÃO DOS DADOS(poderia ser feito de forma direta, sem armazenar o result em uma variável)
# -------------------------------------------------
desc_dados = dfcar.describe()
desc_dados
# -------------------------------------------------

# %% [markdown]
# MARCAS E QUANTIDADE DE LANÇAMENTOS

# %%
# -------------------------------------------------
#  MARCAS E QUANTIDADE DE LANÇAMENTOS
# -------------------------------------------------

df_marca_modelo = dfcar.groupby('Marca')['Marca'].count().sort_values(ascending=False).head(10)
df_marca_modelo.plot.barh(title= "Marcas X Quantidade", grid=True, legend=True, style=sorted, edgecolor="black")
plt.ylabel("Marcas")
plt.xlabel("Quantidade de Lançamentos")
# -------------------------------------------------

# %% [markdown]
# DETALHANDO A AUTONOMIA

# %%
#-------------------------------------------------
# RELACIONANDO OS MODELOS DE MAIOR AUTONOMIA
#-------------------------------------------------
df_max_auton = dfcar[["Autonomia_km", "Marca", "Modelo"]]
df_max_auton.sort_values(by="Autonomia_km", ascending=False).head().reset_index()
#-------------------------------------------------

# %%
#-------------------------------------------------
# RELACIONANDO OS MODELOS DE MAIOR AUTONOMIA USANDO O NLARGEST
# PARA RELACIONAR OS MODELOS DE MENOR AUTONOMIA BASTA USAR O 
#-------------------------------------------------
df_max_auton = dfcar[["Autonomia_km", "Marca"]]
a = df_max_auton.nlargest(5, "Autonomia_km")
a.plot.bar(title='Autonomia (em km)', x="Marca", legend=True, style=sorted, edgecolor="black", rot=8, grid=True, width=0.8)
plt.ylabel("Autonomia")
plt.xlabel("Marca")
#-------------------------------------------------

# %% [markdown]
# MOSTRANDO A AUTONOMIA EM GRÁFICO

# %%
#-------------------------------------------------
# PEGANDO MODELOS COM AUTONOMIA ACIMA DE 400 KM
#-------------------------------------------------
df_max_auton = dfcar.loc[dfcar["Autonomia_km"] > 400, ["Marca", "Autonomia_km"]]
vauton = df_max_auton.sort_values(by="Autonomia_km")
vauton.plot.bar(
    title='Modelos com Autonomia Acima de 400 km', 
    x="Marca", 
    legend=True, 
    style=sorted, 
    edgecolor="green", 
    grid=True
)
#-------------------------------------------------

# %%
#-------------------------------------------------
# LOCALIZANDO O FABRICANTE DO MODELO DE MAIOR AUTONOMIA
#-------------------------------------------------
# Pegando a primeira marca da lista.
# Obaservar que não é necessariamente o que tem a maior autonomia
dfcar.iloc[0, 0]
#-------------------------------------------------

# %%
#-------------------------------------------------
# PERCENTUAL GRÁFICO DOS TIPOS DE TRAÇÃO
#-------------------------------------------------
df_tracao = dfcar.groupby("Tracao")["Tracao"].count()
trac = df_tracao
trac.plot.pie(title="Tipo de Tração", legend=True, style=sorted)
#-------------------------------------------------

# %% [markdown]
# 05 MODELOS DE MAIOR VELOCIDADE (em Kmh).

# %%
# #-------------------------------------------------
# OBTENDO A LISTA DOS MODELOS MAIS VELOZES
# #-------------------------------------------------
df_veloc_max = dfcar.loc[dfcar['Veloc_Max_Kmh'] > 0, ['Marca', 'Modelo', 'Veloc_Max_Kmh']]
# #-------------------------------------------------
# Ordenando os valores e mostrando os cinco primeiros resultados
vmax = df_veloc_max.sort_values(by="Veloc_Max_Kmh", ascending=False).head()
vmax.plot.bar(title = 'Velocidade Máxima', x='Marca', rot=8, legend=True, style=dict)
#-------------------------------------------------

# %% [markdown]
# MODELOS COM DOIS ASSENTOS

# %%
#---------------------------------------------------
# OBTENDO LISTA DE MODELOS COM DOIS ASSENTOS
#---------------------------------------------------
# Agruopando por quantidade de assentos
df_dois_assentos = dfcar.loc[dfcar['Seats'] == 2, ["Marca", "Modelo",  "Seats", "Preco(€)"]]
df_dois_assentos[["Marca", "Preco(€)"]]
#---------------------------------------------------

# %% [markdown]
# MODELO COM QUATRO ASSENTOS

# %%
#-------------------------------------------------
# OBTENDO PERCENTUAL GRÁFICO DA QUANTIDADE DE ASSENTOS
#-------------------------------------------------
df_qtd_assentos_por_modelo = dfcar.loc[dfcar['Seats'] >= 0, ['Marca', 'Seats', "Modelo"]]
qt = df_qtd_assentos_por_modelo.groupby('Seats')['Seats'].count()
qt.plot.pie(title = 'Grafico da Quantidade de Assentos', rot=8, legend=True)
#-------------------------------------------------


# %% [markdown]
# # MODELO COM CINCO ASSENTOS OU MAIS

# %%
#-------------------------------------------------
# OBTENDO PRIMEIROS MODELOS COM CINCO ASSENTOS
#-------------------------------------------------
df_qtd_assentos_por_modelo = dfcar.loc[dfcar['Seats'] == 5, ["Seats", "Marca", "Modelo"]]
df_qtd_assentos_por_modelo.head()
#-------------------------------------------------

# %%
#-------------------------------------------------
# OBTENDO PRIMEIROS MODELOS COM CINCO ASSENTOS
#-------------------------------------------------
df_qtd_assentos_por_modelo = dfcar.loc[dfcar['Seats'] == 5, ["Seats", "Marca", "Modelo"]]
df_qtd_assentos_por_modelo.head()
#-------------------------------------------------

# %%
#-------------------------------------------------
# OBTENDO QUANTIDADE DE ASSENTOS E QUANTIDADE DE MODELOS 
#-------------------------------------------------
df_agrupando_assentos = dfcar.loc[dfcar['Seats'] >= 0, ["Seats", "Marca"]]
df_agrupando_assentos.groupby(by='Seats').count()


# %% [markdown]
# # MODELO COM SEIS E SETE ASSENTOS 

# %%
# --------------------------------------------------
# OBTENDO AS MARCAS E MODELOS COM SEIS OU MAIS ASSENTOS
# --------------------------------------------------
df_qtd_assentos_por_modelo = dfcar.loc[dfcar["Seats"] >= 6, ["Seats", "Marca", "Modelo"]]
df_qtd_assentos_por_modelo.sort_values(by="Seats").reset_index()
# --------------------------------------------------

# %%
# JUNTANDO AUTONOMIA E VELOCIDADE EM UMA UNICA AMOSTRA DE DADOS
#import matplotlib as plot
import matplotlib.pyplot as plot
plot.style.use('ggplot')

# %% [markdown]
# AGRUPANDO POR ESTILO

# %%
# --------------------------------------------------
# RELACIONANDO OS ESTILOS
# --------------------------------------------------
estilos = dfcar['Estilo']
df_est = pd.DataFrame([estilos.unique()])
display(df_est.T)
# --------------------------------------------------

# %% [markdown]
# AGRUPANDO POR MARCA E ESTILO

# %%
# --------------------------------------------------
# RELACIONANDO OS ESTILOS COM OS MODELOS (PEGANDO APENAS UMA AMOSTRA)
# --------------------------------------------------
sedan = dfcar.loc[dfcar["Estilo"] == "Sedan", ["Marca", "Estilo", "Modelo"]]
suv = dfcar.loc[dfcar["Estilo"] == "SUV", ["Marca", "Estilo", "Modelo"]]
Hatch = dfcar.loc[dfcar["Estilo"] == "Hatchback", ["Marca", "Estilo", "Modelo"]]
df = pd.concat([sedan, suv, Hatch])
df.sample(5)
# --------------------------------------------------

# %%
# --------------------------------------------------
# OBTENDO DOIS MODELOS DE UMA MARCA ESPECIFICA 
# E RELACIONANDO MARCA, ESTILO, MODELO E PREÇO
# --------------------------------------------------
marca_espec = dfcar.loc[[51, 8], ["Marca", "Estilo", "Modelo", "Preco(€)"]]
marca_espec
# --------------------------------------------------

# %%
# --------------------------------------------------
# OBTENDO O QUANTITATIVO DE LANÇAMENTOS - OUTRA FORMA, SEM GRÁFICO
# --------------------------------------------------
qtd_lancamentos = dfcar.groupby("Marca")['Marca'].count()
df = pd.Series(qtd_lancamentos, name="Lançamentos (Qtd)")
#df.nlargest(4, 'Veloc_Max_Kmh')
df.to_frame()
# --------------------------------------------------

# %%
# --------------------------------------------------
# OTENDO MARCAS E RESPECTIVOS MODELOS LANÇADOS PELA MESMA
# --------------------------------------------------
qt = dfcar.groupby("Marca")['Modelo'].sum()
qt.to_frame()
# --------------------------------------------------