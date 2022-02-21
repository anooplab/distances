import sys

import sys
import re
import numpy as np
import pandas as pd
from atomic_data import atomic_masses, atomic_numbers, covalent_radii, vdw_radii


def read_xyz(filename):
    with open(filename) as fp:
        f = fp.readlines()
    try:
        number_of_atoms = int(f[0])
    except ValueError as e:
        sys.exit(f"First line should be number of atoms in the file {filename}")
    try:
        geometry_section = [each_line.split() for each_line in f[2:] if
                            len(each_line) >= 4]
    except Exception as e:
        sys.exit(
            "Something wrong with reading the geometry section")
    if len(geometry_section) != number_of_atoms:
        sys.exit('Error in reading %s' % filename)
    atoms_list = []
    coordinates = []
    for c in geometry_section:
        try:
            symbol = c[0].capitalize()
            x_coord = float(c[1])
            y_coord = float(c[2])
            z_coord = float(c[3])
        except ValueError as e:
            sys.exit('Error in reading %s' % filename)
        atoms_list.append(symbol)
        coordinates.append([x_coord, y_coord, z_coord])

    mol_coordinates = np.array(coordinates)
    mol_name = filename[:-4]
    return atoms_list, mol_coordinates, mol_name


def calculate_distances(name, df):
    atoms_list, coordinates, name  = read_xyz(name)
    for i, c in enumerate(coordinates):
        for j, d in enumerate(coordinates):
            a = covalent_radii[atomic_numbers[atoms_list[i]]]
            b = covalent_radii[atomic_numbers[atoms_list[j]]]
            sum_of_covalent_radii = (a+b) * 1.3
            distance = np.linalg.norm(c - d)
            if j > i and distance < sum_of_covalent_radii:
                df = df.append({'Bond': '-'.join(sorted([atoms_list[i], atoms_list[j]])),
                                'Atom 1': i, 'Atom 2': j,
                                'Distance': distance, 'Filename':name},
                               ignore_index=True)
    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('xyz_file_name', nargs='+')
    args = parser.parse_args()
    xyz_files = args.xyz_file_name
    distance_data = pd.DataFrame(columns=['Bond', 'Atom 1', 'Atom 2', 'Distance', 'Filename'])
    for xyz_file in xyz_files:
        df = calculate_distances(xyz_file, distance_data)
        distance_data = distance_data.append(df, ignore_index=True)
    for fr in distance_data.groupby(distance_data.Bond):
        print(fr[0])
        print(fr[1])
        print(fr[1].Distance.describe())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
