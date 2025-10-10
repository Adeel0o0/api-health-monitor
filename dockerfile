#Base Image
FROM python:3.11-alpine

# Where code lives inside the container 
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy code to the container
COPY . .

#Run the application
CMD ["python", "monitor.py"]
