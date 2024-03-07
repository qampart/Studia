# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *

def create_simulation(a, b, job_name):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior

    # Otwórz istniejącą bazę danych
    openMdb(pathName='E:/Narzedzia cwiczeniowe/belka-cwicz.cae')
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=3700.46, 
        farPlane=4299.54, width=2488.31, height=1187.21, viewOffsetX=129.419, 
        viewOffsetY=24.6344)
    p1 = mdb.models['Model-1'].parts['Belka']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)

    # Aktualizuj wymiary belki
    mdb.models['Model-1'].profiles['Prostokat'].setValues(a=a, b=b)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)

    # Stwórz i wyślij zadanie obliczeniowe (Job)
    mdb.Job(name=job_name, model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
    mdb.jobs[job_name].submit(consistencyChecking=OFF)
    mdb.jobs[job_name].waitForCompletion()

    # Otwórz Odb i wyświetl wyniki
    odb_path = 'E:/temp/' + job_name + '.odb'
    o3 = session.openOdb(name=odb_path)
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))


# Wywołanie funkcji create_simulation z różnymi parametrami
create_simulation(a=70.0, b=95.0, job_name='Job-1')
create_simulation(a=80.0, b=100.0, job_name='Job-2')
create_simulation(a=90.0, b=105.0, job_name='Job-3')