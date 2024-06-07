# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_29-03.11.55 183150
# Run by YLM4 on Fri Jun  7 19:41:20 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=211.416656494141, 
    height=98.2870330810547)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup

def beam():
    executeOnCaeStartup()
    #: Executing "onCaeStartup()" in the site directory ...
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    Mdb()
    #: A new model database has been created.
    #: The model "Model-1" has been created.
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=178.15, 
        farPlane=198.973, width=60.6916, height=31.4437, cameraPosition=(18.2748, 
        1.00637, 188.562), cameraTarget=(18.2748, 1.00637, 0))
    s.Line(point1=(0.0, 0.0), point2=(40.0, 0.0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseWire(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Density(table=((7.85e-09, ), ))
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((200000.0, 0.3), 
        ))
    mdb.models['Model-1'].CircularProfile(name='Profile-1', r=5.0)
    mdb.models['Model-1'].BeamSection(name='Section-1', 
        integration=DURING_ANALYSIS, poissonRatio=0.0, profile='Profile-1', 
        material='Material-1', temperatureVar=LINEAR, consistentMassMatrix=False)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(edges=edges, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    edges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    region=p.Set(edges=edges, name='Set-2')
    p = mdb.models['Model-1'].parts['Part-1']
    p.assignBeamSectionOrientation(region=region, method=N1_COSINES, n1=(0.0, 0.0, 
        -1.0))
    #: Beam orientations have been assigned to the selected regions.
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=4.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=2.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#1 ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    a = mdb.models['Model-1'].rootAssembly
    v1 = a.instances['Part-1-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Set(vertices=verts1, name='Set-1')
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Initial', 
        region=region, localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
        maxNumInc=10000, initialInc=0.01, minInc=1e-10, maxInc=0.1, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=72.1323, 
        farPlane=87.8677, width=51.6, height=26.7334, viewOffsetX=0.696811, 
        viewOffsetY=-1.90033)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=64.3113, 
        farPlane=94.3811, width=46.0053, height=23.8348, cameraPosition=(46.9379, 
        34.5846, 66.137), cameraUpVector=(-0.0837634, 0.897526, -0.432933), 
        cameraTarget=(19.8719, -0.156821, -0.649673), viewOffsetX=0.621259, 
        viewOffsetY=-1.69429)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=66.6117, 
        farPlane=92.0806, width=34.9712, height=18.1182, viewOffsetX=2.19117, 
        viewOffsetY=-0.525548)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=68.1908, 
        farPlane=90.0484, width=35.8002, height=18.5477, cameraPosition=(40.8882, 
        38.3949, 65.9502), cameraUpVector=(-0.138455, 0.874618, -0.464622), 
        cameraTarget=(19.8412, -0.386354, -0.780797), viewOffsetX=2.24311, 
        viewOffsetY=-0.538007)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=66.5939, 
        farPlane=91.6452, width=47.6382, height=24.6808, viewOffsetX=1.03576, 
        viewOffsetY=-1.01478)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        renderBeamProfiles=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=59.9517, 
        farPlane=98.2874, width=48.5363, height=25.1461, viewOffsetX=1.23027, 
        viewOffsetY=-1.25419)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=56.4083, 
        farPlane=102.909, width=45.6676, height=23.6599, cameraPosition=(58.2754, 
        30.4051, 62.8971), cameraUpVector=(-0.185771, 0.9238, -0.334787), 
        cameraTarget=(19.7301, -0.201826, -0.170076), viewOffsetX=1.15756, 
        viewOffsetY=-1.18006)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON, mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].profiles['Profile-1'].setValues(r=2.5)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        renderBeamProfiles=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=61.3202, 
        farPlane=97.997, width=49.6443, height=25.7202, viewOffsetX=2.36968, 
        viewOffsetY=-1.27083)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
