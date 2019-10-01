Assessment task for the MRD - Scientific Developer position

## Requirements:

To fulfill this task you will require a recent version of Docker and docker-compose. Please refer to the documentation about installation:

 * Docker-engine Community: [install docs!](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
 * docker-compose: [install docs!](https://docs.docker.com/compose/install/)

## Contents

In this repository is contained a minimal application that uses [Celery](https://docs.celeryproject.org/en/latest/) Tasks to perform periodic queries (every minute) to one of our data APIs (Tide API) requesting water elevation data for different locations around New Zealand, also the API should return an JSON object compliant with this format [CF-JSON](http://cf-json.org/).

Here is provided a [docker-compose.yml](docker-compose.yml) file with the following services to start with:

 * A [RabbitMQ](https://hub.docker.com/_/rabbitmq) node (for Celery)
 * A Celery worker
 * A [Grafana](https://grafana.com/docs/installation/docker/) node, this will expose the service on your local machine at http://localhost:3000 (admin:admin)
 * An [InfluxDB](https://hub.docker.com/_/influxdb) database
 

## Assessment Task

1. Write a minimal Python 3 service that listens for [Celery Worker Events](https://docs.celeryproject.org/en/latest/userguide/monitoring.html#events), filter only the Task events, store the data to the [InfluxDB](https://influxdb-python.readthedocs.io/en/latest/index.html) database (`tidesmonitor`) for monitoring purposes. It's required that all the life-cycle (from `PENDING` to `SUCCESS/FAILURE`) events for each executing task are stored in the InfluxDB database.

The code will be evaluated by:

 * Efficacy
 * Utilization of PEP 8 guidelines
 * Deployability (docker-compose and Dockerfile)
 * Cleanness
 * Unit-testing usage
 * Clear usage of docstrings
 * Performance

2. Go to the [Grafana service in your local machine](http://localhost:3000) and create a Dashboard to visualize the stats about the tasks running in order to monitor exactly when a task is received by the worker, starts to run and finishes. Save and export this Dashboard and attach to your source-code. Before using the InfluxDB data, it's necessary to add it as a Data Source with the following parameters:

  * URL: `http://influxdb:8086`
  * Database: `tidesmonitor`
  * User: `tides`
  * Password: `TidesGoesUpAndDown`


3. Wait until you service accumulate about an hour worth of data then make an evaluation of the different tasks and how they are performing and what insights you have about the API performance for different queries. All Task settings can be checked [here](settings.py).

