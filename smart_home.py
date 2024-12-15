
from smart_device import *
from datetime import datetime
import random
import time

class SmartHome:
    def __init__(self):
        self.__device_list = []
        self.__total_energy = 10000
        self.log = []

    def add_devices(self, devices):
        for device in devices:
            if isinstance(device, SmartDevice):
                self.__device_list.append(device)
                print(f"{device.device_name} has been added.")
            else:
                raise ValueError("'device' object is not an instance of SmartDevice")

    def remove_device(self, *devices):
        for device_name in devices:
            for device in self.devices:
                if device.name == device_name:
                    self.__device_list.remove(device)
                    print(f"Device {device.name} has been removed from the house.")
                else:
                    print(f"Device {device.name} not found.")

    def log_event(self, message):
        self.log.append(f"{datetime.now()} - {message}")

    def __parse_command(self, command_input):
        parts = command_input.split(" --")
        cmd_and_device = parts[0].split(" ", 1)
        command = cmd_and_device[0]
        device_name = cmd_and_device[1] if len(cmd_and_device) > 1 else None
        params = parts[1:] if len(parts) > 1 else []
        return command, device_name, params

    def control_device(self, command_input):
        # Парсим команду
        command, device_name, params = self.__parse_command(command_input)

        if not device_name:
            # Обработка команд без устройств
            if command == "help":
                self.help()
                return
            elif command == "status_report":
                self.status_report()
                return
            elif command == "check_schedule":
                self.check_schedules()
                return
            else:
                print(f"Unknown command: {command}")
                return

        # Поиск устройства
        for device in self.__device_list:
            if device_name.lower() in device.device_name.lower():
                try:
                    device.validate_data()
                except ValueError as e:
                    print(f"Validation error for {device.device_name}: {e}")
                    return False

                if command == "charge":
                    device.charge()
                    self.log_event(f"{device_name} started charging.")

                elif command == "turn_on":
                    device.turn_on()
                    self.log_event(f"{device_name} turned ON.")

                elif command == "turn_off":
                    device.turn_off()
                    self.log_event(f"{device_name} turned OFF.")

                elif command == "start_recording":
                    device.start_recording()
                    self.log_event(f"{device_name} started recording.")

                elif command == "stop_recording":
                    device.stop_recording()
                    self.log_event(f"{device_name} stopped recording.")

                elif command == "change_temperature":
                    if len(params) >= 1:
                        try:
                            device.change_temperature(int(params[0]))
                            self.log_event(f"{device_name} temperature set to {params[0]}°C.")
                        except ValueError:
                            print("Error: Temperature must be an integer.")
                    else:
                        print("Temperature value is required for this command.")

                elif command == "change_brightness":
                    if len(params) >= 1:
                        try:
                            device.change_brightness(int(params[0]))
                            self.log_event(f"{device_name} brightness set to {params[0]}.")
                        except ValueError:
                            print("Error: Brightness level must be an integer.")
                    else:
                        print("Brightness level is required for this command.")

                elif command == "perform_action":
                    device.perform_action()
                    self.log_event(f"{device_name} performed action.")

                elif command == "set_schedule":
                    if len(params) >= 1:
                        device.set_schedule(params[0])
                        self.log_event(f"{device_name} schedule set to {params[0]}.")
                    else:
                        print("Schedule time is required for this command.")

                elif command == "show_battery":
                    device.show_battery()
                    self.log_event(f"{device_name} battery checked.")

                elif command == "set_location":
                    if len(params) >= 2:
                        try:
                            location, floor = params[0], int(params[1])
                            device.set_location(location.strip(), floor)
                            self.log_event(f"{device_name} location set to {location} on floor {floor}.")
                        except ValueError:
                            print("Error: Floor must be an integer.")
                    else:
                        print("Location and floor are required for this command.")

                else:
                    print(f"Invalid command: {command}")
                return

        print(f"Device '{device_name}' not found.")

    def check_energy(self):
        active_energy = sum(d.power_consumption for d in self.__device_list if d._status == "On")
        if active_energy >= self.__total_energy:
            print("Power overload! The house's circuits have tripped.")
            self.log_event("Power overload occurred.")

            if self.battery_level < 15:
                self.send_notification(f"Low battery for {self.device_name}. Please recharge.")
            elif self.battery_level == 0:
                self.turn_off()

        for device in self.__device_list:
            device.update_battery()
        return True

    def status_report(self):
        for device in self.__device_list:
            print(device)

    def set_notification_center(self, notification_center):
        for device in self.__device_list:
            device.attach_notification_center(notification_center)

    def check_schedules(self):
        current_time = datetime.now().strftime("%H:%M")
        for device in self.__device_list:
            device.check_schedule(current_time)

    def save_log(self):
        """Сохраняет лог событий в файл."""
        filename = f"SmartHome.log"
        try:
            with open(filename, "w") as log_file:
                for entry in self.log:
                    log_file.write(entry + "\n")
            print(f"Log saved to {filename}")
        except Exception as e:
            print(f"Error saving log: {e}")

    def help(self):
        help_message = '''
Available commands:
1. charge <device_name>
   Start charging the specified device.

2. turn_on <device_name>
   Turn on the specified device.

3. turn_off <device_name>
   Turn off the specified device.

4. start_recording <device_name>
   Start recording (for cameras only).

5. stop_recording <device_name>
   Stop recording (for cameras only).

6. change_temperature <device_name> <temperature>
   Change the temperature (for thermostats only).
   Example: change_temperature Bedroom Thermostat 22

7. change_brightness <device_name> <brightness>
   Change the brightness (for lights only).
   Brightness should be between 10 and 100.
   Example: change_brightness Living Room Light 50

8. status_report
   Display the status of all devices in the house.

9. check_schedule
   Check and execute schedules for all devices.

10. perform_action <device_name>
    Perform the specific action of the device.

11. set_schedule <device_name> <time>
    Set a schedule for the device.
    Time format: HH:MM.
    Example: set_schedule Living Room Light 18:00

12. show_battery <device_name>
    Update the battery status of the device.

13. set_location <device_name> <room,floor>
    Set the location of the device.
    Example: set_location Living Room Light Kitchen,2

14. help
    Display this help message with all available commands.

15. quit
    Exit the program.
'''
        print(help_message)


class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        print(f"{subscriber} has subscribed to notifications.")

    def send_notification(self, message):
        for subscriber in self.subscribers:
            print(f"Notification to {subscriber}: {message}")
