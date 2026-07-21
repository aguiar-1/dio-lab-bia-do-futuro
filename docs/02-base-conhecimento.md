# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve no JotaF? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |



---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto fundo multimercado foi substituido pelo fundo imobiliário e o produto tesouro selic foi substituído pelo criptomoeda.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Podemos injetar diretamente no prompt ou podemos utilizar os arquivos via código, como abaixo:
```python

import panda as pd
import json
 #CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read-csv('data/transacoes.csv')
 #JSONs
with open('data/perfil_investidor.json','r','encoding= 'utf-8') as f:
   perfil = json.load(f)
with open('data/produtos_financeiros.json','r','encoding= 'utf-8') as f:
   produtos = json.load(f)

```


### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?


```text
Dados do Cliente (data/perfil_investidor.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir uma carteira diversificada",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": true,
  "metas": [
    {
      "meta": "Chegar em 10.000 em renda variável",
      "valor_necessario": 5000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Trocar de veiculo",
      "valor_necessario": 45000.00,
      "prazo": "2027-12"
    }
  ]
}

Histórico de atendimento (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

Transações do Cliente (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5000.00,entrada
2025-10-02,Aluguel,moradia,1200.00,saida
2025-10-03,Supermercado,alimentacao,450.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-07,Farmácia,saude,89.00,saida
2025-10-10,Restaurante,alimentacao,120.00,saida
2025-10-12,Uber,transporte,45.00,saida
2025-10-15,Conta de Luz,moradia,180.00,saida
2025-10-20,Academia,saude,99.00,saida
2025-10-25,Combustível,transporte,250.00,saida

Produtos Disponíveis para ensino (data/produtos_financeiros.json):
[
  {
    "nome": "Criptomoeda",
    "categoria": "renda_variavel",
    "risco": "alto",
    "rentabilidade": "Depende da estratégia adotada",
    "aporte_minimo": 10.00,
    "indicado_para": "Perfil de risco arrojado"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Imobiliário - FII",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "costuma variar entre 10% e 14% ao ano",
    "aporte_minimo": 10.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Objetivo: Construir uma carteira diversificada

Resumo de gastos:
- Apartamento: R$1450,00
- Alimentação: R$650,00
- Transporte: R$250,00
- Saúde: R$275,00
- Lazer: R$240,00
- Total: R$ 2865,00

Produtos disponíveis para aplicar:
- Criptomoedas (risco alto)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Imobiliário - FII (risco moderado)
- Fundo de Ações (risco alto)
...
```

