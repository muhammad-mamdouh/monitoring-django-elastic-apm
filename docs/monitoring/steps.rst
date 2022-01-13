Monitoring
==========


Up and Running with Kibana
----------------------------------------------------------------------

Please follow the following steps to make kibana dashboard up and running, and start
monitor the application.

Please at first make sure the app is up and running using the command::

    docker-compose up


Go to kibana dashboard at: `http://localhost:5601/ <http://localhost:5601/>`_, then click on Add APM.

    .. image:: images/kibana_1.png

From the APM view click on Check APM Server Status, to make sure the server is working as expected.

    .. image:: images/kibana_3.png

From the same page, please click on Check agent status so we can tell that the APM server can contact with the APM agent.

    .. image:: images/kibana_4.png

After seeing the same green messages, all is good you are good to go. Please click on Launch APM button.
Now you'll see the running services, at our case its only one APM service which is coding-task.

        .. image:: images/kibana_5.png

Just click on the service name `coding-task` and this will lead you to the monitoring dashboard.

    .. image:: images/kibana_6.png

Also make sure to make some requests so the transactions list won't be empty.

    .. image:: images/kibana_7.png
