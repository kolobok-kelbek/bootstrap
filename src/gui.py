import os
import time


class Keys:
    ESC = 27


class Cursor:
    @staticmethod
    def on() -> None:
        os.system('setterm -cursor on')

    @staticmethod
    def off() -> None:
        os.system('setterm -cursor off')


class Terminal:
    @staticmethod
    def clear() -> None:
        print("\033[H\033[J")


class Text:
    BLUE = '\033[96m'

    @staticmethod
    def print(text: str, color: str) -> str:
        return ("{start_color}" + text + "{end_color}").format(start_color=color, end_color='\033[0m')


class Menu:
    @staticmethod
    def start() -> None:
        Cursor.off()
        Terminal.clear()

        TARGET_FPS = 60
        CONST = 1_000_000_000
        OPTIMAL_TIME = CONST / TARGET_FPS

        while True:
            last_loop_time = time.time()

            try:
                time.sleep((last_loop_time - time.time() + OPTIMAL_TIME) / CONST)
            except RuntimeError:
                print("error")