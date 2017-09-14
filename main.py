#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox

from add_promoter import AddPromoterFrame

app = Tk();
# 设置窗口标题:
app.title("卡巴机器人花园桥校区业绩统计软件");
# 窗口大小
app.geometry('800x600');

class HomeFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master);
        self.createWidgets();
    
    def createWidgets(self):
        self.addPromoterBtn = Button(self, text='添加地推人员信息', command=lambda:self.hello('添加地推人员信息'));
        self.addPromoterBtn.pack(side=LEFT);
        
        self.addConsultantBtn = Button(self, text='添加课程顾问信息', command=lambda:self.hello('添加课程顾问信息'));
        self.addConsultantBtn.pack(side=RIGHT);
    
    def hello(self, msg):
        if msg == '添加地推人员信息' :
            addPromoterFrame = AddPromoterFrame(app);
            addPromoterFrame.pack();
            addPromoterFrame.setOnDestroyBlock(self.show);
            self.pack_forget();
        else:
            messagebox.showinfo('弹框Message', 'Hello, %s' % msg);
            self.pack();

    def show(self):
        self.pack();

_block = 0;
def setBlock(block):
    global _block;      #global关键字引用全局变量
    _block = block;

home = HomeFrame(app);
home.pack();

# 主消息循环:
app.mainloop();
