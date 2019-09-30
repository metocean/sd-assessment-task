# sd-assessment-task
Assessment task for the MRD - Scientific Developer position


Requirements:

To fulfill this task you will require a recent version of Docker and docker-compose. Please refer to the documentation about installation:

 * Docker-engine Community: https://docs.docker.com/install/linux/docker-ce/ubuntu/
 * docker-compose: https://docs.docker.com/compose/install/


In this repository is contained a minimal application that uses (Celery|https://docs.celeryproject.org/en/latest/) Tasks to perform periodic queries (every minute) to one of our data APIs (Tide API) requesting water elevation data for different locations around New Zealand, also the API should return an JSON object compliant with this format(CF-JSON|http://cf-json.org/).

Here is provided a docker-compose.yml file with the following services to start with:

 * A (RabbitMQ|https://hub.docker.com/_/rabbitmq) node (for Celery)
 * A Celery worker
 * A (Grafana|https://grafana.com/docs/installation/docker/) node, this will expose the service on your local machine at http://localhost:3000 (admin:admin)
 * A (InfluxDB|https://hub.docker.com/_/influxdb) database
 

1. Write a minimal Python 3 asynchronous service that listens for the(Celery Tasks Events|https://docs.celeryproject.org/en/latest/userguide/monitoring.html#events) produced by the Celery Worker and stores the information in an (InfluxDB|https://influxdb-python.readthedocs.io/en/latest/index.html) database for monitoring purposes. It's required that all the life-cycle (from PENDING to SUCCESS/FAILURE) events for a task are stored in the InfluxDB database (`tidesmonitor`). The main objective is to monitor exactly when a task is received by the workers, starts to run and finishes, so we can track stats about the execution of those tasks, as the average runtime, which workers executed tasks, etc.

The code will be evaluated by:

 * Efficacy
 * Utilization of PEP 8 guidelines
 * Deployability (docker-compose and Dockerfile)
 * Cleanness
 * Unit-testing usage
 * Clear usage of docstrings
 * Performance

2. Create a Grafana Dashboard to visualize the stats about the tasks running in the database. To create a Dashboard you need to first set-up the InfluxDB datasource, with the following settings:

  - URL: `http://influxdb:8086`
  - Database: `tidesmonitor`
  - User: `tides`
  - Password: `TidesGoesUpAndDown`

Then proceed to create a Dashboard exposing the values you've stored from the Tasks monitor application.


