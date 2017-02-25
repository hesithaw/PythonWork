#!/usr/bin/python

import sys
import os
import argparse
import Tkinter, tkFileDialog, Tkconstants, tkMessageBox 

top = Tkinter.Tk()
top.title("COPY MAN")
top.geometry("500x300+200+200")

def copy_callback():
	#Code to add copying and resizing will go here...
	tkMessageBox.showinfo( "Copying Completed", "Copied 0 no of items")
	
def source_folder_callback():	
	#defining options for opening a directory
	top.dir_opt = options = {}
	options['initialdir'] = 'C:\\'
	options['mustexist'] = False
	options['parent'] = top
	options['title'] = 'Select Folder Location'
	tkFileDialog.askdirectory(**top.dir_opt)
	
def select_file_callback():
	# define options for opening or saving a file
	top.file_opt = options = {}
	options['defaultextension'] = '.txt'
	options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
	options['initialdir'] = 'C:\\'
	options['initialfile'] = 'imagelist.txt'
	options['parent'] = top
	options['title'] = 'Source File'
	tkFileDialog.askopenfile(mode='r', **top.file_opt)
	
def create_layout():
	# options for buttons
	button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}
	B1 = Tkinter.Button(top, text ="Select Source Folder", command = source_folder_callback)
	B1.pack(**button_opt)
	B2 = Tkinter.Button(top, text ="Select File", command = select_file_callback)
	B2.pack(**button_opt)
	B3 = Tkinter.Button(top, text ="Select Destination Folder", command = source_folder_callback)
	B3.pack(**button_opt)
	b_copy = Tkinter.Button(top, text ="Copy", command = copy_callback)
	b_copy.pack()
	b_quit = Tkinter.Button(top, text="Quit", width=20, command=top.destroy)
	b_quit.pack(side='bottom',padx=0,pady=0)
	
def main():	
	create_layout()
	top.mainloop()
	
if __name__ == "__main__":
    main()    