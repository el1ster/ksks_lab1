import socket


def show_available_commands():
    print("Доступні команди:")
    print("clear display: color")
    print("draw pixel: x0, y0, color")
    print("draw line: x0, y0, x1, y1, color")
    print("draw rectangle: x0, y0, w, h, color")
    print("fill rectangle: x0, y0, w, h, color")
    print("draw ellipse: x0, y0, radius_x, radius_y, color")
    print("fill ellipse: x0, y0, radius_x, radius_y, color")
    print("draw circle: x0, y0, radius, color")
    print("fill circle: x0, y0, radius, color")
    print("draw rounded rectangle: x0, y0, w, h, radius, color")
    print("fill rounded rectangle: x0, y0, w, h, radius, color")
    print("draw text: x0, y0, color, font_number, length, text")
    print("draw image: x0, y0, w, h, data")


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 3306)

    show_available_commands()

    while True:
        user_command = input("Введіть команду: ")

        try:
            client_socket.sendto(user_command.encode('utf-8'), server_address)
        except Exception as e:
            print(f"Помилка відправки команди: {e}")


if __name__ == '__main__':
    main()