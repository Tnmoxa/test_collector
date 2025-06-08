FROM python:3.12

WORKDIR /collector

COPY . .

RUN pip install -e .

CMD ["python3", "statistics_collector/main.py"]