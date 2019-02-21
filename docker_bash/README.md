
## Docker-compose with HAProxy and Nginx on two containers

Create and install two docker containers with nginx and haproxy installed on both

## INSTRUCTIONS

Run with
```console
$ ./script.sh
```
Both containers have their respective dockefile related to docker-compose

## EXPLANATION

	1. docker-compose build to build containers and network
	2. docker-compose up to run get containers running
	3. Containers have a common dockerfile to set nginx and haproxy
	4. In docker-compose.yml containers have a private IP address that's how it can be monitored with HAProxy
	5. After nginx being installed, it will be executed inside the dockerfile
	6. After docker-compose up command being executed, haproxy command is sent to containers
	7. Mapping ports can been seen in docker-compose.yml for further questions

## ACCESS

- 0.0.0.0:8081 - Nginx from container1
- 0.0.0.0:8082/stats - HAProxy from container1 with auth: roberto:roberto
- 0.0.0.0:8083 - Nginx from container2
- 0.0.0.0:8084/stats - HAProxy from container2 with auth: roberto:roberto
	
