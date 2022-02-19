import json

class PressureSensor():
    def __init__(self, device):
        self.device = device
        self.ha_config_topic = f"homeassistant/sensor/{device.id}-{device.name}-pres/config"
        self.ha_state_topic = f"home/converterService/HassAnalogSensor/{device.id}"
        # Config message
        self.config = {
            "state_topic": f"+/+/HassAnalogSensor/{device.id}",
            "name": f"{device.name}-pres",
            "unique_id": f"{device.id}-{device.name}-pres",
            "device_class": "pressure",
            "value_template": "{{ value_json.pres | is_defined }}",
            "unit_of_measurement": "hPa",
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
            "pres": value
        }

        return self.ha_state_topic, json.dumps(state)