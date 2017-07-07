###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################


"""Translational Tetrahedral Order Sk
==============================================================
"""

from __future__ import print_function, division
import os
import six
from six.moves import range
import numpy as np

#from  order import oto
#from order import util
import util
import oto

class Translational(oto.Orientational):
    """translational tetrahedral order parameter"""
    def __init__(self, filename, center, bins=1000):
        print(filename)
        super(Translational, self).__init__(filename, center, bins)
        self.sk = np.zeros(bins+1)
    
    def translational_param(self, freq = 100):
        """compute translational order parameter"""
        for i in range(0, self.traj.n_frames, freq):
            print(i)
            foo = self.four_neighbors(self.traj.coords[i], self.traj.box_size[i])
            for j in range(self.traj.n_atoms):
                s = 0.0
                norms = np.array(map(np.linalg.norm, foo[j]))
                sqrt_norms = (norms - norms.mean()) ** 2
                sum_norms = sqrt_norms.sum() / ( 4 * norms.mean() ** 2)
                s = 1 - 1 / 3 * sum_norms
            
                self.sk[int(round(s * self.bins))] += 1