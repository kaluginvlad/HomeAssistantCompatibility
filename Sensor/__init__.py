import dataFormat

from Sensor.Temperature import TemperatureSensor
from Sensor.Voltage import VoltageSensor
from Sensor.PressureHpa import PressureSensor
from Sensor.Current import CurrentSensor
from Sensor.FrequencyHz import FrequencySensor
from Sensor.Humidity import HumiditySensor
from Sensor.Plug import PlugSensor

sensorsAssignment = {
    "Temperature": TemperatureSensor,
    "Voltage": VoltageSensor,
    "PressureHpa": PressureSensor,
    "Current": CurrentSensor,
    "FrequencyHz": FrequencySensor,
    "Humidity": HumiditySensor,
    "Plug": PlugSensor
}

# Returns specific sensor class
def init(device_config):
    device = dataFormat.get(device_config)
    return sensorsAssignment[device.type](device)