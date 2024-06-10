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
```bash
# development
$ docker compose -f local.yml build --no-cache
$ docker compose -f local.yml up

# To run migrations
$ docker compose -f local.yml run django sh
$ python manage.py migrate
$ python manage.py createsuperuser
```
