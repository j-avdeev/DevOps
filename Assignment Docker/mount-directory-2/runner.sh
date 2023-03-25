docker build -t python-mount:0.1 .
docker run -v /root:/mount-dir python-mount:0.1 /mount-dir