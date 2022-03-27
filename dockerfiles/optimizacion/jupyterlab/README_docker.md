Set:

```
JUPYTERLAB_VERSION=3.2.8
REPO_URL=sancas96/docker_t3
DIR=/home/<user>/<midir>/dockerfiles/ #path where this git repository is cloned, example: /home/user/dockerfiles
BUILD_DIR=$DIR/optimizacion/jupyterlab/$JUPYTERLAB_VERSION
CONTAINER_NAME=docker_t3
DIR_RAIZ=/home/<user>/<midir>

Clone:

```
git clone git@github.com:optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23.git $DIR
```

Build:

```
docker build $BUILD_DIR -t $CONTAINER_NAME
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker build $BUILD_DIR -t $CONTAINER_NAME # amd64 image/container.
```


## Running `docker_t3` docker image in a docker container

```
docker run --rm -v $DIR_RAIZ:/datos --name $CONTAINER_NAME -p 8888:8888 -d $CONTAINER_NAME
```

## jupyter lab running at localhost:8888 , password: qwerty

Stop:

```
docker stop $CONTAINER_NAME
```

## Referencias
* [1] [video](https://youtu.be/wv7JGstFgrU) Construcción de una imagen de dockeR
* [2] [DOCKER DEFAULT PLATFORM](https://stackoverflow.com/questions/65612411/forcing-docker-to-use-linux-amd64-platform-by-default-on-macos)
* [3] [https://github.com/palmoreck/dockerfiles](https://github.com/palmoreck/dockerfiles)
