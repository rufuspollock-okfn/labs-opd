# Description

This website aims to browse Open Product Data (OPD) database.

Open Product Data is a project of [Open Knowledge Foundation Open Product Data] [1].

[1]: <http://product.okfn.org> "OKFN Open Product Data website"

# Installation

## Development environment

### Prerequisites

**Mandatory :**

* [Python 3.5.1] [2]
* [Django 1.9.2] [3]
* [mysqlclient 1.3.7] [4]
* [Django REST framework 3] [5]

[2]: <http://www.python.org/getit/> "Python install documentation"
[3]: <https://www.djangoproject.com/download/> "How to get Django"
[4]: <http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient> "Unofficial Windows Binaries for Python Extension Packages"
[5]: <http://www.django-rest-framework.org/#installation> "Django REST framework - Installation"

**Optionnal :**

* [VirtualEnvWrapper 3.7+] [8]

[8]: <http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation> "VirtualEnvWrapper install documentation"


## Development environment (Docker)

* Make sure you have a running Docker setup (including Docker Compose). For an easy setup, have a look at the [Docker Toolbox](https://www.docker.com/products/docker-toolbox).
* `git clone https://github.com/okfn/opd-product-browser-web.git`
* `cd opd-product-browser-web/scripts/dockerfiles`
* `wget -O - http://www.product-open-data.com/docs/pod_web_2014.01.01_01.sql.gz | gunzip -c > pod_mysql/products.sql`
* `docker create -v /var/lib/postgresql --name opd_postgres_data postgres:9.4 /bin/true`
* `docker-compose up -p opd-product-browser-web -d db`
* `docker exec opdproductbrowserweb_db_1 createdb -Upostgres opd`
* `docker-compose up -d`
* Open port 18080 on your Docker host in a web browser. If you're using the Docker Toolbox, this should be http://192.168.99.100:18080/


## Production environment

* `docker create -v /var/lib/postgresql --name opd_postgres_data postgres:9.4 /bin/true`
* `docker-compose -f docker-compose.prod.yml up -d db`
* `docker exec opdproductbrowserweb_db_1 createdb -Upostgres opd`
* `docker-compose -f docker-compose.prod.yml up -d`
