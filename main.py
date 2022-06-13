import gi

from conexionBase import conexionBase

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Main(Gtk.Window):
    def __init__(self):
        class handler:

            def on_window1_destroy(self,button):
                Gtk.main_quit()


            def on_btnLogin_clicked(self,button):
                nomeLogin = entryNome.get_text()
                contraLogin = entryContra.get_text()

                comboBox = comboLogin.get_active_text()

                consulta = bd.consultaSenParametros("SELECT * from usuarios WHERE nome ='"+nomeLogin+"' AND contrasinal ='"
                                                    +contraLogin+"';")
                if consulta is not None :
                    if comboBox.__eq__("Xestión de Clientes"):
                        window1.hide()
                        window2.show_all()
                    else:
                        window1.hide()
                        window3.show_all()


        Gtk.Window.__init__(self)
        self.set_border_width(10)

        builder = Gtk.Builder()
        builder.add_from_file("recuperacion.glade")

        builder.connect_signals(handler())

        window1 = builder.get_object("window1")
        window1.set_title("Proxecto Recuperación")
        grid1 = builder.get_object("grid1")

        lblInicio = builder.get_object("lblInicio")
        lblNome = builder.get_object("lbNome")
        lblContra = builder.get_object("lblContra")

        entryNome = builder.get_object("entryNome")
        entryContra = builder.get_object("entryContra")

        btnLogin = builder.get_object("btnLogin")

        comboLogin=Gtk.ComboBoxText()
        comboLogin.append_text("Xestión de Clientes")
        comboLogin.append_text("Xestión de Servizos")
        comboLogin.connect("changed", self.cambio)
        grid1.attach(comboLogin, 0,2,1,1)

        window2 = builder.get_object("window2")
        window2.set_title("Xestión de Clientes")

        window3 = builder.get_object("window3")
        window3.set_title("Xestión de Servizos")

        modelo = Gtk.ListStore(str,str,str,str,str,str)
        filtro = modelo.filter_new()
        filtro.set_visible_func(filtro)

        treeview = Gtk.TreeView(model=filtro)

        bd = conexionBase("base.dat")
        bd.conectaBD()
        bd.creaCursor()

        window1.show_all()

    def cambio(self,control):
        print(control.get_active_text())

if __name__ == "__main__":
    Main()
    Gtk.main()