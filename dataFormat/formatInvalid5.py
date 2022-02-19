# данные передаются в топике «SensorИдентификаторУстройства». 
# Данные передаются обычным текстом в виде одного значения.

class Invalid5():
    def __init__(self, device):
        self.id = device['device_id']
        self.name = device['device_name']
        self.model = device['device_model']
        self.manufacturer = device['device_manufacturer']
        self.type = device['device_type']

        self.topic = f"Sensor{self.id}"
    

    def getValue(self, payload):
        return payload