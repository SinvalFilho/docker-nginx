# Usar imagem base do NGINX
FROM nginx:alpine

# Copiar a configuração do NGINX
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar os arquivos estáticos para o diretório do NGINX
COPY static /usr/share/nginx/html
