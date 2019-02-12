FROM centos:centos7
LABEL maintainer="Roberto Gonçalves <roberto.forsaken@gmail.com>"

ENV nginxversion="1.14.0-1" \
    os="centos" \
    osversion="7" \
    elversion="7_4"

RUN yum install -y wget openssl sed net-tools python &&\
    yum -y autoremove &&\
    yum groupinstall -y 'development tools' &&\
    yum clean all &&\
    wget http://nginx.org/packages/$os/$osversion/x86_64/RPMS/nginx-$nginxversion.el$elversion.ngx.x86_64.rpm &&\
    rpm -iv nginx-$nginxversion.el$elversion.ngx.x86_64.rpm

#RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py && pip install pymongo


COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /data/www/index.html
COPY .htpasswd /etc/nginx/.htpasswd


VOLUME [ "/data/www" ]

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
