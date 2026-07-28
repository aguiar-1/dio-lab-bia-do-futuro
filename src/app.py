
import json 
import streamlit as st
import pandas as pd
import requests


#CONFIG
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

perfil = json.load(open('./dados/perfil_investidor.json'))
transacoes = pd.read_csv('./dados/transacoes.csv')
historico = pd.read_csv('./dados/historico_atendimento.csv')
produtos = json.load(open('./dados/produtos_financeiros.json'))


contexto = f"""
CLIENTE: {perfil['nome']},{perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {'reserva_emergencia_atual'}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT 

SYSTEM_PROMPT = """
Você é o JotaF, um educador financeiro especialista.

Seu objetivo é ensinar educação financeira de forma clara e prática, ajudando as pessoas a entender de maneira simples e a tomarem decisões conscientes.

Regras:
- Você NÃO inventa dados
- Você NÃO promete ganhos
- Você NÃO recomenda algum investimento específico
- Você sempre pergunta se o cliente está acompanhando
- Linguagem clara e amigável 

"""

# CHAMAR OLLAMA

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

#INTERFACE

st.title("JotaF,")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))



