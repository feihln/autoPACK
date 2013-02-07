#include as follow : execfile('pathto/POP35.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP35= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP35.sph',
radii = [[2.3399999999999999, 2.96, 3.1600000000000001, 3.27, 1.6000000000000001, 1.97, 3.52, 3.9700000000000002]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP35.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, 1.0],
name = 'POP35',
positions = [[(-0.070000000000000007, 2.9500000000000002, 20.190000000000001), (0.52000000000000002, 3.4500000000000002, 13.699999999999999), (-4.3399999999999999, -4.5499999999999998, 6.3600000000000003), (-1.23, -2.1400000000000001, 20.84), (4.0899999999999999, 2.23, 21.079999999999998), (3.0499999999999998, 1.1699999999999999, 23.760000000000002), (2.46, 3.21, 6.9900000000000002), (-3.52, -4.8799999999999999, 14.380000000000001)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP35)