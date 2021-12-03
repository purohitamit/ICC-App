# ICC-App

Createing a CI/CD pipeline for ICC-App in Jenkins. It will test the app, build and push the Docker images and then deploy the ICC-App to a Docker Swarm as a Stack.

When we push new code to the GitHub repository, it will trigger the job to run using a GitHub webhook, meaning that any changes we make will be reflected on our Swarm server.

The automation pipeline Will have the following stages:

Setup (installing the dependencies)
    

Test (running pytest)
    

Build (building the Docker image)
    

Push (push the Docker image to Docker Hub)
    

Deploy (deploy the app as a Stack to the Swarm)    

--------------------------------------------------------------------------------------------------------------------

The first step was to generate an entity relationship diagran to define the relationship betweeen the tables which is shopwn below:
!https://snipboard.io/IZhLTe.jpg)



