import tkinter as tk
from functions import save_and_send_slider_values, go_back

# Create label for title in the main frame
def create_title_label(main_frame):
    title_label = tk.Label(main_frame, text="Welcome to Robot Control", bg="#add8e6", fg="white", font=("Arial", 24))
    return title_label

# Create buttons for main screen
def create_main_buttons(main_frame, open_start_robot_screen, open_settings_screen):
    button_start_robot = tk.Button(main_frame, text="Start Robot", command=open_start_robot_screen, font=("Arial", 16), bg="white", padx=20, pady=10)
    button_settings = tk.Button(main_frame, text="Settings", command=open_settings_screen, font=("Arial", 16), bg="white", padx=20, pady=10)
    button_exit = tk.Button(main_frame, text="Exit", command=main_frame.master.destroy, font=("Arial", 16), bg="white", padx=20, pady=10)
    return button_start_robot, button_settings, button_exit

# Create buttons for start robot screen
def create_start_robot_buttons(start_robot_frame, open_automatic_control_screen, open_manual_control_screen, go_back):
    button_auto_control = tk.Button(start_robot_frame, text="Automatic Control", command=open_automatic_control_screen, font=("Arial", 16), bg="white", padx=20, pady=10)
    button_manual_control = tk.Button(start_robot_frame, text="Manual Control", command=open_manual_control_screen, font=("Arial", 16), bg="white", padx=20, pady=10)
    button_back_start = tk.Button(start_robot_frame, text="Back", command=go_back, font=("Arial", 16), bg="white", padx=20, pady=10)
    return button_auto_control, button_manual_control, button_back_start

# Create sliders for manual control screen
def create_sliders(manual_control_frame):
    slider_titles = ["Servo1", "Servo2", "Servo3", "Servo4", "Servo5", "Servo6"]
    sliders = []
    sliders_frame = tk.Frame(manual_control_frame, bg="#add8e6")
    for i, title in enumerate(slider_titles):
        slider_label = tk.Label(sliders_frame, text=title, font=("Arial", 12), bg="#add8e6")
        slider_label.grid(row=i % 3, column=(i // 3) * 2, pady=10, padx=20)
        slider = tk.Scale(sliders_frame, from_=0, to=180, orient="horizontal", length=200, bg="light green", bd=2,
                          troughcolor="black", highlightbackground="black", highlightthickness=1, sliderrelief="raised")
        slider.grid(row=i % 3, column=(i // 3) * 2 + 1, pady=10, padx=20)
        sliders.append(slider)
    return sliders, sliders_frame

def create_manual_control_buttons(manual_control_frame, sliders):
    button_save_send = tk.Button(manual_control_frame, text="Save and Send", command=lambda: save_and_send_slider_values(sliders), font=("Arial", 16), bg="white", padx=20, pady=10)
    button_back_manual = tk.Button(manual_control_frame, text="Back", command=go_back, font=("Arial", 16), bg="white", padx=20, pady=10)
    return button_save_send, button_back_manual

# Create buttons for automatic control screen
def create_auto_control_buttons(automatic_control_frame, go_back):
    button_routines = []
    for i in range(1, 5):  # Assuming there are four routines
        button = tk.Button(automatic_control_frame, text=f"Routine {i}", font=("Arial", 12), bg="yellow", fg="black", padx=20, pady=10)
        button.grid(row=(i - 1) // 2, column=(i - 1) % 2, pady=10, padx=20)
        button_routines.append(button)
    button_back_auto = tk.Button(automatic_control_frame, text="Back", command=go_back, font=("Arial", 16), bg="white", padx=20, pady=10)
    return button_routines, button_back_auto
