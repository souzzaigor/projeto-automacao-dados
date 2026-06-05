#%%
import pandas as pd
import sqlite3
import random
from datetime import datetime, timedelta
#%%
# 1. Listas com pedaços de nomes e feedbacks
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana", "Marcos", "Letícia", "Lucas", "Rebeca", "Felipe", "Thiago", "Camilla", "João", "Rosane", "Nathaly", "Laura", "Sofia", "Jorge"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Carvalho", "Banzoli", "Olegário", "Dutra", "Siqueira", "De Castro", "Bertholdo", "Andrade", "Gonsales", "Teixeira", "Saquarema"]

feedbacks_positivos = [
    "Atendimento excelente, médico muito atencioso.",
    "Amei a nova unidade, clínica impecável.",
    "Fui atendido no horário, tudo perfeito.",
]
feedbacks_neutros = [
    "Atendimento normal, dentro do esperado.",
    "Tudo ok com a consulta.",
    "Vim apenas pegar um exame."
]
feedbacks_negativos = [
    "Fiquei mais de 1 hora esperando, um absurdo na recepção.",
    "O aplicativo de agendamento travou e perdi minha vaga.",
    "Médico mal olhou na minha cara, parecia com pressa.",
    "Tentei reagendar e ninguém atende o WhatsApp."
]

novos_clientes = []
#%%

# Gera todas as 195 combinações de nomes possíveis
todas_combinacoes = [f"{n} {s}" for n in nomes for s in sobrenomes]

# Escolhe exatamente 85 nomes dessa lista, garantindo 100% que nenhum se repita
nomes_unicos_sorteados = random.sample(todas_combinacoes, 85)

# 2. Vai rodar 85 vezes para criar os clientes (do ID 16 até o 100)
for i in range(16, 101):
    # Pega um nome da nossa lista de nomes únicos
    nome_sorteado = nomes_unicos_sorteados[i - 16] 
    
    # Sorteia uma data aleatória em Junho de 2026
    data_consulta = datetime(2026, 6, 1) + timedelta(days=random.randint(1, 29))
    data_str = data_consulta.strftime("%Y-%m-%d")

    # Sorteia se o cliente vai reclamar, elogiar ou ser neutro
    tipo_feedback = random.choice(["positivo", "neutro", "negativo", "negativo"]) 
    
    if tipo_feedback == "positivo":
        comentario = random.choice(feedbacks_positivos)
    elif tipo_feedback == "neutro":
        comentario = random.choice(feedbacks_neutros)
    else:
        comentario = random.choice(feedbacks_negativos)

    # Guarda a linha criada
    novos_clientes.append([i, data_str, nome_sorteado, comentario])

# 3. Transforma a lista em um DataFrame do Pandas
df_novos = pd.DataFrame(novos_clientes, columns=['id_atendimento', 'data', 'nome_paciente', 'comentario'])
#%%
# 4. Conecta no seu banco de dados e insere direto nele!
conexao = sqlite3.connect('banco_saude.db')

df_novos.to_sql('historico_pacientes', conexao, if_exists='append', index=False)

conexao.close()

print("Sucesso! 85 novos clientes com nomes 100% ÚNICOS foram inseridos DIRETO no banco de dados.")