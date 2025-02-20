# Exemplos de Loops em Python

Este repositório contém uma coleção de exemplos em Python demonstrando diferentes tipos de loops e suas aplicações em cenários reais.

## Índice
1. [Estruturas Básicas de Loop](#estruturas-básicas-de-loop)
2. [Sistema de Registro de Hóspedes](#sistema-de-registro-de-hóspedes)
3. [Análise de Vendas](#análise-de-vendas)
4. [Gestão de Estoque](#gestão-de-estoque)
5. [Análise de Desempenho de Produtos](#análise-de-desempenho-de-produtos)
6. [Controle de Qualidade de Fabricação](#controle-de-qualidade-de-fabricação)
7. [Desempenho da Equipe de Vendas](#desempenho-da-equipe-de-vendas)
8. [Controle de Loop](#controle-de-loop)
9. [Sistema de Registros Acadêmicos](#sistema-de-registros-acadêmicos)

## Estruturas Básicas de Loop
- Introdução aos diferentes tipos de loops em Python:
  - Loop `for` padrão com `range()`
  - Loop através de listas diretamente
  - Uso de `enumerate()` para acesso ao índice
- Exemplos incluem rastreamento de produtos e produção

## Sistema de Registro de Hóspedes
- Sistema simples de registro de hóspedes que coleta:
  - Nome do hóspede
  - CPF
- Armazenamento de dados em listas aninhadas
- Tratamento dinâmico da quantidade de hóspedes

## Análise de Vendas
- Sistema de acompanhamento de desempenho de vendas
- Funcionalidades:
  - Monitoramento de metas de vendas
  - Acompanhamento de desempenho individual
  - Cálculo de atingimento de meta
  - Análise de desempenho da equipe

## Gestão de Estoque
- Sistema de monitoramento de nível de estoque
- Funcionalidades:
  - Alertas de nível mínimo de estoque
  - Acompanhamento de quantidade de produtos
  - Tratamento de múltiplas categorias de produtos

## Análise de Desempenho de Produtos
- Comparação ano a ano (2023 vs 2024)
- Métricas acompanhadas:
  - Volume de vendas
  - Percentual de crescimento
  - Desempenho específico por produto

## Controle de Qualidade de Fabricação
- Monitoramento de estoque multi-fábrica
- Funcionalidades:
  - Alertas de limite mínimo de estoque
  - Acompanhamento específico por fábrica
  - Comparação entre fábricas

## Desempenho da Equipe de Vendas
- Sistema de análise da equipe de vendas
- Métricas:
  - Percentual de atingimento de meta
  - Identificação do melhor vendedor
  - Estatísticas de desempenho da equipe

## Controle de Loop
- Exemplos de declarações de controle de loop:
  - `break`: Interrupção completa do loop
  - `continue`: Pular para próxima iteração
- Aplicações em cenários reais de vendas

## Sistema de Registros Acadêmicos
- Sistema de gestão de notas de alunos
- Funcionalidades:
  - Acompanhamento de notas individuais
  - Cálculo de média
  - Monitoramento de limite de desempenho
  - Análise estatística

## Exemplos de Uso

### Loop For Básico
```python
for i in range(10):
    print(i)
```

### Iteração de Lista com Enumerate
```python
produtos = ["coca", "pepsi", "guarana"]
for i, produto in enumerate(produtos):
    print(f"{i} é o produto {produto}")
```

### Manipulação de Estrutura de Dados Aninhada
```python
vendas = [
    ["João", 15000],
    ["Maria", 27000],
    ["Milena", 9900]
]
for item in vendas:
    if item[1] >= meta:
        print(f"Vendedor {item[0]} bateu a meta.")
```

## Requisitos
- Python 3.x
- Nenhuma biblioteca adicional necessária

