# Deploy de modelo NLP - FASTAPI + Docker
##Modelo NLP com exemplo de deploy

# 1. Gera a imagem no Docker
docker build -t text-classifier .

# 2. Executa o contêiner
docker run -p 8000:8000 text-classifier
