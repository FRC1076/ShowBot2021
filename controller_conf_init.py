from wpilib.interfaces import GenericHID

CONTROLLER_PORT = 0
my_controller = GenericHID(CONTROLLER_PORT)


def get_pressed_button_num(controller):
    while True:
        for i in range(1, controller.getButtonCount() + 1):
            if controller.getRawButton(i):
                print(f"Button {i} pressed")
                return i


def get_held_axis_num(controller):
    while True:
        for i in range(controller.getAxisCount()):
            if controller.getRawAxis(i) > 0.9:
                print(f"Axis {i} pressed")
                return i


def find_mapping(controller) -> dict:
    controller_map = {}
    print("Hold down the left trigger")
    controller_map['left trigger axis'] = get_held_axis_num(controller)
    print("Hold down the right trigger")
    controller_map['right trigger axis'] = get_held_axis_num(controller)
    print("Press the a button")
    controller_map['a button num'] = get_pressed_button_num(controller)
    print("Press the b button")
    controller_map['b button num'] = get_pressed_button_num(controller)
    print("Press the y button")
    controller_map['y button num'] = get_pressed_button_num(controller)
    print("Press the x button")
    controller_map['x button num'] = get_pressed_button_num(controller)

    return controller_map


def write_config(controller_map):
    conf_string = ""
    conf_string += f"LEFT_TRIGGER_AXIS = {controller_map['left trigger axis']}\n"
    conf_string += f"RIGHT_TRIGGER_AXIS = {controller_map['right trigger axis']}\n"
    conf_string += f"A_BUTTON_NUM = {controller_map['a button num']}\n"
    conf_string += f"B_BUTTON_NUM = {controller_map['b button num']}\n"
    conf_string += f"Y_BUTTON_NUM = {controller_map['y button num']}\n"
    conf_string += f"X_BUTTON_NUM = {controller_map['x button num']}\n"

    with open('controller_conf_init.py', 'w') as file:
        file.write(conf_string)


if __name__ == "__main__":
    mappings = find_mapping(my_controller)
    print(mappings)
    if input("Do you want to write this mapping into controller_conf.py? [y/n]") == 'y':
        write_config(mappings)
    else:
        print("ok")
