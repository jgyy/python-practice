"""
Text Editor - Notepad style application that can open, edit, and save text documents. Optional:
Add syntax highlighting and other features.
"""
# noinspection PyCompatibility
from tkinter import Frame, Text, YES, BOTH, Menu, END, SEL_FIRST, SEL_LAST, Tk
# noinspection PyCompatibility
import tkinter.filedialog as tk
# noinspection PyCompatibility
import tkinter.messagebox as tk2


# noinspection Pylint
class Application(Frame):
    """Application"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.text1 = Text(width=20, height=20)
        self.create_widgets()

    def create_widgets(self):
        """create widgets"""
        self.text1.pack(expand=YES, fill=BOTH)  # to make the textbox fill entire window

        menubar = Menu(self)
        file_menu = Menu(menubar)
        edit_menu = Menu(menubar)
        tools_menu = Menu(menubar)
        file_menu.add_command(label='New', command=self.new_doc)
        file_menu.add_command(label='Save', command=self.save_doc)
        file_menu.add_command(label='Open', command=self.open_doc)
        edit_menu.add_command(label='Copy', command=self.copy)
        edit_menu.add_command(label='Paste', command=self.paste)
        edit_menu.add_command(label='Clear', command=self.clear)
        tools_menu.add_command(label='Word Count', command=self.word_count)
        menubar.add_cascade(label='File', menu=file_menu)
        menubar.add_cascade(label='Edit', menu=edit_menu)
        menubar.add_cascade(label='Tools', menu=tools_menu)
        ROOT.config(menu=menubar)

    def new_doc(self):
        """new document"""
        if tk2.askyesno("Message", "Unsaved work will be lost. Continue?"):
            self.text1.delete("1.0", END)

    def save_doc(self):
        """save document"""
        save_file = tk.asksaveasfile(defaultextension=".txt")
        text2save = str(self.text1.get("1.0", END))
        save_file.write(text2save)
        save_file.close()

    def open_doc(self):
        """open document"""
        openfile = tk.askopenfile()
        text = openfile.read()
        self.text1.insert(END, text)
        openfile.close()

    def copy(self):
        """Copy the selected text into the clipboard"""
        var = str(self.text1.get(SEL_FIRST, SEL_LAST))
        self.clipboard_clear()
        self.clipboard_append(var)

    def paste(self):
        """Insert the clipboard text into the textbox"""
        result = self.selection_get(selection="CLIPBOARD")  # get text from clipboard
        self.text1.insert("1.0", result)

    def clear(self):
        """clear"""
        self.text1.delete("1.0", END)

    def word_count(self):
        """
        Get text from textbox and split it by whitespace characters into a list. Then find
        length of list.
        """
        userText = self.text1.get("1.0", END)
        wordList = userText.split()
        number_of_words = len(wordList)
        tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))


if __name__ == '__main__':
    ROOT = Tk()
    ROOT.title('Text Editor')
    ROOT.geometry('700x600')
    APP = Application(ROOT)
    APP.mainloop()
