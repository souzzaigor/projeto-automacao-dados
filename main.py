#%%
import pandas as pd
import sqlite3

print("Iniciando o Pipeline de Dados...")
conexao = sqlite3.connect('banco_saude.db')
#%%
query = """
SELECT id_atendimento, comentario 
FROM historico_pacientes
"""
df_pacientes = pd.read_sql_query(query, conexao)

conexao.close()

print("\nDados extraídos com sucesso para o Pandas!")
print("-" * 60)

print(df_pacientes.head())