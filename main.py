from evdev import InputDevice, categorize, ecodes, uinput

dev = InputDevice('/dev/input/by-id/usb-Logitech_USB_Keyboard-event-kbd')
dev.grab()

print("script started")

mapping = {
    "KEY_F1": ["KEY_F13"],
    "KEY_F2": ["KEY_F14"],
    "KEY_F3": ["KEY_F15"],
    "KEY_F4": ["KEY_F16"],
    "KEY_F5": ["KEY_F17"],
    "KEY_F6": ["KEY_F18"],
    "KEY_F7": ["KEY_F19"],
    "KEY_F8": ["KEY_F20"],
    "KEY_F9": ["KEY_F21"],
    "KEY_F10": ["KEY_F22"],
    "KEY_F11": ["KEY_F23"],
    "KEY_F12": ["KEY_F24"],
    "KEY_1": ["KEY_LEFTSHIFT", "KEY_F13"],
    "KEY_2": ["KEY_LEFTSHIFT", "KEY_F14"],
    "KEY_3": ["KEY_LEFTSHIFT", "KEY_F15"],
    "KEY_4": ["KEY_LEFTSHIFT", "KEY_F16"],
    "KEY_5": ["KEY_LEFTSHIFT", "KEY_F17"],
    "KEY_6": ["KEY_LEFTSHIFT", "KEY_F18"],
    "KEY_7": ["KEY_LEFTSHIFT", "KEY_F19"],
    "KEY_8": ["KEY_LEFTSHIFT", "KEY_F20"],
    "KEY_9": ["KEY_LEFTSHIFT", "KEY_F21"],
    "KEY_0": ["KEY_LEFTSHIFT", "KEY_F22"],
    "KEY_MINUS": ["KEY_LEFTSHIFT", "KEY_F23"],
    "KEY_EQUAL": ["KEY_LEFTSHIFT", "KEY_F24"],
    "KEY_Q": ["KEY_LEFTCTRL", "KEY_F13"],
    "KEY_W": ["KEY_LEFTCTRL", "KEY_F14"],
    "KEY_E": ["KEY_LEFTCTRL", "KEY_F15"],
    "KEY_R": ["KEY_LEFTCTRL", "KEY_F16"],
    "KEY_T": ["KEY_LEFTCTRL", "KEY_F17"],
    "KEY_Y": ["KEY_LEFTCTRL", "KEY_F18"],
    "KEY_U": ["KEY_LEFTCTRL", "KEY_F19"],
    "KEY_I": ["KEY_LEFTCTRL", "KEY_F20"],
    "KEY_O": ["KEY_LEFTCTRL", "KEY_F21"],
    "KEY_P": ["KEY_LEFTCTRL", "KEY_F22"],
    "KEY_LEFTBRACE": ["KEY_LEFTCTRL", "KEY_F23"],
    "KEY_RIGHTBRACE": ["KEY_LEFTCTRL", "KEY_F24"],
    "KEY_A": ["KEY_LEFTALT", "KEY_F13"],
    "KEY_S": ["KEY_LEFTALT", "KEY_F14"],
    "KEY_D": ["KEY_LEFTALT", "KEY_F15"],
    "KEY_F": ["KEY_LEFTALT", "KEY_F16"],
    "KEY_G": ["KEY_LEFTALT", "KEY_F17"],
    "KEY_H": ["KEY_LEFTALT", "KEY_F18"],
    "KEY_J": ["KEY_LEFTALT", "KEY_F19"],
    "KEY_K": ["KEY_LEFTALT", "KEY_F20"],
    "KEY_L": ["KEY_LEFTALT", "KEY_F21"],
    "KEY_SEMICOLON": ["KEY_LEFTALT", "KEY_F22"],
    "KEY_APOSTROPHE": ["KEY_LEFTALT", "KEY_F23"],
    "KEY_GRAVE": ["KEY_LEFTALT", "KEY_F24"],
    "KEY_Z": ["KEY_LEFTMETA", "KEY_F13"],
    "KEY_X": ["KEY_LEFTMETA", "KEY_F14"],
    "KEY_C": ["KEY_LEFTMETA", "KEY_F15"],
    "KEY_V": ["KEY_LEFTMETA", "KEY_F16"],
    "KEY_B": ["KEY_LEFTMETA", "KEY_F17"],
    "KEY_N": ["KEY_LEFTMETA", "KEY_F18"],
    "KEY_M": ["KEY_LEFTMETA", "KEY_F19"],
    "KEY_COMMA": ["KEY_LEFTMETA", "KEY_F20"],
    "KEY_DOT": ["KEY_LEFTMETA", "KEY_F21"],
    "KEY_SLASH": ["KEY_LEFTMETA", "KEY_F22"],
    "KEY_BACKSLASH": ["KEY_LEFTMETA", "KEY_F23"],
    "KEY_SPACE": ["KEY_LEFTMETA", "KEY_F24"],
}

with uinput.UInput() as ui:
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            key = categorize(event)
            print(key)
            if key.keycode in mapping:

                macro = mapping[key.keycode]
                for k in macro:
                    ui.write(ecodes.EV_KEY, ecodes.ecodes[k], key.keystate)
                ui.syn()
