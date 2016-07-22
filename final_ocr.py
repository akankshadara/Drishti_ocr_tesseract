#!/usr/bin/env python
import os
import codecs
import csv
import sys
import  Tkinter as tk
from tkFileDialog import askopenfile
from tkFileDialog import asksaveasfilename

input_file = ''
output = ''

def find_unicodes(input_file):
	global output
	file = codecs.open(input_file, "r", "utf-8")
	with open("uni_code.txt", "w") as uni_file:
		for line in file:
			for words in line:
				for characters in words:
					output += characters
					print (characters)	
					print (ord(characters))
					uni_file.write(str(ord(characters)))
					uni_file.write("\n")
	file.close()
	return
	
def compare_csv():
	with open("array_output.txt", "a") as array_file:
		array_file.write('1,')
	with open("uni_code.txt", "r") as text:
		for line in text:
			with open('braille_array_ref.csv', 'r') as file:
				reader = csv.reader(file)
				array = [row[1] for row in reader if row[0].lstrip().rstrip() == line.lstrip().rstrip()]
				string = ','.join(array) 
				print string 
				with open("array_output.txt", "a") as array_file:
					array_file.write(str(string))
					array_file.write(',')
	return
					
def truncate():
	with open("array_output.txt", "a") as array_file:
		array_file.seek(-2, os.SEEK_END)
		#array_file.truncate()
	return




class Application(tk.Frame):
	global input_file

	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid(sticky = tk.N+tk.S+tk.E+tk.W)
		self.createWidgets()
				


	def createWidgets(self):		
		self.grid(padx=2, pady=2)
		self.canvas = tk.Canvas(self, height = 300,width = 460, border = 5, relief = "groove", bg = 'white')
		self.canvas.grid(column = 0, row = 0,  padx = 12, rowspan = 21, columnspan = 14)
		self.canvas.create_text(50, 50, text ="\n\tUpload file..", font = "Pursia, 14", justify = tk.LEFT)

		
		def process_file():
			global input_file
			global output 
			print output
			self.canvas.delete("all")
			if(input_file != ''):
				os.system("echo 'Generating corresponding unicodes for every letter in the devanagari script..'")
				find_unicodes(input_file)
				os.system("echo 'Generating the binary array for every character...'")
				compare_csv()
				truncate()
				# self.canvas.create_text(50, 90, text ="Processing file..", font = "Pursia, 9", justify = tk.LEFT)
				self.canvas.create_text(70, 120, text = output, font = "Pursia, 16", justify = tk.LEFT)
				
			else:
				self.canvas.create_text(50, 90, text ="\t\t\tFile path not selected!", font = "Pursia, 12", justify = tk.LEFT)
			
			


		
		def upload_file():
			global input_file
			image_file = askopenfile(mode ='r').name
			print image_file
			os.system("echo 'running tesseract on terminal'")
			os.system("tesseract %s input_file -l hin" %image_file)
			input_file = "input_file.txt"
			self.canvas.delete("all")
			self.canvas.create_text(50, 90, text ="\t\t\tFile selected", font = "Pursia, 12", justify = tk.LEFT)
			print input_file
			

		top = self.winfo_toplevel()
		top.rowconfigure(0, weight = 1)
		top.columnconfigure(0, weight = 1)
		top = self.winfo_toplevel()
		self.menuBar = tk.Menu(top)
		top['menu'] = self.menuBar
		self.subMenu = tk.Menu(self.menuBar)
		self.subMenu1 = tk.Menu(self.menuBar)
		self.menuBar.add_cascade(label='File', menu=self.subMenu)
		self.subMenu.add_command(label='About')
		self.subMenu.add_command(label = 'Exit', command=self.quit)
		self.menuBar.add_cascade(label='Help', menu=self.subMenu1)		
		

		self.uploadButton = tk.Button(self, foreground = 'blue', border = 3, relief = "groove" , text = 'Upload File')
		self.uploadButton["command"] = upload_file
		self.uploadButton.grid(column = 0, row = 25, padx = 15, pady = 5, rowspan = 3,ipadx = 28, ipady = 5,columnspan = 5)

		self.processButton = tk.Button(self, border = 3, relief = "groove" , text = 'Process OCR', foreground = 'green')
		self.processButton["command"] = process_file
		self.processButton.grid(column = 5, row = 25, rowspan = 3,ipadx = 25, ipady = 5, columnspan = 5)

		self.exitButton = tk.Button(self, foreground = 'red', justify = tk.CENTER, border = 3, relief = "groove",text = 'Exit', command = self.quit)
		self.exitButton.grid(column = 10, row = 25,  padx = 5, pady = 1, rowspan = 3,ipadx = 40, ipady = 5)



app = Application()
app.master.title('Drishti')
app.master.minsize(width=500, height=420)
app.master.maxsize(width=500, height=420)
app.mainloop()
