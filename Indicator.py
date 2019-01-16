import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

import time
import type
import unicod
import data_tree as data
from pynput import keyboard
from pynput.keyboard import Key, Controller

import threading

k_bord=Controller()
class Indicator(Gtk.Window):
    state = "Start"
    msg=Gtk.AboutDialog()
    def __init__(self):
        self.app = 'Sinhala Typing Tool'
        iconpath = "./web2.png"
        self.indicator = AppIndicator3.Indicator.new(self.app, iconpath,AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_icon(iconpath)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)       
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label("Panhinda", self.app)
	
    def run(self):
        exec(open('./main.py').read())
        
    def run2():
        exec(open('./main.py').read())

    #t = threading.Thread(target=run2, name='Saying hi')
    #t.daemon = True
   # t.start()

    def about(self, source):
    	print('hello')	
    	

    	self.msg.set_name("Panhinda for Linux")
    	self.msg.set_title("Panhinda About")
    	self.msg.set_authors(["Department of Computer Engineering,","University of Peradeniya.","\t>Chathuranga Piyadarshana","\t>Rochana Pathiraja","\t>Rasika Maduranga"])

    	self.msg.set_comments("Try this aplication and please submit the feedback\n from following URL")
    	self.msg.set_website("www.fb.com")
    	self.msg.set_copyright("aces all right recieved")
    	self.msg.run()
    	self.msg.hide()

    def start_stop(self,source):
        if self.state=="Pause":
            print ("started")
            self.indicator.set_menu(self.create_menu())
            self.state="Start"
            #Start Func
            k_bord.press(Key.esc)
            k_bord.release(Key.esc)
            time.sleep(0.3)
            t = threading.Thread(target=self.run,name='hi')
            t.daemon = True
            t.start()
            
        else:
            print ("Paused")
            self.indicator.set_menu(self.create_menu())
            self.state="Pause"
            #Stop Func
            k_bord.press(Key.esc)
            k_bord.release(Key.esc)
            


        print("start stop")

    def create_menu(self):
        menu = Gtk.Menu()
        # menu item 1
        item_1 = Gtk.MenuItem(self.state)
        item_2 = Gtk.MenuItem('About')
        item_2.connect('activate', self.about)
        item_1.connect('activate',self.start_stop)

        menu.append(item_1)
        menu.append(item_2)
        # separator
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)
        # quit
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def stop(self, source):
        Gtk.main_quit()
        exit()

 #< This actually starts the thread execution in the background

a=Indicator()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()