"""
This module provides a call wrapper for tkinter that displays
exceptions in a messagebox.
"""

import traceback

import tkinter
import tkinter.messagebox


class Catcher:
    """A call wrapper for tkinter that displays exceptions in a messagebox."""

    def __init__(self, func, subst, widget):
        self.func = func
        self.subst = subst
        self.widget = widget

    def __call__(self, *args):
        try:
            if self.subst:
                args = self.subst(*args)
            return self.func(*args)
        except Exception as e:
            traceback.print_exc()
            tkinter.messagebox.showerror(type(e).__name__, str(e))
