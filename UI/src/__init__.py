"""Export menu classes.

See prediction_window.py, about_window.py, change_button_color.py,
configuration.py and screen_satate.py for details.
"""

from .menu import MainMenu
from .prediction_window import PredictionWindow
from .about_window import AboutWindow
from .change_button_color import change_buttons_color
from .configurations import RESOLUTION
from .screen_state import CURRENT_STATE
from .run import execute

__all__ = (
    "MainMenu",
    "PredictionWindow",
    "AboutWindow",
    "change_buttons_color",
    "RESOLUTION",
    "CURRENT_STATE",
    "execute"
)
