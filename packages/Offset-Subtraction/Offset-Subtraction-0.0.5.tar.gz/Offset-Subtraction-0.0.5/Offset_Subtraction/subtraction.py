# -*- coding: utf-8 -*-

"""
Created on Fri Oct 29 09:32:34 2021

@author: Marc Boucsein
"""
import numpy as np
import dask.array as da
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
import napari.types
from napari.types import  LayerDataTuple
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    import napari
    

from concurrent.futures import Future


def on_init(widget):
    """
    Initializes widget layout.
    Updates widget layout according to user input.
    """
    widget.native.setStyleSheet("QWidget{font-size: 12pt;}")
     

    def change_Mode(event):
        if widget.Options_modes.value=='Interactive via Slider':
           setattr(getattr(widget, 'Offset_Slider'), 'visible', True) 
           setattr(getattr(widget, 'Offset_Value'), 'visible', False) 

        else:
           setattr(getattr(widget, 'Offset_Slider'), 'visible', False) 
           setattr(getattr(widget, 'Offset_Value'), 'visible', True)
           
    def values_Offset_slider(event):
           min_value=np.nanmin(widget.image.value.data)
           max_value=np.nanmax(widget.image.value.data)
           setattr(getattr(widget, 'Offset_Slider'), 'value', 0)
           setattr(getattr(widget, 'Offset_Slider'), 'min', min_value)
           setattr(getattr(widget, 'Offset_Slider'), 'max', max_value)
           if max_value<=1:
              setattr(getattr(widget, 'Offset_Slider'), 'step', 0.001) 
           else:
              setattr(getattr(widget, 'Offset_Slider'), 'step', 1)  
    
    widget.image.changed.connect(values_Offset_slider)
    widget.Options_modes.changed.connect(change_Mode)
    widget.native.layout().addStretch() 

def all_image_layers(gui)->List[napari.layers.Layer]:
     from  napari.utils._magicgui import find_viewer_ancestor
     viewer = find_viewer_ancestor(gui.native)
     if not viewer:
         return []
     possible_image_layers= [x  for x in viewer.layers if isinstance(x, napari.layers.image.image.Image)]    
     return possible_image_layers

@magic_factory(widget_init=on_init, layout='vertical',
               image={"widget_type": "ComboBox", 'label': 'Image', 'choices': all_image_layers},
               Options_modes={"widget_type": "RadioButtons", 'value': 'Interactive via Slider', 'choices': ['Interactive via Slider', 'Via offset input' ], 'label': 'Mode:'} ,
               Offset_Slider={"widget_type": "FloatSlider", 'min': 0, 'max': 1, 'step': 0.01, 'label': 'Offset Slider'},
               Offset_Value={"widget_type": "LiteralEvalLineEdit", 'value': 0 ,'label': 'Offset value', 'visible':False} 
                ,auto_call=True)
def Subtraction(viewer: 'napari.viewer.Viewer', image: 'napari.layers.Image', Options_modes: str, Offset_Slider: float, Offset_Value: float) -> Future[LayerDataTuple]:
           if  Offset_Value is not None and (isinstance(Offset_Value, float) or isinstance(Offset_Value, int)):
                Offset=Offset_Value
           else:
                Offset=0
                print('Offset is not an integer or a float. Therefore Offset is set to 0 automatically')
                #return 
           
           if isinstance(image.data, da.core.Array):
               img_data= image.data.compute()
           else:
               img_data= np.copy(image.data)
            
           from napari.qt import thread_worker
           future: Future[LayerDataTuple] = Future()
    
           def _on_done(result, self= Subtraction):
             future.set_result(result)  
           
               
               
             
           @thread_worker
           def subtract():
                   if Options_modes=='Interactive via Slider':
                     img_data[np.where(img_data < Offset_Slider)]=0
                   else:    
                     img_data[np.where(img_data < Offset)]=0  
                   LayerdataTuple=list(viewer.layers[image.name].as_layer_data_tuple())                  
                   LayerdataTuple[0]=img_data
                   LayerdataTuple[1]['name']=image.name+'_Offset_Subtraction'
                   LayerdataTuple_new=tuple(LayerdataTuple)
                   
                  
                   return LayerdataTuple_new 
           worker = subtract()
           worker.returned.connect(_on_done)
           worker.start()
           
           return future
       
    

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Subtraction


