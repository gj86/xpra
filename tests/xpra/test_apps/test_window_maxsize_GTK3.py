#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')  # @UndefinedVariable
gi.require_version('Gdk', '3.0')  # @UndefinedVariable
from gi.repository import Gtk, Gdk  #pylint: disable=wrong-import-position @UnresolvedImport


def main():
	window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
	window.set_size_request(300, 200)
	window.connect("delete_event", Gtk.main_quit)
	window.show_all()
	geom = Gdk.Geometry()
	geom.max_width = 600
	geom.max_height = 400
	hints = Gdk.WindowHints.MAX_SIZE
	window.set_geometry_hints(window, geom, hints)
	Gtk.main()
	return 0


if __name__ == "__main__":
	main()
