#! python3
# -*- coding: utf-8 -*-
import numpy as np
from wxpyJemacs import Layer, Frame

class Plugin(Layer):
    def Init(self):
        self.graph.handler.bind('region_draw', self.on_calc)
        self.graph.handler.bind('frame_shown', self.on_calc)
    
    def Destroy(self):
        self.graph.handler.unbind('region_draw', self.on_calc)
        self.graph.handler.unbind('frame_shown', self.on_calc)
        return Layer.Destroy(self)
    
    def on_calc(self, evt):
        print("avr: {:g}".format(np.average(self.graph.frame.roi)))
