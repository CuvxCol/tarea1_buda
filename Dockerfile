# Use the official Python image from the Docker Hub
FROM python:3.8.10

# Make a new directory to put our code in.
RUN mkdir /code

# Change the working directory.
WORKDIR /code

# Copy to code folder
COPY . /code/

# Update pip
RUN python -m pip install --upgrade pip

# Install the requirements.
RUN pip install -r requirements.txt

# Create migrations
RUN python manage.py makemigrations

# Run migrations
RUN python manage.py migrate

# Run the application:
CMD python manage.py runserver 0.0.0.0:8000