Metrics
=======

phase 1

 * Eeach object in the database might have one or more metrics related to it
 * Metrics may also not be related to any object
 * Metrics store retention policy for each metric
 * database is created automatically on syncdb
 * retention policies are created automatically on syncdb
 * Metrics can be stored easily with a oneliner function
 * Metrics are stored asynchronously (non blocking fashion)
 * fare in modo che si possano recuperare i punti per mostrarli su un grafico
 * fare in modo che si possano scrivere dei punti da un api HTTP

 * Once a metric is deleted the metrics are deleted from the timeseries db

phase 2

 * easy queries via HTTP
 * show graphs

phase 3

 * thresholds
 * delay
 * send signal when threshold is reached
