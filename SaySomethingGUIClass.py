#Attributes and Behaviours
import os
import tkinter as tk 	#tkinter is a module that stores
					 	#buily in funcitions to create
					 	#GUI interfaces.

class Display:

	#Constructor: Is a special method called only once
	#When instantiating (creating) the object for the 1st time
	def __init__(self):

		print("Running display constructor")
		#instance variables in python are self.<variable name>
		self.root = tk.Tk()

		#to add elements we have to construct them then pack them
		self.ent = tk.Entry(self.root)
		self.btn = tk.Button(self.root, text = "Speak", command =self.runMe)

		self.ent.pack()
		self.btn.pack()


		self.root.mainloop()
		print("program end")

	def runMe(self):
		print("Running")
		statement = self.ent.get()
		os.system("say "+ statement)


d = Display() # creates a display object called d. It runs
			  # the constructor
