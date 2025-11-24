# Smart Sensor Gateway

This project implements a containerized IoT gateway that collects, processes, stores, and visualizes sensor data.

## Architecture

The system consists of the following Docker containers:

1.  **Mosquitto (MQTT Broker)**: Receives sensor data from the simulator.
2.  **Sensor Simulator**: A Python script that generates simulated joystick and button data and publishes it to the MQTT broker.
3.  **Node-RED**: Subscribes to MQTT topics, processes/validates the data, and writes it to InfluxDB.
4.  **InfluxDB**: A time-series database for storing sensor data.
5.  **Portainer**: A management UI for the Docker environment.

## Installation

### Prerequisites
- Docker and Docker Compose installed on your machine.

### Quick Start
1.  Clone this repository.
2.  Run the deployment script:
    ```bash
    ./deploy.bat
    ```
    Or manually:
    ```bash
    docker-compose up -d --build
    ```

## Configuration

### Credentials
- **InfluxDB**:
    - Username: `admin`
    - Password: `adminpassword123`
    - Token: `my-super-secret-auth-token`
    - Org: `sensorgateway`
    - Bucket: `sensor_data`

### Services
- **Node-RED**: [http://localhost:1880](http://localhost:1880)
- **InfluxDB**: [http://localhost:8086](http://localhost:8086)
- **Portainer**: [http://localhost:9000](http://localhost:9000)

## Automation & CI/CD

The `deploy.sh` script simulates a simple CI/CD pipeline. It:
1.  Stops the running containers.
2.  Rebuilds the Node-RED image (to ensure plugins are up to date).
3.  Restarts the stack with the new configuration.
4.  Cleans up unused images.

In a real-world scenario, this script could be triggered by a git hook or a CI runner (like GitHub Actions) to deploy changes automatically to the production server.

## Dashboard Setup
To visualize the data in InfluxDB:
1.  Log in to InfluxDB (admin/adminpassword123).
2.  Go to **Boards**.
3.  Import the dashboard template located at `influxdb_setup/dashboard.json` (if available) or create a new dashboard querying the `sensor_data` bucket.

## Data Flow
1.  **Simulator** -> `sensor/controller/joystick` & `sensor/controller/buttons` (MQTT)
2.  **Mosquitto** -> **Node-RED**
3.  **Node-RED** (Validates data) -> **InfluxDB** (Bucket: `sensor_data`)
