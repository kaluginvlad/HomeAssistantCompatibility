import json

class PlugSensor():
    def __init__(self, device):
        self.device = device
        self.ha_config_topic = f"homeassistant/binary_sensor/{device.id}-{device.name}-state/config"
        self.ha_state_topic = f"home/converterService/HassBinarySensor/{device.id}"
        # Config message
        self.config = {
            "state_topic": f"+/+/HassBinarySensor/{device.id}",
            "name": f"{device.name}-state",
            "unique_id": f"{device.id}-{device.name}-state",
            "device_class": "plug",
            "payload_on": "On",
            "payload_off": "Off",
            "value_template": "{{ value_json.state | is_defined }}",
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

        # Plug state override for Invalid2 type
        if value == 1:
            value = "On"
        if value == 0:
            value = "Off"

        state = {
            "Id": self.device.id,
            "name": self.device.name,
            "state": value
        }

        return self.ha_state_topic, json.dumps(state)