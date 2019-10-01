Assessment task for the MRD - Scientific Developer position

## Requirements:

To fulfill this task you will require a recent version of Docker and docker-compose. Please refer to the documentation about installation:

 * Git
 * Docker-engine (Community version): [install docs!](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
 * docker-compose: [install docs!](https://docs.docker.com/compose/install/)

After installing Git, Docker and docker-compose.

 1. `git clone https://github.com/metocean/sd-assessment-task.git`
 2. `$ cd sd-assessment-task`
 3. `$ docker-compose up`

## Contents

In this repository is contained a minimal application that uses [Celery](https://docs.celeryproject.org/en/latest/) Tasks to perform periodic queries (every minute) to one of our data APIs (Tide API) requesting water elevation data for different locations around New Zealand, also the API should return an JSON object compliant with this format [CF-JSON](http://cf-json.org/).

Here is provided a [docker-compose.yml](docker-compose.yml) file with the following services to start with:

 * A [RabbitMQ](https://hub.docker.com/_/rabbitmq) node (for Celery)
 * A Celery worker
 * A [Grafana](https://grafana.com/docs/installation/docker/) node, this will expose the service on your local machine at http://localhost:3000 (admin:admin)
 * An [InfluxDB](https://hub.docker.com/_/influxdb) database

 After installing Docker and docker
 

## Assessment Task

1. Write a minimal Python 3 service that listens for [Celery Worker Events](https://docs.celeryproject.org/en/latest/userguide/monitoring.html#events), filter only the Task events, store the data to the [InfluxDB](https://influxdb-python.readthedocs.io/en/latest/index.html) database (`tidesmonitor`) for monitoring purposes. It's required that all the life-cycle (from `PENDING` to `SUCCESS/FAILURE`) events for each executing task are stored in the InfluxDB database.

The code will be evaluated by:

 * Efficacy 
 * Performance
 * Utilization of PEP 8 guidelines
 * Unit-testing
 * Clear usage of docstrings
 * Usage of language builtin resources
 
You can use the `docker-compose` service to start your service. Please checkout the service configuration [here](docker-compose.yml#53).

2. Go to the [Grafana service in your local machine](http://localhost:3000) and create a Dashboard to visualize the stats about the tasks running in order to monitor exactly when a task is received by the worker, starts to run and finishes. Save and export this Dashboard and attach to your source-code. Before using the InfluxDB data, it's necessary to add it as a Data Source with the following parameters:

  * URL: `http://influxdb:8086`
  * Database: `tidesmonitor`
  * User: `tides`
  * Password: `TidesGoesUpAndDown`


3. Wait until you service accumulate about an hour worth of data then make an evaluation of the different tasks and how they are performing and what insights you have about the API performance for different queries. All Task settings can be checked [here](tides/settings.py).

## Docker and docker-compose usage tips

### Start, restart, recreate services

Docker compose has different states for a container or is `created`, `started`, `stopped` and `exited`. So when you `docker-compose up` a service Docker will first `create`, then `start`, and if you `docker-compose down` it will `stop` and `delete` the container, which is different then `docker-compose stop`.

### Clean the persistent volumes

In this docker-compose file there's 3 volumes being created from start celery, influxdb and grafana each one persists the data for the services accross container restarts and recreation. So if you like to fully reset the persistent volumes contents it's necessary to manually remove them:

```
    $ docker-compose down
    $ docker volume rm tidesmonitor_celery tidesmonitor_grafana tidesmonitor_influxdb
```



