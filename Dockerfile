# Use the official Python image as a base
FROM python:3.8

# Set environment variables for Python (unbuffered mode) and pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container at /app/
COPY . /app/

# Expose the port that the development server will run on
EXPOSE 8000

# Run the Django development server
CMD ["python", "travel_site/manage.py", "runserver", "0.0.0.0:8000"]