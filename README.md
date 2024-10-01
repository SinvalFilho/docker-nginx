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
