```shell
# if the image has a defined entrypoint
# run in interactive mode
docker run -it --entrypoint /bin/bash <image_name>

# -it = interactive
docker run -it busybox sh

# -d = detached
# -P = expose ports to random ports
# --name = name the container
# --rm = remove the container once it exits
docker run --rm -d -P --name static-site prakhar1989/static-site
# -p 8888:80 maps external port 8888 to internal port 80
docker run -p 8888:80 prakhar1989/static-site

# ps = list running containers
# -a list all containers
docker ps -a

#stop a container
docker stop <container_id>

# build dockerfile
docker build -t prakhar1989/catnip

# Tag the image
docker tag <imageId> <username>/<reponame>:tag

# push to docker hub
docker push <username>/<reponame>

# ha: denied: requested access to the resource is denied
docker login docker.io
```