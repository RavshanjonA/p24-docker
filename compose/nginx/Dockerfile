FROM nginx
COPY ./static /var/www/web/static/
COPY ./media /var/www/web/media/

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/nginx/nginx.conf /etc/nginx/conf.d