# Use a lightweight Python base image
#FROM python:3.9-slim

# Set the working directory inside the container
#WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
#COPY requirements.txt requirements.txt

# Install required Python packages
#RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
#COPY . .

# Pre-create the SQLite database file
#RUN python DatabaseFile.py

# Expose the application's port
#EXPOSE 5000

# Command to run the application
#CMD ["python", "app.py"]

# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt requirements.txt

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Pre-create the SQLite database file
RUN python DatabaseFile.py

# Expose the application's port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]


