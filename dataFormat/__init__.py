# Invalid-to-Valid format converter

from dataFormat.formatInvalid1 import Invalid1
from dataFormat.formatInvalid2 import Invalid2
from dataFormat.formatInvalid3 import Invalid3
from dataFormat.formatInvalid4 import Invalid4
from dataFormat.formatInvalid5 import Invalid5

# Classes for each data type
converterAssign = {
    "Invalid1": Invalid1,
    "Invalid2": Invalid2,
    "Invalid3": Invalid3,
    "Invalid4": Invalid4,
    "Invalid5": Invalid5
}

def __init__():
    pass

# Returns specific format class
def get(device_config):
    deviceParser = converterAssign[device_config['data_format']]
    return deviceParser(device_config)

