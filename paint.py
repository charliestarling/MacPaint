# Demo of my Own Paint app so far...
from client import *
import socket
import pygame
import pyautogui
import time

pygame.init()

# Colours
white = (255, 255, 255)
pink = (242, 172, 185)
grey = (42, 42, 42)
blue = (30, 143, 213)
orange = (252, 143, 50)
red = (244, 54, 76)
green = (0, 168, 107)
yellow = (255, 243, 109)
black = (0, 0, 0)
al_grey = (136, 139, 141)

# Current Colour
current_colour = grey
size = 20
count = 0  # Initialize count

# Window Setup
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Paint')
window.fill(grey)
pygame.display.update()

# Drawing coloured circles for the selection
window_width = window.get_size()[0]
window_height = window.get_size()[1]
size_array = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
colours = [red, green, blue, yellow, white, pink, orange, grey, al_grey, al_grey]

# Sockets
connection = Client(6060, 'Charlies-MacBook-Air.local')  # Initialize connection once

def setup():
    for colour in colours:
        global count  # Indicate count is a global variable
        pygame.draw.circle(window, black, (window_width * size_array[count], window_height * 0.05), 30)
        pygame.draw.circle(window, colour, (window_width * size_array[count], window_height * 0.05), 25)
        count += 1
    pygame.display.update()

# Determining Which Colour has been Selected
coords_to_colour = {
    range(42, 102): red,
    range(186, 246): green,
    range(330, 390): blue,
    range(474, 534): yellow,
    range(618, 678): white,
    range(762, 822): pink,
    range(906, 966): orange,
    range(1050, 1110): grey,
}

def dictionary_read(coords):
    for key, value in coords_to_colour.items():
        if coords in key:
            return value
    return grey  # Return a default color if not found

# Actually Drawing
def draw(coords, current_colour):
    pygame.draw.circle(window, current_colour, (coords), size)
    pygame.display.update()

setup()
error = 1
clock = pygame.time.Clock()

# Running Loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Handle window close event
            connection.sock.close()  # Close socket connection before exiting
            pygame.quit()
            exit()

    # Selecting the colour
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[1] in range(15, 75):
            if pygame.mouse.get_pos()[0] in range(1194, 1254):
                try:
                    pygame.draw.rect(window, current_colour, (0, 75, window_width, (window_height - 75)))
                    pygame.display.update()
                except:
                    error = 5
            elif pygame.mouse.get_pos()[0] in range(1338, 1398):
                connection.send_message('Hello World!')  # Modify this as needed

            try:
                current_colour = dictionary_read(pygame.mouse.get_pos()[0])
            except:
                error = 1
            size = 40 if current_colour == grey else 20  # Set size based on color

        elif pygame.mouse.get_pos()[1] > 115:
            try:
                draw(pygame.mouse.get_pos(), current_colour)
            except:
                error = 2
	
		


