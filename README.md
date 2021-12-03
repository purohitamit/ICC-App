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
The first step was to generate an entity relationship diagram to define the relationship between the tables which is shown below:
!(https://snipboard.io/xHN5wz.jpg)
Then the project board was setup with the following tasks:
!(https://snipboard.io/CvYg7h.jpg)
And after completing the task, they were moved to the done section.
!(https://snipboard.io/MEz1mP.jpg)
!(https://snipboard.io/W13gLu.jpg)
!(https://snipboard.io/46mYKk.jpg)
The average time to run the job in the pipeline was roughly 1 min 26sec:
!(https://snipboard.io/4B3RM9.jpg)
There were 5 tests performed for each of the backend and frontend as per below:
!(https://snipboard.io/6dbyAi.jpg)
73% coverage was achieved as per below:
!(https://snipboard.io/s7pebB.jpg)
In the app we were able to add a country, delete a country, update a country, add a player, update a player, delete a player and view all the players for the given country:
!(https://snipboard.io/iRJgvA.jpg)
After layout of the app was changed after the rolling updates were performed and the new app looked like below:
!(https://snipboard.io/WgYpJj.jpg)

