import gi

from conexionBase import conexionBase

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Proxecto Recuperación")
        self.set_border_width(10)

        bd = conexionBase.ConexionBD("base.dat")
        bd.conectaBD()
        bd.creaCursor()

if __name__ == "__main__":
    Main()
    Gtk.main()