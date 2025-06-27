# Deploy de modelo NLP - FASTAPI + Docker

Modelo NLP com exemplo de deploy

## 1. Gera a imagem no Docker
docker build -t text-classifier .

## 2. Executa o contêiner
docker run -p 8000:8000 text-classifier

## 3. Saída do modelo em deploy

### 3.1 - Versão navegador
Executando este URL: **http://0.0.0.0:8000/docs** no navegador você acessar a interface web do modelo.

### 3.2 - Versão python
Via python client: client.py
