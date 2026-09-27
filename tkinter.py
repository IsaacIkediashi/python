import math
import tkinter
from tkinter import Frame, Label, Entry, Button
from number_entry import IntEntry




def main():
 window = tkinter.Tk()
 # window.geometry('200x200')
 frm_main = Frame(window)
 frm_main.master.title('Tire Volume')
 frm_main.pack(padx=4, pady=3, fill='none', expand=0)
 populate_main_window(frm_main)
 window.mainloop()
 

def populate_main_window(frm_main):
  width_label = Label(frm_main, text='Width (80 - 300):')
  diam_label = Label(frm_main, text='Diameter (7 - 30):')
  ratio_label = Label(frm_main, text='Aspect Ratio (30 - 90):')
  

  width_label_units = Label(frm_main, text='millimeters')
  diam_label_units = Label(frm_main, text='inches')
  volume_label = Label(frm_main, text='Volume:')

  text_label = Label(frm_main, text='', width=7, anchor='e')
  text_label_units = Label(frm_main, text='liters')
  
  ent_width = IntEntry(frm_main, width=10)  
  ent_diam = IntEntry(frm_main, width=10)
  ent_ratio = IntEntry(frm_main, width=10)
  btn_calc = Button(frm_main, text='calculate')
  btn_clear = Button(frm_main, text='Clear')

  width_label.grid(row=0, column=0, padx=3, pady=3)
  diam_label.grid(row=1, column=0, padx=3, pady=3)
  ratio_label.grid(row=2, column=0, padx=3, pady=3)
  volume_label.grid(row=1, column=3, padx=3, pady=3)
  
  text_label.grid(row=1, column=4, padx=3, pady=3)
  text_label_units.grid(row=1, column=5, padx=3, pady=3)

  ent_width.grid(row=0, column=1, padx=3, pady=3)
  ent_diam.grid(row=1, column=1, padx=3, pady=3)
  ent_ratio.grid(row=2, column=1, padx=3, pady=3)

  
  width_label_units.grid(row=0, column=2, padx=3, pady=3)
  diam_label_units.grid(row=1, column=2, padx=3, pady=3)
  
  btn_calc.grid(row=3,column=2, padx=3, pady=3)
  btn_clear.grid(row=2, column=2, padx=3, pady=3)
  
  def calculate():
   try:
    width = ent_width.get()
    aspect_ratio = ent_ratio.get()
    diameter = ent_diam.get()
    volume = float((math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000)
                                                                                            
    text_label.config(text=f'Volume: {volume:.2f}')
   except ValueError:
    text_label.config(text='')

  def clear():
   btn_clear.focus()
   ent_width.clear()
   ent_ratio.clear()
   ent_diam.clear()
   text_label.config(text='')

   ent_width.focus()

  btn_clear.config(command=clear)
  
  btn_calc.config(command=calculate)
  

  ent_width.focus()
if __name__ == '__main__':
  main()

