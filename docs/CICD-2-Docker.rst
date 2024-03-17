=======================================
Building a CI/CD Pipeline. Part2 Docker
=======================================

1. Create Docker Image with Dockerfile from you repo forked from https://github.com/Sunagatov/Hello
2. Create Image from directory with Dockerfile

``docker build -t <image_name>:<tag> <path_to_dockerfile_directory>``

3. Run Image 

``docker run [OPTIONS] <image_name>:<tag>``

4. Type command to overview of running containers

``docker ps``
   
5. Type command to overview of running (previously) running containers

``docker ps --all``

6. Sign up on hub.docker.com or quay.io, if you don't have an account
7. Push docker Image to hub.docker.com or quay.io
8. Insert link to your Docker-image in report + add screenshot