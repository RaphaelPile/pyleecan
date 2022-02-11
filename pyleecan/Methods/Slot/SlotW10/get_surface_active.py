from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import WIND_LAB


def get_surface_active(self, alpha=0, delta=0):
    """Return the full winding surface

    Parameters
    ----------
    self : SlotW10
        A SlotW10 object
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_wind: Surface
        Surface corresponding to the Winding Area
    """

    # Create curve list
    curve_list = [line for line in self._comp_line_list()[3:-4] if line is not None]
    curve_list.append(
        Segment(begin=curve_list[-1].get_end(), end=curve_list[0].get_begin())
    )

    # Create surface
    H1 = self.get_H1()
    if self.is_outwards():
        Zmid = self.get_Rbo() + self.H0 + H1 + self.H2 / 2
    else:
        Zmid = self.get_Rbo() - self.H0 - H1 - self.H2 / 2
    label = self.parent.get_label() + "_" + WIND_LAB + "_R0-T0-S0"
    surface = SurfLine(line_list=curve_list, label=label, point_ref=Zmid)

    # Apply transformation
    surface.rotate(alpha)
    surface.translate(delta)

    return surface
