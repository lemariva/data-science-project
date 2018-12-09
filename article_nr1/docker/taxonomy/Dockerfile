FROM python:3.7.1-stretch

LABEL mantainer=@lemariva
COPY . /app
WORKDIR /app
RUN pip install flask && \
    mkdir -p /var/data/

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]