from numpy import sum as np_sum, zeros, array

from ....Functions.Electrical.comp_loss_joule import comp_loss_joule


def comp_loss(self):
    """Calculate joule losses in stator windings

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate joule losses

    Returns
    -------
    Pjoule_density : ndarray
        Joule loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent is None:
        raise Exception("Cannot calculate joule losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise Exception("Cannot calculate joule losses if OutElec is None")

    if self.parent.is_get_meshsolution and output.mag is None:
        raise Exception("Cannot calculate joule losses if OutMag is None")

    machine = output.simu.machine

    OP = output.elec.OP
    felec = OP.get_felec()

    lam = machine.stator
    T_op = self.parent.Tsta

    Rs = lam.comp_resistance_wind(T=T_op)
    qs = lam.winding.qs

    if self.type_skin_effect > 0:
        # Account for skin effect
        k, power = self.comp_coeff(
            T_op=T_op,
        )

    # Calculate overall joule losses
    Pjoule = qs * Rs * (OP.Id_ref ** 2 + OP.Iq_ref ** 2) * (1 + k * felec ** power)

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    Lst = lam.L1

    # Get surface cells for windings
    ms = output.mag.meshsolution
    Se = ms.mesh[0].get_cell_area()[ms.group[self.group]]

    # Constant component and twice the electrical frequency have same joule density values
    freqs = array([felec])
    Pjoule_density = zeros((freqs.size, Se.size))
    Pjoule_density[0, :] = Pjoule / (per_a * Lst * np_sum(Se))

    coeff = qs * Rs * (OP.Id_ref ** 2 + OP.Iq_ref ** 2)
    A= coeff * k
    B = coeff 
    self.coeff_dict = {"A": A, "B": B, "C": 0, "a": power, "b": 0, "c": 0}

    return Pjoule_density, freqs
