# SSL Certificate Expiration Checker

## Description
This Python script checks the SSL certificate of a list of websites and calculates the number of days until it expires. The script then pushes this information to a Prometheus push gateway using the Prometheus client library.

## Prerequisites
- Python 3.x
- Prometheus client library (`pip install prometheus-client`)
- A Prometheus push gateway

## Usage
1. Install the required libraries: `pip install -r requirements.txt`
2. Modify the `websites` list in the `ssl-certificate-checker.py` file to include the URLs of the websites you want to check.
3. Modify the `port` variable in the `ssl-certificate-checker.py` file to the desired port number for the SSL connection.
4. Run the script: `python ssl-certificate-checker.py`
5. Verify that the metrics have been pushed to your Prometheus push gateway by navigating to the Prometheus web interface and searching for the `certificate_check_expiration` metric.
