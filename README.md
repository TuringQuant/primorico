# Primo Rico - Stock Picking 

Algoritmo de seleção de ativos da B3 com método elencado pelo Primo Rico.

1. ROE e ROIC superior a média do setor.
2. P/L inferior a 15 (exceção em caso de CAGR da empresa for muito alto).
3. (Endividamento Líquido) / EBIT < 3
4. Governança Corporativa Perfeita

Esse projeto executará sistematicamente os processos 1-3, cabendo aos usuários
avaliarem a governança corporativa.

## Primeiros passos

### Prerequisitos

No seu ambiente virtual instale os módulos necessários contidos no arquivo requirements.txt

### Instalação

Crie um ambiente virtual python3.x

```
virtualenv venv
```

Ative o ambiente virtual

```
source ./venv/bin/activate
```

Instale os modulos

```
pip install -r requirements.txt
```

## Execução de testes

O arquivo `main.py` retorna uma lista com os ativos que respeitam as condições estabelecidas nos filtros. 

Os dados utilizados para seleção de ativos

## Construído com

* [support](https://github.com/TuringQuant/support) - Repositório do TuringQuant para obter dados

## Fonte dos dados

* [Fundamentus](https://www.fundamentus.com.br/)
* [B3](http://www.b3.com.br/)

## Autores

* **Guilherme Fernandes** - *Versão Incial* - [aateg](https://github.com/aateg)
