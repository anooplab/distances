This repository contains a script (distance.py) that takes a list of XYZ files as an argument and calculates the bond lengths for each one. It also has an option to group the results by bond, file, or both.

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
