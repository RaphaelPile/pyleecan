def comp_force(self, output):
    """Compute magnetic forces based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : ForceMT
        A ForceMT object

    output : Output
        an Output object (to update)
    """

    self.comp_force_field(output)

    if self.is_comp_force_nodal:
        self.comp_force_nodal(output)
