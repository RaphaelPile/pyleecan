def comp_force(self, output):
    """Compute magnetic forces based on Maxwell Tensor (MT).

    Parameters
    ----------
    self : ForceMT
        A ForceMT object

    output : Output
        an Output object (to update)
    """

    name_subpart = self.force.name_subpart

    self.force.comp_force_field(output, name_subpart)

    if self.force.is_comp_nodal_force:
        self.force.comp_force_nodal(output, name_subpart)
