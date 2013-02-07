#include as follow : execfile('pathto/POP5.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP5= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP5.sph',
radii = [[2.5499999999999998, 4.71, 4.5199999999999996, 1.28, 2.2200000000000002, 3.73, 2.0, 4.5800000000000001]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP5.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP5',
positions = [[(-4.2999999999999998, 3.71, -10.279999999999999), (4.5199999999999996, -0.76000000000000001, -12.1), (1.1599999999999999, -2.5, -19.899999999999999), (-6.8099999999999996, 3.0600000000000001, -1.0), (-0.94999999999999996, -0.26000000000000001, -20.27), (-0.82999999999999996, 3.1600000000000001, -16.59), (-5.7800000000000002, 3.5600000000000001, -4.8700000000000001), (3.5, -5.2000000000000002, -3.2200000000000002)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP5)