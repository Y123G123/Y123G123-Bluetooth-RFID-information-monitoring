# import bluetooth
#
# # 蓝牙设备的MAC地址（请替换为实际的MAC地址）
# target_device = "4E:6E:46:D6:8E:A0"
#
# # 创建RFCOMM Bluetooth Socket
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
# # 连接设备（假设服务端口为1）
# sock.connect((target_device, 1))
# while True:
#     data = sock.recv(1024)
#     print( "Received : ", data)


# import bluetooth

# # 搜索已连接的设备
# devices = bluetooth.discover_devices(lookup_names=True)

# # 输出所有已连接的设备
# for addr, name in devices:
#     print("Found device:", name, "with address:", addr)


# import bluetooth
#
# # 蓝牙设备的MAC地址（请替换为实际的MAC地址）
# target_device = "4E:6E:46:D6:8E:A0"
#
# # 创建RFCOMM Bluetooth Socket
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
# # 连接设备（假设服务端口为1）
# sock.connect((target_device, 1))
# while True:
#     data = sock.recv(1024)
#     if data:  # 确保接收到数据后再处理
#         # 转换为字符串（如果需要）
#         string_data = data.decode('utf-8') if isinstance(data, bytes) else data
#         print("Received : ", string_data)

# import bluetooth
# import time
#
# # 蓝牙设备的MAC地址（请替换为实际的MAC地址）
# target_device = "00:24:04:00:0A:3D"
#
# while True:
#     try:
#         # 创建RFCOMM Bluetooth Socket
#         sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
#         # 连接设备（假设服务端口为1）
#         sock.connect((target_device, 1))
#         print("Connected to the device")
#
#         start_time = time.time()
#         while time.time() - start_time < 10:
#             try:
#                 data = sock.recv(1024)
#                 if data:  # 确保接收到数据后再处理
#                     # 转换为UTF-8格式的字符串
#                     string_data = data.decode('utf-8')
#                     print(f"Received: {string_data}")
#                 time.sleep(0.1)  # 短暂休眠0.1秒
#             except Exception as e:
#                 print("Error receiving data: ", e)
#                 break  # 在错误情况下跳出内循环重新连接
#     except Exception as e:
#         print("Error connecting to the device: ", e)
#
#     # 关闭现有连接
#     try:
#         sock.close()
#     except Exception as e:
#         print("Error closing the socket: ", e)
#
#     # 确保总间隔时间为10秒
#     elapsed_time = time.time() - start_time
#     if elapsed_time < 10:
#         time.sleep(10 - elapsed_time)
        
# import bluetooth
# import sys
# import time
#
# name = 'JDY-31-SPP'  # 需连接的设备名字
# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print(nearby_devices)  # 附近所有可连的蓝牙设备
#
# addr = None
# for device in nearby_devices:
#     if name == device[1]:
#         addr = device[0]
#         print("Device found!", name, "address is:", addr)
#         break
#
# if addr is None:
#     print("Device not exist")
#     sys.exit(1)
#
# services = bluetooth.find_service(address=addr)
# print(services)
# for svc in services:
#     print("Service Name: %s" % svc["name"])
#     print("    Host:        %s" % svc["host"])
#     print("    Description: %s" % svc["description"])
#     print("    Provided By: %s" % svc["provider"])
#     print("    Protocol:    %s" % svc["protocol"])
#     print("    Channel/PSM: %s" % svc["port"])
#     print("    Svc classes: %s " % svc["service-classes"])
#     print("    Profiles:    %s " % svc["profiles"])
#     print("    Service id:  %s " % svc["service-id"])
#
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
# # 遍历端口号进行连接
# for i in range(255):
#     try:
#         sock.connect((addr, i))
#         print("连接成功，端口：", i)
#         break
#     except Exception as e:
#         print("端口：", i, "连接失败", e)
# else:
#     print("无法连接到设备")
#     sys.exit(1)
#
# def handle_received_data(data):
#     # 转换为十六进制字符串
#     hex_data = ' '.join(f'{byte:02X}' for byte in data)
#     print("Received: ", hex_data)
#
#     # 处理接收到的字符
#     for byte in data:
#         if byte == 0x31:  # '1'
#             print("Card swipe succeeded")
#         elif byte == 0x30:  # '0'
#             print("Card swipe failed")
#         else:
#             print(f"Received unrecognized data: {byte} (character: {chr(byte)})")
#
# try:
#     while True:
#         data = sock.recv(1024)
#         if data:
#             handle_received_data(data)
# except Exception as e:
#     print("Error receiving data: ", e)
# finally:
#     sock.close()
#     print("Socket closed")
import bluetooth
import time
import requests

# 蓝牙设备的MAC地址（请替换为实际的MAC地址）
target_device = "00:24:04:00:0A:3D"
# Django视图的URL（请替换为实际的URL）
django_url = "http://127.0.0.1:8000/save_bluetooth_data/"

while True:
    try:
        # 创建RFCOMM Bluetooth Socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        # 连接设备（假设服务端口为1）
        sock.connect((target_device, 1))
        print("Connected to the device")

        start_time = time.time()
        buffer = ""
        while time.time() - start_time < 10:
            try:
                data = sock.recv(1024)
                if data:  # 确保接收到数据后再处理
                    # 转换为UTF-8格式的字符串并添加到缓冲区
                    string_data = data.decode('utf-8')
                    buffer += string_data
                    print(f"Received: {string_data}")

                    # 检查缓冲区是否包含完整的数据块
                    if "**End Reading**" in buffer:
                        # 提取number
                        number_start = buffer.find("number:") + len("number:")
                        number_end = buffer.find("**End Reading**")
                        number = buffer[number_start:number_end].strip()
                        print(f"Extracted number: {number}")

                        # 如果number不为空，发送到Django视图
                        if number:
                            response = requests.post(django_url, data={'card_number': number})
                            print(f"Response status code: {response.status_code}")
                            print(f"Response content: {response.content.decode()}")
                            if response.status_code == 200:
                                print("Data sent to Django successfully")
                            else:
                                print("Failed to send data to Django")

                        # 清空缓冲区
                        buffer = ""

                time.sleep(0.1)  # 短暂休眠0.1秒
            except Exception as e:
                print("Error receiving data: ", e)
                break  # 在错误情况下跳出内循环重新连接
    except Exception as e:
        print("Error connecting to the device: ", e)

    # 关闭现有连接
    try:
        sock.close()
    except Exception as e:
        print("Error closing the socket: ", e)

    # 确保总间隔时间为10秒
    elapsed_time = time.time() - start_time
    if elapsed_time < 10:
        time.sleep(10 - elapsed_time)

