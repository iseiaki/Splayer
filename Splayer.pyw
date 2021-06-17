# Script - "Youtubestreamplayer.pyw"
# Creator - Mirian Kurtanidze
# What can It do?
# ---------- it can play your favorite music stream when u are coding
# what language is being used?
# ---------- Python only

import psutil                                                                    # importing module psutil
import vlc                                                                       # importing module vlc
import pafy                                                                      # importing module pafy
import keyboard                                                                  # importing module keyboard

with open('parameters.txt', 'r') as f:                                           # this opens external notepad file where youtube stream link is inserted by user and reads it
    lines = f.readlines()
    url = str(lines[0])
    win_size = float(lines[1])

vscode = "Code.exe" in (p.name() for p in psutil.process_iter())                 # this checks if VScode program is running on device
notepadeditor = "notepad++.exe" in (p.name() for p in psutil.process_iter())     # this checks if notepad++ program is running on device
pycharm = "pycharm64.exe" in (p.name() for p in psutil.process_iter())           # this checks if Pycharm program is running on device
atom = "atom.exe" in (p.name() for p in psutil.process_iter())                   # this checks if Atom  program is running on device
sublime_editor = "sublime_text.exe" in (p.name() for p in psutil.process_iter()) # this checks if sublime text editor program is running on device
list_of_editors = [vscode, pycharm, notepadeditor, atom]                         # this just adds all this programs inside list, and then gets return by boolean

number_for_range = 0                                                             # variable for loop
trueorfalse = True                                                               # boolean for loop
sec_trueorfalse = True                                                           # boolean for loop
sec_number_for_range = 0                                                         # variable for loop
sec_list = []                                                                    # list for loop



def running():                                                                    # this function runs when the music player also runs, it's depended on list - list_of_editors - if any of it's child return True than this function is gonna start
    global number_for_range                                                       # here we get variable outside function as global so then we can modify it
    print(sec_list)                                                               # for testing to see if programs are still running and script can see it
    print("Running LO-FI beats")                                                  # this also testing                                                   # reading part                                                         # gets url
    video = pafy.new(url)                                                         # video player things
    best = video.getbest()                                                        # video player things
    media = vlc.MediaPlayer(best.url)                                             # video player things
    media.video_set_scale(win_size)                                                    # resizing window
    media.play()                                                                  # finally playing
    while True:                                                                   # this checks if user wants pause or turn off on script by simply keypress
        keypress = 0                                                              # variable for future uses
        if keyboard.is_pressed('@') and keypress == 0:                            # if key '@' is pressed
            print('You Pressed A Key!')                                           # test statement
            keypress = 1                                                          # we change keypress variable value cuz we need it in next if statement
            media.stop()                                                          # stop (pause) the player
        if keyboard.is_pressed('#'):                                              # if key '#' is pressed
           exit()                                                                 # shutdown script
        if keyboard.is_pressed('@') and keypress == 1:                            # if key '@' is pressed
            print('You Pressed A Key!')                                           # test statement
            keypress = 0                                                          # modifies variable "keypress" value for above statement (pause)
            media.play()                                                          # plays
        vscode = "Code.exe" in (p.name() for p in psutil.process_iter())          # in loop checks if program is running or not
        notepadeditor = "notepad++.exe" in (p.name() for p in psutil.process_iter()) # in loop checks if program is running or not
        pycharm = "pycharm64.exe" in (p.name() for p in psutil.process_iter())    # in loop checks if program is running or not
        atom = "atom.exe" in (p.name() for p in psutil.process_iter())            # in loop checks if program is running or not
        sublime_editor = "sublime_text.exe" in (p.name() for p in psutil.process_iter()) # in loop checks if program is running or not
        list_of_editors = [vscode, pycharm, notepadeditor, atom, sublime_editor]  # in loop checks if program is running or not
        print(list_of_editors)                                                    # test print statement
        if list_of_editors == [False, False, False, False, False]:                # checks if all this program return False script will be paused
            number_for_range = 0                                                  # we modify variable outside function for future use
            media.stop()                                                          # player stops
            main_loop()                                                           # we return to the main_loop() where we wait for any member (program) from list to return true and then play

def main_loop():                                                                  # main function to detect if any member from list return true to start second function
    global list_of_editors                                                        # get global variable called list_of_editors
    global number_for_range                                                       # get second global variable called "number_for_range"
    global trueorfalse                                                            # get third global variable called "trueorfalse"
    while True:                                                                   # infinite loop
        for i in range(len(list_of_editors)):                                     # detects if any program is on
            if keyboard.is_pressed('#'):                                          # if key '#' is pressed
                exit()                                                            # exits if "#" is being pressed
            vscode = "Code.exe" in (p.name() for p in psutil.process_iter())      # this checks if VScode program is running on device
            notepadeditor = "notepad++.exe" in (p.name() for p in psutil.process_iter())      # this checks if notepad++ program is running on device
            pycharm = "pycharm64.exe" in (p.name() for p in psutil.process_iter()) # this checks if pycharm program is running on device
            atom = "atom.exe" in (p.name() for p in psutil.process_iter())        # this checks if atom program is running on device
            sublime_editor = "sublime_text.exe" in (p.name() for p in psutil.process_iter())  # this checks if sublime_editor program is running on device
            list_of_editors = [vscode, pycharm, notepadeditor, atom, sublime_editor]          # adds all this programs into a list and then check if any return True in future
            print(list_of_editors)                                                # Test Statement
            if list_of_editors[number_for_range] == True and trueorfalse == True: # if any member return True it will run function - running()
                running()                                                         # function runs
                trueorfalse = False                                               # boolean changes into false so this infinite loop won't run anymore
            else:                                                                 # else statement in order above "if" isn't doesn't get executed
                number_for_range += 1                                             # +1 value for global variable called "number_for_range"
        number_for_range = 0                                                      # honestly I don't know what this does, but it works so please don't touch it
        if keyboard.is_pressed('#'):                                              # if key '#' is pressed
            exit()                                                                # shutdown the script

main_loop()                                                                       # starts main function on script run