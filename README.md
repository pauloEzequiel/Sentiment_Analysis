# Sentiment API

MVP desenvolvido com o intuito de alicerçar o conteúdo observado na Sprint 3.

---
## Como instalar e executar a API localmente

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(ambvir)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

>Baixe o modelo treinado a partir da [url](https://drive.google.com/file/d/1HdgCm0eTIpM5G5GDwhyWa0Wp6H8UGaVl/view?usp=sharing) ou execute o [notebook](https://colab.research.google.com/github/pauloEzequiel/Sentiment_Analysis/blob/main/Notebook/Sentiment_Analysis.ipynb) e baixe o modelo.

> Na pasta SentimentApi/resource adicionar o arquivo baixado 'Sentiment_Analitic_model.bin'

Para executar a API REST executar:

```
(ambvir)$ flask run --host 0.0.0.0 --port 5000
```

---
### Acesso no browser

 - Abra o [http://localhost:5000/openapi/](http://localhost:5000/openapi/) no navegador para verificar o status da API Rest em execução.
---
### Acesso no browser

 - Abra o index.html localizado na pasta Sentiment_Analysis

