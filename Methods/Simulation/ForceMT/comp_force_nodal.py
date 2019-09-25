from pyleecan.Methods import NotImplementedYetError


def comp_force_nodal(self, output):
    """Compute the nodal integrated forces based on Maxwell Tensor (MT). The targeted nodes must be specified as imputs.
    By default, it compute lumped tooth force for a point in the middle of each tooth tip.

    Parameters
    ----------
    self : ForceMT
        A ForceMT object

    output : Output
        an Output object (to update)
    """

    raise NotImplementedYetError("Nodal force not available yet for Maxwell tensor")
