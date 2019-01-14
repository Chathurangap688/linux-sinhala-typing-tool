import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class DialogWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="About Sinhala tool for Linux")

        self.set_border_width(6)

        button = Gtk.Button("Ok")
        button.connect("clicked", self.on_button_clicked)

        self.add(button)

    def on_button_clicked(self, widget):
        self.destroy()

