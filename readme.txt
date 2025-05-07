# Build Docker image
docker build -t flask-calculator .

# Run container
docker run -p 5000:5000 flask-calculator
