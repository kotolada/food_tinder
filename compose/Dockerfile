FROM python:3.10

WORKDIR /app

# Install netcat
RUN apt-get update && apt-get install -y netcat-traditional

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./compose/entrypoint.sh

ENTRYPOINT ["sh", "./compose/entrypoint.sh"]