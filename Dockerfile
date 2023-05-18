FROM python:3.10

RUN mkdir /pinaem_serv

WORKDIR /pinaem_serv

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python pinaem_serv.py

