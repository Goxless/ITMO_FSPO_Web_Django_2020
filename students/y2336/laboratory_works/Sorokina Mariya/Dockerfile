version: '3'
services:
  server:
    build:
      context: .
      dockerfile: ./Dockerfile
    stdin_open: true
    tty: true
    command:
      python manage.py runserver 0.0.0.0:8000
    ports:
      - 8000:8000

  web:
    build:
      context: ./client/
      dockerfile: ./Dockerfile
    command: npm run start
    network_mode: host
    ports:
      - 3000:3000
    depends_on:
      - server