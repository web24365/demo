FROM python:3.7-slim
LABEL MAINTAINER="yjwon@isecurekr.com" Description="demo용 dockerfile" Vender="iSecure Inc."
LABEL Version="1.0"


# ENV DEBIAN_FONEND=noninteractive
# apline package management
RUN apt-get -y update 
# apt-get -y install --no-install-recommends apt-utils
RUN apt-get -y dist-upgrade
RUN apt-get -y install build-essential
RUN apt-get -y install nginx supervisor

ENV base /code
RUN mkdir ${base}
WORKDIR ${base}
# 내 컴퓨터의 현재 디렉토리의 모든 파일을 컨테이너의 ${PROJECT_DIR}로 복사
COPY . ${base}

ENV LANG C.UTF-8
ENV DJANGO_SETTINGS_MODULE mysite.settings
ENV PYTHONUNBUFFERED 1

RUN pip3 install -r requirements.txt

# nginx 설정
# RUN cp -f ${base}/.config/nginx.conf /etc/nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN cp -f ${base}/.config/nginx_iSecure.conf /etc/nginx/sites-available/
RUN rm -rf /etc/nginx/sites-enabled/*
# ln source link
# -f : 대상파일이 존재할 경우에 대상파일을 지우고 링크파일을 생성
# -s : 심볼릭 링크파일을 생성
RUN ln -fs /etc/nginx/sites-available/nginx_iSecure.conf /etc/nginx/sites-enabled/nginx_iSecure.conf
RUN ln -sf /etc/nginx/sites-available/nginx_iSecure.conf /etc/nginx/sites-enabled/nginx_iSecure.conf

RUN cp -f ${base}/.config/supervisord.conf /etc/supervisor/conf.d/

EXPOSE 80

CMD ["supervisord", "-n"]

# CMD ["uwsgi", "--plugins", "http,python", \
#               "--http", "0.0.0.0:80", \
#               "--wsgi-file", "/code/mysite/wsgi.py", \
#               "--master", \
#               # reloading 대신 kill
#               # exit instead of brutal reload on SIGTERM(no more needed)
#               "--die-on-term", \
#               # 단일한 python interpreter를 사용
#               "single-interpreter", \
#               # process 들이 stuck이 걸렸을 경우 해당 time 만큼 대기 후 kill
#               "harakiri", "30", \
#               # reload if rss memory is higher than specified megabytes
#               "reload-on-rss", "512", \
#               "--post-buffering-bufsize", "8192"
# ]
