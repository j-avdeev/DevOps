docker build -t python-server:0.1 .
docker run -v /root:/sync-folder -p 9090:8080 python-server:0.1