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

6. Многопоточность
o Добавьте многопоточность для имитации работы устройств в
режиме реального времени, например, каждое устройство
работает в своем потоке, выполняя свои действия (например,
изменение температуры или периодическая запись видео).
o Используйте таймеры для имитации периодических событий
(например, камеры, которые записывают видео каждые 5 минут).

7. Расширенные функции (опционально)
o Добавьте интерфейс (например, через командную строку) для
управления устройствами, так, чтобы пользователь мог вводить
команды для взаимодействия с системой.
o Реализуйте сбор и анализ данных. Например, сохраняйте данные
об активности устройств и строите отчеты по энергопотреблению
и времени работы каждого устройства.
'''

from smart_home import *



def main():
    # Создаем центр уведомлений
    notification_center = NotificationCenter()
    notification_center.subscribe("User 1")
    notification_center.subscribe("User 2")

    # Создаем умный дом
    home = SmartHome()

    # Добавляем устройства
    devices = [
        Camera(device_name="Arlo Pro 4 Spotlight Camera", power_consumption=6, network_connection="Wi-Fi"),
        Camera(device_name="Ring Stick Up Cam Battery", power_consumption=5, network_connection="Wi-Fi"),
        Camera(device_name="Nest Cam (Battery)", power_consumption=4, network_connection="Wi-Fi"),
        Camera(device_name="Eufy Security SoloCam E40", power_consumption=6, network_connection="Wi-Fi"),
        Camera(device_name="Blink Outdoor Camera", power_consumption=5, network_connection="Wi-Fi"),
        
        Light(device_name="White and Color Ambiance Bulb E27", power_consumption=9, network_connection="Wi-Fi"),
        Light(device_name="TRÅDFRI LED Bulb E14 600 lm", power_consumption=8, network_connection="Zigbee"),
        Light(device_name="Mi Smart LED Bulb Essential (White and Color)", power_consumption=10, network_connection="Wi-Fi"),
        Light(device_name="Kasa Smart Wi-Fi Light Bulb", power_consumption=8, network_connection="Wi-Fi"),
        Light(device_name="Cync Full Color Smart Bulb", power_consumption=7, network_connection="Bluetooth"),
        Light(device_name="SMART+ LED GU10 Spot", power_consumption=6, network_connection="Zigbee"),
        Light(device_name="Nanoleaf Essentials A19 Bulb", power_consumption=7, network_connection="Thread"),
        Light(device_name="LIFX Mini Color and White Wi-Fi Smart Bulb", power_consumption=9, network_connection="Wi-Fi"),

        Thermostat(device_name="Nest Learning Thermostat (3rd Gen)", power_consumption=2000, network_connection="Wi-Fi"),
        Thermostat(device_name="Ecobee SmartThermostat with Voice Control", power_consumption=1800, network_connection="Wi-Fi"),
    ]

    # Присоединяем устройства к дому
    home.add_devices(devices)

    # Подключаем уведомления
    home.set_notification_center(notification_center)


    # Получение статуса устройств
    home.status_report()

    # light.set_schedule("18:00")
    # thermostat.set_schedule("18:30")
    # home.check_schedules()


    try:
        while True:
            if not home.check_energy():
                break

            for device in home._SmartHome__device_list:
                device.update_battery()

            # Проверка расписания
            home.check_schedules()

            command = input("Enter command: ")
            if command == "quit":
                break

            parts = command.split()
            if len(parts) < 2:
                print("Invalid command format.")
                continue

            cmd, device_name = parts[0], parts[1]
            param = parts[2] if len(parts) == 3 else None
            home.control_device(cmd, device_name, param)

            time.sleep(1)

    finally:
        home.save_log()


if __name__=="__main__":
    main()