# How to start

## Create conda environment

After cloning this repository, create a conda environment for this project and activate the environment:

```console
$ conda create --name cwindividual python=3.11
$ conda activate cwindividual
```

## Django backend

### Start backend server

To start the backend server cd into the backend folder where the manage.py file is (if not already there)

```console
(cwindividual)$ cd backend
```

and run

```console
(cwindividual)$ python manage.py runserver
```

The server will start on http://localhost:8000

## Vue frontend

### Install frontend (JavaScript) dependencies

To install the frontend (JavaScript) dependencies cd into the frontend folder

```console
(cwindividual)$ cd frontend
```

and run:

```console
(cwindividual)$ npm install
```

The main frontend dependencies (see package.json) are [vue](https://vuejs.org/guide/introduction.html) and [bootstrap](https://getbootstrap.com/docs/5.0/getting-started/download/).

### Start frontend server

To start the frontend server run

```console
(cwindividual)$ npm run dev
```

and the server will start on http://localhost:5173
