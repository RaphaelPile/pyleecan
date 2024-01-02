import numpy as np


def element_loop(
    self,
    mesh,
    B,
    H,
    mu,
    indice,
    dim,
    Nt_tot,
    polynomial_coeffs=[[0.719, -0.078, -0.042], [-0.391, 0.114, 0.004]],
):
    """compute nodal forces with a loop on elements and nodes

    from publications:


    Parameters
    ----------
    self : ForceTensor
        A ForceTensor object

    mesh :
        A Mesh object




    polynomial_coeffs : 2x3 List, optional
        alpha(i,j) coeffs for polynomal expression of alpha1 and alpha2

    Return
    ----------
    f : (nb_nodes*dim*Nt_tot) array
        nodal forces

    connect : (nb_element*nb_node_per_element) array
        table of mesh connectivity

    """

    # For every type of element (now only Triangle3, TO BE extended)
    for key in mesh.element_dict:
        # mesh.element_dict[key].interpolation = Interpolation()
        # mesh.element_dict[key].interpolation.init_key(key=key, nb_gauss=1)

        nb_node_per_element = mesh.element_dict[
            key
        ].nb_node_per_element  # Number of nodes per element

        mesh_element_key = mesh.element_dict[key]
        connect = mesh.element_dict[
            key
        ].get_connectivity()  # Each row of connect is an element

        nb_elem = len(connect)

        nb_node = mesh.node.nb_node  # Total nodes number

        # Nodal forces init
        f = np.zeros((nb_node, dim, Nt_tot), dtype=np.float)

        # ref_element = mesh.element_dict[key].ref_element // pas besoin d'interpoler car tout est cst

        # Gauss nodes
        # pts_gauss, poidsGauss, nb_gauss = mesh.element_dict[
        #     key
        # ].gauss_point.get_gauss_points()

        # indice_elem = mesh.element_dict[key].indice

        # Loop on element (elt)
        for elt_indice, elt_number in enumerate(indice):
            node_number = mesh_element_key.get_connectivity(
                elt_number
            )  # elt nodes numbers, can differ from indices
            element_coordinate = mesh.get_element_coordinate(elt_number)[
                key
            ]  # elt nodes coordonates

            # elt physical fields values
            Be = B[elt_indice, :, :]
            He = H[elt_indice, :, :]
            mue = mu[elt_indice, :]
            mu_0 = 4 * np.pi * 1e-7

            Me = np.reshape(
                Be / mu_0 - He, (dim, 1, Nt_tot)
            )  # reshaped for matrix product purpose

            # Total tensor initalization
            total_tensor = np.zeros((dim, dim, Nt_tot))

            # elt magnetostrictive tensor
            if self.tensor["magnetostriction"]:
                tme = self.comp_magnetostrictive_tensor(
                    M=Me, Nt_tot=Nt_tot, polynomial_coeffs=polynomial_coeffs
                )
                total_tensor += tme

            # Triangle orientation, needed for normal orientation. 1 if trigo oriented, -1 otherwise
            orientation_sign = np.sign(
                np.cross(
                    element_coordinate[1] - element_coordinate[0],
                    element_coordinate[2] - element_coordinate[0],
                )
            )

            # Loop on edges
            for n in range(nb_node_per_element):
                # Get current node + next node indices (both needed since pression will be computed on edges because of Green Ostrogradski)
                node_indice = np.where(mesh.node.indice == node_number[n])[0][0]

                next_node_indice = np.where(
                    mesh.node.indice == node_number[(n + 1) % nb_node_per_element]
                )[0][0]

                # Edge cooordinates
                edge_vector = (
                    element_coordinate[(n + 1) % nb_node_per_element]
                    - element_coordinate[n % nb_node_per_element]
                )  # coordonées du vecteur nn+1

                # Volume ratio (Green Ostrogradski)
                L = np.linalg.norm(edge_vector)
                Ve0 = L

                # Normalized normal vector n, that has to be directed outside the element (i.e. normal ^ edge same sign as the orientation)
                normal_to_edge_unoriented = (
                    np.array((edge_vector[1], -edge_vector[0])) / L
                )
                normal_to_edge = (
                    normal_to_edge_unoriented
                    * np.sign(np.cross(normal_to_edge_unoriented, edge_vector))
                    * orientation_sign
                )
                normal_to_edge.reshape(dim, 1)

                # Green Ostrogradski <tensor, normal> scalar product
                edge_force = np.tensordot(
                    total_tensor, normal_to_edge, [[1], [0]]
                )  # [[1],[0]] means sum product over rows for normal (which is vertical) and over rows for tme

                # Total edge force contribution, to be added to the 2 nodes that made the edge
                fe = -Ve0 * edge_force
                f[node_indice, :, :] = f[node_indice, :, :] + fe / 2
                f[next_node_indice, :, :] = f[next_node_indice, :, :] + fe / 2

    return f, connect
