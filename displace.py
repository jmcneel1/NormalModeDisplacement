import os
import sys
import numpy as np

# Here we read the file into a variable. This shouldn't be an issue except for HUGE molecules

with open(sys.argv[1],'r') as hess:
  lines = hess.readlines();
  
# Now we find the position of the normal modes and atoms section of the hessian file

lnum = 1;
for line in lines:
  if "$normal_modes" in line:
    break;
  lnum = lnum + 1;
alnum = 1;
for line in lines:
  if "$atoms" in line:
    break;
  alnum = alnum + 1;

# The line after $normal_modes should contain 2 equivalent numbers equal to 3N. Here we read it.
# We also read the number of atoms which is on the line after "$atoms"

num_modes = int(lines[lnum].split()[0]);
num_atoms = int(lines[alnum].split()[0]);

# Now we count the number of lines to skip before we get to our NM entry in the hessian

block = int(sys.argv[2]) // 5;
lines_block = block * (num_modes + 1);

# Now we initialize our numpy arrays

displacements = np.zeros(num_modes, dtype = float);
atoms = np.empty(num_atoms, dtype = object);
xs = np.zeros(num_atoms, dtype = float);
ys = np.zeros(num_atoms, dtype = float);
zs = np.zeros(num_atoms, dtype = float);

# Now we read in the displacements. They are given in Angstroem in the Hessian...

for index in range(0,num_modes):
  displacements[index] = float(lines[lnum+index+lines_block+2].split()[int(sys.argv[2]) % 5 + 1]);

# Now we read in the initial geometry ... in Bohrs

for index in range(0,num_atoms):
  atoms[index] = lines[alnum+index+1].split()[0];
  xs[index] = float(lines[alnum+index+1].split()[2]);
  ys[index] = float(lines[alnum+index+1].split()[3]);
  zs[index] = float(lines[alnum+index+1].split()[4]);
  
# And finally displace the atoms, first converting to Bohrs

for index in range(0,num_atoms):
  xs[index] = xs[index] + float(sys.argv[3])*displacements[index*3]/0.529177;
  ys[index] = ys[index] + float(sys.argv[3])*displacements[index*3+1]/0.529177;
  zs[index] = zs[index] + float(sys.argv[3])*displacements[index*3+2]/0.529177;
  
# And Print out the results

print(num_atoms);
print('Displaced '+sys.argv[3]+' : Mode '+sys.argv[2]);
for i in range(0,num_atoms):
  print(atoms[i]+'  '+str(xs[i]*0.529177)+'  '+str(ys[i]*0.529177+'  '+str(zs[i]*0.529177)));


