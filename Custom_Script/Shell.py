# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_29-03.11.55 183150
# Run by YLM4 on Fri Jun  7 19:47:59 2024
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

def shell():
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
    s.rectangle(point1=(0.0, 0.0), point2=(40.0, 5.0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((200000.0, 0.3), 
        ))
    mdb.models['Model-1'].materials['Material-1'].Density(table=((7.85e-09, ), ))
    mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
        preIntegrate=OFF, material='Material-1', thicknessType=UNIFORM, 
        thickness=1.0, thicknessField='', nodalThicknessField='', 
        idealization=NO_IDEALIZATION, poissonDefinition=DEFAULT, 
        thicknessModulus=None, temperature=GRADIENT, useDensity=OFF, 
        integrationRule=SIMPSON, numIntPts=5)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#f ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=4.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#f ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
        maxNumInc=10000, initialInc=0.1, minInc=1e-10, maxInc=0.1, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=72.2956, 
        farPlane=88.9495, width=54.5931, height=28.2841, viewOffsetX=2.90217, 
        viewOffsetY=0.338181)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=64.3955, 
        farPlane=99.0452, width=48.6274, height=25.1933, cameraPosition=(51.2442, 
        -28.5797, 68.8233), cameraUpVector=(-0.211296, 0.85603, 0.47177), 
        cameraTarget=(20.4051, 1.39182, 0.627607), viewOffsetX=2.58503, 
        viewOffsetY=0.301226)
    session.viewports['Viewport: 1'].view.setValues(width=46.3514, height=24.0142, 
        viewOffsetX=2.42081, viewOffsetY=0.33902)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=64.8899, 
        farPlane=98.6119, width=46.0607, height=23.8635, cameraPosition=(53.2911, 
        -39.4867, 61.7578), cameraUpVector=(-0.352785, 0.687176, 0.635085), 
        cameraTarget=(20.6587, 0.813854, 0.0246708), viewOffsetX=2.40562, 
        viewOffsetY=0.336893)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=65.7902, 
        farPlane=97.7116, width=38.788, height=20.0957, viewOffsetX=1.40575, 
        viewOffsetY=1.18376)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=63.1486, 
        farPlane=100.605, width=37.2306, height=19.2888, cameraPosition=(65.4299, 
        -45.0861, 48.7653), cameraUpVector=(-0.37242, 0.487067, 0.789981), 
        cameraTarget=(21.0213, 0.793722, -0.45763), viewOffsetX=1.34931, 
        viewOffsetY=1.13623)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=62.6567, 
        farPlane=101.096, width=39.2986, height=20.3602, viewOffsetX=2.73441, 
        viewOffsetY=1.07801)
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
