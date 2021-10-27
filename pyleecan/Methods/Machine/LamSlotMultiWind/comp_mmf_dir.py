from ....Functions.Load.import_class import import_class


def comp_mmf_dir(self, felec=1, current_dir=1, is_plot=False):
    """Compute the rotation direction of the fundamental magnetomotive force induced by the winding

    Parameters
    ----------
    self : LamSlotMultiWind
        A LamSlotMultiWind object
    felec : float
        Stator current frequency to consider
    current_dir: int
        Stator current rotation direction +/-1
    is_plot: bool
        True to plot fft2 of stator MMF

    Returns
    -------
    mmf_dir : int
        -1 or +1
    """

    # Call method of LamSlotWind
    LamSlotWind = import_class("pyleecan.Classes", "LamSlotWind")

    rot_dir = LamSlotWind.comp_mmf_dir(
        self, felec=felec, current_dir=current_dir, is_plot=is_plot
    )

    return rot_dir
