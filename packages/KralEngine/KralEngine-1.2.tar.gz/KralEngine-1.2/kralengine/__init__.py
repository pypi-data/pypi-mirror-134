from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
from kralengine.main import KralEngine
from kralengine.actor import Actor
from kralengine.text import Text
from kralengine.input import Input
from kralengine.line import Line
from kralengine.animation import SpriteAnimation, ColorAnimation
from kralengine.types import IMAGE, OBJECT
from kralengine.size import IMAGE_SIZE, SIZE
from kralengine.shapes import RECT, ELLIPSE
from kralengine.utils import ResourceLocation, colorRanger
from kralengine.light import PointLight
from kralengine.collider import BoxCollider