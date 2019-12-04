'''''''''
A program that stores dvd information:
Title,Author
Year,ISBN, Quantity

User can:
View all records
Add Books
Update Books
Add to Cart
Checkout Cart
Delete Selected
Exit
'''''''''
from tkinter import *
import webbrowser
import backend
from tkinter import messagebox
import sqlite3
import os

#Button Urls
github_url = 'https://github.com/CyborgVillager?tab=repositories'
bitchute_url = 'https://www.bitchute.com/channel/jonathanai/'
credits_text = 'credits.txt'



##Functions##
# binded to an widget event its called event - get_selected_row
def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        #print(selected_tuple[0])
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
        entry5.delete(0, END)
        entry5.insert(END, selected_tuple[5])
        entry6.delete(0, END)
        entry6.insert(END, selected_tuple[6])

    except IndexError:
        pass
window = Tk()


def viewcart_command():
    # this is an list object
    # uses viewallbt button  new rows will be put at the end of the exisiting row
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def add_command():

    # add info from user request
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), price_text.get(), quantity_text.get())
    list1.delete(0, END)
    # after user has inputed info , it will show as verficiation
    list1.insert(END,
                 (title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), price_text.get(), quantity_text.get()))



def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                   price_text.get(), quantity_text.get())

def addto_cart_command():

    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    print(quantity_text.get(),selected_tuple[6])
    if int(quantity_text.get()) > int(selected_tuple[6]):
        print('Quantity Exeeded')
        messagebox.showwarning("warning", "Exceeded available quantity")
        return


    # backend.addto_cart(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
    #                  price_text.get(), quantity_text.get())
    list1.delete(0, END)
    # after user has inputed info , it will show as verficiation
    flag = 1

    file = open('checkout.txt','a')
    file.write(str(selected_tuple[0])+","+str(title_text.get())+","+ str(author_text.get())+","+ str(year_text.get())+","+ str(isbn_text.get())+","+ str(price_text.get())+","+
                  str(quantity_text.get()))
    file.write('\n')
    file.close()

#file open/read the file
    file = open('checkout.txt','r')
    checkout_info = file.readlines()
    for file_info in range(len(checkout_info)):
        new_checkout_info = checkout_info[file_info].split(',')
        print(new_checkout_info)
        list1.insert(END,
                     (new_checkout_info[0],new_checkout_info[1], new_checkout_info[2], new_checkout_info[3], new_checkout_info[4], new_checkout_info[5],
                      new_checkout_info[6].rstrip("\n")))
#close the file
    file.close()


#re-read checkout info if user exit the program, pretty much saves the info
def checkout_command():
    # backend.checkout(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
    #                  price_text.get(), quantity_text.get())
    file = open('checkout.txt', 'r')
    access_file = file.readlines()
    id = []
    quantity = []
    price = 0
    for info in range(len(access_file)):
        new = access_file[info].split(',')
        id.append(new[0])
        quantity.append(new[6].rstrip("\n"))
        quantity_price = float(new[5])
        quantity_price = quantity_price * int(new[6].rstrip("\n"))
        price = price + quantity_price
        print(price)
        quantity_price = 0

    print('id: ' + str(id))
    print('Quantity: ' + str(quantity))
    for info in range(len(id)):
        print(id[info])
        connection = sqlite3.connect('books.db')
        mouse_cursor = connection.cursor()
        mouse_cursor.execute('SELECT quantity FROM book where id=?', (id[info],))
        rows = mouse_cursor.fetchall()
        print(rows[0][0])
        new_quantity = int(rows[0][0]) - int(quantity[info])
        print(new_quantity)
        connection.commit()
        connection.close()
        connection = sqlite3.connect('books.db')
        mouse_cursor = connection.cursor()
        mouse_cursor.execute('UPDATE book SET quantity=? WHERE id=?',
                    (new_quantity, id[info]))
        connection.commit()
        connection.close()

    file.close()
    subTotal = price
    percent = .7
    two = 2
    tax = subTotal * percent
#results / print out the information
    print('Your subTotal is: $' + str(round(subTotal,two)))
    print('Your tax amount is: $' + str(round(tax,two)))
    total = subTotal + tax
    print('Total Amount is: $' + str(round(total,two)))
#message to the user
    messagebox.showinfo("INVOICE", 'Your subTotal is: $' + str(round(subTotal,two))+'\n'+'Your tax amount is: $' +
                        str(round(tax,two))+'\n'+'Total Amount is: $' + str(round(total,two)) + '\n' +
                        'Thank you for purchasing at Jonathan\'s DVD Shop!')
    os.remove('checkout.txt')


def view_command():
    list1.grid(row=3, column=0, rowspan=6, columnspan=2)
    # this is an list object
    # uses viewallbt button  new rows will be put at the end of the exisiting row
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

##Functions End##
# Ask user program name
# ask_user = input('Hello what would you like to name this program?')


##Top info Start##

# Title for Window Screen
window.wm_title('Jonathan Almawi\'s DVD  Shop')
# Title
l1title = Label(window, text='Title')
l1title.grid(row=0, column=0)

# Author
l2author = Label(window, text='Author')
l2author.grid(row=0, column=2)

# ISBN
l3isbn = Label(window, text='ISBN')
l3isbn.grid(row=1, column=0)

# Year
l4year = Label(window, text='Year')
l4year.grid(row=1, column=2)

# Price
l5price = Label(window, text='Price')
l5price.grid(row=2, column=0)

# Quantity
l6quantity = Label(window, text='Quantity')
l6quantity.grid(row=2, column=2)

##Top info End##

####Entries Start####
# Title
title_text = StringVar()
# textvariable is spatial datatype
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

# Author
author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

# Year
year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

# ISBN
isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# Price
price_text = StringVar()
entry5 = Entry(window, textvariable=price_text)
entry5.grid(row=2, column=1)

# Quantity
quantity_text = StringVar()
entry6 = Entry(window, textvariable=quantity_text)
entry6.grid(row=2, column=3)

# List Box
# box info width and height
list1 = Listbox(window, height=8, width=65)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)
####Entries End####

###Scroll Bar Start###
# scrollbar location
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)  # rowspan - centered

# Apply scrollbar config to list
list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)
# Binding the list t get the the selected row
# From user input
list1.bind('<<ListboxSelect>>', get_selected_row)

###Scroll Bar End###


####Button Start####
# View All
viewallbt = Button(window, text='View all Books', width=12, command=view_command)
viewallbt.grid(row=3, column=3)

# Add entry
entrybt = Button(window, text='Add Books', width=12, command=add_command)
entrybt.grid(row=4, column=3)

# Update Book Info
updatebt = Button(window, text='Update Books', width=12, command=update_command)
updatebt.grid(row=5, column=3)

# Add to Cart
addtocartbt = Button(window, text='Add to Cart', width=12, command=addto_cart_command)
addtocartbt.grid(row=6, column=3)

# Checkout
checkoutbt = Button(window, text='Checkout Cart', width=12, command=checkout_command)
checkoutbt.grid(row=7, column=3)

# Delete Book Button
deletebt = Button(window, text='Delete Selected', width=12, command=delete_command)
deletebt.grid(row=8, column=3)

# Close
closebt = Button(window, text='Exit', width=12, command=window.destroy)
closebt.grid(row=9, column=3)

# Social Buttons
#GitHub
def Open_GitHub_Url():
    webbrowser.open_new(github_url)
social0bt = Button(window, text='Github', width=12, command=Open_GitHub_Url)
social0bt.grid(row=10, column=0)

#BitChute
def Open_BitChute_Url():
    webbrowser.open_new(bitchute_url)
social1bt = Button(window, text='BitChute', width=12, command=Open_BitChute_Url)
social1bt.grid(row=10, column=1)

#Open credits

def Open_Credits():
    webbrowser.open_new(credits_text)
social1bt = Button(window, text='Credits', width=12, command=Open_Credits)
social1bt.grid(row=10, column=2)


####Button End####

# wrap all all widgets
#End of Program
window.mainloop()
