#!/bin/sh
set -eu

# simple deploy script (can be used in gitlab/github actions)
# 1) build nodered image
echo "Building Node-RED image..."
docker build -t sg_nodered_custom:latest ./nodered

# 2) bring down stack (if exists) and bring up fresh
echo "Restarting stack..."
docker compose down
docker compose up -d --build

echo "Done. Use 'docker compose logs -f' or open Portainer at http://localhost:9000 to inspect."
