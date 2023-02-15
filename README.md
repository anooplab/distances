# Analyzing Bond Lengths in Molecules with Python

This is a Python script designed to analyze the bond lengths in molecules using their cartesian coordinates in the .xyz format. It is useful for anyone interested in chemistry or molecular science, and it can be easily used by novices as well.
## Usage

To use the script, simply run the distance.py file from the command line with
the appropriate arguments. The script takes an XYZ file that contains the
coordinates of the atoms of a molecule, and calculates the distances between
pairs of atoms. It then determines which atoms are bonded based on a threshold
that depends on the sum of their covalent radii (adjusted by a scaling
factor), and outputs the information in a Pandas DataFrame. The covalent radii
is read from the `atomic_data.py` file containg the data from ASE ([Atomic
Simukation Environment](https://wiki.fysik.dtu.dk/ase/)).

The output DataFrame contains information about the bond, atoms, distance, and filename. If no bonds are found, it prints a warning message and suggests increasing the threshold value. The script uses the argparse module to parse command line arguments passed to the script. It then iterates over each specified XYZ file and calls the calculate_distances() function to compute the distances between atoms. The resulting data is stored in a Pandas DataFrame called distance_data, which is used to group the results based on the user-specified grouping parameter, by bond, file, or both.

If an output file name is specified, the results are saved to a CSV file. The output format and grouping parameter can be modified using command line options.
Requirements

This script requires the following:

    Python 3.x
    Pandas
    Numpy

## Running the Script

To run the script, simply open a terminal window and navigate to the directory containing the distance.py file. Then, run the following command:

bash
```
python distance.py file1.xyz file2.xyz ... filen.xyz
```
Replace file1.xyz, file2.xyz, etc. with the actual file names that you want to analyze. If you want to modify the output format or grouping parameter, you can use the following options:

```
--groupby {bond,file,both}  # Group the output by bond, file, or both (default: bond)
--format {csv,table}       # Output format (default: csv)
--output OUTPUT_FILE       # Output file name (default: None)
```

For example, if you want to group the output by file and save it to a CSV file named output.csv, you can run the following command:

bash
```
python distance.py --groupby file --format csv --output output.csv file1.xyz file2.xyz ... filen.xyz
```

## Conclusion

With this script, you can easily analyze the bond lengths in molecules using their cartesian coordinates in the .xyz format. It is a great tool for anyone interested in molecular science or chemistry, and it can be easily used by novices as well. If you have any questions or suggestions, feel free to reach out to the author of this script.

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
