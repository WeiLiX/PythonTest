#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

class AddPromoterFrame(Frame):
    
    destroyBlock = 0;
    
    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.pack();
        self.createWidgets();
    
    def createWidgets(self):
        self.nameInput = Entry(self);
        self.nameInput.pack();
        
        self.saveBtn = Button(self, text='保存', command=lambda:self.save(1));
        self.saveBtn.pack();
    
        self.closeBtn = Button(self, text='返回', command=lambda:self.save(2));
        self.closeBtn.pack();
    
    def save(self, index):
        if index == 1:
            name = self.nameInput.get() or 'world';
            messagebox.showinfo('弹框Message', 'Hello, %s' % name);
        else:
            self.pack_forget();
            self.destroyBlock();
            self.destroy();

    def setOnDestroyBlock(self, block):
        self.destroyBlock = block;

