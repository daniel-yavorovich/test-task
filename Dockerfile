FROM ubuntu:16.04
RUN apt-get update && \
    apt-get install -y \
    python-pip \
    python-dev \
    build-essential
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
