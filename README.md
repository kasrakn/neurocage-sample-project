# My Neurocage interview project

## **Description**
This project contains a web applciation developed with Django framework that illustrates some of the functionalities of the systems in Neurocage in a very abstract picture. Let's dive into the technical details of it.

## **Project Structure**
This project includes two main seprate sections. The web application and the sensor API, which had been developed before and now it is used as a service in the system.

Django application is responsible for creating frontend views and handling request receiving the system. The projects consists of a ListView for displaying the cages that created by user and DetailView for details about sensor of each cage and the related tables. In general and in case of having sensor data in database, it has two main tables. First one is for all the correct received data and the other one is for listing all the requests for the cage and their successful and health statuses. The following images displayes these two pages.
   
   <img src="images/cage-list.png">
   <img src="images/cage-detail.png">

As can be seen in the first image, editting and deletting each cage has been provided for the users in the list.

## **Technologies**
1. ### **Database**
In this project, I have used TimeScaleDB, which is an extenssion of PostgresDB to store the data of the web application. Because of some especial tables called heypertables, this is capable of working with timeseries data so much faster that other databases. I read somewhere that it might be over 8000 times faster!

<img src="images/timescaledb-postgres.png">

<br>

2. ### **Backgorund task handling**
In order to make sure that the web application runs smoothly and without any delays, developers must offload any time/resource-intensive task, which runs independently from the web application service. In particular, when the web server receives lots of requests from the users. In case of running those tasks synchronously, our pages are prone to load so much slower. In order to tackle this problem, I have utilized Celery, which is a task queue and task scheduler and redis as a message broker. 
This django app needs to call the sensor mock API every 1 minutes and stores the data in the database. In this case, a Celery worker, which runs on another server/container, takes the task and completes it and then return back the result to the django app to save it. Between our Django app and the celery worker, there is a message broker is responsible for delivering those tasks between the Django and celery workers. When the result of a task comes, the celery worker store it in the Redis and Django reads it back and store it in the database.

<img src="images/architecture.png">

The image above, illustrates the process of delivering tasks to celery workers and getting back the results. It is worth mentioning that there is only one redis server in our system. The capability of using Redis as message broker and a database makes it stands out compare to other message brokers like RabitMQ.

<br>

## **How to run it?**
For running this project, you can clone this repo into your local mechine and then just run:

```shell
docker compose up -d --build
```

And the you can find the application in ```http://localhost```.