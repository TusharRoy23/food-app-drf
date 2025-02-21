## What is this?
It's a simple food application on top of DRF(Django Rest Framework) & Postgres. It can be used for learning purposes & will be extended bit by bit.

## What are the features so far?
* It is possible to register as a customer & restaurant user.
* Get verification link & verified by mail.
* JWT token and role-based authentications are available.
* Restaurant users can perform CRUD operations on the items.
* Customer can perform CRUD operation on carts & also request for the orders.
* Users can search restaurants.
* Rate limiting of requests.
* Restaurants & Customer can receive live notifications regarding their orders. `(Webscoket)`

## ERD
![Food App ERD](https://github.com/TusharRoy23/food-app-drf/blob/master/food_erd.png)

## What has been used so far?
| Name        | version |
| ------------|---------|
| Django      | 4.2     |
| DRF         | 3.14.0  |
| Postgres    | 15      |
| channels    | 4.1.0   |
| celery      | 5.3.6   |
| redis       | 5.0.1   |
| pytest-django|4.8.0   |

## Run the app using docker
# To build & run
```bash
# development
$ docker compose -f local.yml build --no-cache
$ docker compose -f local.yml up
```
# To run migration
```bash
$ docker compose -f local.yml run django sh
$ python manage.py migrate
$ python manage.py createsuperuser
```
# Django admin URL
Go to [Admin URL](http://localhost:8080/admin/)
## Create Contact Group, Django Group, Django contact group, & Contact
```(For this application purpose only)```
## Contact group
| Name             | Code             |
| -----------------|------------------|
| Visitor          | visitor          |
| Restaurant Owner | restaurant_owner |
| Restaurant User  | restaurant_user  |

## Django Group
Create 2 Groups (for now) & assign permissions to them.
* restaurant-owner
* visitors

## Django contact group
* Connect Contact group with django group

## Create a default contact
| Name    | Contact group | Purpose                                                               |
| --------|---------------|-----------------------------------------------------------------------|
| visitor | visitor       | All the visitors' (consumer) contact person will be under this contact|

# Run application in K8 cluster (For development only)
## Minikube
* Download & setup [minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)
* commands to start minikube & setup for docker-env
```bash
$ minikube start --driver=docker
$ eval $(minikube docker-env) # docker env for minikube (only for the initiated session)
$ minikube dashboard # To see the minikube dashboard
```

## First run `environment.yaml` file
```bash
$ kubectl apply -f kuber/environment.yaml
```
## Then run deployment one by one.
```bash
$ kubectl apply -f kuber/postgres
$ kubectl apply -f kuber/redis
$ kubectl apply -f kuber/food-app
$ kubectl apply -f kuber/celery
$ kubectl apply -f kuber/channel
$ kubectl apply -f kuber/nginx
```

# Postgres (Docker)
## Import DB
```bash
# Upload .sql/.sql.gz file to container's volume (backups)
$ docker cp /db.sql.gz containerID:/backups/db.sql.gz

# Go inside docker container
$ docker compose -f local.yml run postgres bash

# If gzip does not exists. (For alpine based postgres image)
$ apk add --no-cache gzip

# Unzip upload db.sql.gz file
$ gunzip /backups/db.sql.gz

# Import .sql file
$ psql -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -d $POSTGRES_DB -f backups/db.sql
```
## DB Backup
```bash
$ docker exec -it containerID pg_dump -U DB_USER DB_NAME | gzip > db.sql.gz
```

# Unit Test
* Go inside the django container: `docker compose -f local.yml run djangoServiceName sh`.
* run all test: `pytest`.
* run a specific file(s): `pytest backend/item/tests/test_views.py`.

# Generate ERD
## Using `django-extensions` [Graph models](https://django-extensions.readthedocs.io/en/latest/graph_models.html#)
* pyparsing
* pydot
```bash
$ python manage.py graph_models backend --arrow-shape normal > food.dot
```

## Stay in touch
- 📖 Checkout my stories - [Medium](https://medium.com/@tushar-chy)
- 🔗 Connect with me - [LinkedIn](https://www.linkedin.com/in/tushar-roy-chy/)
- 📫 Contact Me - [chowdhurytusharroy@gmail.com](mailto:chowdhurytusharroy@gmail.com?subject=Hey%20there)
