
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

    def control_device(self, command, device_name, param=None):
        for device in self.__device_list:
            if device.device_name == device_name:
                try:
                    device.validate_data()
                except ValueError as e:
                    print(f"Validation error for {device_name}: {e}")
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
                    device.change_temperature(param)
                    self.log_event(f"{device_name} temperature set to {param}°C.")
                elif command == "change_brightness":
                    device.change_brightness(param)
                    self.log_event(f"{device_name} brightness set to {param}.")
                elif command == "set_schedule":
                    if param:
                        device.set_schedule(param)
                        self.log_event(f"{device_name} schedule set to {param}.")
                    else:
                        print("Schedule time is required for this command.")
                else:
                    print(f"Invalid command: {command}")
                return True

        print(f"Device '{device_name}' not found.")
        return False

    def check_energy(self):
        active_energy = sum(d.power_consumption for d in self.__device_list if d._status == "On")
        if active_energy >= self.__total_energy:
            print("Power overload! The house's circuits have tripped.")
            self.log.append(f"{datetime.now()} - Power overload occurred.")

            if self.battery_level < 15:
                self.send_notification(f"Low battery for {self.device_name}. Please recharge.")
            elif self.battery_level == 0:
                self.turn_off()
            return False
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
        filename = f"smart_home_log.txt"
        try:
            with open(filename, "w") as log_file:
                for entry in self.log:
                    log_file.write(entry + "\n")
            print(f"Log saved to {filename}.")
        except Exception as e:
            print(f"Error saving log: {e}")


class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        print(f"{subscriber} has subscribed to notifications.")

    def send_notification(self, message):
        for subscriber in self.subscribers:
            print(f"Notification to {subscriber}: {message}")
