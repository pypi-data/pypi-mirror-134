from .game import Game, GameConfig
from .generic import LoadingWindow
from _thread import start_new_thread
from typing import Callable
import sys
import os
import pygame


def show_loading(state, loading_window):
    while not state["ready"]:
        loading_window.draw()


def run_game(argv):
    # if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    #     os.chdir(sys._MEIPASS)

    os.environ['SDL_VIDEO_WINDOW_POS'] = '60,30'  # y x
    os.environ['SDL_VIDEO_CENTERED'] = '0'

    pygame.init()
    screen_info = pygame.display.Info()

    win_data = {
        "screen_w": screen_info.current_w,
        "screen_h": screen_info.current_h,
        "margin": 60
    }

    conf = GameConfig(argv)

    pygame.font.init()
    pygame.display.set_caption(conf.game_name)
    pygame.mouse.set_visible(False)
    icon_path = os.path.join(conf.resources_dir,
                             "animations",
                             "icon",
                             "icon.png")

    if os.path.isfile(icon_path):
        pygame.display.set_icon(pygame.image.load(icon_path))
    else:
        print("[WARNING] icon file was not found in resources directory at "
              + conf.resources_dir
              + "icon/icon.png. Window icon will be not set")

    loading_win = LoadingWindow(conf.game_name + " - Loading ")

    ready_state = {"ready": False}

    start_new_thread(show_loading, (ready_state, loading_win))

    game = Game(conf, win_data)

    ready_state["ready"] = True

    game.main_loop()

    if __name__ == "__main__":
        run_game(sys.argv[1:])
