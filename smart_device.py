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
    def __init__(self, brand, device_name, power_consumption, network_connection):
        self.brand = brand
        self.device_name = device_name
        self.power_consumption = power_consumption
        self.network_connection = network_connection.capitalize()
        self._status = "Off"
        self._battery_level = 100
        self._location = None
        self._floor = None
        self._notification_center = None

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
        print(f"{self.brand} {self.device_name} has been enabled.")

    def turn_off(self):
        self._status = "Off"
        print(f"{self.brand} {self.device_name} has been disabled.")

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

    def send_notification(self, message):
        if self.notification_center:
            self.notification_center.send_notification(message)


class Light(SmartDevice):
    def __init__(self, brand, device_name, power_consumption, network_connection):
        super().__init__(brand, device_name, power_consumption, network_connection)
        self.brightness = 50
        self.color = "white"

    def change_color(self, new_color):
        if type(new_color is str):
            self.color = new_color
            print(f"Color for {self.brand} {self.device_name} changed to {new_color}")
        else:
            raise TypeError("Type of 'new_color' must be str!")

    def change_brightness(self, new_brightness):
        if type(new_brightness is int):
            if new_brightness <= 100 and new_brightness >= 10:
                self.brightness = new_brightness
                print(f"Brightness for {self.brand} {self.device_name} changed to {new_brightness}")
            else:
                raise ValueError("'new_brightness' must be from 10 to 100")
        else:
            raise TypeError("Type of 'new_brightness' must be int!")

    def perform_action(self):
        if self._status == "On":
            print(f"Device {self.brand} {self.device_name} is lighting up with {self.color} color at {self.brightness}% brightness.")
        else:
            print(f"Device {self.brand} {self.device_name} is Off. Pleace, turn it On.")


class Thermostat(SmartDevice):
    def __init__(self, brand, device_name, power_consumption, network_connection):
        super().__init__(brand, device_name, power_consumption, network_connection)
        self.temperature = 20
        self.mode = "Auto"

    def change_temperature(self, new_temp):
        self.__appropriate_temp = range(0, 35)

        if type(new_temp is int):
            if new_temp in self.__appropriate_temp:
                self.temperature = new_temp
                print(f"Temperature for {self.brand} {self.device_name} set on {new_temp}°C")
            else:
                raise ValueError(f"'new_temp' must be in range of {self.__appropriate_temp}")
        else:
            raise TypeError("'new_temp' must be int!")

    def change_mode(self, new_mode):
        self.__appropriate_mods = ["Auto", "Heating", "Cooling", "Fan only", "Dry"]

        if type(new_mode is int):
            if new_mode in self.__appropriate_mods:
                self.mode = new_mode
                print(f"Mode for for {self.brand} {self.device_name} changed to {new_mode}")
            else:
                raise ValueError(f"'new_mod' must be one of the: {self.__ppropriate_mods}")

    def perform_action(self):
        if self._status == "On":
            print(f"Device {self.brand} {self.device_name} is now on {self.mode} mode with {self.temperature}°C")
        else:
            print(f"Device {self.brand} {self.device_name} is Off. Pleace, turn it On.")

class Camera(SmartDevice):
    def __init__(self, brand, device_name, power_consumption, network_connection):
        super().__init__(brand, device_name, power_consumption, network_connection)
        self.is_recording = False

    def start_recording(self):
        if self._status == "On":
            self.is_recording = True
            print(f"{self.device_name} has started recording.")
        else:
            print(f"{self.device_name} is Off. Pleace, turn in Ot.")

    def stop_recording(self):
        self.is_recording = False
        print(f"{self.device_name} has stopped recording.")

    def perform_action(self):
        if self._status == "On" and self.is_recording:
            print(f"{self.brand} {self.device_name} is recording and ready to detect motion.")
        else:
            print(f"{self.brand} {self.device_name} is Off. Pleace, turn it On and run recording.")

    def detect_motion(self):
        if self.is_recording:
            print(f"Camera {self.device_name} on {self._floor} floor has detected some movements!")
        print("No movements were detected.")