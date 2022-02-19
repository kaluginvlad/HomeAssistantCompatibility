# данные передаются в топике «XmlSensor_ИдентификаторУстройства». 
# Данные передаются в xml-формате в виде:
# <sensor><data><name>ИмяЗначения</name><value>Значение</value></data></sensor>

class Invalid3():
    def __init__(self, device):
        self.id = device['device_id']
        self.name = device['device_name']
        self.model = device['device_model']
        self.manufacturer = device['device_manufacturer']
        self.type = device['device_type']

        self.topic = f"XmlSensor_{self.id}"
    

    def getValue(self, payload):
        # Extract value from XML string
        value = payload[payload.find("<value>") + 7: payload.find("</value>")]
        return value