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
from napari.types import ImageData, LayerDataTuple
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
    
    for x in ['Line_Edit_1','Line_Edit_2']:
           setattr(getattr(widget, x), 'visible', False)
    
    
    
    def update_widget(event):
        if widget.layer_choice.value=='All Layers [prefix]':
           for x in ['Line_Edit_1','Line_Edit_2']:
              setattr(getattr(widget, x), 'label', 'Prefix:')  
              setattr(getattr(widget, x), 'visible', True)
        elif widget.layer_choice.value=='All Layers [suffix]':
           for x in ['Line_Edit_1','Line_Edit_2']:
              setattr(getattr(widget, x), 'label', 'Suffix:')  
              setattr(getattr(widget, x), 'visible', True)      
        else:
           for x in ['Line_Edit_1','Line_Edit_2']: 
              setattr(getattr(widget, x), 'visible', False)
    
    
    widget.layer_choice.changed.connect(update_widget)
    widget.native.layout().addStretch()



@magic_factory(widget_init=on_init, layout='horizontal', call_button='Match',
               layer_choice={"widget_type": "RadioButtons", 'label': 'Operation:', 'choices': ['All Layers [prefix]', 'All Layers [suffix]', 'Selected'], 'value': 'Selected',
                "tooltip": 'Select all layers with given prefix or suffix or select just two layer from the layer list'},
               Line_Edit_1={"widget_type": "LineEdit", 'label': 'Prefix:'},
               Line_Edit_2={"widget_type": "LineEdit", 'label': 'Prefix:'},
               Epsilon={"widget_type": "LiteralEvalLineEdit", 'value': 0.005 ,'label': 'Background value:', 'tooltip': 'Choose an epsilon corresponding to the image background noise'}
             )
def Replace(viewer: 'napari.viewer.Viewer', layer_choice: str, Line_Edit_1: str, Line_Edit_2: str, Epsilon: float) -> Future[LayerDataTuple]:
           
           if  Epsilon is not None and (isinstance(Epsilon, float) or isinstance(Epsilon, int)):
                Epsilon_value=Epsilon
           else:
                Epsilon_value=0.005
                print('Epsilon is not an integer or a float. Therefore Epsilon is set to 0.005 automatically')
                #return 
           
           from napari.qt import thread_worker
           future: Future[LayerDataTuple] = Future()
    
           def _on_done(result, self=Replace):
             future.set_result(result)  
           @thread_worker
           def replace():
               if layer_choice=='All Layers [prefix]':
                   list_1=[x.name  for x in viewer.layers if (isinstance(x, napari.layers.image.image.Image) 
                                                   and x.name.startswith(str(Line_Edit_1)))]
                   list_2=[x.name  for x in viewer.layers if (isinstance(x, napari.layers.image.image.Image) 
                                                   and x.name.startswith(str(Line_Edit_2)))] 
                   
                   list_1=sorted(list_1)
                   list_2=sorted(list_2)
                   if len(list_1) != len(list_2):
                    print('The two lists have not the same length')
                    return
                   if not list_1:
                    print('One of the two lists is or both are empty') 
                    return
               elif layer_choice=='All Layers [suffix]':
                   list_1=[x.name  for x in viewer.layers if (isinstance(x, napari.layers.image.image.Image) 
                                                   and x.name.endswith(str(Line_Edit_1)))]
                   list_2=[x.name  for x in viewer.layers if (isinstance(x, napari.layers.image.image.Image) 
                                                   and x.name.endswith(str(Line_Edit_2)))]  
                   
                   list_1=sorted(list_1)
                   list_2=sorted(list_2)
                   if len(list_1) != len(list_2):
                    print('The two lists have not the same length')
                    return  
                   if not list_1:
                    print('One of the two lists is or both are empty') 
                    return
               else:
                  selection_list=[s for s in viewer.layers.selection if isinstance(s, napari.layers.image.image.Image) ]
                  if len(selection_list) != 2:
                    print('You have to select exact two elements of the layer list')
                    return 
                   
               if layer_choice=='Selected':
                  img_1=selection_list[0].data 
                  img_2=selection_list[1].data 
                  img_1[img_1< Epsilon_value]=0
                  img_2[img_2< Epsilon_value]=0
                  img_1_name=selection_list[0].name
                  img_2_name=selection_list[1].name 
                  
                  if isinstance(img_1, da.core.Array):
                     img_1=img_1.compute()
                                       
                  if isinstance(img_2, da.core.Array):
                     img_2=img_2.compute()
                     
                  img_result=img_2.copy()   
                  img_result[img_1!=0]=img_1[img_1!=0]
                  Layer_tuple= (img_result, {'name': img_1_name+'_'+img_2_name})
                  return Layer_tuple
              
               if layer_choice=='All Layers [prefix]': 
                  layer_list=[] 
                  for i, j in zip(list_1, list_2):
                      img_1=viewer.layers[i].data
                      img_2=viewer.layers[j].data
                      img_1[img_1< Epsilon_value]=0
                      img_2[img_2< Epsilon_value]=0
                      img_1_name=i
                      img_2_name=j
                      if isinstance(img_1, da.core.Array):
                         img_1=img_1.compute()
                                       
                      if isinstance(img_2, da.core.Array):
                         img_2=img_2.compute()
                     
                      img_result=img_2.copy()   
                      img_result[img_1!=0]=img_1[img_1!=0]
                      Layer_tuple= (img_result, {'name': img_1_name+'_'+img_2_name})
                      layer_list.append( Layer_tuple)  
                  return layer_list
              
               if layer_choice=='All Layers [suffix]': 
                  layer_list=[] 
                  for i, j in zip(list_1, list_2):
                      img_1=viewer.layers[i].data
                      img_1[img_1< Epsilon_value]=0
                      img_2=viewer.layers[j].data
                      img_2[img_2< Epsilon_value]=0
                      img_1_name=i
                      img_2_name=j
                      if isinstance(img_1, da.core.Array):
                         img_1=img_1.compute()
                                       
                      if isinstance(img_2, da.core.Array):
                         img_2=img_2.compute()
                     
                      img_result=img_2.copy()   
                      img_result[img_1!=0]=img_1[img_1!=0]
                      Layer_tuple= (img_result, {'name': img_1_name+'_'+img_2_name})
                      layer_list.append(Layer_tuple)  
                  return layer_list  
              
              
           worker = replace()
           worker.returned.connect(_on_done)
           worker.start()
           
           return future
       
    

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Replace


