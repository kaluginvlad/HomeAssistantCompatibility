import json

class HumiditySensor():
    def __init__(self, device):
        self.device = device
        self.ha_config_topic = f"homeassistant/sensor/{device.id}-{device.name}-hum/config"
        self.ha_state_topic = f"home/converterService/HassAnalogSensor/{device.id}"
        # Config message
        self.config = {
            "state_topic": f"+/+/HassAnalogSensor/{device.id}",
            "name": f"{device.name}-hum",
            "unique_id": f"{device.id}-{device.name}-hum",
            "device_class": "humidity",
            "value_template": "{{ value_json.hum | is_defined }}",
            "unit_of_measurement": "%",
            "device": {
                "connections": [],
                "identifiers": [
                    f"{device.id}"
                ],
                "manufacturer": f"{device.manufacturer}",
                "model": f"{device.model}",
                "name": f"{device.name}"
            }
        }

    # Returns device config in HA format
    def getConfig(self):
        return self.ha_config_topic, json.dumps(self.config)

    # Returns state in HA
    def getState(self, payload):
        # Get value from formatter
        value = self.device.getValue(payload)
        state = {
            "Id": self.device.id,
            "name": self.device.name,
            "hum": value
        }

        return self.ha_state_topic, json.dumps(state)