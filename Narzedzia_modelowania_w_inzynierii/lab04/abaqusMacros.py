# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
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
    mdb.models['Model-1'].setValues(absoluteZero=-273.15, 
        stefanBoltzmann=5.67037E-11)
    session.viewports['Viewport: 1'].view.setValues(width=2.36497, height=1.11702, 
        viewOffsetX=0.0427281, viewOffsetY=0.00141754)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=2000.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, 200.0))
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(12.5, 300.0))
    s.RadialDimension(curve=g[2], textPoint=(-461.12109375, 9.61227416992188), 
        radius=425.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1681.5, 
        farPlane=2089.74, width=1703.63, height=842.781, cameraPosition=(
        -0.0816261, 24.2533, 1885.62), cameraTarget=(-0.0816261, 24.2533, 0))
    s.RadialDimension(curve=g[3], textPoint=(-691.331359863281, -207.885803222656), 
        radius=995.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1263.92, 
        farPlane=2507.32, width=4584.9, height=2268.14, cameraPosition=(
        619.938, 180.152, 1885.62), cameraTarget=(619.938, 180.152, 0))
    s.undo()
    s.RadialDimension(curve=g[3], textPoint=(-496.991333007812, -444.593322753906), 
        radius=995.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=1224.24, 
        farPlane=2547, width=5520.09, height=2730.77, cameraPosition=(799.799, 
        220.557, 1885.62), cameraTarget=(799.799, 220.557, 0))
    p = mdb.models['Model-1'].Part(name='coil', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['coil']
    p.BaseSolidExtrude(sketch=s, depth=1200.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4275.39, 
        farPlane=8512.65, width=4631.66, height=2187.62, viewOffsetX=320.374, 
        viewOffsetY=96.9513)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4302.02, 
        farPlane=8482.5, width=4660.51, height=2201.25, cameraPosition=(
        3729.93, 3640.31, 4301.49), cameraTarget=(38.3401, -51.2839, 609.898), 
        viewOffsetX=322.369, viewOffsetY=97.5551)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4325.61, 
        farPlane=8504.59, width=4686.06, height=2213.32, cameraPosition=(
        3729.93, 3679.85, 4301.49), cameraTarget=(38.3401, -11.7409, 609.898), 
        viewOffsetX=324.136, viewOffsetY=98.0899)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4314.91, 
        farPlane=8483.86, width=4674.48, height=2207.84, cameraPosition=(
        3292.14, 4051.86, 4301.49), cameraUpVector=(-0.640275, 0.50667, 
        -0.57735), cameraTarget=(52.478, -42.0753, 609.898), 
        viewOffsetX=323.334, viewOffsetY=97.8473)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4325.07, 
        farPlane=8319.11, width=4685.49, height=2213.05, cameraPosition=(
        3292.14, 2815.19, 5207.12), cameraUpVector=(-0.640275, 0.642473, 
        -0.421041), cameraTarget=(52.478, -143.969, 556.147), 
        viewOffsetX=324.095, viewOffsetY=98.0777)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4432.76, 
        farPlane=7841, width=4802.16, height=2268.15, cameraPosition=(723.066, 
        2815.19, 6005.02), cameraUpVector=(-0.378589, 0.642473, -0.666257), 
        cameraTarget=(-45.6583, -143.969, 389.324), viewOffsetX=332.165, 
        viewOffsetY=100.52)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4394.99, 
        farPlane=7829.16, width=4761.24, height=2248.83, cameraPosition=(
        723.066, 2761.59, 6005.02), cameraTarget=(-45.6583, -197.569, 389.324), 
        viewOffsetX=329.335, viewOffsetY=99.6635)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4375.03, 
        farPlane=7803.79, width=4739.63, height=2238.62, cameraPosition=(
        723.066, 2712.63, 6005.02), cameraTarget=(-45.6583, -246.533, 389.324), 
        viewOffsetX=327.839, viewOffsetY=99.2109)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4350.23, 
        farPlane=7773.5, width=4712.77, height=2225.93, cameraPosition=(
        723.066, 2653.1, 6005.02), cameraTarget=(-45.6583, -306.061, 389.324), 
        viewOffsetX=325.981, viewOffsetY=98.6486)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4372.65, 
        farPlane=7789.26, width=4737.06, height=2237.41, cameraPosition=(
        723.066, 2694.35, 6005.02), cameraTarget=(-45.6583, -264.807, 389.324), 
        viewOffsetX=327.661, viewOffsetY=99.1571)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4373.03, 
        farPlane=7794.06, width=4737.48, height=2237.6, cameraPosition=(
        744.595, 2694.35, 6005.02), cameraTarget=(-24.1294, -264.807, 389.324), 
        viewOffsetX=327.69, viewOffsetY=99.1657)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4395.19, 
        farPlane=7738, width=4761.48, height=2248.94, cameraPosition=(477.751, 
        2694.35, 6015.92), cameraUpVector=(-0.345989, 0.642473, -0.683754), 
        cameraTarget=(-19.0194, -264.807, 369.66), viewOffsetX=329.35, 
        viewOffsetY=99.6681)
    session.viewports['Viewport: 1'].view.setValues(width=5018.48, height=2370.32, 
        cameraPosition=(385.847, 6191.28, 500.709), cameraUpVector=(0, 0, 1), 
        cameraTarget=(385.847, 124.689, 500.709), viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(385.847, 
        124.689, 6567.3), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4682.26, 
        farPlane=7252.34, width=5350.05, height=2526.93, cameraPosition=(
        445.946, 227.775, 6567.3), cameraTarget=(445.946, 227.775, 500.709))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.92, 
        farPlane=7249.68, width=5353.09, height=2528.37, cameraPosition=(
        390.357, 189.268, 6567.3), cameraTarget=(390.357, 189.268, 500.709))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.98, 
        farPlane=7249.62, width=5353.16, height=2528.4, cameraPosition=(
        441.666, 189.268, 6567.3), cameraTarget=(441.666, 189.268, 500.709))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.98, 
        farPlane=7249.62, width=5353.16, height=2528.4, cameraPosition=(
        441.666, 334.726, 6567.3), cameraTarget=(441.666, 334.726, 500.709))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.98, 
        farPlane=7249.62, width=5353.16, height=2528.4, cameraUpVector=(
        0.0269669, 0.999636, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.98, 
        farPlane=7249.62, width=5353.16, height=2528.4, cameraPosition=(
        521.831, 334.726, 6567.3), cameraTarget=(521.831, 334.726, 500.709))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.98, 
        farPlane=7249.62, width=5353.16, height=2528.4, cameraPosition=(
        590.217, 334.726, 6567.3), cameraTarget=(590.217, 334.726, 500.709))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4684.98, 
        farPlane=7249.62, width=5353.16, height=2528.4, cameraPosition=(
        633.535, 334.726, 6567.3), cameraTarget=(633.535, 334.726, 500.709))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6700.13, 
        334.726, 500.709), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4973.61, 
        farPlane=8426.65, width=5682.95, height=2684.17, cameraUpVector=(0, 
        0.998198, -0.0600033))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4979.73, 
        farPlane=8420.53, width=5689.95, height=2687.47, cameraUpVector=(0, 
        0.999079, -0.042896))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4979.86, 
        farPlane=8420.4, width=5690.1, height=2687.54, cameraPosition=(6700.13, 
        403.596, 620.576), cameraTarget=(633.535, 403.596, 620.576))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(633.535, 
        403.596, 6687.17), cameraUpVector=(0, 1, 0))
    p = mdb.models['Model-1'].parts['coil']
    e = p.edges
    p.DatumCsysByThreePoints(name='Datum csys-1', coordSysType=CARTESIAN, 
        origin=p.InterestingPoint(edge=e[0], rule=CENTER), line1=(1.0, 0.0, 
        0.0), line2=(0.0, 1.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4749.38, 
        farPlane=7424.96, width=6141.63, height=2900.81, viewOffsetX=-98.7822, 
        viewOffsetY=24.8527)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    orientation = mdb.models['Model-1'].parts['coil'].datums[2]
    mdb.models['Model-1'].parts['coil'].MaterialOrientation(region=region, 
        orientationType=SYSTEM, axis=AXIS_1, localCsys=orientation, 
        fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, 
        additionalRotationField='', stackDirection=STACK_3)
    mdb.models['Model-1'].Material(name='S235')
    mdb.models['Model-1'].materials['S235'].Conductivity(type=ORTHOTROPIC, 
        temperatureDependency=ON, table=((17.976, 59.92, 59.92, 0.0), (
        17.6056125, 58.685375, 58.685375, 50.0), (17.1639, 57.213, 57.213, 
        100.0), (16.6605375, 55.535125, 55.535125, 150.0), (16.1052, 53.684, 
        53.684, 200.0), (15.5075625, 51.691875, 51.691875, 250.0), (14.8773, 
        49.591, 49.591, 300.0), (14.2240875, 47.413625, 47.413625, 350.0), (
        13.5576, 45.192, 45.192, 400.0), (12.8875125, 42.958375, 42.958375, 
        450.0), (12.2235, 40.745, 40.745, 500.0), (11.5752375, 38.584125, 
        38.584125, 550.0), (10.9524, 36.508, 36.508, 600.0), (10.3646625, 
        34.548875, 34.548875, 650.0), (9.8217, 32.739, 32.739, 700.0)))
    mdb.models['Model-1'].materials['S235'].SpecificHeat(temperatureDependency=ON, 
        table=((457300000.0, 0.0), (471944601.3, 50.0), (487449123.8, 100.0), (
        503864061.5, 150.0), (521242873.4, 200.0), (539642157.5, 250.0), (
        559121835.3, 300.0), (579745346.7, 350.0), (601579857.0, 400.0), (
        624696475.1, 450.0), (649170485.5, 500.0), (675081593.5, 550.0), (
        702514184.4, 600.0), (731557598.8, 650.0), (762306423.0, 700.0)))
    mdb.models['Model-1'].materials['S235'].Density(table=((7.8e-09, ), ))
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, optimizationTasks=OFF, 
        geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-S235', 
        material='S235', thickness=None)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['coil']
    a.Instance(name='coil-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].HeatTransferStep(name='Step-1', previous='Initial', 
        timePeriod=216000.0, maxNumInc=100000, initialInc=200.0, minInc=5.0, 
        maxInc=1000.0, deltmx=100.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    a = mdb.models['Model-1'].rootAssembly
    c1 = a.instances['coil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    f1 = a.instances['coil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#f ]', ), )
    e1 = a.instances['coil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#f ]', ), )
    v1 = a.instances['coil-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#f ]', ), )
    region = a.Set(vertices=verts1, edges=edges1, faces=faces1, cells=cells1, 
        name='Set-1')
    mdb.models['Model-1'].Temperature(name='Predefined Field-1', 
        createStepName='Initial', region=region, distributionType=UNIFORM, 
        crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, magnitudes=(650.0, 
        ))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, interactions=ON, constraints=ON, 
        engineeringFeatures=ON)
    mdb.models['Model-1'].FilmConditionProp(name='IntProp-1', 
        temperatureDependency=ON, dependencies=0, property=((0.004, 20.0), (
        0.003, 340.0), (0.002, 650.0)))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['coil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#f ]', ), )
    region=a.Surface(side1Faces=side1Faces1, name='Surf-1')
    mdb.models['Model-1'].FilmCondition(name='Int-1', createStepName='Step-1', 
        surface=region, definition=PROPERTY_REF, 
        interactionProperty='IntProp-1', sinkTemperature=20.0, 
        sinkAmplitude='', sinkDistributionType=UNIFORM, sinkFieldName='')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4347.67, 
        farPlane=8440.37, width=4161.73, height=1965.66, viewOffsetX=30.8782, 
        viewOffsetY=19.2807)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['coil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#5 ]', ), )
    region=a.Surface(side1Faces=side1Faces1, name='Surf-2')
    mdb.models['Model-1'].RadiationToAmbient(name='Int-2', createStepName='Step-1', 
        surface=region, radiationType=AMBIENT, distributionType=UNIFORM, 
        field='', emissivity=0.93, ambientTemperature=20.0, 
        ambientTemperatureAmp='')
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['coil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    surf1 = a.Surface(side1Faces=side1Faces1, name='Surf-3')
    surfaces =(surf1, )
    mdb.models['Model-1'].CavityRadiationProp(name='IntProp-2', property=((0.93, ), 
        ))
    props =("IntProp-2", )
    mdb.models['Model-1'].CavityRadiation(name='Int-3', createStepName='Step-1', 
        surfaces=surfaces, surfaceEmissivities=props, ambientTemp=20.0)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4709.7, 
        farPlane=7464.64, width=6090.33, height=2885.8, cameraPosition=(696.87, 
        403.596, 6687.17), cameraTarget=(696.87, 403.596, 620.576), 
        viewOffsetX=-97.9569, viewOffsetY=24.6451)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4708.62, 
        farPlane=7465.72, width=6088.93, height=2885.14, cameraPosition=(
        700.615, 442.691, 6687.17), cameraUpVector=(-0.297407, 0.954751, 0), 
        cameraTarget=(700.615, 442.691, 620.576), viewOffsetX=-97.9344, 
        viewOffsetY=24.6394)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4708.59, 
        farPlane=7465.75, width=6088.89, height=2885.12, cameraPosition=(
        700.615, 497.082, 6687.17), cameraTarget=(700.615, 497.082, 620.576), 
        viewOffsetX=-97.9337, viewOffsetY=24.6392)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(832.012, 
        497.082, 6687.17), cameraTarget=(832.012, 497.082, 620.576))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(832.204, 
        491.368, 6687.17), cameraUpVector=(-0.255319, 0.966857, 0), 
        cameraTarget=(832.204, 491.368, 620.576))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(832.204, 
        556.99, 6687.17), cameraTarget=(832.204, 556.99, 620.576))
    session.viewports['Viewport: 1'].view.setValues(width=6068.31, height=2875.37, 
        cameraPosition=(6788.83, 555.462, 600.001), cameraUpVector=(0, 1, 0), 
        cameraTarget=(701.661, 555.462, 600.001), viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4966.91, 
        farPlane=8610.75, width=6401.24, height=3033.12, cameraPosition=(
        6788.83, 591.756, 677.729), cameraTarget=(701.661, 591.756, 677.729))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4973.92, 
        farPlane=8603.74, width=6410.28, height=3037.4, cameraPosition=(
        6788.83, 591.756, 785.625), cameraTarget=(701.661, 591.756, 785.625))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5051.23, 
        farPlane=8827.63, width=6509.92, height=3084.61, cameraPosition=(
        3968.88, 591.756, 6293.45), cameraTarget=(410.205, 591.756, 1354.89))
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    v1, e1, d1 = p.vertices, p.edges, p.datums
    p.PartitionCellByPlaneThreePoints(point2=v1[0], point3=v1[1], 
        cells=pickedCells, point1=p.InterestingPoint(edge=e1[0], rule=CENTER))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4939.58, 
        farPlane=9363.58, width=6366.03, height=3016.44, cameraPosition=(
        3968.88, 3145.33, 5681.04), cameraUpVector=(0, 0.891224, -0.453564), 
        cameraTarget=(410.205, 905.372, 1279.68))
    p = mdb.models['Model-1'].parts['coil']
    e = p.edges
    pickedEdges1 = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, ratio=1.0, 
        number=5, constraint=FINER)
    p = mdb.models['Model-1'].parts['coil']
    p.seedPart(size=160.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['coil']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=DC3D8, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=DC3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=DC3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
    mdb.Job(name='Job_coil_s', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON, mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.jobs['Job_coil_s'].submit(consistencyChecking=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5001.8, 
        farPlane=9301.36, width=5714.14, height=2698.9, viewOffsetX=109.425, 
        viewOffsetY=-121.219)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    p.Set(cells=cells, name='Set-2')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region = p.Set(cells=cells, name='Section-1')
    p = mdb.models['Model-1'].parts['coil']
    p.SectionAssignment(region=region, sectionName='Section-S235', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.jobs['Job_coil_s'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='E:/temp/Job_coil_s.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4241.9, 
        farPlane=8536.64, width=4888.81, height=2309.08, viewOffsetX=78.8521, 
        viewOffsetY=64.8488)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4273.75, 
        farPlane=8504.79, width=4629.99, height=2186.83, viewOffsetX=307.276, 
        viewOffsetY=93.0152)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['Model-1'].parts['coil'].sets['Section-1']
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    o3 = session.openOdb(name='E:/temp/Job_coil_s.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['E:/temp/Job_coil_s.odb'])
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4191.89, 
        farPlane=8586.65, width=5816.6, height=2747.29, viewOffsetX=442.655, 
        viewOffsetY=300.638)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['E:/temp/Job_coil_s.odb'])
    odb = session.odbs['E:/temp/Job_coil_s.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].odbDisplay.setValues(viewCut=ON)
    session.viewports['Viewport: 1'].odbDisplay.setValues(viewCut=OFF)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'NT', ), numIntervals=6)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.jobs['Job_coil_s'].submit(consistencyChecking=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2', 
        createStepName='Step-1', variables=('NT', ), numIntervals=6)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region=p.Set(cells=cells, name='Set-6')
    mdb.models['Model-1'].parts['coil'].sectionAssignments[0].setValues(
        region=region)
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.jobs['Job_coil_s'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='E:/temp/Job_coil_s.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4271.8, 
        farPlane=8506.74, width=4627.87, height=2185.83, viewOffsetX=43.2477, 
        viewOffsetY=4.32728)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4288.16, 
        farPlane=8465.78, width=4645.6, height=2194.21, cameraPosition=(
        3699.57, 3637.56, 4308.1), cameraTarget=(10.7261, -51.2839, 619.254), 
        viewOffsetX=43.4134, viewOffsetY=4.34386)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4312.9, 
        farPlane=8486.5, width=4672.41, height=2206.87, cameraPosition=(
        3738.95, 3637.56, 4308.1), cameraTarget=(50.104, -51.2839, 619.254), 
        viewOffsetX=43.6639, viewOffsetY=4.36893)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4301.44, 
        farPlane=8480.37, width=4660, height=2201.01, cameraPosition=(3710.24, 
        3637.56, 4321.58), cameraTarget=(21.3911, -51.2839, 632.734), 
        viewOffsetX=43.5479, viewOffsetY=4.35732)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4313.47, 
        farPlane=8480.25, width=4673.04, height=2207.17, cameraPosition=(
        4040.38, 3278.53, 4321.58), cameraUpVector=(-0.520534, 0.629056, 
        -0.57735), cameraTarget=(21.1699, -47.3022, 632.734), 
        viewOffsetX=43.6697, viewOffsetY=4.36951)
    mdb.saveAs(pathName='E:/temp/Proper_model_coil')
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4351.54, 
        farPlane=8408.15, width=4165.43, height=1967.41, cameraPosition=(
        3673.31, 3640.31, 4336.59), cameraTarget=(-18.2744, -51.2839, 645.002), 
        viewOffsetX=30.9057, viewOffsetY=19.2978)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4353.33, 
        farPlane=8406.36, width=4167.14, height=1968.22, cameraPosition=(
        3713.32, 3640.31, 4296.58), cameraTarget=(21.7381, -51.2839, 604.989), 
        viewOffsetX=30.9184, viewOffsetY=19.3057)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4340.22, 
        farPlane=8421.05, width=4154.59, height=1962.29, cameraPosition=(
        3740.61, 3866.07, 4031.69), cameraUpVector=(-0.569727, 0.539349, 
        -0.620092), cameraTarget=(21.317, -48.3162, 607.082), 
        viewOffsetX=30.8253, viewOffsetY=19.2475)
    session.viewports['Viewport: 1'].view.setValues(width=4163.31, height=1966.41, 
        cameraPosition=(6430.59, -20.4801, 569.155), cameraUpVector=(0, 1, 0), 
        cameraTarget=(49.9548, -20.4801, 569.155), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4836.11, 
        farPlane=8025.07, width=4637.27, height=2190.27, cameraPosition=(
        6430.59, -20.4801, 648.044), cameraTarget=(49.9548, -20.4801, 648.044))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4843.49, 
        farPlane=8017.69, width=4644.35, height=2193.62, cameraPosition=(
        6430.59, -20.4801, 581.258), cameraTarget=(49.9548, -20.4801, 581.258))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4843.6, 
        farPlane=8017.58, width=4644.46, height=2193.67, cameraPosition=(
        6430.59, -16.7683, 581.258), cameraTarget=(49.9548, -16.7683, 581.258))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(49.9548, 
        -16.7683, 6961.89))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5228.17, 
        farPlane=7495.61, width=4429.69, height=2092.23, viewOffsetX=155.392, 
        viewOffsetY=-17.7357)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5005.26, 
        farPlane=9236.85, width=5718.1, height=2700.77, cameraPosition=(
        3968.88, 3145.33, 5638.82), cameraTarget=(410.205, 905.372, 1237.46), 
        viewOffsetX=109.5, viewOffsetY=-121.303)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5042.67, 
        farPlane=9265.22, width=5760.84, height=2720.95, cameraPosition=(
        4080.16, 3145.33, 5594.33), cameraTarget=(521.484, 905.372, 1192.97), 
        viewOffsetX=110.318, viewOffsetY=-122.21)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5097.54, 
        farPlane=9328.08, width=5823.53, height=2750.56, cameraPosition=(
        4080.16, 3170.04, 5663.17), cameraTarget=(521.484, 930.085, 1261.81), 
        viewOffsetX=111.518, viewOffsetY=-123.54)
    session.viewports['Viewport: 1'].view.setValues(width=4914.7, height=2321.3, 
        cameraPosition=(-8.57303, 7531.05, 444.974), cameraUpVector=(0, 0, 1), 
        cameraTarget=(-8.57303, 318.239, 444.974), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5808.58, 
        farPlane=9253.52, width=5609.78, height=2649.61, cameraPosition=(
        -22.2488, 7531.05, 444.974), cameraTarget=(-22.2488, 318.239, 444.974))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-22.2488, 
        318.239, 7657.78), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5751.04, 
        farPlane=8364.52, width=5554.22, height=2623.36, cameraPosition=(
        48.6106, 318.239, 7657.78), cameraTarget=(48.6106, 318.239, 444.974))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5749.98, 
        farPlane=8365.58, width=5553.2, height=2622.88, cameraPosition=(
        141.753, 318.239, 7657.78), cameraTarget=(141.753, 318.239, 444.974))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(7354.56, 
        318.239, 444.974))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(141.753, 
        318.239, 7657.78))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5440.16, 
        farPlane=8517.35, width=5253.99, height=2481.56, cameraPosition=(
        130.261, -1429.19, 7438.03), cameraUpVector=(0.999417, 0.0326489, 
        0.0100229), cameraTarget=(142.005, 356.621, 449.801))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5449.2, 
        farPlane=8456.89, width=5262.72, height=2485.68, cameraPosition=(
        130.261, -1325.34, 7438.03), cameraTarget=(142.005, 460.467, 449.801))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(142.005, 
        7673.27, 449.801), cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(142.005, 
        460.467, 7662.6), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5894.6, 
        farPlane=8230.6, width=4212.28, height=1989.54, viewOffsetX=219.874, 
        viewOffsetY=-174.651)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5744.81, 
        farPlane=8380.39, width=5258.08, height=2483.49, viewOffsetX=-190.577, 
        viewOffsetY=-68.3368)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['Model-1'].parts['coil'].materialOrientations[0]
    p = mdb.models['Model-1'].parts['coil']
    p.DatumCsysByThreePoints(name='Datum csys-2', coordSysType=CYLINDRICAL, 
        origin=(0.0, 0.0, 0.0), line1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5704.26, 
        farPlane=8420.94, width=6285.89, height=2968.95, viewOffsetX=-391.67, 
        viewOffsetY=81.5098)
    p = mdb.models['Model-1'].parts['coil']
    del p.features['Datum csys-1']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5585.02, 
        farPlane=8540.18, width=6547.35, height=3092.44, viewOffsetX=-474.163, 
        viewOffsetY=125.486)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5621.64, 
        farPlane=8503.56, width=6590.27, height=3112.71, cameraPosition=(
        247.401, 460.467, 7662.6), cameraTarget=(247.401, 460.467, 449.801), 
        viewOffsetX=-477.271, viewOffsetY=126.309)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5622.46, 
        farPlane=8502.75, width=6591.23, height=3113.16, cameraPosition=(
        400.078, 460.467, 7662.6), cameraTarget=(400.078, 460.467, 449.801), 
        viewOffsetX=-477.34, viewOffsetY=126.327)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5622.47, 
        farPlane=8502.73, width=6591.24, height=3113.17, cameraPosition=(
        500.105, 544.75, 7662.6), cameraTarget=(500.105, 544.75, 449.801), 
        viewOffsetX=-477.341, viewOffsetY=126.327)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4856.57, 
        farPlane=8394.42, width=5693.37, height=2689.09, cameraPosition=(
        2624.19, -896.389, -5472.44), cameraUpVector=(-0.109371, -0.993993, 
        0.00397801), cameraTarget=(286.891, -611.927, 1345.23), 
        viewOffsetX=-412.317, viewOffsetY=109.119)
    p = mdb.models['Model-1'].parts['coil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region = regionToolset.Region(cells=cells)
    orientation = mdb.models['Model-1'].parts['coil'].datums[12]
    mdb.models['Model-1'].parts['coil'].MaterialOrientation(region=region, 
        orientationType=SYSTEM, axis=AXIS_1, localCsys=orientation, 
        fieldName='', additionalRotationType=ROTATION_NONE, angle=0.0, 
        additionalRotationField='', stackDirection=STACK_3)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4983.91, 
        farPlane=8265.58, width=5842.65, height=2759.6, cameraPosition=(
        2624.19, -686.899, -5498.1), cameraUpVector=(-0.109371, -0.993578, 
        -0.028996), cameraTarget=(286.891, -628.743, 1325.25), 
        viewOffsetX=-423.128, viewOffsetY=111.98)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4957.62, 
        farPlane=8242.58, width=5811.84, height=2745.04, cameraPosition=(
        2548.14, -686.899, -5498.1), cameraTarget=(210.839, -628.743, 1325.25), 
        viewOffsetX=-420.896, viewOffsetY=111.389)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4943.74, 
        farPlane=8222.51, width=5795.57, height=2737.36, cameraPosition=(
        2495.76, -686.899, -5498.1), cameraTarget=(158.454, -628.743, 1325.25), 
        viewOffsetX=-419.718, viewOffsetY=111.077)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5024.1, 
        farPlane=8298.42, width=5889.78, height=2781.86, cameraPosition=(
        2495.76, -686.899, -5580.69), cameraTarget=(158.454, -628.743, 
        1242.66), viewOffsetX=-426.541, viewOffsetY=112.883)
    session.viewports['Viewport: 1'].view.setValues(width=6377.44, height=3012.19, 
        cameraPosition=(6450.64, -718.069, 533.977), cameraUpVector=(0, 1, 0), 
        cameraTarget=(-210.619, -718.069, 533.977), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-210.619, 
        -718.069, 7195.24))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5076.27, 
        farPlane=8114.21, width=6870.85, height=3245.24, viewOffsetX=24.2698, 
        viewOffsetY=9.77185)
    session.viewports['Viewport: 1'].view.setValues(width=6939.63, height=3277.72, 
        cameraPosition=(-179.087, 5889.87, 600), cameraUpVector=(0, 0, 1), 
        cameraTarget=(-179.087, -705.373, 600), viewOffsetX=0, viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6416.16, 
        -705.373, 600), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-179.087, 
        5889.87, 600), cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6416.16, 
        -705.373, 600), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4606.24, 
        farPlane=8226.08, width=6243.92, height=2949.12, cameraPosition=(
        6416.16, -705.373, 1085.13), cameraTarget=(-179.087, -705.373, 
        1085.13))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-179.087, 
        5889.87, 1085.13), cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4187.22, 
        farPlane=7592.52, width=5675.92, height=2680.85, cameraPosition=(
        -179.087, 5889.87, 1080.69), cameraTarget=(-179.087, -705.373, 
        1080.69))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4174.14, 
        farPlane=7605.6, width=5658.2, height=2672.48, cameraPosition=(
        -215.218, 5889.87, 972.234), cameraTarget=(-215.218, -705.373, 
        972.234))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6380.03, 
        -705.373, 972.234), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4298.73, 
        farPlane=8465.29, width=5827.09, height=2752.25, cameraPosition=(
        6219.67, -1549.18, 424.561), cameraUpVector=(-0.318107, -0.909734, 
        0.266819), cameraTarget=(2.37478, 649.766, 509.578))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4272.9, 
        farPlane=8428.6, width=5792.08, height=2735.71, cameraPosition=(
        6219.67, -1253.71, -161.759), cameraUpVector=(-0.318107, -0.939756, 
        -0.125169), cameraTarget=(2.37478, 721.684, 807.984))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4365.43, 
        farPlane=8495.71, width=5917.51, height=2794.95, cameraPosition=(
        6219.67, -1372.94, -461.742), cameraTarget=(2.37478, 602.452, 508.001))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(2.37478, 
        602.452, 7103.25), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5126.98, 
        farPlane=7879.51, width=5772.41, height=2726.42, viewOffsetX=224.134, 
        viewOffsetY=-67.4036)
    p1 = mdb.models['Model-1'].parts['coil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF, 
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
    mdb.jobs['Job_coil_s'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='E:/temp/Job_coil_s.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4329.16, 
        farPlane=8449.38, width=4690.01, height=2215.18, viewOffsetX=-51.7212, 
        viewOffsetY=10.0739)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=4280.51, 
        farPlane=8455.94, width=4637.31, height=2190.29, cameraPosition=(
        3636.84, 3637.56, 4355.68), cameraTarget=(-52.0046, -51.2839, 666.836), 
        viewOffsetX=-51.14, viewOffsetY=9.96068)
    session.viewports['Viewport: 1'].view.setValues(width=4652.63, height=2197.53, 
        cameraPosition=(6268.52, -27.0368, 726.732), cameraUpVector=(0, 1, 0), 
        cameraTarget=(-99.7052, -27.0368, 726.732), viewOffsetX=0, 
        viewOffsetY=0)
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-99.7052, 
        6341.19, 726.732), cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6268.52, 
        -27.0368, 726.732), cameraUpVector=(0, 1, 0))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-99.7052, 
        -27.0368, 7094.96))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5167.35, 
        farPlane=7822.57, width=5613.57, height=2651.4, cameraPosition=(
        5.16345, 4.89826, 7094.96), cameraTarget=(5.16345, 4.89826, 726.732))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=5177.77, 
        farPlane=7812.15, width=5624.9, height=2656.75, cameraPosition=(
        41.1166, 4.89826, 7094.96), cameraTarget=(41.1166, 4.89826, 726.732))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(6409.34, 
        4.89826, 726.732))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(41.1166, 
        4.89826, 7094.96))
    mdb.saveAs(pathName='E:/temp/Proper_model_coil.cae')


