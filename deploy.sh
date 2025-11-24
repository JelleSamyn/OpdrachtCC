#!/bin/bash

# Deploy script for Sensor Gateway

echo "Starting deployment..."

# Stop existing containers
echo "Stopping existing containers..."
docker-compose down

# Build new images (if any)
echo "Building services..."
docker-compose build

# Start the stack
echo "Starting services..."
docker-compose up -d

# Prune unused images to save space
echo "Pruning unused images..."
docker image prune -f

echo "Deployment complete! Access the services at:"
echo " - Node-RED: http://localhost:1880"
echo " - InfluxDB: http://localhost:8086"
echo " - Portainer: http://localhost:9000"
