Projeto Dockerizado com NGINX e Flask

Descrição

Projeto criado com propósito de passar um período na matéria CONFIGURAÇÕES DE SERVIDORES do Professo. Igo Coutinho Moura , onde ele passou uma atividade avaliativa. 
onde temos que desenvolver uma aplicação Dockerizada
com NGINX como servidor frontend e uma aplicação de backend simples
da sua escolha(por exemplo, Node.js ou Python Flask). Onde minha dupla resolve usar Python com Flask pela facilidade.
Esse projeto está configurado de forma correta, é de fácil inicialização, onde com apenas um comando **docker-compose up --build** caso tenhas as competencias já instaladas.

Estrutura do Projeto


├── backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend
│   ├── static
│   │   └── index.html
│   ├── nginx.conf
│   └── Dockerfile
└── docker-compose.yml

Tecnologias Utilizadas

- Docker
- Docker Compose
- NGINX
- Python "Flask"
- Python "Flask Cors"

Instruções para Construir e Executar

**OBS**: Para evitar erros de versões, indica-se usar um virtal env.
1. python -m venv venv
2. No Windows: venv\Scripts\activate
2. No Linux ou macOS: source venv/bin/activate



1. **Certifique-se de que o Docker e o Docker Compose já estejam intalados e em execução.**

2. **Construa os containers:**

   docker-compose build

3. **Inicie os containers:**

   docker-compose up -d

4. **Acesse a aplicação no seu navegador:**

   http://localhost


## Descrição da Arquitetura.

**Frontend:** O NGINX serve arquivos estáticos a partir do diretório `static` onde temos o inex.html e redireciona as requisições para a API do backend.
**Backend:** A aplicação Flask responde a requisições HTTP na porta 5000, retornando dados em formato JSON.

## Repositórios do Docker Hub

### 1. Frontend

**Repositório:** [sinvalfilho/dockerfile-frontend](https://hub.docker.com/repository/docker/sinvalfilho/dockerfile-frontend/general)

**Descrição:**
Este repositório contém a configuração do Docker para a aplicação frontend. Ele utiliza o NGINX como servidor web para servir arquivos estáticos.

**Como usar:**
1. **Puxe a imagem do Docker:**

   docker pull sinvalfilho/dockerfile-frontend

2. **Execute o contêiner:**

   docker run -d -p 80:80 sinvalfilho/dockerfile-frontend

3. **Acesse a aplicação:**
   Abra o navegador e vá para `http://localhost` para ver a aplicação frontend em execução.


### 2. Backend

**Repositório:** [sinvalfilho/dockerfile-backend](https://hub.docker.com/repository/docker/sinvalfilho/dockerfile-backend/general)

**Descrição:**
Este repositório contém a configuração do Docker para a aplicação backend. Ele é construído com Python Flask e fornece uma API RESTful.

**Como usar:**
1. **Puxe a imagem do Docker:**

   docker pull sinvalfilho/dockerfile-backend

2. **Execute o contêiner:**

   docker run -d -p 5000:5000 sinvalfilho/dockerfile-backend

3. **Acesse a API:**
   Use um cliente HTTP ou navegador para acessar a API em `http://localhost:5000`.

## Estrutura do Projeto

- **Frontend:** Contém arquivos estáticos e configurações do NGINX para servir a aplicação.
- **Backend:** Contém o código da aplicação Flask e configurações para expor a API.
