# 🏥 Automação de Triagem de Saúde & Análise de Sentimentos

Este projeto foi desenvolvido para otimizar o processo de triagem em clínicas médicas. Ele utiliza Inteligência Artificial para ler o feedback dos pacientes e avaliar o risco de absenteísmo (*No-Show*), além de utilizar consultas estruturadas em banco de dados para analisar a satisfação geral.

---

## 📷 Demonstração do Sistema Funcionando

<img width="483" height="273" alt="Captura de tela 2026-06-05 135343" src="https://github.com/user-attachments/assets/d73f6b70-853a-47d9-8981-67c47e10465a" />


---

## 🚀 Tecnologias Utilizadas
* **Python** * **Pandas** * **Google Gemini API** * **SQLite** ## 📊 Como o Projeto Funciona
1. **Processamento de Dados:** Leitura e manipulação da base histórica de comentários dos pacientes (`feedbacks_clinica.csv`) utilizando Pandas.
2. **Avaliação com Inteligência Artificial:** O script em Python envia cada comentário para a API do Gemini, que atua como um analista de triagem e devolve o risco de o paciente faltar em consultas futuras (`BAIXO`, `MÉDIO` ou `ALTO`).
3. **Análise de Sentimentos (SQL):** Criação de uma query analítica avançada (`Consulta01.sql`) utilizando `CASE WHEN` para mapear palavras-chave reais da base e `GROUP BY` para contar o volume de comentários Positivos, Negativos e Neutros.

## 🗂️ Estrutura do Repositório
* `main.py`: Script de automação que integra o Pandas com a API do Gemini.
* `feedbacks_clinica.csv`: Base de dados real de testes contendo os históricos de atendimento.
* `Consulta01.sql`: Script de extração e agrupamento de sentimentos no banco de dados.

## 🛠️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/souzzaigor/projeto-automacao-dados.git](https://github.com/souzzaigor/projeto-automacao-dados.git)
