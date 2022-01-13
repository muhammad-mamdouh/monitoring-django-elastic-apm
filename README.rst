Monitor Django APP Via Elastic APM
==================================


     Monitor Django APP Via Elastic APM.

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

.. contents::

Stack Used
----------
+ Docker v. 20.10.5
+ Docker Compose v. 1.29.0
+ PostgreSQL v. 13.2
+ Python v. 3.9
+ Django Framework v. 3.1.12
+ Django Rest Framework v. 3.12.4
+ Elasticsearch v. 7.9.0
+ Elastic APM Server v. 7.9.0
+ Kibana v. 7.9.0

Basic Commands
--------------
Build the docker image.
&&&&&&&&&&&&&&&&&&&&&&&

.. code-block:: bash

     docker-compose build

Run the unit tests.
&&&&&&&&&&&&&&&&&&&&&&&

.. code-block:: bash

     docker-compose run --rm django pytest

Generate the test coverage report.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

.. code-block:: bash

     docker-compose run --rm django coverage run -m pytest
     docker-compose run --rm django coverage report

Build and server the sphinx docs using docker compose.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

.. code-block:: bash

     docker-compose up docs

Run the application using docker compose.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

.. code-block:: bash

     docker-compose up  # use -d to run the services in the background.

Now you can check and test the developed APIs docs at:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
APIs `Swagger docs <http://localhost:8000/swagger/>`_ and `Redoc docs <http://localhost:8000/redoc/>`_

Also you can check the monitoring metrices and details via Elastic APM at:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
`Elastic APM <http://localhost:5601/>`_


Stop the running application using docker compose.
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

.. code-block:: bash

     docker-compose down -v

License
--------------
Open source licensed under the MIT license (see LICENSE file for details).
