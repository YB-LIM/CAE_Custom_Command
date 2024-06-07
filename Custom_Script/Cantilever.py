# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_29-03.11.55 183150
# Run by YLM4 on Fri Jun  7 19:29:07 2024
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

def cantilever():
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
    s.rectangle(point1=(0.0, 0.0), point2=(5.0, 5.0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=40.0)
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
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=None)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(cells=cells, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=67.0762, 
        farPlane=111.159, width=49.7302, height=25.8627, viewOffsetX=3.08929, 
        viewOffsetY=-1.65529)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=4.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=1.5, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
    p.seedEdgeBySize(edges=pickedEdges, size=1.0, deviationFactor=0.1, 
        constraint=FINER)
    p = mdb.models['Model-1'].parts['Part-1']
    p.generateMesh()
    elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, 
        kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF, 
        hourglassControl=DEFAULT, distortionControl=DEFAULT)
    elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
    elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['Part-1']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(cells, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
        adaptiveMeshConstraints=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', 
        maxNumInc=10000, initialInc=0.1, minInc=1e-10, maxInc=0.1, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=67.9036, 
        farPlane=110.332, width=44.4709, height=23.0399, viewOffsetX=0.481045, 
        viewOffsetY=-0.239552)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=60.2288, 
        farPlane=114.863, width=39.4446, height=20.4358, cameraPosition=(23.4004, 
        12.2533, -64.458), cameraUpVector=(-0.526056, 0.789606, 0.31589), 
        cameraTarget=(2.79543, 1.71752, 21.6026), viewOffsetX=0.426675, 
        viewOffsetY=-0.212477)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=65.501, 
        farPlane=109.172, width=42.8974, height=22.2247, cameraPosition=(63.5732, 
        28.586, 76.7316), cameraUpVector=(-0.609586, 0.76122, -0.221242), 
        cameraTarget=(1.18891, 0.985869, 19.3867), viewOffsetX=0.464025, 
        viewOffsetY=-0.231077)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=65.2508, 
        farPlane=109.192, width=42.7336, height=22.1398, cameraPosition=(61.1328, 
        36.8154, 74.711), cameraUpVector=(-0.621699, 0.711975, -0.326467), 
        cameraTarget=(1.22132, 0.859539, 19.3955), viewOffsetX=0.462253, 
        viewOffsetY=-0.230194)
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Model-1'].DisplacementBC(name='BC-1', createStepName='Initial', 
        region=region, u1=SET, u2=SET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(width=45.4447, height=23.5444, 
        viewOffsetX=0.820043, viewOffsetY=-0.444072)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=64.8343, 
        farPlane=109.434, width=45.1711, height=23.4026, cameraPosition=(58.7093, 
        41.5519, 73.9303), cameraUpVector=(-0.540553, 0.687002, -0.485623), 
        cameraTarget=(1.23816, 0.927567, 19.2609), viewOffsetX=0.815104, 
        viewOffsetY=-0.441398)
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].view.setValues(width=66.0531, height=34.2214, 
        cameraPosition=(60.8592, 40.564, 72.4043), cameraTarget=(4.6674, 0.843985, 
        18.9519))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=61.7134, 
        farPlane=112.453, cameraPosition=(60.2461, 43.4425, 70.805), 
        cameraUpVector=(-0.549793, 0.659498, -0.512631), cameraTarget=(4.6674, 
        0.84398, 18.9519))
