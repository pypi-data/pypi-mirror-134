# -*- coding: utf-8 -*-

"""
Created on Fri Oct 29 09:32:34 2021

@author: Marc Boucsein
"""

import napari
from napari_plugin_engine import napari_hook_implementation
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QListWidgetItem, QLabel, QFileDialog, QCheckBox
from qtpy.QtCore import QEvent, Qt
#from qtpy.QtCore import Signal, QObject, QEvent
from magicgui.widgets import ComboBox, Container, LiteralEvalLineEdit
from packaging.version import Version
from napari.layers import Layer


import numpy as np


import napari_nd_cropper.utils as utils
from superqt import QRangeSlider

from superqt.qtcompat import QtCore
Horizontal = QtCore.Qt.Orientation.Horizontal






class nd_Cropper(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()
        self.viewer = napari_viewer

        

        self.setLayout(QVBoxLayout())
        
        possible_images= [x.name  for x in self.viewer.layers if isinstance(x, napari.layers.image.image.Image)]
        self.Image_select=Container(widgets=[ComboBox(choices=possible_images, label="Select an image:", visible=True)])
        self.layout().addWidget(self.Image_select.native)
        select_layer_name=self.Image_select[0].current_choice
        self.layer_sel=self.viewer.layers[select_layer_name]
        self.layer_sel_non_crop=np.copy(self.layer_sel.data)
        self.layer_sel_non_crop_scale=np.copy(self.layer_sel.scale)
        self.layer_sel_non_crop_trans=np.copy(self.layer_sel.translate)
        self.viewer.layers.selection.active=self.viewer.layers[select_layer_name] 
        
        #create mode widget
        if Version(napari.__version__)>Version('0.4.12'):
           self.crop_modes= ['Drag&Drop', 'Crop via mouse click', 'Crop via layer corner pixels','Crop via slider']
        else:
           self.crop_modes= ['Crop via mouse click', 'Crop via layer corner pixels','Crop via slider'] 
        
        self.crop_modes_widget=Container(widgets=[ComboBox(choices=self.crop_modes, label="Select crop modes:", value='Crop via slider', visible=True)])
        self.layout().addWidget(self.crop_modes_widget.native)


        if self.crop_modes_widget[0].value=='Crop via slider':
           self.w_slider_container_total = QWidget() 
           self.w_slider_container_total.setLayout(QVBoxLayout())
           Slider_list=[] 
           for i in range(self.layer_sel.ndim):
              w_slider_container = QWidget()
              w_slider_container.setLayout(QHBoxLayout())
              w_slider_container.layout().addWidget(QLabel('Axis '+str(i)))
              Rangeslider = QRangeSlider(Horizontal)
              Rangeslider.setRange(0,self.layer_sel.data.shape[i])
              Rangeslider.setValue((0, self.layer_sel.data.shape[i])) 
              Slider_list.append(Rangeslider)
              w_slider_container.layout().addWidget(Rangeslider)
              self.w_slider_container_total.layout().addWidget(w_slider_container)
              
           for axis, slider in enumerate(Slider_list):
               slider.valueChanged.connect(lambda event, Slider_list=Slider_list: self.crop_slider(event, Slider_list )) 
              
              
           w_slider_reset = QWidget()
           w_slider_reset.setLayout(QHBoxLayout())
           self.button_slider_reset=QPushButton("Reset", self)
           w_slider_reset.layout().addWidget(self.button_slider_reset)
           self.w_slider_container_total.layout().addWidget(w_slider_reset)
            
           
           self.layout().addWidget(self.w_slider_container_total)
        
        
        
        
        self.Image_select.changed.connect(self.selected_layer)
        self.Image_select.changed.connect(self.add_widgets_crop_modes)
    
        self.viewer.layers.events.inserted.connect(self.change_combo)
        self.viewer.layers.events.inserted.connect(self.remove_combo)
        self.viewer.layers.events.inserting.connect(self.on_off_drag_drop)
        self.viewer.layers.events.inserted.connect(self.on_off_drag_drop)
     
        self.viewer.layers.events.removed.connect(self.change_combo)
        self.viewer.layers.events.removed.connect(self.remove_combo)
        self.viewer.layers.events.removing.connect(self.on_off_drag_drop)
        self.viewer.layers.events.removed.connect(self.on_off_drag_drop)

        self.viewer.layers.selection.events.changed.connect(self.on_off_drag_drop)

        self.crop_modes_widget.changed.connect(self.selected_layer)
        self.crop_modes_widget.changed.connect(self.add_widgets_crop_modes)
        
        self.button_slider_reset.clicked.connect(lambda event,   Slider_list=Slider_list: self.crop_slider_reset(event, Slider_list ))
        
    def on_off_drag_drop(self, event):
           selection_list=[s for s in self.viewer.layers.selection]
           if (self.crop_modes_widget[0].value=='Drag&Drop' and len(selection_list)!=1) or  (self.crop_modes_widget[0].value=='Drag&Drop' and len(selection_list)!=1) or  (self.crop_modes_widget[0].value=='Drag&Drop' and self.viewer.layers.ndim!=2):
             self.viewer.overlays.interaction_box.show = False
             self.viewer.overlays.interaction_box.show_vertices = False
             self.viewer.overlays.interaction_box.show_handle = False
             self.viewer.overlays.interaction_box.allow_new_selection = False
           

             try: 
              self.viewer.layers.selection.active.interactive = True
             except:
              pass
           elif self.crop_modes_widget[0].value=='Drag&Drop':
             self.viewer.overlays.interaction_box.show = True
             self.viewer.overlays.interaction_box.points = self.viewer.layers.selection.active.extent.world
             self.viewer.overlays.interaction_box.show_vertices = True
             self.viewer.overlays.interaction_box.show_handle = False
             self.viewer.overlays.interaction_box.allow_new_selection = True
           

             try: 
              self.viewer.layers.selection.active.interactive = False
             except:
              pass
              

    

    def add_widgets_crop_modes(self):         
         try:

             self.layout().takeAt(2).widget().deleteLater()
             self.layout().setAlignment(Qt.AlignTop)

             self.w_slider_container_total = QWidget() 
             self.w_slider_container_total.setLayout(QVBoxLayout()) 
         except:
             pass 
         
         possible_layers=[x  for x in self.viewer.layers if isinstance(x, napari.layers.image.image.Image)]
         for layer in possible_layers:
           try:
             layer.mouse_double_click_callbacks.clear()
           except:
              pass 
         try: 
              self.viewer.layers.selection.active.interactive = True
              self.viewer.overlays.interaction_box.show = False
              self.viewer.overlays.interaction_box.show_vertices = False
              self.viewer.overlays.interaction_box.show_handle = False
 
         except:
              pass    
             
         if self.crop_modes_widget[0].value=='Crop via slider':
           Slider_list=[] 
           for i in range(self.layer_sel.ndim):
              w_slider_container = QWidget()
              w_slider_container.setLayout(QHBoxLayout())
              w_slider_container.layout().addWidget(QLabel('Axis '+str(i)))
              Rangeslider = QRangeSlider(Horizontal)
              Rangeslider.setRange(0,self.layer_sel.data.shape[i])
              Rangeslider.setValue((0, self.layer_sel.data.shape[i])) 
              Slider_list.append(Rangeslider)
              w_slider_container.layout().addWidget(Rangeslider)
              self.w_slider_container_total.layout().addWidget(w_slider_container)
              
           for axis, slider in enumerate(Slider_list):
               slider.valueChanged.connect(lambda event,   Slider_list=Slider_list: self.crop_slider(event, Slider_list )) 
               

           
           w_slider_reset = QWidget()
           w_slider_reset.setLayout(QHBoxLayout())
           self.button_slider_reset=QPushButton("Reset", self)
           w_slider_reset.layout().addWidget(self.button_slider_reset)
           self.w_slider_container_total.layout().addWidget(w_slider_reset)
           
           self.layout().insertWidget(2,self.w_slider_container_total)
           
           self.button_slider_reset.clicked.connect(lambda event,   Slider_list=Slider_list: self.crop_slider_reset(event, Slider_list ))
         
         elif self.crop_modes_widget[0].value=='Crop via layer corner pixels':
             w_zoom_button = QWidget()
             w_zoom_button.setLayout(QHBoxLayout())
             self.button_zoom=QPushButton("Crop", self)
             w_zoom_button.layout().addWidget(self.button_zoom)
             self.w_slider_container_total.layout().addWidget(w_zoom_button)
             
             self.layout().insertWidget(2,self.w_slider_container_total)
             
             self.button_zoom.clicked.connect(lambda event: self.crop_zoom(event))
             
             
             
         elif self.crop_modes_widget[0].value=='Crop via mouse click':
             self.w_crop_size=Container(widgets=[LiteralEvalLineEdit(value=128, label="Cropping size", visible=True)])
             w_mouse = QWidget()
             w_mouse.setLayout(QHBoxLayout())
             w_mouse.layout().addWidget(self.w_crop_size.native)
             self.w_slider_container_total.layout().addWidget(w_mouse)
             
             self.layout().insertWidget(2,self.w_slider_container_total)
             

             self.layer_sel.mouse_double_click_callbacks.append(self.crop_click)

         elif self.crop_modes_widget[0].value=='Drag&Drop' and self.viewer.layers.ndim==2:
             w_drag_button = QWidget()
             w_drag_button.setLayout(QHBoxLayout())
             self.button_drag=QPushButton("Crop", self)
             w_drag_button.layout().addWidget(self.button_drag)
             self.w_slider_container_total.layout().addWidget(w_drag_button)
             
             self.layout().insertWidget(2,self.w_slider_container_total)
             
             self.viewer.layers.selection.active=self.layer_sel
             self.viewer.layers.selection.active.interactive = False
             self.viewer.overlays.interaction_box.allow_new_selection = True
             self.viewer.overlays.interaction_box.points = self.viewer.layers.selection.active.extent.world
             self.viewer.overlays.interaction_box.show = True
             self.viewer.overlays.interaction_box.show_vertices = True
             self.viewer.overlays.interaction_box.show_handle =False
             self.viewer.overlays.interaction_box.allow_new_selection = True

             self.button_drag.clicked.connect(lambda event: self.crop_drag(event))
             

   
    def selected_layer(self):
            select_layer_name=self.Image_select[0].current_choice
            self.layer_sel=self.viewer.layers[select_layer_name] 
            self.viewer.layers.selection.active=self.viewer.layers[select_layer_name] 
            self.layer_sel_non_crop=np.copy(self.layer_sel.data)
            self.layer_sel_non_crop_scale=np.copy(self.layer_sel.scale)
            self.layer_sel_non_crop_trans=np.copy(self.layer_sel.translate)


    def remove_combo(self, event):
            self.layout().itemAt(0).widget().deleteLater()


             
    def change_combo(self, event):

             possible_images= [x.name  for x in self.viewer.layers if isinstance(x, napari.layers.image.image.Image)]

             Image_select_old=self.Image_select
             try:
              self.Image_select=Container(widgets=[ComboBox(choices=possible_images, label="Select an image", value=Image_select_old[0].current_choice)])

              self.layout().insertWidget(0,self.Image_select.native )
             except:
              self.Image_select=Container(widgets=[ComboBox(choices=possible_images, label="Select an image")])
              self.layout().insertWidget(0,self.Image_select.native ) 

             self.Image_select.changed.connect(self.selected_layer)
             self.Image_select.changed.connect(self.add_widgets_crop_modes)


                  
    def crop_click(self, layer, event):
        if isinstance(self.w_crop_size[0].value, tuple) and len(self.w_crop_size[0].value)==layer.ndim:
            crop_size=np.array(self.w_crop_size[0].value)

        elif isinstance(self.w_crop_size[0].value, int): 
            crop_size = self.w_crop_size[0].value

        elif isinstance(self.w_crop_size[0].value, float): 
            crop_size = int(self.w_crop_size[0].value)

        else:
            print('No support of provided cropping size')
        try:
               scale = np.asarray(layer.scale)
               translate = np.asarray(layer.translate)
               izyx = translate // scale
               layer_coordinates= layer.world_to_data(self.viewer.cursor.position)


               cords = np.round(layer_coordinates).astype(int)
               min_vals = np.maximum([0]*len(cords), cords - crop_size // 2)
               max_vals = np.minimum(layer.data.shape, cords + crop_size // 2)
               for i, min_val in enumerate(min_vals):
                   izyx[i]=min_val
               crop = np.copy(layer.data[tuple(slice(n, x) for n, x in zip(min_vals, max_vals))])
               translate_crop=scale * izyx + translate
               #self.viewer.add_image(crop,  name=layer.name+'_Crop', translate=translate_crop, scale=scale)
               new_layer_data_tup=list(layer.as_layer_data_tuple())
               new_layer_data_tup[0]=crop
               new_layer_data_tup[1]['name']=layer.name+'_Crop' 
               new_layer_data_tup[1]['translate']=translate_crop
               new_layer_data_tup[1]['scale']=scale     
               new_layer_data_tup[1]['colormap']='gray' 
               new_layer_data_tup=tuple(new_layer_data_tup)
               new_layer=Layer.create(*new_layer_data_tup)
               self.viewer.add_layer(new_layer)
        except:
              print('No support of provided cropping size ') 
        
    def crop_zoom(self, event):
        try:
            scale = np.asarray(self.layer_sel_non_crop_scale)
            translate = np.asarray(self.layer_sel_non_crop_trans)
            izyx = translate // scale
            corner_pixel=[list(self.layer_sel.corner_pixels.T[i]) for i in range(len(scale))]
            
            for i,pixel in enumerate(list(self.layer_sel.corner_pixels.T)):
                pixel=list(pixel)
                if pixel[0]==pixel[1]:
                  pixel[0]= None
                  pixel[1]= None
                if pixel[0] is not None:
                   izyx[i]=pixel[0]
                else:
                   izyx[i]=0 
                corner_pixel[i][0]= pixel[0]
                corner_pixel[i][1]= pixel[1]
            crop = np.copy(self.layer_sel.data[tuple(slice(i[0], i[1]) for i in corner_pixel)])
            translate_crop=scale * izyx + translate
            new_layer_data_tup=list(self.layer_sel.as_layer_data_tuple())
            new_layer_data_tup[0]=crop
            new_layer_data_tup[1]['name']=self.layer_sel.name+'_Crop' 
            new_layer_data_tup[1]['translate']=translate_crop
            new_layer_data_tup[1]['scale']=scale  
            new_layer_data_tup[1]['colormap']='gray'             
            new_layer_data_tup=tuple(new_layer_data_tup)
            new_layer=Layer.create(*new_layer_data_tup)
            self.viewer.add_layer(new_layer)
            
            #self.viewer.add_image(crop,  name=self.layer_sel.name+'_Crop', translate=translate_crop, scale=scale)
        except:
               print('No support of selected view ') 
            
    def crop_slider(self, event, Slider_list):
        scale = np.asarray(self.layer_sel_non_crop_scale)
        translate = np.asarray(self.layer_sel_non_crop_trans)
        izyx = translate // scale
        
        Slider_Values=[]
        for axis, slider in enumerate(Slider_list):
               izyx[axis]=slider.value()[0]
               Slider_Values.append(slider.value())
        Slider_Values=tuple(Slider_Values)   
        axis_ndim=tuple(range(self.layer_sel.ndim))

        self.layer_sel.data=self.nd_cropper(self.layer_sel_non_crop, axis=axis_ndim, slices=Slider_Values)
        self.layer_sel.translate= scale * izyx + translate


    def crop_slider_reset(self, event, Slider_list):
        for i, slider in enumerate(Slider_list):
              slider.setRange(0,self.layer_sel_non_crop.shape[i])
              slider.setValue((0, self.layer_sel_non_crop.shape[i]))
        
    
    def nd_cropper(self,a, axis=None, slices=None):
      if not hasattr(axis, '__iter__'):
        axis = [axis]
      if not hasattr(slices, '__iter__') or len(slices) != len(axis):
        slices = [slices]
      slices = [ sl if isinstance(sl,slice) else slice(*sl) for sl in slices ]
      mask = []
      fixed_axis = np.array(axis) % a.ndim
      case = dict(zip(fixed_axis, slices))
      for dim, size in enumerate(a.shape):
        mask.append( case[dim] if dim in fixed_axis else slice(None) )
      return a[tuple(mask)]

    def crop_drag(self,  event):
        try:
               scale = np.asarray(self.layer_sel.scale)
               translate = np.asarray(self.layer_sel.translate)
               izyx = translate // scale

               min_vals= self.layer_sel.world_to_data(self.viewer.overlays.interaction_box._box[[0]][0])
               min_vals = np.round(min_vals).astype(int)
               max_vals= self.layer_sel.world_to_data(self.viewer.overlays.interaction_box._box[[4]][0])
               max_vals = np.round(max_vals).astype(int)
               min_vals = np.maximum([0]*len(min_vals),min_vals)
               max_vals = np.minimum(self.layer_sel.data.shape,  max_vals)

               for i, min_val in enumerate(min_vals):
                   izyx[i]=min_val
               crop = np.copy(self.layer_sel.data[tuple(slice(n, x) for n, x in zip(min_vals, max_vals))])
               translate_crop=scale * izyx + translate
               new_layer_data_tup=list(self.layer_sel_layer.as_layer_data_tuple())
               new_layer_data_tup[0]=crop
               new_layer_data_tup[1]['name']=self.layer_sel.name+'_Crop' 
               new_layer_data_tup[1]['translate']=translate_crop
               new_layer_data_tup[1]['scale']=scale              
               new_layer_data_tup=tuple(new_layer_data_tup)
               new_layer=Layer.create(*new_layer_data_tup)
               self.viewer.add_layer(new_layer)
             #  self.viewer.add_image(crop,  name=self.layer_sel.name+'_Crop', translate=translate_crop, scale=scale)
              
        except:
               print('No support of provided cropping size ') 
  



@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return [nd_Cropper]
