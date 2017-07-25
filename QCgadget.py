#!/usr/bin/python

##################################################
#
# Import necessary modules
#
##################################################

#from ImageTk import PhotoImage
from CommConvert import *
from ChemFormular import *
from tkMessageBox import *
from Tkinter import *
import webbrowser

class ConvertPanelV1(LabelFrame):
      def __init__(self, parent = None):
          LabelFrame.__init__(self, parent)
	  self.config(text = 'UNIT CONVERT',font = ('times', 15))
	  self.pack()
          #
	  column1 = Frame(self)
	  column1.pack(side = LEFT)
	  column2 = Frame(self)
	  column2.pack(side = RIGHT)	  
	  #
	  # Energy converter
	  converter = {
	      'Hartree':       1.0000,
	      'eV':           27.2113961,
	      'kcal/mol':    627.5096,
	      'kJ/mol':     2625.500,
	      'cm-1':     219474.63067
	  }
	  CommConvert(converter, 'ENERGY', column1).pack(side = TOP)
	  #
	  # Length converter
	  converter = {
	      'Angstrom': 0.529177249,
	      'Bohr':     1.0000
	  }
	  CommConvert(converter, 'LENGTH', column1).pack(side = TOP)
	  #
	  # Time converter
	  converter = {
	      '10^-17 s': 2.41889,
	      'a.u.':     1.0000
	  }
	  CommConvert(converter, 'TIME', column1).pack(side = TOP)
	  #
	  # Velocity converter
	  converter = {
	      'm/s':  2187686.289992517,
	      'a.u.':       1.0000
	  }
	  CommConvert(converter, 'VELOCITY', column1).pack(side = TOP)
	  #
	  # Force constant
	  converter = {
	      'N/m':  1556.86,
	      'a.u.':    1.0000
	  }
	  CommConvert(converter, 'FORCE CONSTANT', column1).pack(side = TOP)
	  #
	  # Charge converter
	  converter = {
	      '10^-19 SI e': 1.602188,
	      'a.u.':        1.0000
	  }
	  CommConvert(converter, 'CHARGE', column2).pack(side = TOP)
          #
	  # Dipole converter
	  converter = {
	      'Debye':      2.541765,
	      '10^-30 C*m': 8.4784,
	      'a.u.':       1.0000
	  }
	  CommConvert(converter, 'DIPOLE MOMENT', column2).pack(side = TOP)
          #
	  # Electric field strength
	  converter = {
	      'V/Angstrom': 51.422,
	      'a.u.':        1.0000
	  }
	  CommConvert(converter, 'ELECTRIC FIELD STRENGTH', column2).pack(side = TOP)
          #
	  # Magnetic flux density
	  converter = {
	      'Tesla': 235060,
	      'Gauss':     23.506,
	      'a.u.':       1.0000
	  }
	  CommConvert(converter, 'MAGNETIC FLUX DENSITY', column2).pack(side = TOP)
          #
	  # Magnetic dipole moment
	  converter = {
	      '10^-23 J/T':    1.8546,
	      '10^23\nBohr magneton': 0.9273,
	      'a.u.':          1.0000
	  }
	  CommConvert(converter, 'MAGNETIC DIPOLE MOMENT', column2).pack(side = TOP)


class ChemFormularV1(LabelFrame):
      def __init__(self, parent = None):
          LabelFrame.__init__(self, parent)
	  self.config(text = 'MOLECULAR INFORMATION',font = ('times', 15))
	  self.pack()
	  self.reportent = 0 
	  self.drawgadget()
      def drawgadget(self):
          #
	  # Draw labels and entries
	  Label(self, text = 'Please enter the chemical formular here.\nExample: Ba, CuSO4(H2O)5, PdH0.7 etc. ', font = ('times', 12)).pack(side = TOP)
	  ent = Entry(self, width = 30, font = ('times', 12))
	  ent.pack(side = TOP)	 
	  ent.bind('<Return>', self.crack)
	  Button(self, text = 'Copy the information to the clipboard', command = self.cpy).pack(side = TOP)
	  #
	  # Draw report
	  sbar = Scrollbar(self)
	  reportent = Text(self, relief = SUNKEN)
	  sbar.config(command = reportent.yview)
	  reportent.config(yscrollcommand = sbar.set)
	  sbar.pack(side = RIGHT, fill = Y)
	  reportent.pack(side = LEFT,  fill = BOTH)
	  self.reportent = reportent	  
      def cpy(self):
          string =  self.reportent.get('1.0', END)
	  self.clipboard_clear()
	  self.clipboard_append(string)
      def crack(self, event):
          string =  event.widget.get()
	  (mass, charge, component) = CrackFormular(string)
	  if mass == NOELEMENT:
	     showerror('QCgadget', 'Element %s is undefined.' % charge)
	  elif mass == INVALIDFORMULAR:
	     showerror('QCgadget', 'The chemical formular is invalid.')
	  else:   
	     report = ''
	     report += 'Molecular: %s \n' % string 
	     report += 'Molecular Weight: %.5f\n' % float(mass)
	     report += 'Total Charge: %.1f\n' % float(charge)
	     report += '\n'
	     report += 'Information on each element:\n' 
	     report += 'Radius in pm, and the covalent radius shown is for single bond.\n'
	     for em in component:
	         report += '\nElement: %5s\n' % em
		 report += ' %17s: %-10s\n' % ('Charge', str(component[em][ICHARGE]))
		 report += ' %17s: %-10s\n' % ('Electronegativity', str(component[em][IKAI]))
		 
		 report += ' %17s: %-10s\n' % ('Atomic radius', str(component[em][IATMR]))
		 report += ' %17s: %-10s\n' % ('Covalent radius', str(component[em][ICOVR]))
		 report += ' %17s: %10s\n' % ('Ionic radius', str(component[em][IIONR]))
	     report += '\n'
	     self.reportent.delete('1.0', END)
	     self.reportent.insert('1.0', report)

class AboutQCgadget(Frame):
      def __init__(self, parent = None):
          Frame.__init__(self, parent)
	  try:
	      img = PhotoImage(file = './logo.gif')
	  except:
	      img = None
	  
	  if img != None:	      
  	     pic = Label(self, image = img)
	     pic.image = img
	     pic.pack(side = LEFT)
	  else:
  	     pic = Label(self, text = '\"Logo.gif\" lost?   :P', font = ('times', 15, 'underline'))
	     pic.pack(side = LEFT)
	     


	  info = 'QCgadget Version 0.01\n\n'
	  info += 'Author: Zhang Jun, Nankai University\n\n'
	  info += 'This is a gift for those computational chemists like me who are boiling night oils for cracking their data.\n\n'	  
	  info += 'If you have any ideas, please feel free to contact me!\n'
	  info += 'mailto: zhangjunqcc@gmail.com'
	  Message(self, text = info, width = 500, font = ('times', 15, 'italic')).pack(side = TOP)
	  info = '... And since the atoms never reach the light,\n   They must be colorless ...\n\n         by Lucretius, \"The way things are\"'
	  Message(self, text = info, width = 500, font = ('times', 15, 'italic'), fg = 'red').pack(side = TOP)



	  

class QCgadgetMain(Frame):
      def __init__(self, parent = None):
          Frame.__init__(self, parent)
	  self.pack()
	  self.drawgadget()
      def drawgadget(self):
	  Button(self, text = 'About QCgadget', font = ('times', 12, 'bold'), command = self.showabout).pack()
          Button(self, text = 'More...', font = ('times', 12, 'bold'), command = self.openmore).pack()
	  Label(self, text = 'Press ENTER in the entry to get what you need!', font = ('times', 15, 'italic')).pack()
	  ConvertPanelV1(self).pack(side = LEFT)
          ChemFormularV1(self).pack(side = LEFT)
      def openmore(self):
          webbrowser.open("http://www.zhjun-sci.com/")
      def showabout(self):
          win = Toplevel()
	  AboutQCgadget(win).pack()
	  #
	  # Make a modal window
          win.focus_set()
          win.grab_set()
	  win.wait_window()
	 	  
          
if __name__ == '__main__': 
   
   root = Tk()
   root.title('QCgadget V0.01')
   QCgadgetMain(root).pack()
   print root.size()
   root.mainloop()




