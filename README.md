## Introduction

Are you an experimentalist who wants to compare structures from X-ray with optimized geometries? Or a beginner in computational chemistry who wants to compare the geometries of optimized molecules? Maybe you just want to analyze the bond distances between different isomers. Whatever your goal is, we have a Python script that can help automate the process of analyzing bond distances in one or multiple molecules.

To use this script, you will need the molecular structure in cartesian coordinates. You can obtain this information from various sources, such as X-Ray crystallography or computational chemistry calculations. You will also need a Python programming environment. If you're new to Python, don't worry! There are many resources available to help you get started. One easy option is to install the Anaconda package, which includes the necessary tools for writing and executing Python scripts.

The script reads an XYZ file that contains the coordinates of the atoms of a molecule. It calculates the distances between pairs of atoms, determines which atoms are bonded based on a threshold that depends on the sum of their covalent radii (adjusted by a scaling factor), and outputs the information in a Pandas DataFrame. The DataFrame contains information about the bond, atoms, distance, and filename. If no bonds are found, it prints a warning message and suggests increasing the threshold value.

The script uses the argparse module to parse command line arguments passed to the script. It then iterates over each specified XYZ file and calls the calculate_distances() function to compute the distances between atoms. The resulting data is stored in a Pandas DataFrame called distance_data, which is used to group the results based on the user-specified grouping parameter. If an output file name is specified, the results are saved to a CSV file. The output format and grouping parameter can be modified using command line options.

This repository contains the script (distance.py) that takes a list of XYZ files as an argument and calculates the bond lengths for each one. It also has an option to group the results by bond, file, or both.

## Usage

To use the script, download the repository and open a terminal. Navigate to the repository and run the command 
`python bond_lengths.py xyz_file_name1 xyz_file_name2 ...`

## Options

The script has the following options:

- -g, --groupby: Group the results by bond, file, or both.
- -t, --tolerance: Tolerance for bond distance cutoff. Default is 1.3, i.e., 1.3 times the sum of covalent radii.
- -o, --output: Create a csv file of the distance data.

## Example

To calculate the bond lengths of the xyz files molecule1.xyz and molecule2.xyz and save the results in a csv file, run the command
`python bond_lengths.py molecule1.xyz molecule2.xyz -g both -o results.csv`

## Help

```
python distances.py -h

usage: distances.py [-h] [-g {bond,file,both,none}] [-t TOLERANCE] [-o OUTPUT]
                    xyz_file_name [xyz_file_name ...]

positional arguments:
  xyz_file_name

optional arguments:
  -h, --help            show this help message and exit
  -g {bond,file,both,none}, --groupby {bond,file,both,none}
                        Group the results by bond, file, or both
  -t TOLERANCE, --tolerance TOLERANCE
                        Tolerance for bond distance cutoff. Default is 1.3, i.e., 1.3 times
                        the sum of covalent radii
  -o OUTPUT, --output OUTPUT
                        Create a csv file of the distance data.
```
