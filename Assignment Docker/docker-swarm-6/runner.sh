# create 3 containers 192.168.0.21 192.168.0.22 192.168.0.23

docker swarm init --advertise-addr 192.168.0.23


# to get tocken run on 0.23
docker swarm join tocken -q worker

# on 0.22 run
docker swarm join --token abcabcliuhlijabc 192.168.0.23:2377

# on 0.21 run
docker swarm join --token abcabcliuhlijabc 192.168.0.23:2377

# on 0.23 run
docker service ls
git clone https://github.com/dockersamples/docker-swarm-visualizer
cat run-vis.sh

cd docker-swarm-visualizer
docker-compose up -d

# go to :8080

# on 0.23 to create network
docker network create --driver overlay backnet

# on 0.23
docker stack deploy --compose-file docker-compose.yaml file-service

# go to :8080

# go to :8888

# go to :8888/file-server-1
# go to :8888/file-server-1 again
