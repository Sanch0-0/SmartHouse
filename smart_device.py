'''
1. Базовый класс SmartDevice
o Создайте абстрактный класс SmartDevice, представляющий
базовый интерфейс для всех умных устройств. Он должен
включать:
 Поля для имени устройства, состояния
(включено/выключено), и уровня заряда.
 Методы turn_on() и turn_off(), которые включают и
выключают устройство.
 Абстрактный метод perform_action(), который будет
переопределяться в подклассах, чтобы каждое устройство
выполняло свою уникальную функцию.

2. Подклассы для разных устройств
o Создайте подклассы для различных типов устройств, таких как:
 Light: устройство, которое может включаться и
выключаться, а также менять яркость и цвет.
 Thermostat: устройство, которое регулирует температуру и
позволяет устанавливать разные режимы.
 Camera: устройство, которое может записывать видео,
делать фотографии и отправлять уведомления при
обнаружении движения.
o Каждый из этих классов должен реализовать свой вариант метода
perform_action() для выполнения своих уникальных функций.
'''

class SmartDevice:
    def __init__(self, device_name, brand, power_consumption, network_connection):
        self.device_name = device_name
        self.brand = brand
        self.power_consumption = power_consumption
        self.network_connection = network_connection.capitalize()
        self._status = "Off"
        self._location = None
        self._floor = None

    def validate_data(self):
        appropriate_connections = ["Wi-Fi", "Bluetooth", "Ethernet"]

        if self.power_consumption >= 220:
            raise ValueError(f"Device '{self.device_name}' is too energy-consuming!")
        elif not self.power_consumption.isdigit():
            raise ValueError("power_consuption must be an integer!")
        
        if self.network_connection not in appropriate_connections:
            raise ValueError("'network_connection' must be Wi-Fi / Bluetooth / Ethernet")

    def turn_on(self):
        self._status = "On"
        print("Device has been enabled.")

    def turn_off(self):
        self._status = "Off"
        print("Device has been disabled.")

    def set_location(self, room, floor):
        if room.isalpha() and floor.isdigit():
            self._location = room

            if floor == 1:
                self._floor = floor + "st"
            elif floor == 2:
                self._floor = floor + "nd"
            elif floor == 3:
                self._floor = floor + "rd"
            else:
                self._floor = floor + "th"
        else:
            raise ValueError("Invalid arguments' type!")

        print(f"New location for {self.device_name}: {self._location} on {self._floor} floor.")

    def perform_action(self):
        print("Device is doing it's job...")
