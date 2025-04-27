FROM python:3-alpine
WORKDIR /proxy_server
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY https_to_http_proxy.py . 
ENTRYPOINT ["python3", "https_to_http_proxy.py"]
EXPOSE 8088
