"""CLass Defines the behavior of the mouse tracker in the screen.

    Typical usage:
        mouse_tracker = MouseTracker(image=(image_path))
"""

import pygame

#  pylint: disable=locally-disabled, too-few-public-methods
#  pylint: disable=locally-disabled, undefined-variable
class MouseTracker:
    """Defines the behavior of the mouse screen tracker.

    Methods:
        __init__
        update
    """

    def __init__(self, image: filePath) -> None:
        """Construct the mouse tracker object.

        Args:
            image: File path to weathever the image is located.
        """
        self._image = pygame.image.load(image)

    def update(self, coord: tuple[int, int], surface: pygame.display) -> None:
        """Draws the Mouse Tracker in the screen."""
        surface.blit(image, coord)
