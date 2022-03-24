#Chapter 13 HW


import tkinter
import tkinter.messagebox



class PizzaOrder:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("700x200")
        self.main_window.title("Pizza Order")
        self.main_window.configure(bg ="Pink")

        self.name_frame = tkinter.Frame(self.main_window,bg = "Pink")
        self.middle_frame = tkinter.Frame(self.main_window,bg = "Pink")
        self.bottom_frame = tkinter.Frame(self.main_window,bg = "Pink")


        self.Name_Label = tkinter.Label(self.name_frame, text = "Enter Customer's Name: ", bg = "Purple", fg = "White", font = ("Comic Sans", 14))
        self.Toppings_Label = tkinter.Label(self.middle_frame,text = "Toppings: ", bg= "Purple", fg = "White", font = ("Comic Sans", 14))
        self.Crust_Label = tkinter.Label(self.bottom_frame,text = "Crust: ", bg= "Purple", fg = "White", font = ("Comic Sans", 14))
        self.Customer_Entry = tkinter.Entry(self.name_frame, width = 65)

        self.Name_Label.pack(side = "left")
        self.Customer_Entry.pack(side = "right")
        self.Toppings_Label.pack(side = "left")
        self.Crust_Label.pack(side = "left")

############################################

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.topping4_var = tkinter.IntVar()
        self.topping5_var = tkinter.IntVar()
        self.topping6_var = tkinter.IntVar()
        self.topping7_var = tkinter.IntVar()

        self.radio_var = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.topping4_var.set(0)
        self.topping5_var.set(0)
        self.topping6_var.set(0)
        self.topping7_var.set(0)

        self.cb1 = tkinter.Checkbutton(self.middle_frame, text = "Pepperoni", variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.middle_frame, text = "Bacon", variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.middle_frame, text = "Jalapenos", variable = self.cb_var3)
        self.toppings4 = tkinter.Checkbutton(self.middle_frame, text = "Black Olives", variable = self.topping4_var)
        self.toppings5 = tkinter.Checkbutton(self.middle_frame, text = "Ham", variable = self.topping5_var)
        self.toppings6 = tkinter.Checkbutton(self.middle_frame, text = "Basil", variable=self.topping6_var)
        self.toppings7 = tkinter.Checkbutton(self.middle_frame, text = "Sausage", variable = self.topping7_var)

        self.rb1 = tkinter.Radiobutton(self.bottom_frame, text = "Hand-Tossed", variable = self.radio_var, value = 1)
        self.rb2 = tkinter.Radiobutton(self.bottom_frame, text = "Thin", variable = self.radio_var,value = 2)
        self.rb3 = tkinter.Radiobutton(self.bottom_frame, text = "Deep Dish", variable = self.radio_var,value = 3)
        self.rb4 = tkinter.Radiobutton(self.bottom_frame, text = "Personal Pan", variable = self.radio_var,value = 4)
        self.rb5 = tkinter.Radiobutton(self.bottom_frame, text = "Cauliflower", variable = self.radio_var,value = 5)      
        
        self.cb1.pack(side = "left")
        self.cb2.pack(side = "left")
        self.cb3.pack(side = "left")
        self.toppings4.pack(side = "left")
        self.toppings5.pack(side = "left")
        self.toppings6.pack(side = "left")
        self.toppings7.pack(side = "left")

        self.rb1.pack(side = "left")
        self.rb2.pack(side = "left")
        self.rb3.pack(side = "left")
        self.rb4.pack(side = "left")
        self.rb5.pack(side = "left")


        self.Calculation_Button = tkinter.Button(self.main_window, text = "Calculate", command = self.calc)

        self.Quit_Button = tkinter.Button(self.main_window, text = "Quit", command = self.main_window.destroy)

        self.name_frame.pack(side = "top")
        self.middle_frame.pack(side = "top")
        self.bottom_frame.pack(side = "top")

        
        self.Quit_Button.pack(side = "bottom")
        self.Calculation_Button.pack(side = "bottom")

        tkinter.mainloop()

    def calc(self):
        self.message = "Pizza Toppings/Crust Selected:   \n"
        self.total = 0

        if self.cb_var1.get() == 1:
             self.message += 'Pepperoni \n'
             self.total += 8

        if self.cb_var2.get() == 1:
            self.message += 'Bacon \n'
            self.total += 7

        if self.cb_var3.get() == 1:
            self.message += 'Jalapenos \n'
            self.total += 4

        if self.topping4_var.get() == 1:
            self.message += 'Black Olives \n'
            self.total += 5

        if self.topping5_var.get() == 1:
            self.message += 'Ham \n'
            self.total += 3

        if self.topping6_var.get() == 1:
            self.message += 'Basil \n'
            self.total += 2

        if self.topping7_var.get() == 1:
           self.message += 'Sausage \n'
           self.total += 6


        if self.radio_var.get() == 1:
            self.message += 'Hand-Tossed \n'
            self.total += 0

        if self.radio_var.get() == 2:
            self.message += 'Thin \n '
            self.total += 1

        if self.radio_var.get() == 3:
            self.message += 'Deep Dish \n '
            self.total += 2

        if self.radio_var.get() == 4:
            self.message += 'Personal Pan \n '
            self.total += 3

        if self.radio_var.get() == 5:
            self.message += 'Cauliflower \n '
            self.total += 5

           
        tkinter.messagebox.showinfo("Receipt",self.message + "\n" + "Customer Name: " + self.Customer_Entry.get() + "\n"  + "Total: $" + str(self.total))

customer_order = PizzaOrder()
