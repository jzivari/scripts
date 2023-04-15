# Prometheus Gauge for Kubernetes Certificate Expiration

This Python script uses the `prometheus_client` library to create a [Prometheus](https://prometheus.io/) Gauge metric that tracks the expiration time of the Kubernetes master certificate. It also pushes this metric to a Prometheus server using the `pushadd_to_gateway` function.

## Prerequisites

- `prometheus_client` library (can be installed via pip)

## Usage

1. Modify the `pushadd_to_gateway` function to point to your Prometheus server's IP and port, and customize the `job` parameter as needed.
2. Run the script using Python 3 with sudo privileges, as it needs to access the Kubernetes configuration file.
3. Verify that the metric is being tracked in Prometheus.

## How it works

The script uses the `subprocess` module to execute the `kubeadm` command that checks the expiration time of the Kubernetes master certificate. The output of this command is then parsed using `awk` and stored in the `kube_output` variable.

Next, a `CollectorRegistry` object is created, and a `Gauge` object is registered with it. The `Gauge` object is named `kubeMaster_certExpiration` and has a description of `mydigipay`. The value of the `Gauge` is set to the parsed expiration time.

Finally, the `pushadd_to_gateway` function is called with the IP address and port of the Prometheus server, along with a customized `job` parameter. This pushes the metric to the Prometheus server, where it can be queried and visualized using a monitoring tool such as Grafana.
