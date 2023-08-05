#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python modules for plot utilities:
    ImageViewer: embed matplotlib objects into wx

Author: Tong Zhang
Created: Feb. 3rd, 2015
"""

#import wxversion
#wxversion.ensureMinimal('2.8')

from __future__ import division

import wx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import epics
import time
import os
import xml.etree.cElementTree as ET
from . import resutils
from . import funutils
#import resutils
#import funutils

APPVERSION = "1.2.0" # application version

class ConfigFile(object):

    def __init__(self, infilename='config.xml', *args, **kwargs):
        self.xmlfile = infilename
        self.namelist = {}
        self.parseConfigs()

    def parseConfigs(self):
        tree = ET.parse(self.xmlfile)
        root = tree.getroot()
        self.root = root
        self.tree = tree
        namelist_image      = {}
        namelist_control    = {}
        namelist_style      = {}
        namelist_histplot   = {}
        namestring_image    = ['width', 'height', 'savePath', 'saveImgName', 'saveImgExt', 'saveIntName', 'saveIntExt', 'cmFavor']
        namestring_control  = ['frequency', 'imgsrcPV', 'imgsrcPVlist']
        namestring_histplot = ['heightRatio']
        namestring_style    = ['backgroundColor']
        for group in root.iter('group'):
            if group.get('name') == 'Image':
                namelist_image = {s:group.find('properties').get(s) for s in namestring_image}
            elif group.get('name') == 'Control':
                namelist_control   = {s:group.find('properties').get(s) for s in namestring_control}
            elif group.get('name') == 'Style':
                namelist_style  = {s:group.find('properties').get(s) for s in namestring_style}
            elif group.get('name') == 'HistPlot':
                namelist_histplot  = {s:group.find('properties').get(s) for s in namestring_histplot}
        self.namelist.update(namelist_image)
        self.namelist.update(namelist_control)
        self.namelist.update(namelist_style)
        self.namelist.update(namelist_histplot)

    def getConfigs(self):
        return self.namelist
    
    def updateConfigs(self, params_dict, savetofile=None):
        if not savetofile:
            savetofile = self.xmlfile
        for p in self.root.iter('properties'):
            for k in params_dict.keys():
                if p.get(k):
                    p.set(k, params_dict[k])
        self.tree.write(savetofile)
        #print ET.tostring(self.root)

class ImageViewer(wx.Frame):
    def __init__(self, parent, size = (800, 600), **kwargs):
        super(self.__class__, self).__init__(parent = parent, size = size, id = wx.ID_ANY, name = 'imageviewer', **kwargs) #style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        self.parent = parent
        self.cmlist_seq1 = ['Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'Oranges', 
                            'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu','Reds', 
                            'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']
        self.cmlist_seq2 = ['afmhot', 'autumn', 'bone', 'cool', 'copper', 'gist_heat', 
                            'gray', 'hot', 'pink', 'spring', 'summer', 'winter']
        self.cmlist_dive = ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr', 'RdBu', 
                            'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral', 'seismic']
        self.cmlist_qual = ['Accent', 'Dark2', 'Paired', 'Pastel1',
                            'Pastel2', 'Set1', 'Set2', 'Set3']
        self.cmlist_misc = ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                            'brg', 'CMRmap', 'cubehelix', 'gnuplot', 'gnuplot2', 
                            'gist_ncar', 'nipy_spectral', 'jet', 'rainbow',
                            'gist_rainbow', 'hsv', 'flag', 'prism']
        self.cmlist = {'Sequential-I' : self.cmlist_seq1,
                       'Sequential-II': self.cmlist_seq2,
                       'Diverging'    : self.cmlist_dive,
                       'Qualitative'  : self.cmlist_qual,
                       'Miscellaneous': self.cmlist_misc}
        
        self.rcmflag = '' # flag for reverse colormap
        self.configlist = {} # configurations dict
        self.xmlconfig = {} # xml config class

        self.loadConfig()
        #self.printConfig() # just for debug
        self.Bind(wx.EVT_CLOSE, self.onExit)
        self.InitUI()

    def loadConfig(self, configfilename = 'config.xml'):
        if (configfilename == None) or (not os.path.isfile(configfilename)):
            configfilename = funutils.getFilename(self)
        self.xmlconfig = ConfigFile(configfilename)
        namelist = self.xmlconfig.getConfigs()

        # Image
        self.wpx, self.hpx = int(float(namelist['width'])), int(float(namelist['height']))
        dirdate = time.strftime('%Y%m%d', time.localtime())
        self.save_path_str_head = os.path.expanduser(namelist['savePath'])
        self.save_path_str      = os.path.join(self.save_path_str_head, dirdate)
        self.save_img_name_str = namelist['saveImgName']
        self.save_img_ext_str  = namelist['saveImgExt']
        self.save_int_name_str = namelist['saveIntName']
        self.save_int_ext_str  = namelist['saveIntExt']

        self.cmlist_favo = namelist['cmFavor'].split()
        self.cmlist['Favorites'] = self.cmlist_favo

        # Control
        self.timer_freq = int(float(namelist['frequency']))
        self.timer_msec = 1./self.timer_freq*1000 
        self.imgsrcPV     = namelist['imgsrcPV']
        self.imgsrcPVlist = namelist['imgsrcPVlist'].split()

        # Style
        self.bkgdcolor    = funutils.hex2rgb(namelist['backgroundColor'])

        # HistPlot
        self.heightRatio  = float(namelist['heightRatio'])

        self.configdict = namelist

    def printConfig(self):
        for (key,value) in sorted(self.configdict.items()):
            print("%s --- %s" % (key, value))

    def InitUI(self):
        self.createMenubar()
        self.createPanel()
        self.createStatusbar()

    def createMenubar(self):
        self.menubar = wx.MenuBar()
        
        ## File menu
        fileMenu = wx.Menu()
        openItem = fileMenu.Append(wx.ID_OPEN, '&Open file\tCtrl+O', 
                'Open file to view')
        saveItem = fileMenu.Append(wx.ID_SAVE, '&Save plot\tCtrl+S', 
                'Save figure to file')
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT, 'E&xit\tCtrl+W',
                'Exit window')
        self.Bind(wx.EVT_MENU, self.onOpen, id = wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.onSave, id = wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.onExit, id = wx.ID_EXIT)
        
        ## Configurations menu
        configMenu = wx.Menu()
        loadConfigItem = configMenu.Append(wx.ID_ANY, 'Load from file\tCtrl+Shift+L',
                'Loading configurations from file')
        saveConfigItem = configMenu.Append(wx.ID_ANY, 'Save to file\tCtrl+Shift+S',
                'Saving configurations to file')
        appsConfigItem = configMenu.Append(wx.ID_ANY, 'Preferences\tCtrl+Shift+I',
                'Configurations for application')
        self.Bind(wx.EVT_MENU, self.onConfigApps, id = appsConfigItem.GetId())
        self.Bind(wx.EVT_MENU, self.onConfigLoad, id = loadConfigItem.GetId())
        self.Bind(wx.EVT_MENU, self.onConfigSave, id = saveConfigItem.GetId())
        
        ## Methods menu
        methMenu = wx.Menu()
        showIntItem   = methMenu.Append(wx.ID_ANY, 'Show intensity\tCtrl+Shift+V', 'Monitor intensity')
        showXhistItem = methMenu.Append(wx.ID_ANY, 'Show hist-X\tAlt+X', 'Show histogram along X-axis', kind = wx.ITEM_CHECK)
        showYhistItem = methMenu.Append(wx.ID_ANY, 'Show hist-Y\tAlt+Y', 'Show histogram along Y-axis', kind = wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.onShowInt,   id =   showIntItem.GetId())
        self.Bind(wx.EVT_MENU, self.onShowXhist, id = showXhistItem.GetId())
        self.Bind(wx.EVT_MENU, self.onShowYhist, id = showYhistItem.GetId())

        ## Help menu
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT, '&About\tF1',
                'Show about information')
        self.Bind(wx.EVT_MENU, self.onAbout, id = wx.ID_ABOUT)
        
        ## make menu
        self.menubar.Append(fileMenu,   '&File')
        self.menubar.Append(configMenu, '&Configurations')
        self.menubar.Append(methMenu,   '&Methods')
        self.menubar.Append(helpMenu,   '&Help')
        
        ## set menu
        self.SetMenuBar(self.menubar)

    def onOpen(self, event):
        pass

    def onSave(self, event):
        if not os.path.exists(self.save_path_str):
            os.system('mkdir -p' + ' ' + self.save_path_str) # I've not found pure python way (simple) to do that yet.
        filelabel = time.strftime('%H%m%S', time.localtime())
        savetofilename = self.save_path_str + '/' + self.save_img_name_str + filelabel + self.save_img_ext_str
        self.imgpanel.figure.savefig(savetofilename)
        hintText = 'Image file: ' + savetofilename + ' was saved.'
        self.statusbar.SetStatusText(hintText)

    def onShowInt(self, event):
        self.menuShowInt = ShowIntPanel(self)
        self.menuShowInt.SetTitle('Image Intensity Monitor')
        #self.menuShowInt.SetSize((620,550))
        self.menuShowInt.Show()

    def onShowXhist(self, event):
        flag = not self.imgpanel.linex.get_visible()
        self.imgpanel.linex.set_visible(flag)

    def onShowYhist(self, event):
        flag = not self.imgpanel.liney.get_visible()
        self.imgpanel.liney.set_visible(flag)

    def onConfigApps(self, event):
        self.menuAppConfig = AppConfigPanel(self)
        self.menuAppConfig.SetTitle('Application Preferences')
        #self.menuAppConfig.SetSize((580,450))
        self.menuAppConfig.Show()

    def onConfigLoad(self, event):
        self.loadConfig(None)
        self.onUpdateUI()

    def onConfigSave(self, event):
        dlg = wx.FileDialog(self, "Save present configurations as", wildcard = 'XML files (*.xml)|*.xml', style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_CANCEL:
            return
        savetofilename = dlg.GetPath()
        self.xmlconfig.updateConfigs(self.configdict, savetofilename)
        self.statusbar.SetStatusText('Present configurations were just saved to ' + savetofilename + '.')
        dlg.Destroy()

    def onExit(self, event):
        dial = wx.MessageDialog(self, message = "Are you sure to exit this application?",
                                caption = "Exit Warning",
                                style = wx.YES_NO | wx.NO_DEFAULT | wx.CENTRE | wx.ICON_QUESTION)
        if dial.ShowModal() == wx.ID_YES:
            self.Destroy()

    def onAbout(self, event):
        try:
            from wx.lib.wordwrap import wordwrap
        except:
            dial = wx.MessageDialog(self, message = u"Cannot show about information, sorry!",
                    caption = u"Unknow Error", 
                    style = wx.OK | wx.CANCEL | wx.ICON_ERROR | wx.CENTRE)
            if dial.ShowModal() == wx.ID_OK:
                dial.Destroy()
        info = wx.AboutDialogInfo()
        info.Name = "Image Viewer"
        info.Version = APPVERSION
        info.Copyright = "(C) 2014-2015 Tong Zhang, SINAP, CAS"
        info.Description = wordwrap(
            "This application is created for being an profile/image monitor and image data processing.\n"

            "It is designed by Python language, using GUI module of wxPython.",
            350, wx.ClientDC(self))
        info.WebSite = ("http://everyfame.me", "Image Viewer home page")
        info.Developers = [ "Tong Zhang <zhangtong@sinap.ac.cn>"]
        licenseText = "Image Viewer is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.\n" + "\nImage Viewer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n" + "\nYou should have received a copy of the GNU General Public License along with Image Viewer; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA"
        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))
        wx.AboutBox(info)

    def onUpdateUI(self):
        self.imgsrc_tc.SetValue(self.imgsrcPV)
        self.panel.SetBackgroundColour(self.bkgdcolor)
        self.imgpanel.setColor(self.bkgdcolor) # make color as private var
        self.imgpanel.repaint() # rewrite repaint func
        self.imgcm.setColor(self.bkgdcolor)
        self.imgcm.repaint()

    def createStatusbar(self):
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusWidths([-4, -1])
        self.statusbar.SetStatusText(u'ImageViewer powered by Python' ,0)
        versionfield =  0*' ' + time.strftime('%Y-%m-%d', time.localtime()) + ' ' + '(Version: ' + APPVERSION + ')'
        #print type(versionfield)
        self.statusbar.SetStatusText(versionfield, 1)

    def createPanel(self):
        self.panel = wx.Panel(self, id = wx.ID_ANY)
        self.panel.SetBackgroundColour(self.bkgdcolor)

        vbox = wx.BoxSizer(wx.VERTICAL)
        ## title and horizontal line
        title_st = self.createStaticText(self.panel,
                label = u'Image Viewer', style = wx.ALIGN_CENTER,
                fontsize = 20, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'blue')
        vbox.Add(title_st, flag = wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER, border = 10)
        hline = wx.StaticLine(self.panel, style = wx.LI_HORIZONTAL)
        vbox.Add((-1, 10))
        vbox.Add(hline, proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 28)

        ## hbox to put left and right panels
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        ## left panel
        vboxleft  = wx.BoxSizer(wx.VERTICAL)
        
        ## StaticText for time indication
        self.timenow_st = self.createStaticText(self.panel,
                label = u'2015-02-11 15:10:16 CST', style = wx.ALIGN_CENTER,
                fontsize = 12, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'black')

        self.imgpanel = ImagePanel(self.panel, figsize = (12,12), dpi = 75, bgcolor = self.bkgdcolor, heightratio = self.heightRatio)
        
        vboxleft.Add(self.timenow_st, proportion = 0, flag = wx.ALIGN_CENTER | wx.TOP, border = 10)
        vboxleft.Add(self.imgpanel, proportion = 1, flag = wx.EXPAND | wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT | wx.BOTTOM, border = 10)

        hbox.Add(vboxleft, proportion = 8, flag = wx.EXPAND | wx.LEFT, border = 8)

        ## separation line
        vline = wx.StaticLine(self.panel, style = wx.LI_VERTICAL)
        hbox.Add(vline, proportion = 0, flag = wx.EXPAND | wx.TOP | wx.BOTTOM, border = 20)
        
        ## right panel
        vboxright = wx.BoxSizer(wx.VERTICAL)

        imgsrc_st = self.createStaticText(self.panel,
                label = u'Image Source:', style = wx.ALIGN_LEFT,
                fontsize = 10, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'black')
        ## define pv value here!
        self.imgsrc_tc = wx.TextCtrl(self.panel, value = self.imgsrcPV,style=wx.TE_PROCESS_ENTER)
        
        ## add/remove pv from imgsrcPVlist
        self.addpvbtn = wx.BitmapButton(self.panel, bitmap = resutils.addicon.GetBitmap())
        self.rmpvbtn  = wx.BitmapButton(self.panel, bitmap = resutils.delicon.GetBitmap())

        pvbox = wx.BoxSizer(wx.HORIZONTAL)
        pvbox.Add(self.imgsrc_tc, proportion = 1, flag = wx.EXPAND | wx.ALIGN_LEFT | wx.RIGHT, border = 8)
        pvbox.Add(self.addpvbtn,  flag = wx.ALIGN_CENTER_VERTICAL)
        pvbox.Add(self.rmpvbtn,   flag = wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border = 6)
        
        ## color map
        cm_st = self.createStaticText(self.panel,
                label = u'Color Map:', style = wx.ALIGN_LEFT,
                fontsize = 10, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'black')
        ## combobox for color maps
        self.cmlist_cb = wx.ComboBox(self.panel, value = 'Favorites', choices = sorted(self.cmlist.keys()), style = wx.CB_READONLY)
        ## list one of classified color map 
        self.cm_cb = wx.ComboBox(self.panel, value = self.cmlist['Favorites'][0], choices = self.cmlist['Favorites'], style = wx.CB_READONLY)
        ## book and unbook btn
        #self.bookbtn   = wx.BitmapButton(self.panel, bitmap = wx.BitmapFromImage(wx.Image('add.png')))
        #self.unbookbtn = wx.BitmapButton(self.panel, bitmap = wx.BitmapFromImage(wx.Image('remove.png')))
        self.bookbtn   = wx.BitmapButton(self.panel, bitmap = resutils.addicon.GetBitmap())
        self.unbookbtn = wx.BitmapButton(self.panel, bitmap = resutils.delicon.GetBitmap())
        ## color range box
        cr_st = self.createStaticText(self.panel,
                label = u'Color Range:', style = wx.ALIGN_LEFT,
                fontsize = 10, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'black')
        min_st = self.createStaticText(self.panel,
                label = u'min:', style = wx.ALIGN_LEFT,
                fontsize = 8, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'black')
        max_st = self.createStaticText(self.panel,
                label = u'max:', style = wx.ALIGN_LEFT,
                fontsize = 8, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'black')
        ### get the cmin and cmax from imgpanel object
        cmin_now = self.imgpanel.cmin
        cmax_now = self.imgpanel.cmax
        ### initial values for min&max sliders
        self.min_value_st = self.createStaticText(self.panel,
                label = ('%.1f' % (cmin_now)), style = wx.ALIGN_RIGHT,
                fontsize = 8, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'blue')
        self.max_value_st = self.createStaticText(self.panel,
                label = ('%.1f' % (cmax_now)), style = wx.ALIGN_RIGHT,
                fontsize = 8, fontweight = wx.FONTWEIGHT_NORMAL,
                fontcolor = 'blue')
        self.min_slider = wx.Slider(self.panel, id = wx.ID_ANY, value = cmin_now, minValue = cmin_now, maxValue = cmax_now)
        self.max_slider = wx.Slider(self.panel, id = wx.ID_ANY, value = cmax_now, minValue = cmin_now, maxValue = cmax_now)
        
        ## colormap line: st + combox for cm categories
        cmstbox = wx.BoxSizer(wx.HORIZONTAL)
        cmstbox.Add(cm_st, flag = wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border = 10)
        cmstbox.Add(self.cmlist_cb, proportion = 1, flag = wx.ALIGN_RIGHT)

        ## selected colormap + add/remove to/from bookmarks btn
        cbbookbox = wx.BoxSizer(wx.HORIZONTAL)
        cbbookbox.Add(self.cm_cb, proportion = 1, flag = wx.EXPAND | wx.ALIGN_LEFT | wx.RIGHT, border = 8)
        cbbookbox.Add(self.bookbtn,   flag = wx.ALIGN_CENTER_VERTICAL)
        cbbookbox.Add(self.unbookbtn, flag = wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border = 6)

        ## show the selected colormap image
        self.imgcm = ImageColorMap(self.panel, figsize = (0.8,0.2),  dpi = 75, bgcolor = self.bkgdcolor)
        
        ## checkbox for reverse colormap
        self.rcmchkbox = wx.CheckBox(self.panel, label = u'Reverse Colormap')

        ## colorrange box
        crbox = wx.FlexGridSizer(2, 3, 6, 6)
        crbox.Add(min_st,            proportion = 0, flag = wx.LEFT | wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        crbox.Add(self.min_slider,   proportion = 1, flag = wx.EXPAND | wx.ALIGN_LEFT)
        crbox.Add(self.min_value_st, proportion = 0, flag = wx.ALIGN_RIGHT)
        crbox.Add(max_st,            proportion = 0, flag = wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        crbox.Add(self.max_slider,   proportion = 1, flag = wx.EXPAND | wx.ALIGN_LEFT)
        crbox.Add(self.max_value_st, proportion = 0, flag = wx.ALIGN_RIGHT)
        crbox.AddGrowableCol(1)
        ##
        vboxright.Add(imgsrc_st,      flag = wx.TOP, border = 25)
        vboxright.Add(pvbox, flag = wx.EXPAND | wx.TOP, border = 10)
        ##
        vboxright.Add((-1,25))
        vboxright.Add(cmstbox,   flag = wx.EXPAND)
        vboxright.Add(cbbookbox, flag = wx.EXPAND | wx.TOP, border = 10)
        """
        ## put rcmchkbox and imgcm into hbox3
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.imgcm, flag = wx.ALIGN_LEFT)
        hbox3.Add(self.rcmchkbox, flag = wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, border = 5)
        vboxright.Add(hbox3, flag = wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT | wx.EXPAND | wx.TOP, border = 10)
        """
        vboxright.Add(self.rcmchkbox, flag = wx.ALIGN_LEFT | wx.EXPAND | wx.TOP, border = 10)
        vboxright.Add(self.imgcm,     flag = wx.ALIGN_CENTER | wx.EXPAND | wx.TOP, border = 10)
        ##
        vboxright.Add(cr_st, flag = wx.TOP, border = 25)
        vboxright.Add(crbox, flag = wx.EXPAND | wx.TOP, border = 10)

        ## for debug: add a statictext and button to vboxright sizer 2015.Feb.11
        self.daqtgl_btn = wx.Button(self.panel,     label = 'DAQ START')
        self.inten_st   = wx.StaticText(self.panel, label = 'Intensity:')
        self.inten_val  = wx.StaticText(self.panel, label = '0')
        hbox_int = wx.BoxSizer(wx.HORIZONTAL)
        hbox_int.Add(self.inten_st,  proportion = 0, flag = wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        hbox_int.Add(self.inten_val, proportion = 1, flag = wx.EXPAND | wx.ALIGN_RIGHT | wx.LEFT, border = 10)
        ## add color range for imgsrc
        self.imgcr_st     = wx.StaticText(self.panel, label = 'CR of Image:')
        self.imgcr_min_tc = wx.TextCtrl(self.panel, value = '0'  )
        self.imgcr_max_tc = wx.TextCtrl(self.panel, value = '200')
        hbox_imgcr = wx.BoxSizer(wx.HORIZONTAL)
        hbox_imgcr.Add(self.imgcr_st,     proportion = 0, flag = wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
        hbox_imgcr.Add(self.imgcr_min_tc, proportion = 1, flag = wx.EXPAND | wx.ALIGN_RIGHT | wx.RIGHT | wx.LEFT, border = 5)
        hbox_imgcr.Add(self.imgcr_max_tc, proportion = 1, flag = wx.EXPAND | wx.ALIGN_RIGHT)

        vboxright.Add(hbox_imgcr, proportion = 0, flag = wx.EXPAND | wx.ALIGN_CENTER | wx.TOP, border = 20)
        vboxright.Add(hbox_int,   proportion = 0, flag = wx.EXPAND | wx.ALIGN_CENTER | wx.TOP, border = 20)
        vboxright.Add(self.daqtgl_btn, flag = wx.ALIGN_RIGHT | wx.TOP, border = 20)

        ##
        hbox.Add(vboxright, proportion = 3, flag = wx.EXPAND | wx.LEFT | wx.RIGHT, border = 10)
       
        ## set sizer
        vbox.Add(hbox, proportion = 1, flag = wx.EXPAND | wx.ALIGN_CENTER)
        self.panel.SetSizer(vbox)
        osizer = wx.BoxSizer(wx.HORIZONTAL)
        osizer.Add(self.panel, proportion = 1, flag = wx.EXPAND)
        self.SetSizerAndFit(osizer)

        ### event bindings

        ## add input pv namestring to imgsrcPVlist or not
        self.Bind(wx.EVT_BUTTON, self.onAddPV, self.addpvbtn)
        self.Bind(wx.EVT_BUTTON, self.onRmPV,  self.rmpvbtn )

        ## colormap categories
        self.Bind(wx.EVT_COMBOBOX, self.onSetCmclass, self.cmlist_cb)

        ## color map value from specific category
        self.Bind(wx.EVT_COMBOBOX, self.onSetColormap, self.cm_cb)

        ## add selected colormap to favorites or not
        self.Bind(wx.EVT_BUTTON, self.onBookmark,   self.bookbtn  )
        self.Bind(wx.EVT_BUTTON, self.onUnBookmark, self.unbookbtn)

        ## color range min and max sliders
        self.Bind(wx.EVT_SCROLL, self.onSetColorRange, self.min_slider)
        self.Bind(wx.EVT_SCROLL, self.onSetColorRange, self.max_slider)

        ## when reverse color map checked/unchecked
        self.Bind(wx.EVT_CHECKBOX, self.onCheckRCM, self.rcmchkbox, self.cm_cb)

        ## bind self.imgsrc_tc
        self.Bind(wx.EVT_TEXT_ENTER, self.onSetImgSrc, self.imgsrc_tc)

        ## timer for update image
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER,  self.onUpdate, self.timer     )
        self.Bind(wx.EVT_BUTTON, self.onDAQbtn, self.daqtgl_btn)

        ## another timer for showing time now
        self.timernow = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTickTime, self.timernow)

        ## start timernow (clock)
        self.timernow.Start(1000)

    def onTickTime(self, event):
        fmt='%Y-%m-%d %H:%M:%S %Z'
        self.timenow_st.SetLabel(time.strftime(fmt, time.localtime()))

    def onDAQbtn(self, event):
        label = event.GetEventObject().GetLabel()
        try:
            isinstance(self.mypv, epics.pv.PV)
        except AttributeError:
            self.mypv = epics.PV(self.imgsrc_tc.GetValue(), auto_monitor = True)

        if self.timer.IsRunning():
            self.timer.Stop()
            self.min_slider.Enable()
            self.max_slider.Enable()
            self.daqtgl_btn.SetLabel('DAQ START')
        else:
            self.timer.Start(self.timer_msec)
            self.min_slider.Disable()
            self.max_slider.Disable()
            self.daqtgl_btn.SetLabel('DAQ STOP')

    def onUpdate(self, event):
        if self.mypv.connected == True:
            self.inten_val.SetLabel("%.5e" % (np.sum(self.mypv.get())))

            #self.wpx, self.hpx = 494, 659
            self.imgpanel.z = self.mypv.get()[0:self.wpx*self.hpx].reshape((self.wpx,self.hpx))
            try:
                cmin_now = float(self.imgcr_min_tc.GetValue())
                cmax_now = float(self.imgcr_max_tc.GetValue())
            except ValueError:
                cmin_now = None
                cmax_now = None
            self.imgpanel.im.set_clim(vmin = cmin_now, vmax= cmax_now)
            self.imgpanel.im.set_array(self.imgpanel.z)
            self.imgpanel.repaint()
        else:
            dial = wx.MessageDialog(self, message = u"Lost connection, may be caused by network error or the IOC server is down.",
                    caption = u"Lost Connection", 
                    style = wx.OK | wx.CANCEL | wx.ICON_ERROR | wx.CENTRE)
            if dial.ShowModal() == wx.ID_OK:
                dial.Destroy()
    
    def onSetImgSrc(self, event):
        """
        set image data source and show in the image panel
        """
        self.mypv = epics.PV(event.GetEventObject().GetValue(), auto_monitor = True)
        #self.wpx, self.hpx = 494, 659
        self.imgpanel.z = self.mypv.get()[0:self.wpx*self.hpx].reshape((self.wpx,self.hpx))
        self.imgpanel.cmin = self.imgpanel.z.min()
        self.imgpanel.cmax = self.imgpanel.z.max()
        cmin_now = self.imgpanel.cmin
        cmax_now = self.imgpanel.cmax
        # update self.min_slider and self.max_slider,
        # as well as self.min_value_st and self.max_value_st
        self.min_value_st.SetLabel('%.1f' % (cmin_now))
        self.max_value_st.SetLabel('%.1f' % (cmax_now))
        self.min_slider.SetMin  (cmin_now)
        self.min_slider.SetMax  (cmax_now)
        self.min_slider.SetValue(cmin_now)
        self.max_slider.SetMin  (cmin_now)
        self.max_slider.SetMax  (cmax_now)
        self.max_slider.SetValue(cmax_now)
        self.imgcr_min_tc.SetValue('%.1f' % cmin_now)
        self.imgcr_max_tc.SetValue('%.1f' % cmax_now)
        self.imgpanel.im.set_clim(vmin = cmin_now, vmax= cmax_now)
        self.imgpanel.im.set_array(self.imgpanel.z)
        self.imgpanel.repaint()

    def onCheckRCM(self, event):
        if event.GetEventObject().IsChecked(): # checked
            self.rcmflag = '_r'
        else:
            self.rcmflag = ''
        cmap = self.cm_cb.GetValue() + self.rcmflag
        self.imgpanel.onSetcm(cmap)
        self.imgcm.onSetcm(cmap)
            
    def onSetColorRange(self, event):
        clickedobj = event.GetEventObject()
        if clickedobj.GetId() == self.min_slider.GetId():
            self.min_value_st.SetLabel('%.1f' % (clickedobj.GetValue()))
        elif clickedobj.GetId() == self.max_slider.GetId():
            self.max_value_st.SetLabel('%.1f' % (clickedobj.GetValue()))

        cmin = self.min_slider.GetValue()
        cmax = self.max_slider.GetValue()
        self.imgpanel.onSetCr(sorted([cmin, cmax]))

    def onBookmark(self, event):
        cmvalue = self.cm_cb.GetValue()
        if cmvalue not in self.cmlist_favo:
            self.cmlist_favo.append(cmvalue)
        ## update self.cm_cb choices field
        cmclass = self.cmlist_cb.GetValue()
        self.cm_cb.Clear()
        self.cm_cb.AppendItems(self.cmlist[cmclass])

    def onUnBookmark(self, event):
        cmvalue = self.cm_cb.GetValue()
        if cmvalue in self.cmlist_favo:
            self.cmlist_favo.remove(cmvalue)
        ## update self.cm_cb choices field
        cmclass = self.cmlist_cb.GetValue()
        self.cm_cb.Clear()
        self.cm_cb.AppendItems(self.cmlist[cmclass])

    def onAddPV(self, event):
        pvstr = self.imgsrc_tc.GetValue()
        if pvstr not in self.imgsrcPVlist:
            self.imgsrcPVlist.append(pvstr)
        ## update imgsrcPVcb choices field of self.menuAppConfig
        imgsrcPVcb_point = self.menuAppConfig.controlPage.imgsrcPVcb
        imgsrcPVcb_point.Clear()
        imgsrcPVcb_point.AppendItems(self.imgsrcPVlist)

    def onRmPV(self, event):
        pvstr = self.imgsrc_tc.GetValue()
        if pvstr in self.imgsrcPVlist:
            self.imgsrcPVlist.remove(pvstr)
        ## update imgsrcPVcb choices field of self.menuAppConfig
        imgsrcPVcb_point = self.menuAppConfig.controlPage.imgsrcPVcb
        imgsrcPVcb_point.Clear()
        imgsrcPVcb_point.AppendItems(self.imgsrcPVlist)

    def onSetColormap(self, event):
        self.imgpanel.onSetcm(event.GetEventObject().GetValue() + self.rcmflag)
        self.imgcm.onSetcm(event.GetEventObject().GetValue() + self.rcmflag)

    def onSetCmclass(self, event):
        cmclass = event.GetEventObject().GetValue()
        self.cm_cb.Clear()
        self.cm_cb.AppendItems(self.cmlist[cmclass])

    def createStaticText(self, parent, label, style = wx.ALIGN_LEFT, 
            fontname=wx.SYS_SYSTEM_FONT, 
            fontsize=12,
            fontweight=wx.FONTWEIGHT_NORMAL,
            fontcolor='black'):
        font = wx.SystemSettings_GetFont(fontname)
        font.SetPointSize(fontsize)
        font.SetWeight(fontweight)
        st = wx.StaticText(parent = parent, 
                label = label, style = style)
        st.SetFont(font)
        st.SetForegroundColour(fontcolor)
        return st

    def createButton(self, parent, label,
            fontname=wx.SYS_SYSTEM_FONT, 
            fontsize=10,
            fontweight=wx.FONTWEIGHT_NORMAL,
            fontcolor='black'):
        font = wx.SystemSettings_GetFont(fontname)
        font.SetPointSize(fontsize)
        font.SetWeight(fontweight)
        btn = wx.Button(parent = parent, 
                label = label)
        btn.SetFont(font)
        btn.SetForegroundColour(fontcolor)
        return btn

class ConfigNoteBook(wx.Notebook):
    def __init__(self, parent, style = wx.NB_LEFT, *args, **kws):
        super(self.__class__, self).__init__(parent = parent, *args, **kws)
        self.parent = parent
        self.MakePages()
        
    def MakePages(self):
        self.imagePage    =    ImageConfigPanel(self)
        self.stylePage    =    StyleConfigPanel(self)
        self.controlPage  =  ControlConfigPanel(self)
        self.histPlotPage = HistPlotConfigPanel(self)

        self.AddPage(self.imagePage,    'Image'   )
        self.AddPage(self.stylePage,    'Style'   )
        self.AddPage(self.controlPage,  'Control' )
        self.AddPage(self.histPlotPage, 'HistPlot')

class AppConfigPanel(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__(parent = parent,
                id = wx.ID_ANY, style = wx.DEFAULT_FRAME_STYLE, **kwargs)
                #style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX), **kwargs)
        self.parent = parent
        self.InitUI()

    def InitUI(self):
        self.createMenu()
        self.createStatusbar()
        self.createNotebooks()

    def createMenu(self):
        pass

    def createStatusbar(self):
        pass

    def createNotebooks(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # config notebook
        self.configNB = ConfigNoteBook(self, style = wx.NB_TOP)

        # btns
        # btn style
        """
        lbtnfont = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        lbtnfont.SetPointSize(12)
        lbtnfont.SetWeight(wx.FONTWEIGHT_NORMAL)
        lbtnfontcolor = '#FF00B0'
        lbtnfacecolor = '#BFD9F0'
        self.applybtn.SetFont(lbtnfont)
        self.applybtn.SetForegroundColour(lbtnfontcolor)
        self.applybtn.SetBackgroundColour(lbtnfacecolor)
        """

        self.cancelbtn = wx.Button(self, label = 'Cancel')
        self.applybtn  = wx.Button(self, label = 'Apply' )
        self.okbtn     = wx.Button(self, label = 'OK'    )

        self.Bind(wx.EVT_BUTTON, self.onCancelData, self.cancelbtn)
        self.Bind(wx.EVT_BUTTON, self.onApplyData,  self.applybtn )
        self.Bind(wx.EVT_BUTTON, self.onUpdateData, self.okbtn    )

        hboxbtn = wx.BoxSizer(wx.HORIZONTAL)
        hboxbtn.Add(self.cancelbtn, proportion = 0, flag = wx.EXPAND |           wx.BOTTOM, border = 10)
        hboxbtn.Add(self.applybtn,  proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM, border = 10)
        hboxbtn.Add(self.okbtn,     proportion = 0, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM, border = 10)
        
        # set sizer
        vbox.Add(self.configNB, proportion = 1, flag = wx.EXPAND | wx.ALL, border = 15)
        vbox.Add(hboxbtn, flag = wx.ALIGN_RIGHT | wx.RIGHT | wx.TOP, border = 15)
        vbox.Add((-1,10))
        self.SetSizerAndFit(vbox)

        # config pages references:
        self.imagePage    = self.configNB.imagePage
        self.stylePage    = self.configNB.stylePage
        self.controlPage  = self.configNB.controlPage
        self.histPlotPage = self.configNB.histPlotPage
        
        # main App panel reference
        self.thisapp = self.parent

    def onCancelData(self, event):
        self.Close(True)

    def onApplyData(self, event):
        self.setParams()

    def onUpdateData(self, event):
        self.setParams()
        self.Close(True)

    def setParams(self):
        # imagePage
        self.thisapp.wpx = int(self.imagePage.imgwpxtc.GetValue())
        self.thisapp.hpx = int(self.imagePage.imghpxtc.GetValue())
        self.thisapp.save_path_str_head = os.path.expanduser(self.imagePage.pathtc.GetValue())
        self.thisapp.save_path_str = os.path.join(self.thisapp.save_path_str_head, time.strftime('%Y%m%d', time.localtime()))
        self.thisapp.save_img_name_str = self.imagePage.imgnamepretc.GetValue()
        self.thisapp.save_img_ext_str  = self.imagePage.imgnameexttc.GetValue()
        self.thisapp.save_int_name_str = self.imagePage.intnamepretc.GetValue()
        self.thisapp.save_int_ext_str  = self.imagePage.intnameexttc.GetValue()

        # stylePage
        self.thisapp.bkgdcolor = funutils.hex2rgb(self.stylePage.bkgdcolortc.GetValue())

        # controlPage
        self.thisapp.timer_freq = int(self.controlPage.freqtc.GetValue())
        self.thisapp.timer_msec = 1.0/self.thisapp.timer_freq * 1000
        self.thisapp.imgsrcPV   = self.controlPage.imgsrcPVcb.GetValue()

        # histPlotPage
        self.thisapp.heightRatio = float(self.histPlotPage.heightratiotc.GetValue())

        # update parameters
        self.thisapp.configdict['width'          ] = str(self.thisapp.wpx)
        self.thisapp.configdict['height'         ] = str(self.thisapp.hpx)
        self.thisapp.configdict['savePath'       ] = self.thisapp.save_path_str_head
        self.thisapp.configdict['saveImgName'    ] = self.thisapp.save_img_name_str
        self.thisapp.configdict['saveImgExt'     ] = self.thisapp.save_img_ext_str
        self.thisapp.configdict['saveIntName'    ] = self.thisapp.save_int_name_str
        self.thisapp.configdict['saveIntExt'     ] = self.thisapp.save_int_ext_str
        self.thisapp.configdict['frequency'      ] = str(self.thisapp.timer_freq)  
        self.thisapp.configdict['imgsrcPV'       ] = self.thisapp.imgsrcPV
        self.thisapp.configdict['imgsrcPVlist'   ] = ' '.join(str(i) + ' ' for i in self.thisapp.imgsrcPVlist).rstrip()
        self.thisapp.configdict['cmFavor'        ] = ' '.join(str(i) + ' ' for i in self.thisapp.cmlist_favo).rstrip()
        self.thisapp.configdict['backgroundColor'] = self.stylePage.bkgdcolortc.GetValue()
        self.thisapp.configdict['heightRatio'    ] = str(self.thisapp.heightRatio)
        self.thisapp.xmlconfig.updateConfigs(self.thisapp.configdict)
        self.thisapp.onUpdateUI()
        
        # for debug
        #self.thisapp.printConfig()
 

class ImageConfigPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__(parent = parent, id = wx.ID_ANY, **kwargs)
        self.parent = parent
        self.thisapp = self.parent.parent.parent
        self.initUI()
    
    def initUI(self):
        self.initConfig()
        self.createPanel()

    def initConfig(self):
        self.bkgdcolor   = wx.BLUE
        self.fontcolor   = wx.BLACK
        self.fontptsize  = 10
        self.fontweight  = wx.FONTWEIGHT_NORMAL

    def createPanel(self):
        #self.SetBackgroundColour(self.bkgdcolor)

        vboxsizer = wx.BoxSizer(wx.VERTICAL)
        
        """
        sbfont.SetPointSize(self.fontptsize)
        sbfont.SetWeight(self.fontweight)
        sbfontcolor = 'GREY'
        sbox.SetFont(sbfont)
        sbox.SetForegroundColour(sbfontcolor)
        sbsizer = wx.StaticBoxSizer(sbox, orient = wx.VERTICAL)
        """

        #### input items
        gs = wx.GridBagSizer(5, 5)
        imgwpxst     = wx.StaticText(self, label = u'Image Width [px]',         style = wx.ALIGN_LEFT)
        imghpxst     = wx.StaticText(self, label = u'Image Height [px]',        style = wx.ALIGN_LEFT)
        pathst       = wx.StaticText(self, label = u'Save Figure to Path',      style = wx.ALIGN_LEFT)
        imgnameprest = wx.StaticText(self, label = u'Image Name Prefix',        style = wx.ALIGN_LEFT)
        imgnameextst = wx.StaticText(self, label = u'Image Name Extension',     style = wx.ALIGN_LEFT)
        intnameprest = wx.StaticText(self, label = u'Intensity Name Prefix',    style = wx.ALIGN_LEFT)
        intnameextst = wx.StaticText(self, label = u'Intensity Name Extension', style = wx.ALIGN_LEFT)

        self.imgwpxtc     = wx.TextCtrl(self, value = str(self.thisapp.wpx),          style = wx.TE_PROCESS_ENTER)
        self.imghpxtc     = wx.TextCtrl(self, value = str(self.thisapp.hpx),          style = wx.TE_PROCESS_ENTER)
        self.pathtc       = wx.TextCtrl(self, value = self.thisapp.save_path_str_head,style = wx.TE_PROCESS_ENTER)
        self.pathtc.SetToolTip(wx.ToolTip('Fullpath (subdired by the date) the config file be saved.'))
        self.pathbtn      = wx.Button(self, label = 'Browse', style = wx.CB_READONLY)
        self.imgnamepretc = wx.TextCtrl(self, value = self.thisapp.save_img_name_str, style = wx.TE_PROCESS_ENTER)
        self.imgnameexttc = wx.ComboBox(self, value = self.thisapp.save_img_ext_str,  style = wx.CB_READONLY, choices = ['.png','.jpg','.jpeg','.svg','.tiff','.eps','.pdf','.ps'])
        self.intnamepretc = wx.TextCtrl(self, value = self.thisapp.save_int_name_str, style = wx.TE_PROCESS_ENTER)
        self.intnameexttc = wx.ComboBox(self, value = self.thisapp.save_int_ext_str,  style = wx.CB_READONLY, choices = ['.png','.jpg','.jpeg','.svg','.tiff','.eps','.pdf','.ps'])

        gs.Add(imgwpxst,          pos = (0, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.imgwpxtc,     pos = (0, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(imghpxst,          pos = (1, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.imghpxtc,     pos = (1, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(pathst,            pos = (2, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.pathtc,       pos = (2, 1), span = (1, 2), flag = wx.EXPAND | wx.LEFT  | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.pathbtn,      pos = (2, 3), span = (1, 1), flag = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(imgnameprest,      pos = (3, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.imgnamepretc, pos = (3, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(imgnameextst,      pos = (4, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.imgnameexttc, pos = (4, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(intnameprest,      pos = (5, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.intnamepretc, pos = (5, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(intnameextst,      pos = (6, 0), span = (1, 1), flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.Add(self.intnameexttc, pos = (6, 1), span = (1, 3), flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        gs.AddGrowableCol(1, 2)
        gs.AddGrowableCol(2, 0)
        vboxsizer.Add(gs, proportion = 0, flag = wx.EXPAND | wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT | wx.TOP, border = 15)

        vboxsizer.Add((-1, 10))
        
        ## set boxsizer
        self.SetSizer(vboxsizer)
        
        ## bind events
        self.Bind(wx.EVT_TEXT_ENTER, self.onUpdateParams,  self.imgwpxtc)
        self.Bind(wx.EVT_TEXT_ENTER, self.onUpdateParams,  self.imghpxtc)
        self.Bind(wx.EVT_BUTTON,     self.onChooseDirpath, self.pathbtn     )

    def onChooseDirpath(self, event):
        dlg = wx.DirDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            dirpath = dlg.GetPath()
            self.pathtc.SetValue(dirpath)
        dlg.Destroy()

    def onUpdateParams(self, event):
        obj = event.GetEventObject() 
        try:
            int(obj.GetValue())
        except ValueError:
            dial = wx.MessageDialog(self, message = u"Error, please input an integer number!",
                    caption = u"Input Error", 
                    style = wx.OK | wx.CANCEL | wx.ICON_ERROR | wx.CENTRE)
            if dial.ShowModal() == wx.ID_OK:
                obj.SetValue('')
                dial.Destroy()

class StyleConfigPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__(parent = parent, id = wx.ID_ANY, **kwargs)
        self.parent = parent
        self.thisapp = self.parent.parent.parent
        self.initUI()
    
    def initUI(self):
        self.initConfig()
        self.createPanel()

    def initConfig(self):
        self.bkgdcolor   = wx.BLUE
        self.fontcolor   = wx.BLACK
        self.fontptsize  = 10
        self.fontweight  = wx.FONTWEIGHT_NORMAL

    def createPanel(self):
        vboxsizer = wx.BoxSizer(wx.VERTICAL)
        
        bkgdcolorst  = wx.StaticText(self, label = u'Background Color',  style = wx.ALIGN_LEFT)

        self.bkgdcolortc  = wx.TextCtrl(self, value = funutils.rgb2hex(self.thisapp.bkgdcolor).upper(), style = wx.CB_READONLY)
        self.bkgdcolorbtn = wx.Button(self, label = 'Choose Color')

        hboxbtn = wx.BoxSizer(wx.HORIZONTAL)
        hboxbtn.Add(bkgdcolorst,       proportion = 0, flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        hboxbtn.Add(self.bkgdcolortc,  proportion = 3, flag = wx.EXPAND | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        hboxbtn.Add(self.bkgdcolorbtn, proportion = 2, flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        vboxsizer.Add(hboxbtn, flag = wx.EXPAND | wx.ALL, border = 15)

        vboxsizer.Add((-1, 10))
        
        ## set boxsizer
        self.SetSizer(vboxsizer)
        
        ## bind events
        self.Bind(wx.EVT_BUTTON, self.onChooseColor, self.bkgdcolorbtn)

    def onChooseColor(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True) # only windows
        if dlg.ShowModal() == wx.ID_OK:
            color = dlg.GetColourData().GetColour()
            self.bkgdcolortc.SetValue(color.GetAsString(wx.C2S_HTML_SYNTAX))
        dlg.Destroy()

class ControlConfigPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__(parent = parent, id = wx.ID_ANY, **kwargs)
        self.parent = parent
        self.thisapp = self.parent.parent.parent
        self.initUI()

    def initUI(self):
        self.initConfig()
        self.createPanel()

    def initConfig(self):
        self.bkgdcolor   = wx.BLUE
        self.fontcolor   = wx.BLACK
        self.fontptsize  = 10
        self.fontweight  = wx.FONTWEIGHT_NORMAL

    def createPanel(self):
        vboxsizer = wx.BoxSizer(wx.VERTICAL)
        
        # frequency
        freqst       = wx.StaticText(self, label = u'Monitor Frequency [Hz]',   style = wx.ALIGN_RIGHT)
        self.freqtc  = wx.TextCtrl(self, value = str(self.thisapp.timer_freq),  style = wx.TE_PROCESS_ENTER)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(freqst,       proportion = 0, flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        hbox1.Add(self.freqtc,  proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        vboxsizer.Add(hbox1, flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border = 10)

        # PV list
        imgsrcPVst      = wx.StaticText(self, label = u'Image PV Name', style = wx.ALIGN_RIGHT)
        self.imgsrcPVcb = wx.ComboBox(self, value = self.thisapp.imgsrcPV,  style = wx.CB_READONLY,
                                            choices = sorted(self.thisapp.imgsrcPVlist))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(imgsrcPVst,       proportion = 0, flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        hbox2.Add(self.imgsrcPVcb,  proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        vboxsizer.Add(hbox2, flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border = 10)
        
        vboxsizer.Add((-1, 10))
        
        ## set boxsizer
        self.SetSizer(vboxsizer)

class HistPlotConfigPanel(wx.Panel):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__(parent = parent, id = wx.ID_ANY, **kwargs)
        self.parent = parent
        self.thisapp = self.parent.parent.parent
        self.initUI()

    def initUI(self):
        self.initConfig()
        self.createPanel()

    def initConfig(self):
        self.bkgdcolor   = wx.BLUE
        self.fontcolor   = wx.BLACK
        self.fontptsize  = 10
        self.fontweight  = wx.FONTWEIGHT_NORMAL

    def createPanel(self):
        vboxsizer = wx.BoxSizer(wx.VERTICAL)

        # height ratio
        heightratiost       = wx.StaticText(self, label = u'Height Ratio',   style = wx.ALIGN_RIGHT)
        self.heightratiotc  = wx.TextCtrl(self, value = str(self.thisapp.heightRatio),  style = wx.TE_PROCESS_ENTER)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(heightratiost,       proportion = 0, flag = wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        hbox1.Add(self.heightratiotc,  proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border = 10)
        vboxsizer.Add(hbox1, flag = wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border = 10)

        vboxsizer.Add((-1, 10))

        ## set boxsizer
        self.SetSizer(vboxsizer)

class ShowIntPanel(wx.Frame):
    def __init__(self, parent, **kwargs):
        super(self.__class__, self).__init__(parent = parent,
                id = wx.ID_ANY, style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX), **kwargs)
        self.parent = parent
        self.x = []
        self.y = []
        self.cnt = 0
        self.InitUI()
    
    def InitUI(self):
        self.createMenu()
        self.createPanel()
        self.createStatusbar()

    def createMenu(self):
        pass

    def createStatusbar(self):
        pass

    def createPanel(self):
        self.panel = wx.Panel(self, id = wx.ID_ANY)
        self.panel.SetBackgroundColour(self.parent.bkgdcolor)

        vbox = wx.BoxSizer(wx.VERTICAL)
        
        sbox = wx.StaticBox(self.panel, id = wx.ID_ANY, 
                label = u'Intensity Monitor', style = wx.ALIGN_LEFT)
        sbfont = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        sbfont.SetPointSize(8)
        sbfont.SetWeight(wx.FONTWEIGHT_NORMAL)
        sbfontcolor = 'GREY'
        sbox.SetFont(sbfont)
        sbox.SetForegroundColour(sbfontcolor)
        sbsizer = wx.StaticBoxSizer(sbox, orient = wx.VERTICAL)

        self.intdisp = ImagePanelxy(self.panel, figsize = (9,7), dpi = 80, bgcolor = self.parent.bkgdcolor)
        sbsizer.Add(self.intdisp, flag = wx.ALIGN_CENTER | wx.ALL, border = 10)

        #### btns
        self.daqbtn  = wx.Button(self.panel, label = 'Start')
        self.savebtn = wx.Button(self.panel, label = 'Save' )
        self.Bind(wx.EVT_BUTTON, self.onTimerControl, self.daqbtn )
        self.Bind(wx.EVT_BUTTON, self.onSaveFigure,   self.savebtn)
        hboxbtn = wx.BoxSizer(orient = wx.HORIZONTAL)
        hboxbtn.Add(self.daqbtn,  proportion = 1, flag = wx.EXPAND | wx.BOTTOM, border = 10)
        hboxbtn.Add(self.savebtn, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM, border = 10)
        sbsizer.Add(hboxbtn, flag = wx.ALIGN_RIGHT | wx.ALL, border = 10)

        vbox.Add(sbsizer, flag = wx.ALL, border = 15)

        self.panel.SetSizer(vbox)
        osizer = wx.BoxSizer(wx.HORIZONTAL)
        osizer.Add(self.panel)
        self.SetSizerAndFit(osizer)

        ## timer for update plotting curve
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onUpdate, self.timer)

    def onTimerControl(self, event):
        label = event.GetEventObject().GetLabel()
        if self.timer.IsRunning():
            self.timer.Stop()
            self.daqbtn.SetLabel('Start')
        else:
            self.timer.Start(self.parent.timer_msec)
            self.daqbtn.SetLabel('Stop')

    def onSaveFigure(self, event):
        if not os.path.exists(self.parent.save_path_str):
            os.system('mkdir -p' + ' ' + self.parent.save_path_str)
        filelabel = time.strftime('%H%m%S', time.localtime())
        savetofilename = self.parent.save_path_str + '/' + self.parent.save_int_name_str + filelabel + self.parent.save_int_ext_str
        self.intdisp.figure.savefig(savetofilename)

    def onUpdate(self, event):
        self.cnt += 1
        self.x.append(self.cnt)
        self.y.append(float(self.parent.inten_val.GetLabel()))
        self.intdisp.x = np.array(self.x)
        self.intdisp.y = np.array(self.y)
        self.intdisp.xyplot.set_marker('o')
        self.intdisp.xyplot.set_markersize(4)
        self.intdisp.xyplot.set_markerfacecolor('b')
        self.intdisp.xyplot.set_markeredgecolor('b')
        self.intdisp.xyplot.set_linestyle('-')
        self.intdisp.xyplot.set_color('r')
        self.intdisp.repaint()

class ImagePanel(wx.Panel):
    def __init__(self, parent, figsize, dpi, bgcolor, heightratio = 0.4, **kwargs):
        super(self.__class__, self).__init__(parent = parent, **kwargs)
        self.parent   = parent
        self.figsize  = figsize
        self.dpi      = dpi
        self.bgcolor  = bgcolor
        self.hratio   = heightratio
        self.figure   = Figure(self.figsize, self.dpi)
        self.canvas   = FigureCanvasWxAgg(self, -1, self.figure)
        self.cmaptype = 'jet'
        self.setColor(self.bgcolor)
        self.onGetData()
        self.doPlot()
        wx.CallAfter(self.fitCanvas) # fit canvas size after initialization

        # resize figure when size event trigged
        self.Bind(wx.EVT_SIZE, self.onSize)

    def setColor(self, rgbtuple = None):
        """Set figure and canvas colours to be the same."""
        if rgbtuple is None:
            rgbtuple = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE).Get()
        clr = [c/255. for c in rgbtuple]
        self.figure.set_facecolor(clr)
        self.figure.set_edgecolor(clr)
        self.canvas.SetBackgroundColour(wx.Colour(*rgbtuple))

    def repaint(self):
        self.onSetHist()
        self.figure.canvas.draw_idle()

    def onSetcm(self, cmap):
        self.cmaptype = cmap
        self.im.set_cmap(self.cmaptype)
        self.im.set_array(self.z)
        self.repaint()

    def onSetHist(self):
        self.histx = self.z.sum(axis = 0)
        self.histy = self.z.sum(axis = 1)
        idxmaxx, idxmaxy = np.where(self.histx==self.histx.max()), np.where(self.histy==self.histy.max())
        self.maxidx, self.maxidy = idxmaxx[0][0], idxmaxy[0][0]
        self.xx = np.arange(self.histx.size) + 1
        self.yy = np.arange(self.histy.size) + 1
        self.linex.set_xdata(self.xx)
        self.linex.set_ydata(self.histx/self.histx.max()*self.maxidy*self.hratio)
        self.liney.set_xdata(self.histy/self.histy.max()*self.maxidx*self.hratio)
        self.liney.set_ydata(self.yy)
        self.xyscalar = [self.xx.min(), self.xx.max(), self.yy.min(), self.yy.max()]
        self.im.set_extent(self.xyscalar)

    def onSetCr(self, crange):
        self.im.set_clim(crange)
        self.repaint()

    def doPlot(self):
        if not hasattr(self, 'axes'):
            self.axes = self.figure.add_subplot(111)
        self.linex, = self.axes.plot(self.xx, self.histx/self.histx.max()*self.maxidy*self.hratio, 'w--')
        self.liney, = self.axes.plot(self.histy/self.histy.max()*self.maxidx*self.hratio, self.yy, 'w--')

        #self.axes.set_title(r'$f(x,y)=\sin x + \cos y$')
        self.im = self.axes.imshow(self.z, aspect = 'equal', cmap = plt.get_cmap(self.cmaptype), 
                                   origin = 'lower left', vmin = self.cmin, vmax = self.cmax)
        self.im.set_extent(self.xyscalar)
        self.linex.set_visible(False)
        self.liney.set_visible(False)
        self.figure.canvas.draw()

    def onGetData(self):
        x = np.arange(100.0)*2*np.pi/50.0
        y = np.arange(100.0)*2*np.pi/50.0
        self.x, self.y = np.meshgrid(x, y)
        self.z = 100*np.sin(self.x) + 100*np.cos(self.y)
        self.cmin = self.z.min()
        self.cmax = self.z.max()
        
        self.histx = self.z.sum(axis = 0)
        self.histy = self.z.sum(axis = 1)
        self.xx = np.arange(self.histx.size)+1
        self.yy = np.arange(self.histy.size)+1
        idxmaxx, idxmaxy = np.where(self.histx==self.histx.max()), np.where(self.histy==self.histy.max())
        self.maxidx, self.maxidy = idxmaxx[0][0], idxmaxy[0][0]
        self.xyscalar = [self.xx.min(), self.xx.max(), self.yy.min(), self.yy.max()]


    def fitCanvas(self):
        self.canvas.SetSize(self.GetSize())
        self.figure.set_tight_layout(True)
        self.figure.subplots_adjust(top  = 0.9999, bottom = 0.0001, 
                                    left = 0.0001, right  = 0.9999)

    def onSize(self, event):
        self.canvas.SetSize(self.GetSize())
        self.figure.set_tight_layout(True)
        self.figure.subplots_adjust(top  = 0.9999, bottom = 0.0001, 
                                    left = 0.0001, right  = 0.9999)
        #heresize = self.GetSize()
        #self.figure.set_size_inches(float(heresize[0])/self.figure.get_dpi(),
        #                            float(heresize[1])/self.figure.get_dpi())

class ImagePanelxy(wx.Panel):
    def __init__(self, parent, figsize, dpi, bgcolor, **kwargs):
        super(self.__class__, self).__init__(parent = parent, **kwargs)
        self.parent  = parent
        self.figsize = figsize
        self.dpi     = dpi
        self.bgcolor = bgcolor
        self.figure = Figure(self.figsize, self.dpi)
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.setColor(self.bgcolor)
        self.onGetData()
        self.doPlot()
        wx.CallAfter(self.fitCanvas) # fit canvas size after initialization

    def setColor(self, rgbtuple = None):
        """Set figure and canvas colours to be the same."""
        if rgbtuple is None:
            rgbtuple = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE).Get()
        clr = [c/255. for c in rgbtuple]
        self.figure.set_facecolor(clr)
        self.figure.set_edgecolor(clr)
        self.canvas.SetBackgroundColour(wx.Colour(*rgbtuple))

    def repaint(self):
        self.xyplot.set_xdata(self.x)
        self.xyplot.set_ydata(self.y)
        self.axes.set_xlim(min(self.x), max(self.x))
        self.axes.set_ylim(min(self.y), max(self.y))
        self.figure.canvas.draw_idle()

    def doPlot(self):
        if not hasattr(self, 'axes'):
            self.axes = self.figure.add_subplot(111)
        self.xyplot, = self.axes.plot(self.x, self.y, '.', markersize = 1)
        self.figure.canvas.draw()

    def onGetData(self):
        #x = np.linspace(-np.pi, np.pi, 100)
        #y = np.sin(x)
        x = y = None
        self.x, self.y = x, y

    def fitCanvas(self):
        self.canvas.SetSize(self.GetSize())
        self.figure.set_tight_layout(True)
        self.figure.subplots_adjust(top  = 0.9999, bottom = 0.0001, 
                                    left = 0.0001, right  = 0.9999)

class ImageColorMap(wx.Panel):
    def __init__(self, parent, figsize, dpi, bgcolor, **kwargs):
        super(self.__class__, self).__init__(parent = parent, **kwargs)
        self.parent  = parent
        self.figsize = figsize
        self.dpi     = dpi
        self.bgcolor = bgcolor
        self.cmin = 0
        self.cmax = 1
        self.figure = Figure(self.figsize, self.dpi)
        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.cmaptype = 'jet'
        self.setColor(self.bgcolor)
        self.onGetData()
        self.doPlot()
        wx.CallAfter(self.fitCanvas)

        # resize figure when size event trigged
        self.Bind(wx.EVT_SIZE, self.onSize)

    def setColor(self, rgbtuple = None):
        """Set figure and canvas colours to be the same."""
        if rgbtuple is None:
            rgbtuple = wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE).Get()
        clr = [c/255. for c in rgbtuple]
        self.figure.set_facecolor(clr)
        self.figure.set_edgecolor(clr)
        self.canvas.SetBackgroundColour(wx.Colour(*rgbtuple))

    def repaint(self):
        self.figure.canvas.draw_idle()

    def onSetCr(self, crange):
        self.im.set_clim(crange)
        self.repaint()

    def onSetcm(self, cmap):
        self.cmaptype = cmap
        self.im.set_cmap(self.cmaptype)
        self.repaint()

    def doPlot(self):
        if not hasattr(self, 'axes'):
            self.axes = self.figure.add_subplot(111)
        self.im = self.axes.imshow(self.z, cmap = plt.get_cmap(self.cmaptype),
                                   origin = 'lower left', vmin = self.cmin, vmax = self.cmax)
        self.axes.set_axis_off()
        self.figure.canvas.draw()

    def onGetData(self):
        g = np.linspace(self.cmin, self.cmax, 80)
        self.z = np.vstack((g,g))

    def fitCanvas(self):
        self.canvas.SetSize(self.GetSize())
        self.figure.set_tight_layout(True)
        self.figure.subplots_adjust(top  = 0.9999, bottom = 0.0001, 
                                    left = 0.0001, right  = 0.9999)

    def onSize(self, event):
        self.canvas.SetSize(self.GetSize())
        self.figure.set_tight_layout(True)
        self.figure.subplots_adjust(top  = 0.9999, bottom = 0.0001, 
                                    left = 0.0001, right  = 0.9999)

def main():
    app = wx.App(redirect = False)
    myframe = ImageViewer(None, title = 'ImageViewer --- Another Profile Monitor')
    myframe.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
