# Usar imagem base do Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos para dentro do container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar dependências
RUN pip install -r requirements.txt

# Expor a porta 5000 para o Flask
EXPOSE 5000

# Comando para iniciar o servidor
CMD ["python", "app.py"]
