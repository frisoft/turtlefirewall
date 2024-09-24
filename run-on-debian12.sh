#!/usr/bin/env sh

docker stop webmin-container
docker rm webmin-container
docker build --progress=plain -t webmin-debian .
# docker run -d -p 10000:10000 --name webmin-container webmin-debian
docker run -d -p 10000:10000 -e WEBMIN_PASSWORD=webmin \
    --name webmin-container webmin-debian
    # -v ./src/turtlefirewall:/tmp/turtlefirewall \

echo
echo Visit https://localhost:10000
echo User: root
echo Password: webmin
