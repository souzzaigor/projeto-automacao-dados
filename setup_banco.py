#%%
import pandas as pd
import sqlite3
#%%
df = pd.read_csv("feedbacks_clinica.csv")
conexao = sqlite3.connect('banco_saude.db')
#%%
df.to_sql('historico_pacientes', conexao, if_exists='replace', index= False)
print("Banco de Dados criado com sucesso!")
conexao.close()