# -*- coding: utf-8 -*-
from collections import Counter
from itertools import combinations

import numpy as np

from ....Classes.ElementMat import ElementMat
from ....Classes.FPGNSeg import FPGNSeg
from ....Classes.RefSegmentP1 import RefSegmentP1


def interface(self, other_mesh: "MeshMat") -> "MeshMat":
    """Define a MeshMat object corresponding to the exact intersection between two meshes (nodes must be in both meshes).

    Parameters
    ----------
    self : MeshMat
        a Mesh object
    other_mesh : Mesh
        an other Mesh object

        Returns
    -------
    """

    # Dynamic import
    new_mesh = self.copy()
    new_mesh._is_renum = True

    # new_mesh.node = NodeMat()
    new_mesh.element_dict = dict()

    for key in self.element_dict:
        # Developer info: IDK if this code works with other than triangle elements. To be checked.
        if self.element_dict[key].nb_node_per_element == 3:  # Triangle case
            new_mesh.element_dict["line"] = ElementMat(
                nb_node_per_element=2, gauss_point=FPGNSeg(), ref_element=RefSegmentP1()
            )

            connect = self.element_dict[key].get_connectivity()
            connect2 = other_mesh.element_dict[key].get_connectivity()

            nodes_tags = np.unique(connect)
            other_nodes_tags = np.unique(connect2)

            # Find the nodes on the interface (they are in both in and out)
            interface_nodes_tags = np.intersect1d(nodes_tags, other_nodes_tags)
            nb_interf_nodes = len(interface_nodes_tags)

            comb = combinations(range(self.element_dict[key].nb_node_per_element), 2)

            for duo in list(comb):
                col1i = np.mod(duo[0], 3)
                col2i = np.mod(duo[1], 3)
                col1 = connect[:, col1i]
                col2 = connect[:, col2i]

                col1_bin = np.zeros(len(col1))
                col2_bin = np.zeros(len(col1))

                for node in interface_nodes_tags:
                    Icol1i = np.where(col1 == node)[0]
                    Icol2i = np.where(col2 == node)[0]
                    col1_bin[Icol1i] = 1
                    col2_bin[Icol2i] = 1

                # Position in vector where 2 nodes of the same element are on the interface (potential line element)
                I_target = np.where(col1_bin + col2_bin == 2)[0]

                comb2 = combinations(
                    range(other_mesh.element_dict[key].nb_node_per_element), 2
                )
                for duo2 in list(comb2):
                    col1j = np.mod(duo2[0], 3)
                    col2j = np.mod(duo2[1], 3)
                    col12 = connect2[:, col1j]
                    col22 = connect2[:, col2j]

                    col12_bin = np.zeros(len(col12))
                    col22_bin = np.zeros(len(col12))

                    for node in interface_nodes_tags:
                        Icol1i = np.where(col12 == node)[0]
                        Icol2i = np.where(col22 == node)[0]
                        col12_bin[Icol1i] = 1
                        col22_bin[Icol2i] = 1

                    # Same but in the second mesh
                    I_target2 = np.where(col12_bin + col22_bin == 2)[0]

                    for itag in I_target2:
                        e_tag1 = col12[itag]
                        e_tag2 = col22[itag]
                        Iline = np.where(
                            ((col1[I_target] == e_tag1) & (col2[I_target] == e_tag2))
                            | ((col2[I_target] == e_tag1) & (col1[I_target] == e_tag2))
                        )[0]
                        if Iline.size != 0:
                            new_mesh.add_element([e_tag1, e_tag2], "line")

    return new_mesh
