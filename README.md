# Epic Events CRM

![made-with-django-rest](https://user-images.githubusercontent.com/45998296/166694632-eee84900-3ef4-4adc-bbf3-6cc2ef16ac7f.svg) ![use-django-admin](https://user-images.githubusercontent.com/45998296/166691519-839a7d13-833f-46e6-a33a-d053e6b04bd8.svg) ![use-postgresql](https://user-images.githubusercontent.com/45998296/166709231-905140e5-a6f6-4e62-8255-9b6f5a7fe6c5.svg) ![use-jwt](../../../Downloads/use-json-web-token.svg)

![openclassrooms-project](https://user-images.githubusercontent.com/45998296/166692502-a22abdc0-e774-4ec6-8d7c-f86cb6e55825.svg)



![pablo-heimplatz-ZODcBkEohk8-unsplash](https://user-images.githubusercontent.com/45998296/166689593-7f350168-4631-4462-98a1-8c33be3528bc.jpg)
_Photo by Pablo Heimplatz on Unsplash_

## Introduction

This is a CRM project made with Django REST Framework in which the admin interface is used by non developer to manage their clients and the related data. 


## Setup

First of all you'll need to create a virtual environement like so :

**on Mac or Linux**

```sh

$ python3 -m venv venv

```

once it's done, activate it

```sh

$ source venv/bin/activate

```


**on Windows**

```sh

$ py -m venv env

```

once it's done, activate it

```sh

$ .\env\Scripts\activate

```


## Installation

to launch the project


```sh

$ python manage.py runserver

```

## Usage

to access CRM content go to the generated url then to the admin section endpoint and fill in your credentials

```sh

localhost:3000/admin

```

to access the API content go to the generated url then to the admin section endpoint and fill in your credentials

```sh

localhost:3000/api/login

```