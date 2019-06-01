"""
Mp3 Player - A simple program for playing your favorite music files. Add features you think are
missing from your favorite music player.
"""
# noinspection PyCompatibility
from tkinter import Frame, Listbox, SINGLE, END, Button, Tk
# noinspection PyCompatibility
import tkinter.filedialog as tk
# noinspection PyCompatibility
import tkinter.messagebox as tk2
import pygame
# noinspection Pylint
from pygame import init

PLAYLIST = []


# noinspection Pylint
class Application(Frame):
    """Application Class"""
    def __init__(self, master):
        super(Application, self).__init__(master)

        # self.create_widgets()
        # noinspection SpellCheckingInspection
        self.playlistbox = Listbox(self, width=40, height=10,
                                   selectmode=SINGLE)
        for song in PLAYLIST:
            self.playlistbox.insert(END, song)

        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row=1)
        self.play_button = Button(self, text= 'Play', command=self.play)
        self.loop_button = Button(self, text= 'Loop', command=self.loop)
        self.add_button = Button(self, text= 'Add', command=self.add)
        self.play_button.grid(row=4, column=0)
        self.loop_button.grid(row=4, column=1)
        self.add_button.grid(row=4, column=2)
        self.pack()

        init()

    def play(self):
        """play function"""
        if PLAYLIST:
            tk2.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:
            pygame.mixer.music.stop()
            selected_songs = self.playlistbox.curselection()
            play_it = PLAYLIST[int(selected_songs[0])]
            pygame.mixer.music.load(play_it)
            pygame.mixer.music.play()

    @staticmethod
    def loop():
        """loop function"""
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1)

    def add(self):
        """add function"""
        # noinspection SpellCheckingInspection
        file = tk.askopenfilenames(initialdir='~/Downloads')
        songs_tuple = Tk.splitlist(file)  # turn user's opened filenames into tuple
        songs_list = list(songs_tuple)  # convert to list
        # Add the full filename of song to playlist list, and a shortened version to the listBox
        for song in songs_list:
            PLAYLIST.append(song)
            temp_array = song.split('/')
            song_short = temp_array[len(temp_array) - 1]
            self.playlistbox.insert(END, song_short)


if __name__ == '__main__':
    ROOT = Tk()
    ROOT.title("Text Editor")
    ROOT.geometry("500x200")
    APP = Application(ROOT)
    APP.mainloop()
