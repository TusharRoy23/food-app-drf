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
* Restaurants & Customer can receive live notifications regarding their orders.

## ERD
will be ERD here

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
## Create Contact Group, Django Group, Django contact group & Contact
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
$ kubectl apply -f kuber/food-app
$ kubectl apply -f kuber/nginx
```
