import serial
import time

# Specify the correct COM port
COM_PORT = "COM3"  # Change this if needed

# Create serial connection
try:
    hc05_serial = serial.Serial(COM_PORT, 9600, timeout=2)
    print(f"Connected to {COM_PORT}")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

def send_command(command):
    try:
        if hc05_serial.is_open:
            print(f"Sending command to Arduino: {command}")
            hc05_serial.write(command.encode())
            time.sleep(0.2)  # Small delay to allow Arduino to process
        else:
            print("Serial port is not open")
    except Exception as e:
        print(f"Error sending command: {e}")

def switch_screen(from_frame, to_frame):
    from_frame.pack_forget()
    to_frame.pack()

def go_back(start_robot_frame, manual_control_frame, automatic_control_frame, main_frame):
    start_robot_frame.pack_forget()
    manual_control_frame.pack_forget()
    automatic_control_frame.pack_forget()
    main_frame.pack()

def open_start_robot_screen(main_frame, start_robot_frame):
    switch_screen(main_frame, start_robot_frame)

def open_settings_screen(main_frame, settings_frame):
    switch_screen(main_frame, settings_frame)

def open_manual_control_screen(start_robot_frame, manual_control_frame):
    switch_screen(start_robot_frame, manual_control_frame)

def open_automatic_control_screen(start_robot_frame, automatic_control_frame):
    switch_screen(start_robot_frame, automatic_control_frame)

def save_and_send_slider_values(sliders):
    commands = [f"{i+1},{slider.get()};" for i, slider in enumerate(sliders)]
    command_string = "@" + "".join(commands).strip() + "#"
    send_command(command_string)

def send_test_command():
    send_command("@T#")

def send_store_command():
    send_command("@S#")

def send_repeat_command():
    send_command("@R#")

def send_clear_command():
    send_command("@C#")

import atexit
atexit.register(lambda: hc05_serial.close() if hc05_serial.is_open else None)
