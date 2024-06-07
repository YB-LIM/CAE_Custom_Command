# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2023 replay file
# Internal Version: 2022_09_29-03.11.55 183150
# Run by YLM4 on Fri Jun  7 19:54:59 2024
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

def single_ct():
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
    s.rectangle(point1=(0.0, 0.0), point2=(10.0, 10.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=177.531, 
        farPlane=199.593, width=64.3025, height=33.3144, cameraPosition=(10.7904, 
        2.93246, 188.562), cameraTarget=(10.7904, 2.93246, 0))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseSolidExtrude(sketch=s, depth=10.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].UserMaterial(
        mechanicalConstants=(0.0, ))
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
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=21.0531, 
        farPlane=52.1177, width=45.1652, height=23.4886, cameraPosition=(30.2622, 
        23.9514, 24.1542), cameraTarget=(9.13958, 2.82881, 3.0316))
    p = mdb.models['Model-1'].parts['Part-1']
    e = p.edges
    pickedEdges = e.getSequenceFromMask(mask=('[#fff ]', ), )
    p.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=FINER)
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
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Uniaxial_Tension', previous='Initial', 
        maxNumInc=10000, initialInc=0.1, minInc=1e-10, maxInc=0.1, nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        step='Uniaxial_Tension')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=23.4002, 
        farPlane=50.634, cameraPosition=(22.0798, -10.1651, 34.1315), 
        cameraUpVector=(-0.729654, 0.607602, 0.313728), cameraTarget=(5.20979, 
        4.58042, 5.20979))
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#8 ]', ), )
    region = a.Set(faces=faces1, name='Set-1')
    mdb.models['Model-1'].DisplacementBC(name='Y_Fix', createStepName='Initial', 
        region=region, u1=UNSET, u2=SET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=22.2273, 
        farPlane=51.807, width=40.8198, height=21.1483, cameraPosition=(23.254, 
        -9.13722, 33.9707), cameraTarget=(6.38398, 5.6083, 5.04894))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=22.4784, 
        farPlane=52.1754, cameraPosition=(29.8681, -5.70656, 30.7342), 
        cameraUpVector=(-0.800273, 0.411776, 0.435894), cameraTarget=(6.46112, 
        5.64831, 5.0112))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=21.6278, 
        farPlane=50.5982, cameraPosition=(-2.61808, -24.2938, 24.7109), 
        cameraUpVector=(-0.46767, 0.799033, 0.377931), cameraTarget=(5.8158, 
        5.27909, 4.89155))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=21.4066, 
        farPlane=50.776, cameraPosition=(-3.88711, -22.3219, 26.8551), 
        cameraUpVector=(-0.390752, 0.853976, 0.343566), cameraTarget=(5.8324, 
        5.25329, 4.8635))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=22.2322, 
        farPlane=50.5067, cameraPosition=(9.80875, -17.6573, 33.0485), 
        cameraUpVector=(-0.631528, 0.732657, 0.253746), cameraTarget=(5.6449, 
        5.18943, 4.77871))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=21.6898, 
        farPlane=51.8527, cameraPosition=(30.5084, -16.7457, 20.1284), 
        cameraUpVector=(-0.462814, 0.525812, 0.71367), cameraTarget=(5.52203, 
        5.18402, 4.8554))
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Set(faces=faces1, name='Set-2')
    mdb.models['Model-1'].DisplacementBC(name='X_Sym', createStepName='Initial', 
        region=region, u1=SET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=23.0056, 
        farPlane=50.5406, cameraPosition=(3.41367, -14.9, -25.8873), 
        cameraUpVector=(0.466971, -0.522324, 0.713524), cameraTarget=(5.38508, 
        5.19335, 4.62282))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=22.3499, 
        farPlane=51.4979, cameraPosition=(15.9148, -12.6167, -25.5641), 
        cameraUpVector=(0.265575, -0.527128, 0.807221), cameraTarget=(5.44886, 
        5.205, 4.62447))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=21.0073, 
        farPlane=52.8405, width=52.2828, height=27.0872, cameraPosition=(13.4605, 
        -12.6706, -26.3832), cameraTarget=(2.99451, 5.15115, 3.80537))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.426, 
        farPlane=51.1186, cameraPosition=(29.2011, -20.4579, 1.39962), 
        cameraUpVector=(-0.382728, -0.00929821, 0.923814), cameraTarget=(3.13878, 
        5.07978, 4.06001))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.189, 
        farPlane=52.8415, cameraPosition=(20.3467, -11.9824, -22.8433), 
        cameraUpVector=(0.238792, -0.455284, 0.857727), cameraTarget=(3.46843, 
        4.76423, 4.96259))
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
    region = a.Set(faces=faces1, name='Set-3')
    mdb.models['Model-1'].DisplacementBC(name='Z_Sym', createStepName='Initial', 
        region=region, u1=UNSET, u2=UNSET, u3=SET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
        amplitude=UNSET, distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].view.setValues(width=55.62, height=28.8161, 
        cameraPosition=(20.2078, -12.2899, -22.7424), cameraTarget=(3.32954, 
        4.45675, 5.06347))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3401, 
        farPlane=52.1707, cameraPosition=(25.5638, -24.1471, 7.95329), 
        cameraUpVector=(-0.375647, 0.237399, 0.895841), cameraTarget=(3.24474, 
        4.64448, 4.57747))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.7602, 
        farPlane=52.2233, cameraPosition=(31.9695, -9.75066, 21.7809), 
        cameraUpVector=(-0.728967, 0.190032, 0.657643), cameraTarget=(3.09604, 
        4.31029, 4.25648))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7266, 
        farPlane=50.2568, width=40.8198, height=21.1483, cameraPosition=(32.6185, 
        -9.14709, 21.1959), cameraTarget=(3.74503, 4.91387, 3.67148))
    session.viewports['Viewport: 1'].view.setValues(cameraPosition=(32.6185, 
        -9.14709, 21.1959), cameraUpVector=(-0.616803, 0.425794, 0.662007), 
        cameraTarget=(3.74503, 4.91387, 3.67148))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.7266, 
        farPlane=50.2569, width=46.1971, height=23.9342, cameraPosition=(32.153, 
        -10.2683, 21.0633), cameraTarget=(3.2795, 3.79271, 3.53892))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        step='Uniaxial_Tension')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.9268, 
        farPlane=49.3551, cameraPosition=(31.0085, 14.8824, 23.9684), 
        cameraUpVector=(-0.86351, 0.144669, 0.483138), cameraTarget=(3.33162, 
        2.64723, 3.40661))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.964, 
        farPlane=50.308, cameraPosition=(32.4593, -9.13878, 20.714), 
        cameraUpVector=(-0.658962, 0.322757, 0.679409), cameraTarget=(3.20463, 
        4.74972, 3.69145))
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#2 ]', ), )
    region = a.Set(faces=faces1, name='Set-4')
    mdb.models['Model-1'].DisplacementBC(name='Tension', 
        createStepName='Uniaxial_Tension', region=region, u1=UNSET, u2=5.0, 
        u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 
        'SDV', 'STATUS'), numIntervals=100)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(width=49.1459, height=25.4619, 
        cameraPosition=(32.5921, -8.91307, 20.6699), cameraTarget=(3.33747, 
        4.97543, 3.6473))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.3918, 
        farPlane=50.4341, cameraPosition=(27.7416, 24.0357, 21.4568), 
        cameraUpVector=(-0.656764, -0.380897, 0.650829), cameraTarget=(3.61048, 
        3.12094, 3.60301))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.8674, 
        farPlane=49.9587, width=43.4253, height=22.4982, cameraPosition=(27.1736, 
        24.9771, 21.1217), cameraTarget=(3.04248, 4.06238, 3.26788))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.3414, 
        farPlane=49.2318, cameraPosition=(29.5841, 19.777, 22.8705), 
        cameraUpVector=(-0.702343, -0.361231, 0.613373), cameraTarget=(2.85252, 
        4.47217, 3.13007))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7616, 
        farPlane=48.8117, width=38.3706, height=19.8794, cameraPosition=(29.784, 
        19.4244, 22.8732), cameraTarget=(3.05237, 4.1196, 3.13279))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3082, 
        farPlane=48.2636, cameraPosition=(31.2351, 17.7978, 22.0189), 
        cameraUpVector=(-0.697763, -0.3274, 0.637131), cameraTarget=(2.93216, 
        4.25434, 3.20356))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.9132, 
        farPlane=48.6586, width=38.3706, height=19.8794, cameraPosition=(30.3247, 
        19.7045, 22.0158), cameraTarget=(2.02178, 6.16109, 3.2005))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].steps.changeKey(fromName='Uniaxial_Tension', 
        toName='Confined_Tension')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.1378, 
        farPlane=46.6737, cameraPosition=(29.1595, -1.3361, 25.7369), 
        cameraUpVector=(-0.835402, 0.168467, 0.523184), cameraTarget=(2.11833, 
        7.90459, 2.89216))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7817, 
        farPlane=46.4728, cameraPosition=(29.9685, 2.40303, 25.9292), 
        cameraUpVector=(-0.841185, 0.142026, 0.521763), cameraTarget=(2.01398, 
        7.42231, 2.86736))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.6854, 
        farPlane=45.907, cameraPosition=(33.4459, 6.13956, 21.3938), 
        cameraUpVector=(-0.751181, 0.072915, 0.656057), cameraTarget=(1.59212, 
        6.96901, 3.41757))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=20.4056, 
        farPlane=45.1867, width=31.87, height=16.5115, cameraPosition=(33.3401, 
        6.22194, 21.5851), cameraTarget=(1.4863, 7.05139, 3.60888))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.5293, 
        farPlane=44.8877, cameraPosition=(34.4123, -2.16883, 16.1669), 
        cameraUpVector=(-0.604134, 0.153079, 0.782042), cameraTarget=(1.36242, 
        8.02087, 4.2349))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=20.9469, 
        farPlane=44.8515, cameraPosition=(35.6529, 10.0242, 15.992), 
        cameraUpVector=(-0.619436, -0.0161549, 0.784881), cameraTarget=(1.19383, 
        6.36391, 4.25867))
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#30 ]', ), )
    region = a.Set(faces=faces1, name='Set-5')
    mdb.models['Model-1'].boundaryConditions['Z_Sym'].setValues(region=region)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.2687, 
        farPlane=45.1357, cameraPosition=(27.7105, -14.2383, 16.0011), 
        cameraUpVector=(-0.454075, 0.41971, 0.785913), cameraTarget=(2.08375, 
        9.08245, 4.25765))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.3591, 
        farPlane=45.0245, cameraPosition=(33.5004, -2.80305, 17.8371), 
        cameraUpVector=(-0.607199, 0.283278, 0.742336), cameraTarget=(1.1919, 
        7.321, 3.97483))
    a = mdb.models['Model-1'].rootAssembly
    f1 = a.instances['Part-1-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#5 ]', ), )
    region = a.Set(faces=faces1, name='Set-6')
    mdb.models['Model-1'].boundaryConditions['X_Sym'].setValues(region=region)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=19.0311, 
        farPlane=45.3526, width=36.0684, height=18.6866, cameraPosition=(33.1047, 
        -3.40228, 18.3218), cameraTarget=(0.796162, 6.72177, 4.45953))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.7718, 
        farPlane=46.3121, cameraPosition=(32.057, 16.2672, 19.1933), 
        cameraUpVector=(-0.663786, -0.187526, 0.724032), cameraTarget=(0.939148, 
        4.03722, 4.34058))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        step='Confined_Tension')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.5855, 
        farPlane=47.4984, width=46.1971, height=23.9342, cameraPosition=(31.2994, 
        19.2204, 18.3489), cameraTarget=(0.1815, 6.99042, 3.49621))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.2199, 
        farPlane=48.7688, cameraPosition=(29.001, 22.6232, 19.6591), 
        cameraUpVector=(-0.62085, -0.3628, 0.694925), cameraTarget=(0.467077, 
        6.56761, 3.33341))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=17.6669, 
        farPlane=48.3218, width=40.8198, height=21.1483, cameraPosition=(29.1317, 
        22.4514, 19.5996), cameraTarget=(0.597771, 6.39581, 3.27394))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=18.4965, 
        farPlane=48.6189, cameraPosition=(26.4677, 27.2252, 18.5053), 
        cameraUpVector=(-0.569874, -0.397504, 0.71919), cameraTarget=(0.887717, 
        5.87623, 3.39305))
