import json

class VoltageSensor():
    def __init__(self, device):
        self.device = device
        self.ha_config_topic = f"homeassistant/sensor/{device.id}-{device.name}-volt/config"
        self.ha_state_topic = f"home/converterService/HassAnalogSensor/{device.id}"
        # Config message
        self.config = {
            "state_topic": f"+/+/HassAnalogSensor/{device.id}",
            "name": f"{device.name}-volt",
            "unique_id": f"{device.id}-{device.name}-volt",
            "device_class": "voltage",
            "value_template": "{{ value_json.volt | is_defined }}",
            "unit_of_measurement": "V",
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
            "volt": value
        }

        return self.ha_state_topic, json.dumps(state)