#!/bin/sh
echo "Waiting for InfluxDB to be ready..."
sleep 10

echo "Importing dashboard..."
curl -X POST $INFLUX_URL/api/v2/dashboards \
  -H "Authorization: Token $INFLUX_TOKEN" \
  -H "Content-Type: application/json" \
  --data @/tmp/sensor_gateway.json

echo "Dashboard import finished."
