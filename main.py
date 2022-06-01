import gi

from conexionBase import conexionBase

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Main(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Proxecto Recuperación")
        self.set_border_width(10)

        builder = Gtk.Builder()
        builder.add_from_file("recuperacion.glade")

        window1 = builder.get_object("window1")
        grid1 = builder.get_object("grid1")

        lblInicio = builder.get_object("lblInicio")
        lblNome = builder.get_object("lbNome")
        lblContra = builder.get_object("lblContra")

        entryNome = builder.get_object("entryNome")
        entryContra = builder.get_object("entryContra")

        btnLogin = builder.get_object("btnLogin")
        comboLogin = builder.get_object("comboLogin")

        bd = conexionBase.ConexionBD("base.dat")
        bd.conectaBD()
        bd.creaCursor()

if __name__ == "__main__":
    Main()
    Gtk.main()