FROM python:3.8.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["laptop_model_1_0.pkl", "laptop_dv.pkl", "predict.py", "common_function.py", "./"]

RUN apt-get update && apt-get install -y libaio1 libgomp1

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
