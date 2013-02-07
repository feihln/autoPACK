#include as follow : execfile('pathto/POP45.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP45= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP45.sph',
radii = [[1.79, 4.0899999999999999, 2.96, 4.8799999999999999, 0.76000000000000001, 1.9199999999999999, 2.21, 1.3]],
cutoff_boundary = 0,
Type = 'MultiSphere',
cutoff_surface = 0,
gradient = '',
jitterMax = [0.5, 0.5, 0.10000000000000001],
packingPriority = 0,
rotAxis = [0.0, 2.0, 1.0],
nbJitter = 5,
molarity = 1.0,
rotRange = 6.2831,
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP45.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP45',
positions = [[(-3.0800000000000001, 2.4199999999999999, -3.96), (-2.3700000000000001, -0.27000000000000002, -20.289999999999999), (4.79, -4.6200000000000001, -4.0899999999999999), (2.6400000000000001, -3.8799999999999999, -12.23), (-0.56999999999999995, 3.4900000000000002, -9.9800000000000004), (-0.93000000000000005, 5.1200000000000001, -13.359999999999999), (0.45000000000000001, 4.21, -18.0), (-0.82999999999999996, 3.1800000000000002, -7.2199999999999998)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP45)