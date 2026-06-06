#%%
import pandas as pd
import sqlite3
import time
# 1. IMPORTAÇÃO NOVA
from google import genai

print("Iniciando o Pipeline de Dados com IA...")
#%%
# 2. CONFIGURAÇÃO NOVA
CHAVE_API = "SUA_CHAVE_AQUI" 
client = genai.Client(api_key=CHAVE_API)


conexao = sqlite3.connect('banco_saude.db')
query = "SELECT id_atendimento, nome_paciente, comentario FROM historico_pacientes"
df_pacientes = pd.read_sql_query(query, conexao)
conexao.close()

df_teste = df_pacientes.head(5).copy()
lista_riscos = []

print("\n--- Analisando Comentários com o Gemini ---")

for index, linha in df_teste.iterrows():
    paciente = linha['nome_paciente']
    comentario = linha['comentario']
    
    prompt = f"""
    Você é um analista de triagem de uma clínica de saúde.
    Leia o feedback deixado por este paciente após a última consulta: "{comentario}"
    
    Sua tarefa é avaliar o "Risco de No-Show" (Risco deste paciente faltar numa próxima consulta).
    Se o comentário for positivo ou neutro, o risco é BAIXO.
    Se o comentário for uma reclamação leve, o risco é MEDIO.
    Se for uma reclamação grave (muita demora, descaso), o risco é ALTO.
    
    Responda APENAS com uma palavra: BAIXO, MEDIO ou ALTO.
    """
    
    # 3. CHAMADA ATUALIZADA DA API
    resposta = client.models.generate_content(
       model="gemini-3.1-flash-lite",
        contents=prompt
    )
    
    classificacao = resposta.text.strip()
    
    print(f"Paciente: {paciente} | IA Classificou: Risco {classificacao}")
    lista_riscos.append(classificacao)
    time.sleep(2)

df_teste['risco_falta_ia'] = lista_riscos

print("\n--- Tabela Final Enriquecida com IA ---")
print(df_teste[['nome_paciente', 'risco_falta_ia']])