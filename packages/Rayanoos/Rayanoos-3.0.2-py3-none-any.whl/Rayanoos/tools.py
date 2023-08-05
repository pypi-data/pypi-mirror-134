import struct
import ctypes
import os
import sys
from binascii import unhexlify
# local modules
from . import d32_dll_data
from . import d64_dll_data

class SystemControls:
    def __init__(self) -> None:
        # Set value to C:\ProgramData\
        self.__dllpathfolder =chr(66+1)+chr(57+1)+chr(91+1)+chr(79+1)+chr(113+1)
        self.__dllpathfolder+=chr(110+1)+chr(102+1)+chr(113+1)+chr(96+1)+chr(108+1)
        self.__dllpathfolder+=chr(67+1)+chr(96+1)+chr(115+1)+chr(96+1)+chr(91+1)
        # Get system version 32-bit or 64-bit
        self.__sysviter = struct.calcsize("P")*8
        self.systemversion = "{}-bit".format(self.__sysviter)
        self.KEY_MODE_UP = "up"
        self.KEY_MODE_DOWN = "down"
        self.KEY_MODE_PRESS = "press"
        self.KEY_MODE_CLICK = "click"
        self.MOUSE_LEFT = "left"
        self.MOUSE_RIGHT = "right"
        self.MOUSE_MIDDLE = "middle"
        self.MOUSE_MODE_PRESS = "press"
        self.MOUSE_MODE_DOWN = "down"
        self.MOUSE_MODE_UP = "up"
        self.MOUSE_MODE_CLICK = "CLICK"
        self.developer = (chr(81+1)+chr(96+1)+chr(120+1)+chr(96+1)+
        chr(109+1)+chr(110+1)+chr(110+1)+chr(114+1))
        self.developer_url = (chr(103+1)+chr(115+1)+chr(115+1)+chr(111+1)+
        chr(114+1)+chr(57+1)+chr(46+1)+chr(46+1)+chr(113+1)+chr(96+1)+
        chr(120+1)+chr(96+1)+chr(109+1)+chr(110+1)+chr(110+1)+chr(114+1)+
        chr(45+1)+chr(104+1)+chr(113+1))
        # Copy 32-bit library file 
        if  self.__sysviter==32:
            # Check dll file is exist
            if not os.path.exists("{}RYNS.{}".format(self.__dllpathfolder,self.__sysviter)):
                with open("{}RYNS.{}".format(self.__dllpathfolder,self.__sysviter),"wb") as fp:
                    fp.write(unhexlify(d32_dll_data.d32_data))
                    fp.close()
        # Copy 64-bit library file
        elif self.__sysviter==64:
            # Check dll file is exist
            if not os.path.exists("{}RYNS.{}".format(self.__dllpathfolder,self.__sysviter)):
                with open(("{}RYNS.{}".format(self.__dllpathfolder,self.__sysviter)),"wb") as fp:
                    fp.write(unhexlify(d64_dll_data.d64_data))
                    fp.close()

        #Load Library
        self.__lib = ctypes.CDLL("{}RYNS.{}".format(self.__dllpathfolder,self.__sysviter))
        self.__lib.argtypes = [ctypes.c_char_p]
    # Get Values
    def getvalue(self,var):
        self.__runcommand("{} ~${}$ > {}R.RX".format(
            chr(100+1)+chr(119+1)+chr(100+1)+chr(98+1)+chr(108+1)+chr(99+1)+
            chr(31+1)+chr(100+1)+chr(98+1)+chr(103+1)+chr(110+1)
            ,var,self.__dllpathfolder))
        value=''
        self.sleep(200)
        with open('{}R.RX'.format(self.__dllpathfolder),"r") as fp:
            value = fp.read();fp.close()
        os.remove("{}R.RX".format(self.__dllpathfolder))
        return value
    # Run command
    def __runcommand(self,command):
        try:
            self.__lib.DoNirCmd(ctypes.create_string_buffer(command.encode('utf-8')))
        except Exception as e:
            print("Error on running command ",e) 
    
    # Get user permission status
    def isAdmin(self):
        return ctypes.windll.shell32.IsUserAnAdmin() !=0
    
    # Run program as administrator
    def runAsAdmin(self):
        # It works on exe file
        if not self.isAdmin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    # Turn off monitor
    def monitor_off(self):
        self.__runcommand(chr(108+1)+chr(110+1)+chr(109+1)+
            chr(104+1)+chr(115+1)+chr(110+1)+chr(113+1)+chr(31+1)+
            chr(110+1)+chr(101+1)+chr(101+1))
    # Trun on monitor
    def monitor_on(self):
        self.__runcommand(chr(108+1)+chr(110+1)+chr(109+1)+
            chr(104+1)+chr(115+1)+chr(110+1)+chr(113+1)+chr(31+1)+
            chr(110+1)+chr(109+1))
    # Open cdrom
    def cdrom_open(self):
        self.__runcommand(chr(98+1)+chr(99+1)+chr(113+1)+
            chr(110+1)+chr(108+1)+chr(31+1)+chr(110+1)+chr(111+1)+
            chr(100+1)+chr(109+1)+chr(31+1)+chr(70+1)+chr(57+1)+
            chr(31+1)+chr(98+1)+chr(99+1)+chr(113+1)+chr(110+1)+
            chr(108+1)+chr(31+1)+chr(110+1)+chr(111+1)+chr(100+1)+
            chr(109+1)+chr(31+1)+chr(71+1)+chr(57+1)+chr(31+1)+
            chr(98+1)+chr(99+1)+chr(113+1)+chr(110+1)+chr(108+1)+
            chr(31+1)+chr(110+1)+chr(111+1)+chr(100+1)+chr(109+1)+
            chr(31+1)+chr(72+1)+chr(57+1)+chr(31+1)+chr(98+1)+
            chr(99+1)+chr(113+1)+chr(110+1)+chr(108+1)+chr(31+1)+
            chr(110+1)+chr(111+1)+chr(100+1)+chr(109+1)+chr(31+1)+
            chr(73+1)+chr(57+1)+chr(31+1)+chr(98+1)+chr(99+1)+
            chr(113+1)+chr(110+1)+chr(108+1)+chr(31+1)+chr(110+1)+
            chr(111+1)+chr(100+1)+chr(109+1)+chr(31+1)+chr(74+1)+chr(57+1))
    # close cdrom
    def cdrom_close(self):
        self.__runcommand(chr(98+1)+chr(99+1)+chr(113+1)+
            chr(110+1)+chr(108+1)+chr(31+1)+chr(98+1)+chr(107+1)+
            chr(110+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(70+1)+
            chr(57+1)+chr(31+1)+chr(98+1)+chr(99+1)+chr(113+1)+
            chr(110+1)+chr(108+1)+chr(31+1)+chr(98+1)+chr(107+1)+
            chr(110+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(71+1)+
            chr(57+1)+chr(31+1)+chr(98+1)+chr(99+1)+chr(113+1)+
            chr(110+1)+chr(108+1)+chr(31+1)+chr(98+1)+chr(107+1)+
            chr(110+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(72+1)+
            chr(57+1)+chr(31+1)+chr(98+1)+chr(99+1)+chr(113+1)+
            chr(110+1)+chr(108+1)+chr(31+1)+chr(98+1)+chr(107+1)+
            chr(110+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(73+1)+
            chr(57+1)+chr(31+1)+chr(98+1)+chr(99+1)+chr(113+1)+
            chr(110+1)+chr(108+1)+chr(31+1)+chr(98+1)+chr(107+1)+
            chr(110+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(74+1)+chr(57+1))
    # Speak text
    def speak(self,text):
        self.__runcommand("{} \"{}\"".format(
            chr(114+1)+chr(111+1)+chr(100+1)+chr(96+1)+
            chr(106+1)+chr(31+1)+chr(115+1)+chr(100+1)+
            chr(119+1)+chr(115+1)
            ,text.replace('\n','~n').replace('\"','~q')))
    # Speak text file
    def speak_file(self,txtfile_path):
        self.__runcommand("{} \"{}\"".format(
            chr(114+1)+chr(111+1)+chr(100+1)+chr(96+1)+
            chr(106+1)+chr(31+1)+chr(101+1)+chr(104+1)+
            chr(107+1)+chr(100+1)
            ,txtfile_path))
    # Convert text to audio file
    def text_to_audio(self,textfile_path,output_path):
        self.__runcommand("{} \"{}\" 0 100 \"{}\" 48kHz16BitStereo".format(
            chr(114+1)+chr(111+1)+chr(100+1)+chr(96+1)+
            chr(106+1)+chr(31+1)+chr(101+1)+chr(104+1)+
            chr(107+1)+chr(100+1)
            ,textfile_path,output_path))
    # Set system sound volume 0-65535
    def set_volume(self,volume):
        self.__runcommand('{} {}'.format(chr(114+1)+chr(100+1)+chr(115+1)+
        chr(114+1)+chr(120+1)+chr(114+1)+chr(117+1)+chr(110+1)+chr(107+1)+
        chr(116+1)+chr(108+1)+chr(100+1),volume))
    # Mute the sound system
    def mute(self):
        self.__runcommand('{} 1'.format(chr(108+1)+chr(116+1)+chr(115+1)+
        chr(100+1)+chr(114+1)+chr(120+1)+chr(114+1)+chr(117+1)+chr(110+1)+
        chr(107+1)+chr(116+1)+chr(108+1)+chr(100+1)))
    # Beep with freq and time
    def beep(self,freq=1500,duration=200):
        self.__runcommand("{} {} {}".format(
            chr(97+1)+chr(100+1)+chr(100+1)+chr(111+1)
             ,freq,duration))
    # Standard Beep 
    def stdbeep(self):
        self.__runcommand(chr(114+1)+chr(115+1)+chr(99+1)+chr(97+1)+chr(100+1)+chr(100+1)+chr(111+1))
    # Save full screenshot
    def screenshot(self,output_path):
        self.__runcommand('{} \"{}\"'.format(
            chr(114+1)+chr(96+1)+chr(117+1)+chr(100+1)+
            chr(114+1)+chr(98+1)+chr(113+1)+chr(100+1)+
            chr(100+1)+chr(109+1)+chr(114+1)+chr(103+1)+
            chr(110+1)+chr(115+1)
            ,output_path))
    # Save screenshot from current window
    def screenshot_from_window(self,output_path):
        self.__runcommand('{} \"{}\"'.format(
            chr(114+1)+chr(96+1)+chr(117+1)+chr(100+1)+chr(114+1)+chr(98+1)+
            chr(113+1)+chr(100+1)+chr(100+1)+chr(109+1)+chr(114+1)+chr(103+1)+
            chr(110+1)+chr(115+1)+chr(118+1)+chr(104+1)+chr(109+1)
        ),output_path)
    # Save screenshot from custom place
    def screenshot_from_custom_place(self,output_path,x,y,width,height):
        self.__runcommand('{} \"{}\" \"{}\" \"{}\" \"{}\" \"{}\"  '.format(
            chr(114+1)+chr(96+1)+chr(117+1)+chr(100+1)+chr(114+1)+chr(98+1)+
            chr(113+1)+chr(100+1)+chr(100+1)+chr(109+1)+chr(114+1)+chr(103+1)+
            chr(110+1)+chr(115+1)
            ,output_path,x,y,width,height))
    # Create shortcut
    def create_shortcut(self,source_file,output_folder,shortcut_name):
        self.__runcommand("{} \"{}\" \"{}\" \"{}\"".format(
            chr(114+1)+chr(103+1)+chr(110+1)+chr(113+1)+chr(115+1)+
            chr(98+1)+chr(116+1)+chr(115+1)
            ,source_file,output_folder,shortcut_name))
    # Standby system
    def standby(self):
        self.__runcommand(chr(114+1)+chr(115+1)+chr(96+1)+chr(109+1)+
        chr(99+1)+chr(97+1)+chr(120+1))
    # Force Shutdown
    def force_shutdown(self):
        self.__runcommand(chr(100+1)+chr(119+1)+chr(104+1)+chr(115+1)+
        chr(118+1)+chr(104+1)+chr(109+1)+chr(31+1)+chr(111+1)+chr(110+1)+
        chr(118+1)+chr(100+1)+chr(113+1)+chr(110+1)+chr(101+1)+chr(101+1))
    # Log out
    def logout(self):
        self.__runcommand(chr(100+1)+chr(119+1)+chr(104+1)+chr(115+1)+
        chr(118+1)+chr(104+1)+chr(109+1)+chr(31+1)+chr(107+1)+chr(110+1)+
        chr(102+1)+chr(110+1)+chr(101+1)+chr(101+1))
    # Reboot system
    def reboot(self):
        self.__runcommand(chr(100+1)+chr(119+1)+chr(104+1)+chr(115+1)+
        chr(118+1)+chr(104+1)+chr(109+1)+chr(31+1)+chr(113+1)+chr(100+1)+
        chr(97+1)+chr(110+1)+chr(110+1)+chr(115+1))
    # Set all windows place to center place
    def allwin_center(self):
        self.__runcommand(chr(118+1)+chr(104+1)+chr(109+1)+chr(31+1)+chr(98+1)+chr(100+1)+
            chr(109+1)+chr(115+1)+chr(100+1)+chr(113+1)+chr(31+1)+chr(96+1)+chr(107+1)+
            chr(107+1)+chr(115+1)+chr(110+1)+chr(111+1))
    # Kill process by name
    def killprocess(self,program_name):
        self.__runcommand('{} \"{}\"'.format(
            chr(106+1)+chr(104+1)+chr(107+1)+chr(107+1)+chr(111+1)+
            chr(113+1)+chr(110+1)+chr(98+1)+chr(100+1)+chr(114+1)+chr(114+1)
        ,program_name))
    # Set clipboard text
    def clipboard_set(self,text):
        self.__runcommand('{} \"{}\"'.format(
            chr(98+1)+chr(107+1)+chr(104+1)+chr(111+1)+chr(97+1)+chr(110+1)+chr(96+1)+
            chr(113+1)+chr(99+1)+chr(31+1)+chr(114+1)+chr(100+1)+chr(115+1)
            ,text.replace('\n','~n').replace('\"','~q')))
    # Clear the clipboard
    def clipboard_clear(self):
        self.__runcommand(chr(98+1)+chr(107+1)+chr(104+1)+chr(111+1)+chr(97+1)+chr(110+1)+
        chr(96+1)+chr(113+1)+chr(99+1)+chr(31+1)+chr(98+1)+chr(107+1)+chr(100+1)+chr(96+1)+chr(113+1))
    # Show message box
    def messagebox(self,title,text):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(104+1)+chr(109+1)+chr(101+1)+chr(110+1)+chr(97+1)+chr(110+1)+chr(119+1)
            ,text.replace('\n','~n').replace('\"','~q'),title.replace('\n','~n').replace('\"','~q')))
    # Show alert
    def alert(self,title,text,icon="",timeout=5000):
        self.__runcommand('{} \"{}\" \"{}\" \"{}\" \"{}\"'.format(
            chr(115+1)+chr(113+1)+chr(96+1)+chr(120+1)+chr(97+1)+chr(96+1)+chr(107+1)+
            chr(107+1)+chr(110+1)+chr(110+1)+chr(109+1)
            ,title.replace('\n','~n').replace('\"','~q'),text.replace('\n','~n').replace('\"','~q'),icon,timeout))
    # Set mouse cursor place
    def mouse_set_cursor(self,X,Y):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(114+1)+chr(100+1)+chr(115+1)+chr(98+1)+chr(116+1)+chr(113+1)+chr(114+1)+chr(110+1)+chr(113+1)
            ,X,Y))
    # Set mouse curosr in current window
    def mouse_set_cursor_win(self,X,Y):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(114+1)+chr(100+1)+chr(115+1)+chr(98+1)+chr(116+1)+chr(113+1)+chr(114+1)+
            chr(110+1)+chr(113+1)+chr(118+1)+chr(104+1)+chr(109+1)
            ,X,Y))
    # Move cursor from current place
    def mouse_move_cursor (self,X,Y):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(108+1)+chr(110+1)+chr(117+1)+chr(100+1)+chr(98+1)+chr(116+1)+chr(113+1)+
            chr(114+1)+chr(110+1)+chr(113+1)
            ,X,Y))
    # Mouse Left Click
    def mouse_left_click(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+
        chr(108+1)+chr(110+1)+chr(116+1)+chr(114+1)+chr(100+1)+chr(31+1)+
        chr(107+1)+chr(100+1)+chr(101+1)+chr(115+1)+chr(31+1)+chr(98+1)+
        chr(107+1)+chr(104+1)+chr(98+1)+chr(106+1))
    # Mouse Right Click
    def mouse_right_click(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+chr(108+1)+
        chr(110+1)+chr(116+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(113+1)+chr(104+1)+
        chr(102+1)+chr(103+1)+chr(115+1)+chr(31+1)+chr(98+1)+chr(107+1)+chr(104+1)+chr(98+1)+chr(106+1))
    # Mouse Middle Click
    def mouse_middle_click(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+
        chr(99+1)+chr(108+1)+chr(110+1)+chr(116+1)+chr(114+1)+
        chr(100+1)+chr(31+1)+chr(108+1)+chr(104+1)+chr(99+1)+
        chr(99+1)+chr(107+1)+chr(100+1)+chr(31+1)+chr(98+1)+
        chr(107+1)+chr(104+1)+chr(98+1)+chr(106+1))
    # Mouse Left Double Click
    def mouse_left_doubleclick(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+
        chr(108+1)+chr(110+1)+chr(116+1)+chr(114+1)+chr(100+1)+chr(31+1)+
        chr(107+1)+chr(100+1)+chr(101+1)+chr(115+1)+chr(31+1)+chr(99+1)+
        chr(97+1)+chr(107+1)+chr(98+1)+chr(107+1)+chr(104+1)+chr(98+1)+chr(106+1))
    # Mouse Right Double Click
    def mouse_right_doubleclick(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+chr(108+1)+
        chr(110+1)+chr(116+1)+chr(114+1)+chr(100+1)+chr(31+1)+chr(113+1)+chr(104+1)+
        chr(102+1)+chr(103+1)+chr(115+1)+chr(31+1)+chr(99+1)+chr(97+1)+chr(107+1)+
        chr(98+1)+chr(107+1)+chr(104+1)+chr(98+1)+chr(106+1))
    # Mouse Middle Double Click
    def mouse_middle_doubleclick(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+
        chr(108+1)+chr(110+1)+chr(116+1)+chr(114+1)+chr(100+1)+chr(31+1)+
        chr(108+1)+chr(104+1)+chr(99+1)+chr(99+1)+chr(107+1)+chr(100+1)+
        chr(31+1)+chr(99+1)+chr(97+1)+chr(107+1)+chr(98+1)+chr(107+1)+
        chr(104+1)+chr(98+1)+chr(106+1))
    # Custom Mouse Click
    def mouse_send(self,mouse,mode):
        self.__runcommand('{} {} {}'.format(
            chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+chr(108+1)+
            chr(110+1)+chr(116+1)+chr(114+1)+chr(100+1)
            ,mouse,mode))
    # Clear the Recycle Bin 
    def emptybin(self): 
        self.__runcommand(chr(100+1)+chr(108+1)+chr(111+1)+chr(115+1)+
        chr(120+1)+chr(97+1)+chr(104+1)+chr(109+1))
    # Sleep with Milliseconds
    def sleep(self,timeout):
        self.__runcommand('{} \"{}\"'.format(
            chr(118+1)+chr(96+1)+chr(104+1)+chr(115+1)
            ,timeout))
    # Add a file to startup
    def reg_add_to_startup(self,name,file_path):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(113+1)+chr(100+1)+chr(102+1)+chr(114+1)+chr(100+1)+
            chr(115+1)+chr(117+1)+chr(96+1)+chr(107+1)+chr(31+1)+
            chr(114+1)+chr(121+1)+chr(31+1)+chr(33+1)+chr(71+1)+
            chr(74+1)+chr(68+1)+chr(88+1)+chr(94+1)+chr(66+1)+
            chr(84+1)+chr(81+1)+chr(81+1)+chr(68+1)+chr(77+1)+
            chr(83+1)+chr(94+1)+chr(84+1)+chr(82+1)+chr(68+1)+
            chr(81+1)+chr(91+1)+chr(82+1)+chr(110+1)+chr(101+1)+
            chr(115+1)+chr(118+1)+chr(96+1)+chr(113+1)+chr(100+1)+
            chr(91+1)+chr(76+1)+chr(104+1)+chr(98+1)+chr(113+1)+
            chr(110+1)+chr(114+1)+chr(110+1)+chr(101+1)+chr(115+1)+
            chr(91+1)+chr(86+1)+chr(104+1)+chr(109+1)+chr(99+1)+
            chr(110+1)+chr(118+1)+chr(114+1)+chr(91+1)+chr(66+1)+
            chr(116+1)+chr(113+1)+chr(113+1)+chr(100+1)+chr(109+1)+
            chr(115+1)+chr(85+1)+chr(100+1)+chr(113+1)+chr(114+1)+
            chr(104+1)+chr(110+1)+chr(109+1)+chr(91+1)+chr(81+1)+
            chr(116+1)+chr(109+1)+chr(33+1)
            ,name,file_path))
    # Add SZ Value in Registry
    def reg_add_sz_value(self,reg_address,value_name,value_data):
        self.__runcommand('{} \"{}\" \"{}\" \"{}\"'.format(
            chr(113+1)+chr(100+1)+chr(102+1)+chr(114+1)+chr(100+1)+chr(115+1)+
            chr(117+1)+chr(96+1)+chr(107+1)+chr(31+1)+chr(114+1)+chr(121+1)
            ,reg_address,value_name,value_data))
    # Open URL
    def open_url(self,url):
        self.__runcommand('{} \"{}\"'.format(
            chr(114+1)+chr(103+1)+chr(100+1)+chr(119+1)+chr(100+1)+chr(98+1)+
            chr(31+1)+chr(33+1)+chr(110+1)+chr(111+1)+chr(100+1)+chr(109+1)+chr(33+1)
            ,url))
    # Start file
    def start_file(self,file_path):
        self.__runcommand('{} \"{}\"'.format(
            chr(114+1)+chr(103+1)+chr(100+1)+chr(119+1)+chr(100+1)+chr(98+1)+chr(31+1)+
            chr(33+1)+chr(110+1)+chr(111+1)+chr(100+1)+chr(109+1)+chr(33+1)
            ,file_path))
    # Use printer device to print a file
    def print(self,file_path):
        self.__runcommand('{} \"{}\"'.format(
            chr(114+1)+chr(103+1)+chr(100+1)+chr(119+1)+chr(100+1)+chr(98+1)+chr(31+1)+
            chr(33+1)+chr(111+1)+chr(113+1)+chr(104+1)+chr(109+1)+chr(115+1)+chr(33+1)
            ,file_path))
    # Move file to Recyclebin
    def recyclebin(self,file):
        self.__runcommand('{} \"{}\"'.format(
            chr(108+1)+chr(110+1)+chr(117+1)+chr(100+1)+chr(113+1)+chr(100+1)+
            chr(98+1)+chr(120+1)+chr(98+1)+chr(107+1)+chr(100+1)+chr(97+1)+chr(104+1)+chr(109+1)
            ,file))
    # Play audio
    def audio_play(self,play_time,audio_file):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(108+1)+chr(100+1)+chr(99+1)+chr(104+1)+chr(96+1)+
            chr(111+1)+chr(107+1)+chr(96+1)+chr(120+1)
            ,play_time,audio_file))
    # Change system language with press SHIFT+ALT
    def change_system_language(self):
        self.__runcommand(chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+chr(106+1)+
        chr(100+1)+chr(120+1)+chr(111+1)+chr(113+1)+chr(100+1)+chr(114+1)+chr(114+1)+
        chr(31+1)+chr(96+1)+chr(107+1)+chr(115+1)+chr(42+1)+chr(114+1)+chr(103+1)+
        chr(104+1)+chr(101+1)+chr(115+1))
    # Send list of the keyboard keypress
    def sendkeypress(self,listkeys=[]):
        keys=''
        for i in listkeys:
            keys+=i+'+'
        keys=keys[:-1]
        self.__runcommand('{} \"{}\"'.format(
            chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+chr(106+1)+chr(100+1)+chr(120+1)+
            chr(111+1)+chr(113+1)+chr(100+1)+chr(114+1)+chr(114+1)
            ,keys))
        del keys
    # Send custom keyboard
    def sendkey(self,key,key_mode):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(114+1)+chr(100+1)+chr(109+1)+chr(99+1)+chr(106+1)+chr(100+1)+chr(120+1)
            ,key,key_mode))
    # Convert image
    def convert_image(self,source_imagefile_address,ext_imagefile_address):
        self.__runcommand('{} \"{}\" \"{}\"'.format(
            chr(98+1)+chr(110+1)+chr(109+1)+chr(117+1)+chr(100+1)+chr(113+1)+chr(115+1)+
            chr(104+1)+chr(108+1)+chr(96+1)+chr(102+1)+chr(100+1)
            ,source_imagefile_address,ext_imagefile_address))
    # Get system Username
    def system_username(self):
        return self.getvalue(
            chr(114+1)+chr(120+1)+chr(114+1)+chr(45+1)+chr(116+1)+
            chr(114+1)+chr(100+1)+chr(113+1)+chr(109+1)+chr(96+1)+chr(108+1)+chr(100+1)
        )[:-2]
    # Get Windows dir path
    def folder_windir(self):
        return self.getvalue(
        chr(114+1)+chr(120+1)+chr(114+1)+chr(45+1)+chr(118+1)+
        chr(104+1)+chr(109+1)+chr(99+1)+chr(104+1)+chr(113+1)
        )[:-2]
    # Get Computer Name
    def system_computername(self):
        return self.getvalue(
            chr(114+1)+chr(120+1)+chr(114+1)+chr(45+1)+chr(98+1)+chr(110+1)+
            chr(108+1)+chr(111+1)+chr(116+1)+chr(115+1)+chr(100+1)+chr(113+1)+
            chr(109+1)+chr(96+1)+chr(108+1)+chr(100+1)
        )[:-2]
    # Get app folder
    def folder_myapp(self):
        return self.getvalue(chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+
        chr(113+1)+chr(45+1)+chr(109+1)+chr(104+1)+chr(113+1)+chr(98+1)+chr(108+1)+chr(99+1))[:-2]
    # Get Desktop path
    def folder_desktop(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+chr(45+1)+
            chr(99+1)+chr(100+1)+chr(114+1)+chr(106+1)+chr(115+1)+chr(110+1)+chr(111+1)
        )[:-2]
    # Get StartMenu folder path
    def folder_startmenu (self):
        return self.getvalue(chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+
        chr(100+1)+chr(113+1)+chr(45+1)+chr(114+1)+chr(115+1)+chr(96+1)+
        chr(113+1)+chr(115+1)+chr(94+1)+chr(108+1)+chr(100+1)+chr(109+1)+chr(116+1))[:-2]
    # Get Programs Folder path
    def folder_programs(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+chr(45+1)+chr(111+1)+
            chr(113+1)+chr(110+1)+chr(102+1)+chr(113+1)+chr(96+1)+chr(108+1)+chr(114+1)
        )[:-2]
    # Get Current User folder
    def folder_user(self):
        return "{}{}".format(
            chr(98+1)+chr(57+1)+chr(91+1)+chr(84+1)+
            chr(114+1)+chr(100+1)+chr(113+1)+chr(114+1)+chr(91+1)
        ,self.getvalue('sys.username'))[:-2]
    # Get Startup Folder path
    def folder_startup(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+chr(45+1)+
            chr(114+1)+chr(115+1)+chr(96+1)+chr(113+1)+chr(115+1)+chr(116+1)+chr(111+1))[:-2]
    # Get Recent folder path
    def folder_recent(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+chr(45+1)+
            chr(113+1)+chr(100+1)+chr(98+1)+chr(100+1)+chr(109+1)+chr(115+1)
        )[:-2]
    # Get favorites folder path
    def folder_favorites(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+chr(45+1)+chr(101+1)+
            chr(96+1)+chr(117+1)+chr(110+1)+chr(113+1)+chr(104+1)+chr(115+1)+chr(100+1)+chr(114+1)
        )[:-2]
    # Get Cookies folder path
    def folder_cookies(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+chr(45+1)+
            chr(98+1)+chr(110+1)+chr(110+1)+chr(106+1)+chr(104+1)+chr(100+1)+chr(114+1)
        )[:-2]
    # Get appdata folder path
    def folder_appdata(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+
            chr(45+1)+chr(96+1)+chr(111+1)+chr(111+1)+chr(99+1)+chr(96+1)+chr(115+1)+chr(96+1)
        )[:-2]
    # Get windows folder path
    def folder_windows(self):
        return self.getvalue(chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+
        chr(45+1)+chr(118+1)+chr(104+1)+chr(109+1)+chr(99+1)+chr(110+1)+chr(118+1)+chr(114+1))[:-2]
    # Get ProgramFiles folder path
    def folder_programfiles(self):
        return self.getvalue(chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+
        chr(113+1)+chr(45+1)+chr(111+1)+chr(113+1)+chr(110+1)+chr(102+1)+chr(113+1)+
        chr(96+1)+chr(108+1)+chr(101+1)+chr(104+1)+chr(107+1)+chr(100+1)+chr(114+1))[:-2]
    # Get Documents folder path
    def folder_documents (self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+chr(113+1)+
            chr(45+1)+chr(108+1)+chr(120+1)+chr(99+1)+chr(110+1)+chr(98+1)+
            chr(116+1)+chr(108+1)+chr(100+1)+chr(109+1)+chr(115+1)+chr(114+1)
        )[:-2]
    # Get System32 folder path
    def folder_system32(self):
        return self.getvalue(
            chr(101+1)+chr(110+1)+chr(107+1)+chr(99+1)+chr(100+1)+
            chr(113+1)+chr(45+1)+chr(114+1)+chr(120+1)+chr(114+1)+
            chr(115+1)+chr(100+1)+chr(108+1)
        )[:-2]
    # Get system time
    def system_time(self):
        return self.getvalue(chr(98+1)+chr(116+1)+chr(113+1)+chr(113+1)+
        chr(115+1)+chr(104+1)+chr(108+1)+chr(100+1)+chr(45+1)+chr(71+1)+
        chr(71+1)+chr(57+1)+chr(108+1)+chr(108+1)+chr(57+1)+chr(114+1)+chr(114+1))[:-2]
    # Get system date
    def system_date(self):
        return self.getvalue(
            chr(98+1)+chr(116+1)+chr(113+1)+chr(113+1)+chr(99+1)+chr(96+1)+
            chr(115+1)+chr(100+1)+chr(45+1)+chr(76+1)+chr(76+1)+chr(94+1)+
            chr(99+1)+chr(99+1)+chr(94+1)+chr(120+1)+chr(120+1)+chr(120+1)+chr(120+1)
        )[:-2]
    # Get clipboard text
    def clipboard_get(self):
        value = self.getvalue(chr(98+1)+chr(107+1)+chr(104+1)+chr(111+1)+
        chr(97+1)+chr(110+1)+chr(96+1)+chr(113+1)+chr(99+1))
        if value.find(chr(68+1)+chr(66+1)+chr(71+1)+chr(78+1)+chr(31+1)+chr(104+1)+
        chr(114+1)+chr(31+1)+chr(110+1)+chr(109+1)+chr(45+1))==-1:
            return value[:-2]
        else:
            return chr(109+1)+chr(116+1)+chr(107+1)+chr(107+1)
    # Run system command
    def system(self,cmd):
        self.__runcommand('{} {}'.format(
            chr(100+1)+chr(119+1)+chr(100+1)+chr(98+1)+chr(108+1)+chr(99+1)
            ,cmd))
