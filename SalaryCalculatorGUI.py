"""
1/3/2023  Program: GUItemplate.py

Template code for all GUI-based applications.

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# other imports can go here

class SalaryCalculatorGUI(EasyFrame):

	# defintion of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Salary Calculator", background = "pink")
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "pink", foreground = "blue", font = Font(family = "Arial", size = 100))
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "pink", foreground = "blue")	
		self.hourlyWage = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.addLabel(text = "No. of Hours Worked:", row = 2, column = 0, background = "pink", foreground = "blue")
		self.hoursWorked = self.addIntegerField(value = 0, row = 2, column = 1)
		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.button["background"] = "blue"
		self.button["foreground"] = "pink"
		self.button["width"] = 25
		self.addLabel(text = "The employee's salary is:", row = 4, column = 0, background = "pink", foreground = "blue")
		self.total = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2, state = "readonly")

# definition of the calculate method
	def compute(self):
		# input phase from the GUI
		wage = self.hourlyWage.getNumber()
		worked = self.hoursWorked.getNumber()
		# processing
		result = (wage * worked)
		# output phase back to the GUI
		self.total.setNumber(result)
# definition of the main() method which will establish class objects
def main():
 # instantiate an object from the class into mainloop()
	SalaryCalculatorGUI().mainloop()

# global call to the main() method
main()

