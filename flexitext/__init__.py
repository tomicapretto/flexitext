from importlib.metadata import version

from .flexitext import FlexiText, flexitext
from .style import Style

__version__ = version("flexitext")

__all__ = ["flexitext", "FlexiText", "Style"]
