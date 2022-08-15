#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygtk
pygtk.require ('2.0')
import gtk


w=gtk.Window(gtk.WINDOW_TOPLEVEL)
w.connect("destroy", gtk.main_quit)
w.set_title("Mi Programa")
w.set_default_size(300,200)


tv=gtk.TextView()
tv.set_editable(True)
sw=gtk.ScrolledWindow()
sw.add(tv)


mb=gtk.MenuBar()
mi=gtk.MenuItem("Archivo")
mb.add(mi)
m=gtk.Menu()
mi.set_submenu(m)


def nuevo(self):
    b=tv.get_buffer()
    b.set_text("")


mi=gtk.MenuItem("Nuevo")
mi.connect("activate", nuevo)
m.append(mi)
mi=gtk.MenuItem("Salir")
mi.connect("activate", gtk.main_quit)
m.append(mi)


vbox=gtk.VBox()
vbox.pack_start(mb, False, False, 00)
vbox.pack_start(sw, True, True, 00)


w.add(vbox)
w.show_all()
gtk.main()

