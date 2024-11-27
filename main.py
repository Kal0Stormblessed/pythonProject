import tkinter as tk
from functions import save_and_send_slider_values, open_start_robot_screen, open_settings_screen, open_manual_control_screen, open_automatic_control_screen, go_back, send_test_command, send_store_command, send_repeat_command, send_clear_command
from objects import create_title_label, create_main_buttons, create_start_robot_buttons, create_sliders, create_auto_control_buttons

def on_slider_change(slider, index):
    value = slider.get()
    command = f"{index + 1},{value};"
    print(f"Slider {index + 1} changed to {value}: {command}")  # Debugging print statement

# Create Tkinter window
window = tk.Tk()
window.title("Motor Control")
window.geometry("1600x900")  # Set window size to 1600x900

# Configure window background
window.configure(bg="#add8e6")  # Light blue background

# Main Frame
main_frame = tk.Frame(window, bg="#add8e6")
main_frame.pack()  # Pack the main frame

# Start Robot Frame
start_robot_frame = tk.Frame(window, bg="#add8e6")

# Manual Control Frame
manual_control_frame = tk.Frame(window, bg="#add8e6")

# Automatic Control Frame
automatic_control_frame = tk.Frame(window, bg="#add8e6")

# Routine1 Control Frame
routine1_control_frame = tk.Frame(window, bg="#90ee90")

# Label for title in the main frame
title_label = create_title_label(main_frame)
title_label.pack(pady=50)

# Buttons for main screen
button_start_robot, button_settings, button_exit = create_main_buttons(main_frame,
                                                                      lambda: open_start_robot_screen(main_frame, start_robot_frame),
                                                                      lambda: open_settings_screen(main_frame, main_frame))
button_start_robot.pack(pady=(150, 10))
button_settings.pack(pady=10)
button_exit.pack(pady=10)

# Buttons for start robot screen
button_auto_control, button_manual_control, button_back_start = create_start_robot_buttons(start_robot_frame,
                                                                                            lambda: open_automatic_control_screen(start_robot_frame, automatic_control_frame),
                                                                                            lambda: open_manual_control_screen(start_robot_frame, manual_control_frame),
                                                                                            lambda: go_back(start_robot_frame, manual_control_frame, automatic_control_frame, main_frame))
button_auto_control.pack(pady=(150, 10))
button_manual_control.pack(pady=10)
button_back_start.pack(pady=10)

# Call the function to create the sliders with the updated callback
sliders, sliders_frame = create_sliders(manual_control_frame)
sliders_frame.pack(pady=50)

# Update sliders to call on_slider_change on change
for index, slider in enumerate(sliders):
    slider.configure(command=lambda value, s=slider, i=index: on_slider_change(s, i))

# Add SAVE AND SEND button
save_send_button = tk.Button(manual_control_frame, text="Save and Send", command=lambda: save_and_send_slider_values(sliders))
save_send_button.pack()

# Add new buttons for Test, Store, Repeat, Clear
test_button = tk.Button(manual_control_frame, text="Test", command=send_test_command)
test_button.pack()
store_button = tk.Button(manual_control_frame, text="Store", command=send_store_command)
store_button.pack()
repeat_button = tk.Button(manual_control_frame, text="Repeat", command=send_repeat_command)
repeat_button.pack()
clear_button = tk.Button(manual_control_frame, text="Clear", command=send_clear_command)
clear_button.pack()

# Back button for manual control screen
button_back_manual = tk.Button(manual_control_frame, text="Back", command=lambda: go_back(start_robot_frame, manual_control_frame, automatic_control_frame, main_frame), font=("Arial", 16), bg="white", padx=20, pady=10)
button_back_manual.pack(pady=50)

# Buttons for automatic control screen
button_routines, button_back_auto = create_auto_control_buttons(automatic_control_frame, lambda: go_back(start_robot_frame, manual_control_frame, automatic_control_frame, main_frame))
button_back_auto.grid(row=2, column=1, pady=(10, 150))

# Run the Tkinter event loop
window.mainloop()
