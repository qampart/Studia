# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
from odbAccess import *
import visualization
import numpy as np
from scipy.optimize import least_squares


def dataMises():
    odb = openOdb('E:/Narzedzia cwiczeniowe/belka2/Job-1.odb')
    lastFrame = odb.steps['Step-1'].frames[-1]
    stressValues = lastFrame.fieldOutputs['S'].getSubset(region=odb.rootAssembly.instances['Belka-1'].sets['Set-1']).values
    max_stress = max([np.sqrt(0.5*((s.mises)**2 + 3*((s.misesPlasticity)**2))) for s in stressValues])
    odb.close()
    return max_stress


def modify_beam_dimensions(a):
    mdb.models['Model-1'].profiles['Prostokat'].setValues(a=a, b=a/2)
    p = mdb.models['Model-1'].parts['Belka']
    p.regenerate()
    p.generateMesh()


def calculate_sf(a):
    modify_beam_dimensions(a[0])
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.viewports['Viewport: 1'].setValues(displayedObject=mdb.models['Model-1'].rootAssembly)
    max_stress = dataMises()
    Re = 200e6  # 200 MPa
    sf = Re / max_stress
    return sf


def objective_function(a):
    sfe = 3
    sf = calculate_sf(a)
    return abs(sf - sfe)


a0 = [70]
bndl = [10]
bndu = [100]
bounds = (bndl, bndu)
epsX = 0.01
maxits = 0
diff_step = 0.0001

result = least_squares(objective_function, a0, bounds=bounds, ftol=epsX, max_nfev=100, x_scale=diff_step)

print("Optymalny wymiar 'a':", result.x[0])
print("Optymalny wymiar 'b':", result.x[0] / 2)
