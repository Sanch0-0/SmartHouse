from smart_device import *

class SmartHome:
    def __init__(self):
        self.__device_list = []

    def add_devices(self, *devices):
        for device in devices:
            if isinstance(device, SmartDevice):
                self.__device_list.append(device)
                print(f"{device.name} has been added.")
            else:
                raise ValueError("'device' object is not an instance of SmartDevice")
