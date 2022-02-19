import json

class Invalid1():
    # данные передаются в топике «DeviceИдентификаторУстройства». Данные передаются в формате JSON, в виде «{"value":"ЗНАЧЕНИЕ"}».
    def __init__(self, device):
        self.id = device['device_id']
        self.name = device['device_name']
        self.model = device['device_model']
        self.manufacturer = device['device_manufacturer']
        self.type = device['device_type']

        self.topic = f"Device{self.id}"
    

    def getValue(self, payload):
        data = json.loads(payload)
        return data['value']