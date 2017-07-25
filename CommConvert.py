#!/usr/bin/python

from Tkinter import *
from tkMessageBox import *
from math import *
#
# This module constructs the common unit convert class
# 
class CommConvert(LabelFrame):
      def __init__(self, tconverter, description, parent = None):
          LabelFrame.__init__(self, parent)
	  self.config(text = description, font = ('times', 12))
	  self.entries = {}
	  self.converter = tconverter
	  self.makegadget()
	  self.pack(padx = 5, pady = 5)
	  #
	  # The threshold to determine which format to use
	  self.threshold = 1.0E-05
      def makegadget(self):
          for unit in self.converter.keys():
	      row = Frame(self)
	      row.config(padx = 5, pady = 2)
	      row.pack(side = TOP)
	      lb = Label(row, width = 15, text = unit)
	      lb.pack(side = LEFT)
	      ent = Entry(row)
	      ent.bind('<Return>', self.actrefresh)
	      ent.pack(side = RIGHT) 
	      self.entries[unit] = ent
      def actrefresh(self, event):          
	  for (unit, ent) in self.entries.items():
	      if (event.widget == ent): 
	         try:
		     tvalue = float(ent.get())
		 except ValueError:
		     showerror('QCgadget', 'The string in the entry is not a number.') 
		     return None     
	         tscale = self.converter[unit]
          for (unit, factor) in self.converter.items():
	      self.converter[unit] /= tscale
	  for (unit, ent) in self.entries.items():	     
	      result = tvalue*self.converter[unit]
	      ent.delete(0, END)
	      if abs(result) > self.threshold:
	         ent.insert(0, '%.7f' % result)
	      else:	 
	         ent.insert(0, '%.7e' % result)
          for (unit, factor) in self.converter.items():
	      self.converter[unit] *= tscale

