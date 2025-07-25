# Using linux with python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl

# Install node through nodesource (better)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY package.json package-lock.json ./
RUN npm ci 

# Copy code all app code (backend, frontend, etc.)
COPY . .

# Expose port and run app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]