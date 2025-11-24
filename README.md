# Smart Sensor Gateway

Dit project implementeert een gecontaineriseerde IoT-gateway die sensordata verzamelt, verwerkt, opslaat en visualiseert. Het simuleert een joystick-controller, verzendt data via MQTT, verwerkt deze met Node-RED, slaat het op in InfluxDB en maakt visualisatie mogelijk.

## Architectuur

Het systeem bestaat uit de volgende Docker-containers, aangestuurd via Docker Compose:

1.  **Mosquitto (MQTT Broker)**:
    -   Fungeert als de centrale berichtenbus.
    -   Luistert op poort `1883`.
2.  **Sensor Simulator**:
    -   Een Python-script (`simulator/sensor_simulator.py`) dat gesimuleerde joystick- (`x`, `y`, `magnitude`) en knopdata genereert.
    -   Publiceert data naar `sensor/controller/joystick` en `sensor/controller/buttons`.
3.  **Node-RED**:
    -   Abonneert zich op de MQTT-topics.
    -   Verwerkt en formatteert de data (JSON-parsing, typeconversie).
    -   Schrijft de data naar InfluxDB.
    -   Bereikbaar via [http://localhost:1880](http://localhost:1880).
4.  **InfluxDB**:
    -   Een tijdreeks-database voor het opslaan van de sensordata.
    -   Bereikbaar via [http://localhost:8086](http://localhost:8086).
5.  **Portainer**:
    -   Een beheerinterface voor de Docker-omgeving om containers te monitoren.
    -   Bereikbaar via [http://localhost:9000](http://localhost:9000).

## Projectstructuur

```
.
├── deploy.bat               # script voor geautomatiseerde (her)installatie
├── docker-compose.yml      # Docker Compose configuratie voor de stack
├── influxdb_config/        # Configuratiebestanden voor InfluxDB
├── influxdb_data/          # Persistente opslag voor InfluxDB data
├── influxdb_setup/         # Bevat dashboard templates (dashboard.json)
├── mosquitto/              # Mosquitto configuratie, data en logs
├── nodered_data/           # Node-RED flows en configuratie
└── simulator/              # Broncode van de Python simulator en Dockerfile
```

## Installatie

### Vereisten
- Docker en Docker Compose geïnstalleerd op je machine.

### Snel aan de slag
1.  Kloon deze repository.
2.  Voer het installatiescript uit:
    ```bash
    ./deploy.bat
    ```
    Of handmatig via Docker Compose:
    ```bash
    docker-compose up -d --build
    ```

## Configuratie

### InfluxDB Logingegevens
Deze gegevens zijn geconfigureerd in `docker-compose.yml` en zijn nodig om in te loggen op de InfluxDB UI of om externe tools te verbinden.

-   **Gebruikersnaam**: `admin`
-   **Wachtwoord**: `adminpassword123`
### Portainer Logingegevens

-   **Gebruikersnaam**: `admin`
-   **Wachtwoord**: `adminpassword123`
  
### Service Endpoints
-   **Node-RED**: [http://localhost:1880](http://localhost:1880)
-   **InfluxDB**: [http://localhost:8086](http://localhost:8086)
-   **Portainer**: [http://localhost:9000](http://localhost:9000)

## Dataflow

1.  **Generatie**: De `simulator` genereert willekeurige data:
    -   **Joystick**: JSON-object `{"x": ..., "y": ..., "magnitude": ...}` verzonden naar `sensor/controller/joystick`.
    -   **Knoppen**: Integer (aantal) verzonden naar `sensor/controller/buttons`.
2.  **Transmissie**: Data wordt naar de **Mosquitto** broker gestuurd.
3.  **Verwerking**: **Node-RED** ontvangt de berichten:
    -   Converteert waarden naar getallen.
    -   Voegt tags toe (bijv. `location: "controller"`).
4.  **Opslag**: Verwerkte data wordt weggeschreven naar **InfluxDB** in de `sensor_data` bucket onder de measurements `joystick` en `buttons`.

## Dashboard Setup

Het InfluxDB dashboard wordt automatisch geïmporteerd en geconfigureerd tijdens de installatie.

Om het te bekijken:
1.  Log in op InfluxDB via [http://localhost:8086](http://localhost:8086) met de bovenstaande inloggegevens.
2.  Ga naar **Boards** in de zijbalk.
3.  Klik op het beschikbare dashboard om de visualisaties van de joystick en knoppen te zien.

*Mocht het dashboard onverhoopt niet zichtbaar zijn, dan kun je het bestand `influxdb_setup/dashboard.json` handmatig importeren via de 'Import Dashboard' knop.*

## Verificatie

Om te controleren of alles correct werkt, kun je de logs van de simulator en Node-RED containers bekijken:

```bash
# Controleer of de simulator data verstuurt
docker logs -f simulator

# Controleer of Node-RED data verwerkt (indien debug nodes aan staan) of bekijk algemene logs
docker logs -f nodered
```

Je kunt ook een tool zoals **MQTT Explorer** gebruiken om verbinding te maken met `localhost:1883` en te verifiëren of berichten binnenkomen op de `sensor/controller/#` topics.
