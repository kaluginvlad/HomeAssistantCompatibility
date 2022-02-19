# данные передаются в топике «CSV-ИдентификаторУстройства». 
# Данные передаются в CSV-формате в виде: ИмяЗначения;Значение

class Invalid4():
    def __init__(self, device):
        self.id = device['device_id']
        self.name = device['device_name']
        self.model = device['device_model']
        self.manufacturer = device['device_manufacturer']
        self.type = device['device_type']

        self.topic = f"CSV-{self.id}"
    

    def getValue(self, payload):
        return payload.split(";")[1]