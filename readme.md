<h1 align="center">
<img src="https://weef.com.br/assets/images/logo-header.svg" />
</h1>

<h3 align="center">
	Twitter API - Weef Challenge
</h3>

# About the project

This project was developed as a challenge proposed by Weef. The objective was to build a Twitter like API.

The API is now online on the path https://challenge-weef-twitter.herokuapp.com

    THE FULL API DOCUMENTATION CAN BE FOUND HERE https://documenter.getpostman.com/view/17927585/UV5UkeMD

## Required functionalities

As a project scope, the API must have:

-   User registration
-   User login (any form of session)
-   Feed
-   Tweet
-   Like system
-   Retweet

Additional functionalities:

-   Follwers system
-   Folowers Feed

## Technologies used in the project

-   <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" />
-   <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" />

## Database

The database was planned using [dbdiaram](https://dbdiagram.io).
The API uses the following structure:

<h1 align="center">
<img src="https://i.ibb.co/jZb7pKM/Challenge-Weef-1.png" />
</h1>

# How to use

This instructions will guide you in how to run the project in localhost.

## Prerequisites

To run this project you must have installed

-   Python 3.9
-   Python poetry

Python can be downloaded [here](https://www.python.org/ftp/python/3.9.5/python-3.9.5-embed-amd64.zip). After installing python, just run `python -m pip install poetry` to add poetry dependence.

## Running the server

To start the server first clone this repository:

```bash
$   git clone https://github.com/jhelison/challenge-weef-twitter.git
$   cd challenge-weef-twitter
```

In to the project path, just run:

```bash
$   poetry install
```

To install all the projects dependencies. If it's the first time acessing the **Django** server, first you must make the database migrations with:

```bash
$   poetry run python manage.py makemigrations
$   poetry run python manage.py migrate
```

You can also run `python manage.py createsuperuser` to create a superuser admin. Finnaly just run:

```bash
$   poetry run python manage.py runserver
```

To start the **Django** server on localhost.

# License

This project is under the license of (MIT).
