# -*- coding: utf-8 -*-

"""
Created on Fri Oct 29 09:32:34 2021

@author: Marc Boucsein
"""
import numpy as np
from magicgui import magic_factory
from napari_plugin_engine import napari_hook_implementation
import napari.types
from napari.types import  LayerDataTuple
import napari





@magic_factory(layout='vertical', 
               Background={"widget_type": "CheckBox", 'value': True, 'text': 'Background'},
               call_button="Select a part",            
               auto_call=False)                  
def Selecter(viewer: 'napari.viewer.Viewer'  ,
    Image: 'napari.layers.Image', Label: 'napari.layers.Labels',
    Background: bool= True) ->LayerDataTuple:
    

    if Image is not None:

       img=Image.data 

       try: 
          lb= Label.data
          img_part=np.copy(img)  
          img_part[lb==0]=0
       except:
          img_part=np.copy(img) 
       try: 
          img_remaining=np.copy(img)  
          img_remaining[lb!=0]=0
       except:
          img_remaining=np.copy(img)   
       LayerdataTuple=list(viewer.layers[Image.name].as_layer_data_tuple())                  
       LayerdataTuple[0]=img_part
       LayerdataTuple[1]['name']=Image.name+'_Select'
       LayerdataTuple_new=tuple(LayerdataTuple)
       LayerdataTuple_rem=list(viewer.layers[Image.name].as_layer_data_tuple())                  
       LayerdataTuple_rem[0]=img_remaining
       LayerdataTuple_rem[1]['name']=Image.name+'_Background'
       LayerdataTuple_new_rem=tuple(LayerdataTuple_rem)
       
       if Background:
          return  [LayerdataTuple_new, LayerdataTuple_new_rem]
       else:
          return LayerdataTuple_new 
       
       
    else:
       return
   

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Selecter

