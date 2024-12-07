import tkinter as tk 
from Serial_Interface import diag_SerData
from IHM_Global import *

    

def win_diag_creation(root_win,DiagToPrint):
	win_diag=tk.Toplevel(root_win)
	win_diag.geometry("800x480+0+0")  # taille en pixels
	win_diag.resizable(width=0, height=0)
	win_diag.title("Diagnostic")
	# --top boutons--
	button_exit = tk.Button(win_diag, text="Back", width=13,
                          height=1 , command=win_diag.destroy)
	button_exit.place(x=5, y=0)
	win_diag.grab_set() 
	diag_SerData.ask_diag_to_SGw()
	
	#frame principale
	frame_main = tk.Frame(win_diag, width=600, height=300, borderwidth=3,relief='groove',bg=COLOUR_FRAME)
	frame_main.place(x=50, y=50)

	Label_main=tk.Label(frame_main, text=DiagToPrint, bg=COLOUR_FRAME)
	Label_main.place(x=10, y=20)
	#Label_main.config(text=Data_Diag.StackFct)
