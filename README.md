# QR App

![CI/CD Pipeline](https://github.com/HannaRamzyHanna/T-to-QR/actions/workflows/action.yml/badge.svg)

## Description
QR App is a simple web application for converting text into QR codes. This project demonstrates how to build a Python-based web app with Flask, Dockerize it, and deploy it using Docker.


## Features
1. Convert text to QR code
2. Dockerized for easy deployment
3. Uses pytest for testing

## Prerequisites
- Docker
- Docker Compose
- Python 3.x
- pytest for testing

## Setup and Installation
- Clone the Repository
```
git clone https://github.com/HannaRamzyHanna/T-to-QR.git
cd T-to-QR
```
## Local Setup
Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate
Install Dependencies

pip install -r requirements.txt
Run the Application
```
## python app.py
- By default, the application will be available at http://127.0.0.1:5000.

## Docker Setup
Build the Docker Image

```
docker build -t hannaramzy/qr-app .
Run the Docker Container
docker run -dp 5050:5000 hannaramzy/qr-app
The application will be accessible at http://localhost:5050.
```
## Testing
Run Tests Locally

```
pytest
```
## Pushing Changes
Pushing to GitHub
Add and Commit Changes
```
git add .
git commit -m "Describe your changes here"
Push Changes to GitHub
```
## git push origin main
Replace main with the appropriate branch name if different.

## Pushing to DockerHub
Tag the Docker Image

```
docker tag hannaramzy/qr-app hannaramzy/qr-app:latest
```
## Push the Docker Image
```
docker push hannaramzy/qr-app:latest
```
## Deployment
Deploy to Cloud Service

Follow the specific instructions of your cloud provider to deploy a Docker container. Generally, you will need to:

Pull the Docker image
Run the Docker container on the desired port
Example for AWS ECS or similar service:

```
docker pull hannaramzy/qr-app:latest
docker run -dp 5050:5000 hannaramzy/qr-app
```
## Troubleshooting
- Port Already Allocated Error: Ensure no other services are using the same port. 
- Stop any conflicting services or change the port in your Docker run command.

```
docker ps
docker stop <container_id>
docker rm <container_id>
Application Not Running: Check Docker logs for errors.
docker logs <container_id>
Contact
```
## For questions or feedback, please reach out to
-  hannaramzyhanna@gmail.com.

