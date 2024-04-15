FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE 7080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7080"]


