# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the bot.py file from the current directory to the working directory in the container
COPY bot.py .
COPY bottoken.private .
COPY act.txt .

# Install any required packages
RUN pip install telebot

# Set the command that will be run when the container starts
CMD ["python", "bot.py"]