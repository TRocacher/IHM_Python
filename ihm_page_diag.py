import tkinter as tk 


def win_diag_creation(root_win):
	win_diag=tk.Toplevel(root_win)
	win_diag.geometry("800x480+0+0")  # taille en pixels
	win_diag.resizable(width=0, height=0)
	win_diag.title("Diagnostic")
	# --top boutons--
	button_exit = tk.Button(win_diag, text="Back", width=13,
                          height=1 , command=win_diag.destroy)
	button_exit.place(x=5, y=0)
	win_diag.grab_set() 
