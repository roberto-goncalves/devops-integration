#!/bin/bash

docker-compose build && docker-compose up -d && docker exec -it docker_bash_nginx1_1 /usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg && docker exec -it docker_bash_nginx2_1 /usr/sbin/haproxy -f /etc/haproxy/haproxy.cfg
