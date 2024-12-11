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
        self.network_connection = network_connection
        self._status = "Off"
        self._location = None # Положение в комнате

    def validate_data():
        pass

    def turn_on():
        pass

    def turn_off():
        pass

    def change_location():
        pass

    def perform_action():
        pass
