#include as follow : execfile('pathto/POP10.py',globals(),{'recipe':recipe_variable_name})
from AutoFill.Ingredient import SingleSphereIngr, MultiSphereIngr
POP10= MultiSphereIngr( 
packingMode = 'random',
color = [1, 0, 0],
sphereFile = 'http://autofill.googlecode.com/svn/data//Lipids/spheres/POP10.sph',
radii = [[2.0899999999999999, 2.6899999999999999, 3.0699999999999998, 1.97, 1.3400000000000001, 2.54, 3.7999999999999998, 4.6500000000000004]],
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
meshFile = 'http://autofill.googlecode.com/svn/data//Lipids/geoms/0/POP10.c4d',
perturbAxisAmplitude = 0.1,
principalVector = [0.0, 0.0, -1.0],
name = 'POP10',
positions = [[(-0.070000000000000007, 3.1200000000000001, -23.079999999999998), (4.0199999999999996, 2.6200000000000001, -13.1), (0.27000000000000002, 3.3399999999999999, -18.550000000000001), (1.04, -6.8399999999999999, -13.539999999999999), (2.2999999999999998, 2.1899999999999999, -21.489999999999998), (3.0800000000000001, -2.2599999999999998, -12.17), (-3.8300000000000001, -0.57999999999999996, -16.719999999999999), (-2.46, -3.1099999999999999, -7.7999999999999998)]],
placeType = 'jitter',
useRotAxis = 1,
nbMol = 0,
)
recipe.addIngredient(POP10)