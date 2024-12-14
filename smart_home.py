from smart_device import *

class SmartHome:
    def __init__(self):
        self.__device_list = []
        self.__total_energy = 1000

    def add_devices(self, devices):
        for device in devices:
            if isinstance(device, SmartDevice):
                self.__device_list.append(device)
                print(f"{device.name} has been added.")
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

    def control_device(self, device_name, command, param=None):
        for device in self.__device_list:
            if device.device_name == device_name:
                if command == "turn_on":
                    device.turn_on()
                elif command == "turn_off":
                    device.turn_off()
                elif command == "perform_action":
                    device.perform_action()

                elif isinstance(device, Camera) and command == "start_recording":
                    device.start_recording()
                elif isinstance(device, Camera) and command == "stop_recording":
                    device.stop_recording()

                elif isinstance(device, Thermostat) and command == "change_temperature":
                    device.change_temperature(param)
                elif isinstance(device, Thermostat) and command == "change_mode":
                    device.change_mode(param)

                elif isinstance(device, Light) and command == "change_color":
                    device.change_color(param)
                elif isinstance(device, Light) and command == "change_brightness":
                    device.change_brightness(param)
                else:
                    print(f"Invalid command '{command}' for device '{device_name}'.")
                return
        print(f"Device '{device_name}' not found.")

    def status_report(self):
        for device in self.__device_list:
            print(device)

    def check_battery(self):
        if self.battery_level < 15:
            self.send_notification(f"Low battery for {self.device_name}. Please recharge.")
        elif self.battery_level == 0:
            self.turn_off()

    def set_notification_center(self, notification_center):
        for device in self.__device_list:
            device.attach_notification_center(notification_center)



class NotificationCenter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        print(f"{subscriber} has subscribed to notifications.")

    def send_notification(self, message):
        for subscriber in self.subscribers:
            print(f"Notification to {subscriber}: {message}")
'''
5. Энергосбережение и планирование работы
o Реализуйте режим энергосбережения для устройств. Например,
когда уровень заряда устройства падает ниже определенного
значения, оно должно выключаться автоматически и отправлять
уведомление о необходимости подзарядки.
o Добавьте возможность устанавливать расписание для устройств.
Например, включение света в определенное время или изменение
температуры.
'''
