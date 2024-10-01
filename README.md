Projeto Dockerizado com NGINX e Flask

Descrição

Este projeto consiste em uma aplicação Dockerizada com NGINX como servidor frontend e uma aplicação de backend simples construída com Flask. O objetivo é servir arquivos estáticos e fazer proxy reverso para a API do backend.

Estrutura do Projeto


├── backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend
│   ├── static
│   │   └── index.html
│   ├── nginx.conf
│   └── Dockerfile
└── docker-compose.yml

Tecnologias Utilizadas

- Docker
- Docker Compose
- NGINX
- Python "Flask"

Instruções para Construir e Executar

1. **Certifique-se de que o Docker e o Docker Compose estão instalados e em execução.**

2. **Clone o repositório ou baixe os arquivos do projeto.**

3. **Navegue até o diretório do projeto:**

   ```bash
   cd /caminho/para/o/projeto
   ```

4. **Construa os containers:**

   ```bash
   docker-compose build
   ```

5. **Inicie os containers:**

   ```bash
   docker-compose up -d
   ```

6. **Acesse a aplicação no seu navegador:**

   ```
   http://localhost
   ```

## Descrição da Arquitetura

- **Frontend:** O NGINX serve arquivos estáticos a partir do diretório `static` e redireciona as requisições para a API do backend.
- **Backend:** A aplicação Flask responde a requisições HTTP na porta 5000, retornando dados em formato JSON.

## Comunicação entre Frontend e Backend

- O NGINX é configurado para atuar como um proxy reverso, redirecionando as requisições feitas para `/api/` para a aplicação Flask que está rodando no container do backend.
- O backend se comunica com o frontend através da rede definida no Docker Compose, permitindo que ambos os serviços se descubram e se comuniquem facilmente.

