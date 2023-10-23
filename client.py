import socket
from tkinter import *
import tkinter as tk
from  threading import Thread
import random
from PIL import ImageTk, Image
from tkmacosx import Button
import platform

screen_width = None
screen_height = None
font_size =None

SERVER = None
PORT  = 8080
IP_ADDRESS = '127.0.0.1'
player_name = None

canvas1 = None
canvas2 = None

name_entry = None
name_window = None
gameWindow = None

ticket_grid  = []
current_number_list = []
marked_number_list = []
flash_number_list = []
flash_number_label = None
game_over = False

# Create save_name() function 
def save_name():
    # Access SERVER, player_name, name_window, name_entry as global
    global SERVER, player_name, name_window, name_entry
    
    # Call get() method on name_entry and save it in player_name
    player_name = name_entry.get()
    # Call delete() method on name_entry from 0 to END
    name_entry.delete(0, END)
    # Call destroy() method on name_window
    name_window.destroy()

    # Send player_name to server
    SERVER.send(player_name.encode())

def ask_player_name():
    global player_name, name_entry, name_window, canvas1, font_size

    name_window  = Tk()
    name_window.title("Tambola Family Fun")

    screen_width = name_window.winfo_screenwidth()
    screen_height = name_window.winfo_screenheight()
    font_size = int(screen_width * 0.03)
    
    image = Image.open("./assets/background.png")
    image = image.resize((screen_width, screen_height))
    bg = ImageTk.PhotoImage(image)

    # Make sure canvas is of full screen
    canvas1 = Canvas( name_window, width = screen_width, height = screen_height)
    # canvas1 = Canvas( name_window, width = 600, height = 400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2,screen_height/8, text = "Enter Name", font=("Chalkboard SE",font_size), fill="#3e2723")

    name_entry = Entry(name_window, justify='center', font=('Chalkboard SE', int(font_size/2)), bd=5, bg='white')
    name_entry.place(relx = 0.25, rely=0.3, relwidth = 0.5)

    button = tk.Button(name_window, text="Save", font=("Chalkboard SE", int(font_size/2)),width=11, command=save_name, height=1, bd=3)
    button.place(relx= 0.33, rely=0.5, relwidth = 0.34)

    name_window.resizable(True, True)
    name_window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    ask_player_name()

setup()
