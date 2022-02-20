import json
from paho.mqtt import client as mqtt_client
import Sensor

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("converter.log"),
        logging.StreamHandler()
    ]
)

logging.info("Converter on Power!")

conf = json.loads(open("config.json").read()) # Load JSON configuration

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("MQTT connect ok!")
    else:
        logging.info("MQTT connect fail")


def on_message(client, userdata, msg):
    # Identify sensor
    sensor = devicesTopics.get(msg.topic)
    # If message from unknown
    if sensor is None:
        return

    payload = msg.payload.decode('utf-8')
    payload_clean = payload.replace('\n', '').replace('\t', '').replace("\r", "").replace("  ", "")

    logging.info(f"[{sensor.device.name}]\tRECV FROM {msg.topic} DATA {payload_clean}")

    # Get state data
    state_topic, state_data = sensor.getState(payload)

    # Publish state data
    client.publish(state_topic, state_data)

    logging.info(f"[{sensor.device.name}]\tSENT TO {state_topic} DATA {state_data}")

# Init MQTT connection

client = mqtt_client.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(conf['mqtt']['user'], conf['mqtt']['pass'])
client.connect(conf['mqtt']['host'], conf['mqtt']['port'])
client.subscribe("#")

logging.info("Loading devices...")

devicesTopics = {}

# Load configuration
for device_config in conf['devices']:
    logging.info(f"Configuring device {device_config['device_name']}")
    sensor = Sensor.init(device_config)
    
    # Generate HA configuration for device
    config_topic, config_payload = sensor.getConfig()

    # Send configuration data to MQTT
    client.publish(config_topic, config_payload, retain=True)
    
    # Add configured device to subscription list
    devicesTopics[sensor.device.topic] = sensor

logging.info("Init succeeded!")

client.loop_forever()
