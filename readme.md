Simple proxy to get https pages with http. May be used for old systems or for debug/test purposes.

# Requirements

* Linux machine
* Python 3
* Python modules: flask and requests

# Usage

## Configure and run proxy

Install python modules

```
pip install -r requirements.txt
```

Run web server

```
python3 https_to_http_proxy.py
```

## Or with Docker

```
docker-compose up --build
```

or in the background

```
docker-compose up --build -d
```

## Test it


Make get request with curl

```
curl -v http://127.0.0.1:8088/proxy?url=https%3A%2F%2Fhttpbin.org%2Fget
```