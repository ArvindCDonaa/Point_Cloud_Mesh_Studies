# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:12:23 2023

@author: 
"""

import numpy as np
import pyvista as pv

points = np.genfromtxt('E:/Internships_and_Jobs/Donaa_Internship/FEA_Internship/Coding/Updates_March_2023/Sample_Attempt.csv', delimiter=",", dtype=np.float32)
point_cloud = pv.PolyData(points)
mesh = point_cloud.reconstruct_surface()
mesh.plot(color='orange')
mesh.save('try_2.stl')
