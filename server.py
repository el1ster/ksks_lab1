import socket


def parse_command(command_bytes):
    try:
        command_str = command_bytes.decode('utf-8')
        parts = command_str.split(':')
        if len(parts) == 2:
            command_name = parts[0].strip()
            parameters = parts[1].strip().split(',')
            return (command_name, parameters)
    except Exception as e:
        print(f"Помилка розбору команди: {e}")
    return None


def process_command(command):
    command_name, parameters = command
    if command_name == "clear display":
        if len(parameters) == 1:
            color = parameters[0].strip()
            print(f"Виконано команду: {command_name}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw pixel":
        if len(parameters) == 3:
            x0, y0, color = map(str.strip, parameters)
            print(f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw line":
        if len(parameters) == 5:
            x0, y0, x1, y1, color = map(str.strip, parameters)
            print(f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, x1: {x1}, y1: {y1}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw rectangle":
        if len(parameters) == 5:
            x0, y0, w, h, color = map(str.strip, parameters)
            print(f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, w: {w}, h: {h}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "fill rectangle":
        if len(parameters) == 5:
            x0, y0, w, h, color = map(str.strip, parameters)
            print(f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, w: {w}, h: {h}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw ellipse":
        if len(parameters) == 5:
            x0, y0, radius_x, radius_y, color = map(str.strip, parameters)
            print(
                f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, radius_x: {radius_x}, radius_y: {radius_y}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "fill ellipse":
        if len(parameters) == 5:
            x0, y0, radius_x, radius_y, color = map(str.strip, parameters)
            print(
                f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, radius_x: {radius_x}, radius_y: {radius_y}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw circle":
        if len(parameters) == 4:
            x0, y0, radius, color = map(str.strip, parameters)
            print(f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, radius: {radius}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "fill circle":
        if len(parameters) == 4:
            x0, y0, radius, color = map(str.strip, parameters)
            print(f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, radius: {radius}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw rounded rectangle":
        if len(parameters) == 6:
            x0, y0, w, h, radius, color = map(str.strip, parameters)
            print(
                f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, w: {w}, h: {h}, radius: {radius}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "fill rounded rectangle":
        if len(parameters) == 6:
            x0, y0, w, h, radius, color = map(str.strip, parameters)
            print(
                f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, w: {w}, h: {h}, radius: {radius}, color: {color}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw text":
        if len(parameters) == 6:
            x0, y0, color, font_number, length, text = map(str.strip, parameters)
            print(
                f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, color: {color}, font_number: {font_number}, length: {length}, text: {text}")
        else:
            print("Помилка: невірна кількість параметрів")
    elif command_name == "draw image":
        if len(parameters) == 4:
            x0, y0, w, h = map(str.strip, parameters[:4])
            data = parameters[4]
            data_length = int(w) * int(h) * 4  # assuming color is represented with 4 bytes (e.g., RGBA)
            if len(data) == data_length:
                print(
                    f"Виконано команду: {command_name}, x0: {x0}, y0: {y0}, w: {w}, h: {h}, data_length: {data_length}")
            else:
                print("Помилка: невірна довжина даних")
        else:
            print("Помилка: невірна кількість параметрів")
    else:
        print(f"Невідома команда: {command_name}")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print("Сервер запущено")

    while True:
        data, client_address = server_socket.recvfrom(1024)

        command = parse_command(data)
        if command is not None:
            process_command(command)
        else:
            print("Помилка розбору команди")


if __name__ == '__main__':
    main()