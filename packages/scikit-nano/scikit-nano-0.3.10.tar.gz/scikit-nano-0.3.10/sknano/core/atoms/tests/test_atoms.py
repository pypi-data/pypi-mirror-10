#! /usr/bin/env python

from __future__ import absolute_import, division, print_function
from __future__ import unicode_literals
from builtins import range

import nose
from nose.tools import *
from sknano.core.atoms import Atom, Atoms
from sknano.testing import generate_atoms


def test_instantiation():
    atoms = Atoms()
    assert_is_instance(atoms, Atoms)
    for Z in range(1, 101):
        atoms.append(Atom(Z))
    assert_equals(atoms.Natoms, 100)


def test_delete():
    atoms = generate_atoms(elements='periodic_table')
    print(atoms)


def test3():
    atoms = generate_atoms(elements='periodic_table')

    atoms_slice = atoms[5:10]
    print(atoms_slice)


def test4():
    atoms = generate_atoms(elements='periodic_table')
    print(atoms[:5])

    atoms_slice = atoms[5:10]

    atoms[:5] = atoms_slice
    assert_equal(atoms[:5], atoms[5:10])
    print(atoms[:5])

    atoms[:5] = ['C', 'H', 'N', 'Ar', 'He']
    print(atoms[:8])

    atoms[0] = 'Au'
    print(atoms[:2])


if __name__ == '__main__':
    nose.runmodule()
