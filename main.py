import random
from datetime import date

from reportlab.lib.colors import red, maroon
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, Spacer
from reportlab.pdfgen import canvas
import gi

from conexionBase import conexionBase

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Main(Gtk.Window):
    def __init__(self):
        class handler:

            def on_window1_destroy(self,button):
                Gtk.main_quit()

            def on_window2_destroy(self,button):
                Gtk.main_quit()

            def on_window3_destroy(self,button):
                Gtk.main_quit()

            def on_btnLogin_clicked(self, button):
                nomeLogin = entryNome.get_text()
                contraLogin = entryContra.get_text()

                comboBox = comboLogin.get_active_text()
                texto = "SELECT * from usuarios WHERE nome ='" + nomeLogin + "' AND contrasinal ='"+ contraLogin + "';"
                consulta = bd.consultaSenParametros(texto)

                if len(consulta)!= 0 :
                    if comboBox.__eq__("Xestión de Clientes"):
                        window1.hide()
                        window2.show_all()
                    else:
                        window1.hide()
                        window3.show_all()

            def on_btnInsertar_clicked(self, selec):

                consulta = bd.consultaSenParametros("insert into clientes (nome,apelido,dni,teléfono,cidade,fecha_nacemento)"
                                                      "values ('" + nome.get_text() + "','" + apelido.get_text() + "','" + dni.get_text() + "','"
                                                    + teléfono.get_text() + "','" + cidade.get_text()+ "','" + fecha_nacemento.get_text() + "')")
                if consulta is not None:
                    modelo, puntero = selec.get_selected()
                    modelo.append(
                        [nome.get_text(), apelido.get_text(), dni.get_text(), int(teléfono.get_text()), cidade.get_text(), fecha_nacemento.get_text()])

            def on_btnBorrar_clicked(self, selec):
                consulta = bd.consultaSenParametros("delete from clientes where dni ='" + dni.get_text() + "';")
                if consulta is not None:
                    modelo, puntero = selec.get_selected()
                    modelo.remove(puntero)


            def on_btnConsultar_clicked(self, selec):
                consulta = bd.consultaSenParametros("update clientes "
                                                      "set nome='" + nome.get_text() + "',apelido='" + apelido.get_text() + "',dni='" + dni.get_text() + "',teléfono='"+ teléfono.get_text() + "',cidade='" + cidade.get_text() + "',fecha_nacemento='" + fecha_nacemento.get_text() + "' "                                                                                                                                                                                                         "where dni='" + dni.get_text() + "';")
                if consulta is not None:
                    modelo, fila = selec.get_selected()
                    modelo[fila][0] = nome.get_text()
                    modelo[fila][1] = apelido.get_text()
                    modelo[fila][2] = dni.get_text()
                    modelo[fila][3] = int(teléfono.get_text())
                    modelo[fila][4] = cidade.get_text()
                    modelo[fila][5] = fecha_nacemento.get_text()

            def on_treeview_changed(self, selec):
                modelo, puntero = selec.get_selected()
                nome.set_text(modelo[puntero][0])
                apelido.set_text(modelo[puntero][1])
                dni.set_text(modelo[puntero][2])
                teléfono.set_text(str(modelo[puntero][3]))
                cidade.set_text(modelo[puntero][4])
                fecha_nacemento.set_text(str(modelo[puntero][5]))

            def on_btnInforme_clicked(self,button):
                canvasPrincipal = canvas.Canvas("/home/oracle/Escritorio/informe.pdf")
                canvasPrincipal.setLineWidth(.3)
                canvasPrincipal.setFont('Courier', 40)
                canvasPrincipal.drawString(30, 700, 'INFORME DOS PRODUTOS')
                canvasPrincipal.drawString(320, 735, date.today().strftime("%d/%m/%Y"))
                canvasPrincipal.setStrokeColor(maroon)
                canvasPrincipal.line(20, 770, 570, 770)
                canvasPrincipal.line(20, 690, 570, 690)
                canvasPrincipal.line(20, 770, 20, 690)
                canvasPrincipal.line(570, 770, 570, 690)

                produtos = bd.consultaSenParametros("select * from produtos")
                i = 650
                canvasPrincipal.setFont('Courier', 12)
                for prod in produtos:
                    canvasPrincipal.line(50, i, 540, i)
                    canvasPrincipal.line(50, i-50, 540, i-50)
                    canvasPrincipal.line(50, i, 50, i-50)
                    canvasPrincipal.line(540, i, 540, i-50)
                    i = i - 75

                    canvasPrincipal.drawString(60, i + 35, "Prezo: " + str(prod[2]) + " eur.")
                    canvasPrincipal.drawString(60, i + 45, "Codigo: " + str(prod[1]))
                    canvasPrincipal.drawString(60, i + 55, "Nome: " + str(prod[0]))

                canvasPrincipal.save()

        Gtk.Window.__init__(self)
        self.set_border_width(10)

        bd = conexionBase("base.dat")
        bd.conectaBD()
        bd.creaCursor()

        builder = Gtk.Builder()
        builder.add_from_file("recuperacion.glade")

        builder.connect_signals(handler())

        window1 = builder.get_object("window1")
        window1.set_title("Proxecto Recuperación")
        grid1 = builder.get_object("grid1")
        grid2 = builder.get_object("grid2")
        grid3 = builder.get_object("grid3")
        lblInicio = builder.get_object("lblInicio")
        lblNome = builder.get_object("lbNome")
        lblContra = builder.get_object("lblContra")
        entryNome = builder.get_object("entryNome")
        entryContra = builder.get_object("entryContra")
        btnLogin = builder.get_object("btnLogin")
        nome = builder.get_object("nome")
        apelido = builder.get_object("apelido")
        cidade = builder.get_object("cidade")
        dni = builder.get_object("dni")
        teléfono = builder.get_object("teléfono")
        fecha_nacemento = builder.get_object("fecha_nacemento")

        comboLogin=Gtk.ComboBoxText()
        comboLogin.append_text("Xestión de Clientes")
        comboLogin.append_text("Xestión de Produtos")
        comboLogin.connect("changed", self.cambio)
        comboLogin.set_active(0)
        grid1.attach(comboLogin, 0,2,1,1)

        window2 = builder.get_object("window2")
        window2.set_title("Xestión de Clientes")
        window3 = builder.get_object("window3")
        window3.set_title("Xestión de Produtos")

        modelo = Gtk.ListStore(str,str,str,int,str,str)
        consulta = bd.consultaSenParametros("SELECT * from clientes;")
        for c in consulta:
            modelo.append(c)

        treeview = Gtk.TreeView(model=modelo)

        for i, titulo in enumerate(["Nome", "Apelido", "DNI", "Teléfono", "Cidade", "Fecha de Nacemento"]):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(titulo, cell, text=i)
            treeview.append_column(column)

        grid2.attach(treeview, 0,1,6,1)

        seleccion = treeview.get_selection()
        seleccion.connect("changed", handler.on_treeview_changed, seleccion)

        self.btnConsultar = Gtk.Button(label="Consultar")
        self.btnConsultar.connect("clicked", handler.on_btnConsultar_clicked, seleccion)
        grid2.attach(self.btnConsultar, 1, 0, 1, 1)

        self.btnInsertar = Gtk.Button(label="Insertar")
        self.btnInsertar.connect("clicked", handler.on_btnInsertar_clicked, seleccion)
        grid2.attach(self.btnInsertar, 0, 0, 1, 1)

        self.btnBorrar = Gtk.Button(label="Borrar")
        self.btnBorrar.connect("clicked", handler.on_btnBorrar_clicked, seleccion)
        grid2.attach(self.btnBorrar, 2, 0, 1, 1)

        treeview.show()
        window1.show_all()

    def cambio(self,control):
        print(control.get_active_text())

if __name__ == "__main__":
    Main()
    Gtk.main()