import json
import pandas as pd
import streamlit as st
import requests

# ------- CONFIGURAÇÕES -------
OLLAMA_URL = "http://localhost:11434/api/generate"
ollama_model = "gpt-oss:20b"

# ------- CARREGANDO DADOS -------

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ------- MONTAR CONTEXTO -------
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']}, anos, {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ------- SYSTEM PROMPT -------
SYSTEM_PROMPT = f""" Você é o FinTutor, um educador financeiro amigável e didático.

OBJETIVO:
Seu objetivo é ensinar sobre finanças de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais. Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# ------- CHAMAR OLLAMA -------
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

PERGUNTA: 
{msg}"""

    r = requests.post(OLLAMA_URL, json={"model": "gpt-oss:20b", "prompt": prompt, "stream": False})
    return r.json()['response']

# ------- INTERFACE DO USUÁRIO -------
st.title("💰FinTutor, Educador Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
