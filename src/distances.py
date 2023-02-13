import sys
import numpy as np
import pandas as pd
from atomic_data import atomic_numbers, covalent_radii


def read_xyz(filename):
    """
    
    This function reads an XYZ file and returns the coordinates, atoms list and molecule name.
    
    Parameters:
        filename (str): The file name of the XYZ file
    
    Returns:
        atoms_list (list): A list of atoms in the molecule
        mol_coordinates (numpy.ndarray): The coordinates of the molecule
        mol_name (str): The name of the molecule
    """
    with open(filename) as fp:
        f = fp.readlines()
    try:
        number_of_atoms = int(f[0])
    except ValueError as e:
        sys.exit(f"First line should be number of atoms in the file"
                 f" {filename} {e}")
    try:
        geometry_section = [each_line.split() for each_line in f[2:]
                            if len(each_line) >= 4]

    except ValueError as e:
        sys.exit(f"Something wrong with reading the geometry section \n{e}")
    if len(geometry_section) != number_of_atoms:
        sys.exit(f'Error in reading {filename}')
    atoms_list = []
    coordinates = []
    for c in geometry_section:
        try:
            symbol = c[0].capitalize()
            x_coord = float(c[1])
            y_coord = float(c[2])
            z_coord = float(c[3])
        except ValueError as e:
            sys.exit(f'Error in reading {filename}\n{e}')
        atoms_list.append(symbol)
        coordinates.append([x_coord, y_coord, z_coord])
    mol_coordinates = np.array(coordinates)
    mol_name = filename[:-4]
    return atoms_list, mol_coordinates, mol_name


def calculate_distances(name, scale):
    """
    This function calculates distances between atoms in an XYZ file.
    
    Parameters
    ----------
    name : str
        XYZ filename
    scale : float
        scaling factor for covalent radii
    
    Returns
    -------
    df : Pandas DataFrame
        DataFrame of bonds, atoms, distances, and filename
    
    """
    atoms_list, coordinates, name = read_xyz(name)
    df = pd.DataFrame(
        columns=['Bond', 'Atom 1', 'Atom 2', 'Distance', 'Filename'])
    for i, c in enumerate(coordinates):
        for j, d in enumerate(coordinates):
            a = covalent_radii[atomic_numbers[atoms_list[i]]]
            b = covalent_radii[atomic_numbers[atoms_list[j]]]
            sum_of_covalent_radii = (a + b) * scale
            distance = np.linalg.norm(c - d)
            if j > i and distance < sum_of_covalent_radii:
                df_tmp = pd.DataFrame(
                         {'Bond': '-'.join([atoms_list[i], atoms_list[j]]), 
                          'Atom 1': i, 'Atom 2': j, 
                          'Distance': distance, 'Filename': name}, 
                          index=[0])
                df = pd.concat([df, df_tmp], ignore_index=True)
    if df.empty:
        print(f"{name}.xyz: Warning: No bonds were found!.")
        print("Consider increasing the threshold value by using the '-t <scale>' command line argument, where <scale> is the factor by which the sum of covalent radii will be multiplied.")

    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('xyz_file_name', nargs='+')
    parser.add_argument('-g', '--groupby',
                        choices=['bond', 'file', 'both', 'none'],
                        default='none',
                        help='Group the results by bond, file, or both')
    parser.add_argument('-t', '--tolerance',
                        default=1.3,
                        help='Tolerance for bond distance cutoff. Default is '
                             '1.3, i.e., 1.3 times the sum of covalent radii')
    parser.add_argument('-o', '--output', metavar='output_file_name',
                        help='Create a csv file of the distance data.')

    args = parser.parse_args()

    xyz_files = args.xyz_file_name
    grouping = args.groupby
    bond_tolerance = float(args.tolerance)

    distance_data = pd.DataFrame(
        columns=['Bond', 'Atom 1', 'Atom 2', 'Distance', 'Filename'])

    for xyz_file in xyz_files:
        df_this_file = calculate_distances(xyz_file, bond_tolerance)
        # distance_data = distance_data.append(df_this_file, ignore_index=True)
        distance_data = pd.concat([distance_data, df_this_file], ignore_index=True)

    if distance_data.empty:
        print("\n\nNo bonds found in ", xyz_files)
        print("Consider increasing the threshold value by using the '-t <scale>' command line argument, where <scale> is the factor by which the sum of covalent radii will be multiplied.")
        sys.exit()

    if grouping == 'bond':
        for each_group in distance_data.groupby(distance_data.Bond):
            print(f"Grouped by: {each_group[0]}")
            print("Distance data\n", each_group[1])
            print(each_group[1].Distance.describe())
    elif grouping == 'file':
        for each_group in distance_data.groupby(
                distance_data.Filename):
            print(f"Grouped by: {each_group[0]}")
            print("Distance data\n", each_group[1])
            print(each_group[1].Distance.describe())
    elif grouping == 'both':
        for each_group in distance_data.groupby(
                [distance_data.Bond, distance_data.Filename]):
            print(f"Grouped by: {each_group[0]}")
            print("Distance data\n", each_group[1])
            print(each_group[1].Distance.describe())
    elif grouping == 'none':
        print(distance_data.to_string())
    if args.output:
        distance_data.to_csv(args.output)
