import json

class Invalid2():
    # данные передаются в топике «Binary-ИдентификаторУстройства-Sensor». 
    # Данные передаются в шестнадцатиричном формате, при этом, если число вещественное, 
    # последние два десятичных числа будут идти после запятой. Например: передается число 6466, 
    # что при переводе в десятичную систему дает: 25702. Зная, что исходное число было вещественным,
    # мы делим полученное число на 100 и получаем результат: 257,02. 
    # Целые числа передаются без дробных знаков. Булевские данные передаются числом 1 и 0.
    def __init__(self, device):
        self.id = device['device_id']
        self.name = device['device_name']
        self.model = device['device_model']
        self.manufacturer = device['device_manufacturer']
        self.type = device['device_type']

        self.decimal_points = device['hex_decimal_points']

        self.topic = f"Binary-{self.id}-Sensor"
    

    def getValue(self, payload):
        # Convert hex 2 int with decimal points
        return int(payload, 16) / 10 ** self.decimal_points