Calculate all bond distances from an .xyz file.

```
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