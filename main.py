import pygame, sys
from model import Model
from controller import Controller
from view import View

#makes a view, a controller and starts game
v = View()
c = Controller(v)
c.startGame()       