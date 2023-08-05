## Rayanoos package for special control system

###### Note: that's only work in Windows

###### Note: The volume of the source code of this packet is 200 KB, but when you create a exe file with  pyinstaller tool, it will only have 100 KB in size with all the tools of this package. This is very amazing.


###### Installation
Install on Windows: python -m pip install rayanoos

Report Bugs: contact@rayanoos.ir

###### Example:

from Rayanoos import tools

t = tools.SystemControls()

t.alert("Hello","Call me")


## Features:

###### Save Full ScreenShot
t.screenshot('file.png')

###### Save Screenshot from current window
t.screenshot_from_window('file.png')

###### Save Screenshot from custom place with custom size
t.screenshot_from_custom_place('file.png',x,y,width,height)

###### Turn off the monitor
t.monitor_off()

###### Turn on the monitor
t.monitor_on()

###### Open CDROM
t.cdrom_open()

###### Close CDROM
t.cdrom_Close()

###### Set mouse cursor place
t.mouse_set_cursor(x,y)

###### Move cursor from old place to new place
t.mouse_move_cursor(x,y)

###### Mouse Click Left
t.mouse_left_click()

###### Mouse Click Right
t.mouse_right_click() 

###### Mouse Click Middle
t.mouse_middle_click() 

###### Mouse doubleClick Left
t.mouse_left_doubleclick() 

###### Mouse doubleClick Right
t.mouse_right_doubleclick()

###### Mouse doubleClick Middle
t.mouse_middle_doubleclick()

###### Custom mouse click control.
t.mouse_send(t.MOUSE_LEFT,t.MOUSE_MODE_DOWN)

###### Move files to Recycle bin
t.recyclebin('file.exe')

###### Clear the Recycle Bin
t.emptybin() 

###### Speak Text (text to audio)
t.speak('Hello')

###### Speak Text File
t.speak_file('file.txt')

###### Convert text file to audio file
t.text_to_audio('file.txt','file.wav')

###### Set sound volume in range of 0 to 65500
t.set_volume(1000)

######  Mute sound volume
t.mute()

###### Standard Beep 
t.stdbeep()

###### Beep with freq and time
t.beep(freq=2000,duration=1000)

###### Create shortcut
t.create_shortcut('file.exe','C:\\','Name')

###### Standby system
t.standby()

###### Force Shutdown system
t.force_shutdown()

###### Logout system
t.logoff() 'Logoff user

###### Reboot system
t.reboot() Reboot system

###### Set all windows place to center place
t.allwin_center()

###### Kill process by name
t.killprocess('process.exe')

###### Set Clipboard text
t.clipboard_set('Hello')

###### Get Clipboard text
t.clipbord_get()

###### Clear Clipboard
t.clipboard_clear()

###### Show a message box with custom title and text
t.messagebox(“Title”,”Text”)

###### Show Notification
t.alert('title','text','icon.ico/.exe',2000)

###### Seep with Milliseconds
t.sleep(1000)

###### Add file to startup in Registry
t.reg_add_to_startup('Name','file.exe')

###### Add sz value to Registry
t.reg_add_sz_value('HKEY_CURRENT_USER','name','data')

###### Open Url in default system explorer
t.open_url(”https://Rayanoos.ir”)

###### Start file
t.start_file(“file.exe”)

###### Send docs/pdf and … to printer device to print
t.print('sample.pdf')

###### Play audio with custom timeout
t.audio_play(1000,”file.mp3”)

###### Change system language with SHIFT+ALT
t.change_system_language()

###### Press simultaneously keyboard keys
t.sendkeypress(['ctrl','alt','delete'])

###### Send keys with custom mode click/down/up…
t.sendkey('a',t.KEY_MODE_CLICK)

###### Convert image format
t.convert_image('file.png','file.jpg')

###### Use system commands and CMD
t.system('cls')

###### Get system Time
t.system_time() 

###### Get system Date
t.system_date()

###### Get system Username
t.system_username()

###### Get windir folder path
t.folder_windir() 

######  Get computer name
t.system_computername()

###### Get your app file folder path
t.folder_myapp()

###### Get desktop folder path
t.folder_desktop()

###### Get startmenu folder path
t.folder_startmenu()

###### Get programs folder path
t.folder_programs()

###### Get username folder path
t.folder_username()

###### Get startup folder path
t.folder_startup()

###### Get recent folder path
t.folder_recent()

###### Get favorites folder path
t.folder_favorites()

###### Get cookies folder path
t.folder_cookies()

###### Get appdata folder path
t.folder_appdata()

###### Get windows folder path
t.folder_windows()

###### Get programfiles folder path
t.folder_programfiles()

###### Get documents folder path
t.folder_documents()

###### Get system32 folder path
t.folder_system32()