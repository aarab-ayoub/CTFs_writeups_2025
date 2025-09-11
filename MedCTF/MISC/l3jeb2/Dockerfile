FROM python:3.9-slim

WORKDIR /app

# Copy your directory structure
COPY . /app

# Make sure the Python script is executable
RUN chmod +x server.py

# Expose the port your server will run on
EXPOSE 9999

# Command to run the server
CMD ["python", "server.py"]