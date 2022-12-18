"""CLass Defines the behavior of the mouse tracker in the screen.
This class paste an image under the user cursor, and it moves the image
relative to the user cursor movement.

    Typical usage:
        mouse_tracker = MouseTracker(image=(image_path))
"""

import pygame


class MouseTracker:
    """Defines the behavior of the mouse screen tracker.

    Methods:
        __init__
        update
    """

    def __init__(self, image_path: str) -> None:
        """Construct the mouse tracker object.

        Args:
            image_path: File path to the image location.
        """
        self._image = pygame.image.load(image_path)

    def update(self, coord: tuple[int, int], surface: pygame.display) -> None:
        """Draws the Mouse Tracker in the screen."""
        image_rect = self._image.get_rect(center=coord)
        surface.blit(self._image, image_rect)
