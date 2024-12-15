FROM python:3.9

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --requirement /tmp/requirements.txt

copy ./src/faker-name.py /src/faker-name.py

ENTRYPOINT ["python", "./src/faker-name.py"]
