Docker practice

# the starting point of the Docker is pass-argument.py file
docker build -t pass-argument

# run the docker created
docker run pass-argument Hi

# push the docker file \ RepoName should be same as docker name with userid
docker push username/reponame

# this is the base image
FROM python:3.9

# copy from local to Root-of-docker
COPY ./src/pass-argument.py /src/pass-argument.py

# remove Image and pull new from REPO
docker rmi username/repo:latest 
docker pull username/repo

# Entry point or CMD run these commands inside Docker
ENTRYPOINT ["python","./src/pass-argument.py"]
