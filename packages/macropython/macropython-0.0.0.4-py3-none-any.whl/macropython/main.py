import threading
import pynput, time, os
from .classes import _Data
from .mouse_functions import on_mouse_click, on_mouse_move, on_mouse_scroll
from .keyboard_functions import on_keyboard_press, on_keyboard_release
from .misc_functions import save_file, load_file

class Record:
    def __init__(self, filename: str = "My Macro.txt", startup_delay: int = 5):
        if not os.path.exists(filename): self.filename = filename # path to file to save to
        else: raise FileExistsError(f"file '{filename}' already exists")
        self.startup_delay = startup_delay # delay before start recording
        self.macro_data: list[_Data] = []
        self.keyboard_listener = pynput.keyboard.Listener(
            on_press = lambda key: self.logic(on_keyboard_press(key)),
            on_release = lambda key: self.logic(on_keyboard_release(key))
        ) # thread that listens to keyboard inputs

        self.mouse_listener = pynput.mouse.Listener(
            on_click = lambda x, y, button, pressed: self.logic(on_mouse_click(x, y, button, pressed)),
            on_scroll = lambda x, y, dx, dy: self.logic(on_mouse_scroll(x, y, dx, dy)),
            on_move = lambda x, y: self.logic(on_mouse_move(x, y))
        ) # thread that listens to your mouse actions

    def logic(self, stuff: dict | bool):
        if stuff == False:

            try: self.keyboard_listener.stop()
            except: pass

            try: self.mouse_listener.stop()
            except: pass

            return False
        else:
            self.macro_data.append(_Data(**stuff))
            return None

    def start(self, startup_delay: int = None):
        print(f"waiting {self.startup_delay} before recording")
        time.sleep(self.startup_delay or startup_delay) # wait startup_delay before recording
        print(f"recording started. press Escape key to exit")

        start_time = time.time()

        self.keyboard_listener.start()
        self.mouse_listener.start()
        self.keyboard_listener.join()
        self.mouse_listener.join()

        if self.macro_data == []:
            print("No Data To Save")

        else:
            _save_data = [d._to_dict() for d in self.macro_data]

            for i in range(len(_save_data)):
                _d = _save_data[i]
                _save_data[i]['time'] = _d['time'] - start_time

            print(f"Saving {len(_save_data)} Inputs")
            save_file(self.filename, _save_data)
            print(f"Saved {len(_save_data)} Inputs")

class Play:
    def __init__(self, filename: str = "My Macro.txt", startup_delay: int = 5):
        if os.path.exists(filename): self.filename = filename # path to file to save to
        else: raise FileNotFoundError(f"file '{filename}' does not exist")

        self.startup_delay = startup_delay # delay before start recording

    def start(self, startup_delay: int = None):
        special_keys = {'Key.' + key: eval(f"pynput.keyboard.Key.{key}") for key in dir(pynput.keyboard.Key)}

        print(f"waiting {self.startup_delay} before playing macro '{self.filename}'")
        time.sleep(startup_delay or self.startup_delay)
        print(f"playing macro '{self.filename}'")

        _macro_data: list[_Data] = [_Data(**_l) for _l in load_file(self.filename)]
        self.keyboard_controller = pynput.keyboard.Controller()
        self.mouse_controller = pynput.mouse.Controller()
        _current = None
        _future = None
        _before = None
        action_len = len(_macro_data)-1

        for i in range(len(_macro_data)):

            _current: _Data = _macro_data[i]
            if not i == 0: _before = _macro_data[i-1]
            if not i == action_len: _future = _macro_data[i+1]

            if _current.action in ["mouse_scroll", "mouse_move", "mouse_press", "mouse_release"]:
                if _current.action in ["mouse_press", "mouse_release"]:
                    button = pynput.mouse.Button.left if _current.button == "Button.left" else pynput.mouse.Button.right

                if _current.action == "mouse_press":
                    self.mouse_controller.press(button)
                elif _current.action == "mouse_release":
                    self.mouse_controller.release(button)
                elif _current.action == "mouse_scroll":
                    self.mouse_controller.scroll(_current.dx, _current.dy)
                elif _current.action == "mouse_move":
                    self.mouse_controller.position  = (_current.x, _current.y)
                
            if _current.action in ["release_key", "press_key"]:
                key = _current.key if 'Key.' not in _current.key else special_keys[_current.key]
                if _current.action == "press_key":
                    self.keyboard_controller.press(key)
                elif _current.action == "release_key":
                    self.keyboard_controller.release(key)
            
            if not _future == None:
                time.sleep(_future.time - _current.time)

class GetKeyInput:
    def __init__(self, startup_delay: int = 5):
        self.startup_delay = startup_delay
        self.input_key = None
        self.keyboard_listener = pynput.keyboard.Listener(
            on_press = lambda key: self.logic(on_keyboard_press(key)),
            on_release = lambda key: self.logic(on_keyboard_release(key))
        ) # thread that listens to keyboard inputs
    
    def start(self, startup_delay: int = None):
        wait_time = startup_delay or self.startup_delay

        print(f"waiting {wait_time} before recording input")
        time.sleep(wait_time)
        print(f"recording started. press a key to capture it. press Escape to cancel")

        self.keyboard_listener.start()
        self.keyboard_listener.join()
        if not self.input_key == None: return self.input_key
    
    def logic(self, key: dict | bool):
        if key == False:
            try: self.keyboard_listener.stop()
            except: pass

            print("input canceled")
            return False
        else:
            self.input_key = key['key']

            try: self.keyboard_listener.stop()
            except: pass

            return False

class HotKeyMacro:
    def __init__(self, activate: str = "Key.space", macro_file: str = "My Macro.txt", repeat_forever: bool = False, repeat_delay: int = 2, startup_delay: int = 5):
        self.activate_key = activate
        if not os.path.isfile:
            raise FileNotFoundError(f"file '{macro_file}' not found")
        self.macro_file = macro_file
        self.repeat_forever = repeat_forever
        self.repeat_delay = repeat_delay
        self.startup_delay = startup_delay
        self.stop = False
        self.play = False
        self.keyboard_listener = pynput.keyboard.Listener(
            on_press = lambda key: self.logic(on_keyboard_press(key)),
            on_release = lambda key: self.logic(on_keyboard_release(key))
        ) # thread that listens to keyboard inputs
        self.keyboard_controller = None
        self.mouse_controller = None

        self.special_keys = {'Key.' + key: eval(f"pynput.keyboard.Key.{key}") for key in dir(pynput.keyboard.Key)}

    def logic(self, key: dict | bool):
        if key == False:
            self.stop = True
            self.play = False
            try: self.keyboard_listener.stop()
            except: pass
        else:
            print(key['key'] == self.activate_key, f'{key["key"]}', f'{self.activate_key}', f"self.play: {self.play}")
            if key['action'] == "press_key":
                if key['key'] == self.activate_key:
                    self.play = True
            elif key['action'] == "release_key":
                if key['key'] == self.activate_key:
                    self.play = False

    def _play_logic(self):
        _macro_data = [_Data(**entry) for entry in load_file(self.macro_file)]
        action_len = len(_macro_data)-1

        self.mouse_controller = pynput.mouse.Controller()
        self.keyboard_controller = pynput.keyboard.Controller()

        while True:
            if self.stop: return

            if self.play:
                if self.repeat_forever:
                    while True:
                        if self.stop: return

                        if self.play:
                            self._play(_macro_data, action_len)
                else:
                    self._play(_macro_data, action_len)

    def _play(self, _macro_data: list, action_len: int,):
        if self.play:
            if self.stop: return
            _current = None
            _future = None
            _before = None
            for i in range(len(_macro_data)):
                if self.stop: return
                if self.play:
                    _current: _Data = _macro_data[i]
                    if not i == 0: _before = _macro_data[i-1]
                    if not i == action_len: _future = _macro_data[i+1]

                    if _current.action in ["mouse_scroll", "mouse_move", "mouse_press", "mouse_release"]:
                        if _current.action in ["mouse_press", "mouse_release"]:
                            button = pynput.mouse.Button.left if _current.button == "Button.left" else pynput.mouse.Button.right

                        if _current.action == "mouse_press":
                            self.mouse_controller.press(button)
                        elif _current.action == "mouse_release":
                            self.mouse_controller.release(button)
                        elif _current.action == "mouse_scroll":
                            self.mouse_controller.scroll(_current.dx, _current.dy)
                        elif _current.action == "mouse_move":
                            self.mouse_controller.position  = (_current.x, _current.y)
                        
                    if _current.action in ["release_key", "press_key"]:
                        key = _current.key if 'Key.' not in _current.key else self.special_keys[_current.key]
                        if _current.action == "press_key":
                            self.keyboard_controller.press(key)
                        elif _current.action == "release_key":
                            self.keyboard_controller.release(key)
                    
                    if not _future == None:
                        if self.stop: return
                        if self.play:
                            time.sleep(_future.time - _current.time)

    def start(self, startup_delay: int = None):
        wait_time = startup_delay or self.startup_delay
        print(f"waiting {wait_time} before starting hotkey macro")
        time.sleep(wait_time)
        print(f"hotkey macro starting. hold '{self.activate_key}' to start hotkey")

        macro_thread = threading.Thread(target = self._play_logic, daemon = True)

        macro_thread.start()
        self.keyboard_listener.start()

        self.keyboard_listener.join()