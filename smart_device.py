
class SmartDevice:
    def __init__(self, device_name, power_consumption, network_connection):
        self.device_name = device_name
        self.power_consumption = power_consumption
        self.network_connection = network_connection
        self._status = "Off"
        self._battery_level = 100
        self._location = None
        self._floor = None
        self._notification_center = None
        self._schedule = None
        self._is_charging = False

    def __str__(self):
        # Format the device details into a readable string
        location = self._location if self._location else "Not Set"
        floor = self._floor if self._floor else "Not Set"
        charging_status = "Yes" if self._is_charging else "No"
        return (f"Device Name: {self.device_name}\n"
                f"Power Consumption: {self.power_consumption}W\n"
                f"Network Connection: {self.network_connection}\n"
                f"Status: {self._status}\n"
                f"Battery Level: {self._battery_level}%\n"
                f"Location: {location}\n"
                f"Floor: {floor}\n"
                f"Charging: {charging_status}\n")

    def validate_data(self):
        appropriate_connections = ["Wi-Fi", "Bluetooth", "Ethernet"]
        if not isinstance(self.power_consumption, int):
            raise ValueError("power_consumption must be an integer!")
        elif self.power_consumption <= 0:
            raise ValueError(f"Device '{self.device_name}' must consume at least 1W!")
            
        if self.network_connection not in appropriate_connections:
            raise ValueError("'network_connection' must be Wi-Fi / Bluetooth / Ethernet")

    def turn_on(self):
        self._status = "On"
        print(f"{self.device_name} has been enabled.")

    def turn_off(self):
        self._status = "Off"
        print(f"{self.device_name} has been disabled.")

    def set_location(self, room, floor):
        if not isinstance(room, str) or not isinstance(floor, int):
            raise ValueError("Invalid arguments' type!")

        self._location = room
        if floor == 1:
            self._floor = f"{floor}st"
        elif floor == 2:
            self._floor = f"{floor}nd"
        elif floor == 3:
            self._floor = f"{floor}rd"
        else:
            self._floor = f"{floor}th"
        print(f"New location for {self.device_name}: {self._location} on {self._floor} floor.")

    def perform_action(self):
        print("Device is doing it's job...")

    def send_notification(self, message):
        if self.notification_center:
            self.notification_center.send_notification(message)

    def attach_notification_center(self, notification_center):
        self._notification_center = notification_center

    def charge(self):
        if self._battery_level < 100:
            self._is_charging = True
            print(f"{self.device_name} is now charging.")
        else:
            print(f"{self.device_name} is already fully charged.")
            self._is_charging = False

    def update_battery(self):
        if self._is_charging and self._battery_level < 100:
            self._battery_level += 1
            if self._battery_level >= 100:
                self._battery_level = 100
                self._is_charging = False
                message = f"{self.device_name} is fully charged."
                print(message)
                self.send_notification(message)
        elif self._status == "On":
            self._battery_level -= 0.3
            if self._battery_level <= 0:
                self._battery_level = 0
                self.turn_off()
                message = f"{self.device_name} turned off due to low battery."
                print(message)
                self.send_notification(message)
            elif self._battery_level < 15 and not self._is_charging:
                message = f"Low battery for {self.device_name}. Please recharge."
                print(message)
                self.send_notification(message)

    def show_battery(self):
        print(f"{self.device_name} - {self._battery_level}%")

    def set_schedule(self, time):
        self._schedule = time
        print(f"Schedule for {self.device_name} set to {time}.")

    def check_schedule(self, current_time):
        if self._schedule == current_time and self._status == "Off":
            self.turn_on()


class Light(SmartDevice):
    def __init__(self, device_name, power_consumption, network_connection):
        super().__init__(device_name, power_consumption, network_connection)
        self.brightness = 50
        self.color = "white"

    def change_color(self, new_color):
        if type(new_color is str):
            self.color = new_color
            print(f"Color for {self.device_name} changed to {new_color}")
        else:
            raise TypeError("Type of 'new_color' must be str!")

    def change_brightness(self, new_brightness):
        if type(new_brightness is int):
            if new_brightness <= 100 and new_brightness >= 10:
                self.brightness = new_brightness
                print(f"Brightness for {self.device_name} changed to {new_brightness}")
            else:
                raise ValueError("'new_brightness' must be from 10 to 100")
        else:
            raise TypeError("Type of 'new_brightness' must be int!")

    def perform_action(self):
        if self._status == "On":
            print(f"Device {self.device_name} is lighting up with {self.color} color at {self.brightness}% brightness.")
        else:
            print(f"Device {self.device_name} is Off. Pleace, turn it On.")


class Thermostat(SmartDevice):
    def __init__(self, device_name, power_consumption, network_connection):
        super().__init__(device_name, power_consumption, network_connection)
        self.temperature = 20
        self.mode = "Auto"

    def change_temperature(self, new_temp):
        self.__appropriate_temp = range(0, 35)

        if type(new_temp is int):
            if new_temp in self.__appropriate_temp:
                self.temperature = new_temp
                print(f"Temperature for {self.device_name} set on {new_temp}°C")
            else:
                raise ValueError(f"'new_temp' must be in range of {self.__appropriate_temp}")
        else:
            raise TypeError("'new_temp' must be int!")

    def change_mode(self, new_mode):
        self.__appropriate_mods = ["Auto", "Heating", "Cooling", "Fan only", "Dry"]

        if new_mode in self.__appropriate_mods:
            self.mode = new_mode
            print(f"Mode for {self.device_name} changed to {new_mode}")
        else:
            raise ValueError(f"'new_mode' must be one of the: {self.__appropriate_mods}")

    def perform_action(self):
        if self._status == "On":
            print(f"Device {self.device_name} is now on {self.mode} mode with {self.temperature}°C")
        else:
            print(f"Device {self.device_name} is Off. Pleace, turn it On.")
            

class Camera(SmartDevice):
    def __init__(self, device_name, power_consumption, network_connection):
        super().__init__(device_name, power_consumption, network_connection)
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
            print(f"{self.device_name} is recording and ready to detect motion.")
        else:
            print(f"{self.device_name} is Off. Pleace, turn it On and run recording.")

    def detect_motion(self):
        if self.is_recording:
            print(f"Camera {self.device_name} on {self._floor} floor has detected some movements!")
        print("No movements were detected.")