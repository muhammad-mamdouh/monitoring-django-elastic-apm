How To Start
======================================================================

Stack Used
----------------------------------------------------------------------

+ Docker v. 20.10.5
+ Docker Compose v. 1.29.0
+ PostgreSQL v. 13.2
+ Python v. 3.9
+ Django Framework v. 3.1.12
+ Django Rest Framework v. 3.12.4
+ Elasticsearch v. 7.9.0
+ Elastic APM Server v. 7.9.0
+ Kibana v. 7.9.0
+ Sphinx v. 4.0.2

Get Started
----------------------------------------------------------------------
To build the application, use the command::

    docker-compose build


To build and serve docs, use the command::

    docker-compose up docs


Changes to files in `docs/_source` will be picked up and reloaded automatically.

To run the application, use the command::

    docker-compose up
    docker-compose up -d  # run the services in the background.


Stop the running application, using the command::

    docker-compose down -v


Run Tests
----------------------------------------------------------------------
You can run the unit tests, using the command::

    docker-compose run --rm django pytest


Also you can generate the test coverage report, using the commands::

    docker-compose run --rm django coverage run -m pytest
    docker-compose run --rm django coverage report


API Swagger Documentation
----------------------------------------------------------------------
After making the application up and running, you can check the API's docs
at:
    + `Swagger style docs <http://localhost:8000/swagger/>`_
    + `Redoc style docs <http://localhost:8000/redoc/>`_


Monitoring Via Elastic APM
----------------------------------------------------------------------
After making couple of requests, you can see the implemented monitoring solution at:
`Elastic APM <http://localhost:5601/>`_
