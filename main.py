'''
Описание задачи: Вам нужно разработать систему управления умным домом.
Система должна контролировать разные устройства, такие как лампы,
термостаты, камеры, и должна предоставлять интерфейс для управления
этими устройствами, а также собирать и анализировать данные о работе
устройств.
Основные требования:

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

3. Класс SmartHome
o Создайте класс SmartHome, который будет управлять всеми
устройствами:
 Храните список всех устройств в доме.
 Создайте методы для добавления и удаления устройств.
 Создайте метод control_device(), который будет находить
устройство по имени и выполнять для него команду
(включение, выключение или выполнение действия).
 Реализуйте метод status_report(), который будет выводить
текущий статус всех устройств, включая их состояние и
уровень заряда.

4. Обработка событий и уведомлений
o Реализуйте систему уведомлений, используя паттерн
"Наблюдатель". Создайте класс NotificationCenter, который будет
принимать подписчиков (например, пользователей) и отправлять
уведомления, когда сработает какое-то событие (например,
обнаружение движения камерой или достижение низкого уровня
заряда у устройства).
o Устройства, такие как Camera, должны отправлять уведомления
при обнаружении движения.

5. Энергосбережение и планирование работы
o Реализуйте режим энергосбережения для устройств. Например,
когда уровень заряда устройства падает ниже определенного
значения, оно должно выключаться автоматически и отправлять
уведомление о необходимости подзарядки.
o Добавьте возможность устанавливать расписание для устройств.
Например, включение света в определенное время или изменение
температуры.

6. Расширенные функции (опционально)
o Добавьте интерфейс (например, через командную строку) для
управления устройствами, так, чтобы пользователь мог вводить
команды для взаимодействия с системой.
o Реализуйте сбор и анализ данных. Например, сохраняйте данные
об активности устройств и строите отчеты по энергопотреблению
и времени работы каждого устройства.

7. Многопоточность
o Добавьте многопоточность для имитации работы устройств в
режиме реального времени, например, каждое устройство
работает в своем потоке, выполняя свои действия (например,
изменение температуры или периодическая запись видео).
o Используйте таймеры для имитации периодических событий
(например, камеры, которые записывают видео каждые 5 минут).
'''

from smart_home import *
import time


def main():
    # Дом
    home = SmartHome()
    home.start_battery_drain() 
    home.start_motion_detection() 

    # Центр уведомлений
    notification_center = NotificationCenter(home)
    notification_center.subscribe("Mr Anderson")

    devices = [
        Camera(device_name="Arlo Spotlight Cam", power_consumption=12, network_connection="Wi-Fi"),
        Camera(device_name="Ring Stick Up Cam", power_consumption=15, network_connection="Wi-Fi"),
        Camera(device_name="Nest Cam Pro 4", power_consumption=14, network_connection="Wi-Fi"),
        Camera(device_name="Eufy Security Cam", power_consumption=16, network_connection="Wi-Fi"),
        Camera(device_name="Blink Outdoor Cam", power_consumption=15, network_connection="Wi-Fi"),

        Light(device_name="Ambiance Bulb E27", power_consumption=9, network_connection="Wi-Fi"),
        Light(device_name="TRADFRI LED Bulb E14", power_consumption=8, network_connection="Wi-Fi"),
        Light(device_name="Mi Smart LED Bulb", power_consumption=10, network_connection="Wi-Fi"),
        Light(device_name="Kasa Smart Light Bulb", power_consumption=8, network_connection="Wi-Fi"),
        Light(device_name="Cync Smart Bulb", power_consumption=7, network_connection="Bluetooth"),
        Light(device_name="SMART+ LED GU10 Spot", power_consumption=6, network_connection="Wi-Fi"),
        Light(device_name="Nanoleaf A19 Bulb", power_consumption=7, network_connection="Bluetooth"),
        Light(device_name="LIFX Mini Smart Bulb", power_consumption=9, network_connection="Wi-Fi"),

        Thermostat(device_name="Nest Learning Thermostat", power_consumption=2000, network_connection="Wi-Fi"),
        Thermostat(device_name="Ecobee SmartThermostat", power_consumption=1800, network_connection="Wi-Fi"),
    ]

    home.add_devices(devices)
    home.set_notification_center(notification_center)

    try:
        while True:
            if not home.check_energy():
                break

            print('')
            command_input = input("Enter command: ").strip()
            if command_input.lower() == "quit":
                break

            home.control_device(command_input)

            time.sleep(1)

    finally:
        home.stop_battery_drain() 
        home.save_log()


if __name__=="__main__":
    main()