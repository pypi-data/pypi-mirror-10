#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    02.06.2015 17:45:11 CEST
# File:    _hamilton.py

from __future__ import division, print_function

from . import vectors

import warnings
import numpy as np
import scipy.linalg as la


class Hamilton(object):
    """
    Describes a tight-binding model for use with :class:`z2pack.tb.System`.
    """
    def __init__(self):
        self._reset_atoms()

    def _reset_atoms(self):
        self._atoms = []
        self._hoppings = []
        self._electrons = 0

    def __getattr__(self, key):
        if key == 'hamiltonian':
            return self.create_hamiltonian()

        else:
            raise AttributeError

    def add_atom(self, element, position):
        """
        :param element:     A tuple ``(orbitals, num_electrons)``, where \
        ``orbitals`` is the list of orbital energies and ``num_electrons`` \
        the number of electrons.

        :param position:    Position relative to the reciprocal lattice vector
        :type position:     list of length 3

        :returns:           Index of the atom
        :rtype:             int
        """

        # check input
        if len(position) != 3:
            raise ValueError('position must be a list/tuple of length 3')
        if len(element) != 2:
            raise ValueError("bad argument for 'element' input variable")
        if not isinstance(element[1], int):
            raise ValueError("num_electrons must be an integer")

        # add the atom - store as (orbitals, num_electrons, position)
        self._atoms.append((tuple(element[0]), element[1], tuple(position)))
        # return the index the atom will get
        return len(self._atoms) - 1

    def add_hopping(self, orbital_pairs, rec_lattice_vec,
                    overlap, phase=None, add_conjugate=True):
        r"""
        Adds a hopping term between orbitals. If the orbitals are not equal,
        the complex conjugate term is also added.

        :param orbital_pairs:       A tuple ``(orbital_1, orbital_2)``, where
            ``orbital_*`` is again a tuple ``(atom_index, orbital_index)``. Can
            also be a list of orbital pairs.

        :param rec_lattice_vec:     Vector connecting unit cells (``list`` of
            length 3), or list of such vectors

        :param overlap:             Strength of the hopping

        :param phase:               Multiplicative factor for the overlap or
            a ``list`` of factors (one for each ``rec_lattice_vec``)

        :param add_conjugate:       Toggles adding the complex conjugate hopping
            automatically.
        :type add_conjugate:        Boolean
        """
        # check if there are multiple orbital pairs
        try:
            orbital_pairs[0][0][0]
            for pair in orbital_pairs:
                self.add_hopping(pair, rec_lattice_vec, overlap, phase)
        except TypeError:
            # check if the orbitals exist
            num_atoms = len(self._atoms)
            if not(orbital_pairs[0][0] < num_atoms and orbital_pairs[1][0] <
                   num_atoms):
                raise ValueError("atom index out of range")
            if not(orbital_pairs[0][1] <
                   len(self._atoms[orbital_pairs[0][0]][0])):
                raise ValueError("orbital index out of range \
                                 (orbital_pairs[0])")
            if not(orbital_pairs[1][1] <
                   len(self._atoms[orbital_pairs[1][0]][0])):
                raise ValueError("orbital index out of range \
                                 (orbital_pairs[1])")

            # check if there are multiple rec_lattice_vec
            if(hasattr(rec_lattice_vec[0], '__getitem__') and
               hasattr(rec_lattice_vec[0], '__iter__')):
                if phase is None:
                    phase = 1
                if (hasattr(phase, '__getitem__') and
                        hasattr(phase, '__iter__')):
                    if len(phase) == 1:
                        for vec in rec_lattice_vec:
                            self.add_hopping(orbital_pairs,
                                             vec,
                                             overlap * phase[0])
                    else:
                        for i, vec in enumerate(rec_lattice_vec):
                            self.add_hopping(orbital_pairs,
                                             vec,
                                             overlap * phase[i])
                else:
                    for vec in rec_lattice_vec:
                        self.add_hopping(orbital_pairs, vec, overlap * phase)

            else:
                # check rec_lattice_vec
                if len(rec_lattice_vec) != 3:
                    raise ValueError('length of rec_lattice_vec must be 3')
                for coord in rec_lattice_vec:
                    if not isinstance(coord, int):
                        raise ValueError('rec_lattice_vec must consist \
                                         of integers')

                # add hopping
                rec_lattice_vec = np.array(rec_lattice_vec)
                indices_1 = (orbital_pairs[0][0], orbital_pairs[0][1])
                indices_2 = (orbital_pairs[1][0], orbital_pairs[1][1])
                self._hoppings.append((overlap,
                                       indices_1,
                                       indices_2,
                                       rec_lattice_vec))
                if add_conjugate:
                    self._hoppings.append((overlap.conjugate(),
                                           indices_2,
                                           indices_1,
                                           -rec_lattice_vec))

    def explicit_hamiltonian(self, hamiltonian, atoms_at_origin=True,
                             occupied=None):
        r"""
        Deprecated function for creating a Hamiltonian from an explicit function. Use the :class:`ExplicitHamilton` class instead.
        """
        warnings.warn('Using deprecated function explicit_hamiltonian. Use the ExplicitHamilton class instead.',
            DeprecationWarning, stacklevel=2)
        size = len(hamiltonian([0, 0, 0])) # assuming to be square...

        # add one atom for each orbital in the hamiltonian
        if atoms_at_origin:
            self._reset_atoms()
            for i in range(size):
                self.add_atom(([0], 1), [0, 0, 0])

        self._parse_atoms()

        if len(self._T_list) != size:
            raise ValueError('The number of orbitals found in the atoms ({0}) does not match the size of the Hamiltonian ({1})'.format(len(self._T_list), size))

        if occupied is not None:
            self._num_electrons = occupied

        self.hamiltonian = hamiltonian


    def create_hamiltonian(self):
        """
        Creates the ``hamiltonian`` member variable, which returns the
        Hamiltonian matrix as a function of k (as a ``list`` of lenth 3).

        :returns: ``hamiltonian``
        """
        self._parse_atoms()

        # checking for the minimum and maximum rec_lattice vecs
        xmin = xmax = ymin = ymax = zmin = zmax = 0
        for hopping in self._hoppings:
            vec = hopping[3]
            xmin = min(xmin, vec[0])
            ymin = min(ymin, vec[1])
            zmin = min(zmin, vec[2])
            xmax = max(xmax, vec[0])
            ymax = max(ymax, vec[1])
            zmax = max(zmax, vec[2])

        pow_fac = 2j * np.pi
        def _H(k):
            # precomputing the exponential
            k = np.array(k)
            exp_precomputed = []
            for x in range(xmin, xmax + 1):
                tmp_x = []
                for y in range(ymin, ymax + 1):
                    tmp_y = []
                    for z in range(zmin, zmax + 1):
                        tmp_z = np.exp(pow_fac *  np.dot([x, y, z], k))
                        tmp_y.append(tmp_z)
                    tmp_x.append(tmp_y)
                exp_precomputed.append(tmp_x)

            # setting up the hamiltonian
            H = np.diag([complex(energy) for atom in self._atoms for energy in atom[0]])
            for hopping in self._hoppings:
                index1 = self._orbital_to_index[hopping[1][0]][hopping[1][1]]
                index2 = self._orbital_to_index[hopping[2][0]][hopping[2][1]]
                mat_element = hopping[0] * exp_precomputed[hopping[3][0] - xmin][hopping[3][1] - ymin][hopping[3][2] - zmin]
                H[index1, index2] += mat_element
            return H

        self.hamiltonian = _H
        return self.hamiltonian

    def _parse_atoms(self):
        # create conversion from index to orbital/vice versa
        count = 0
        self._orbital_to_index = []
        self._T_list = []
        for _, atom in enumerate(self._atoms):
            num_orbitals = len(atom[0])
            self._orbital_to_index.append([count + i for i in range(num_orbitals)])
            for i in range(num_orbitals):
                self._T_list.append(atom[2])
            count += num_orbitals
        # needed for _get_m
        self._num_electrons = sum(atom[1] for atom in self._atoms)

    def _get_m(self, kpt):
        """
        returns:        M-matrices

        args:
        ~~~~
        string_dir:     axis along which string goes (index in 0,1,2)
        string_pos:     position of string as a list where the coord.
                        in string_dir has been removed
        N:              number of steps in the string
        """
        # create k-points for string
        N = len(kpt) - 1
        k_points = kpt[:-1]

        # get eigenvectors corr. to occupied states
        eigs = []
        for k in k_points:
            eigval, eigvec = la.eig(self.hamiltonian(k))
            eigval = np.real(eigval)
            idx = eigval.argsort()
            idx = idx[:self._num_electrons]
            idx.sort()  # preserve the order of the wcc
            eigvec = eigvec[:, idx]
            # take only the lower - energy eigenstates
            eigs.append(np.array(eigvec))

        # last eigenvector = first one
        eigs.append(eigs[0])
        eigsize, eignum = eigs[0].shape

        # create M - matrices
        M = []
        for i in range(0, N):
            deltak = list(np.array(kpt[i + 1]) - np.array(kpt[i]))
            Mnew = [[sum(np.conjugate(eigs[i][j, m]) *
                     eigs[i + 1][j, n] *
                     np.exp(-2j * np.pi * np.dot(deltak, self._T_list[j]))
                     for j in range(eigsize))
                     for n in range(eignum)]
                    for m in range(eignum)]
            M.append(Mnew)
        return M

