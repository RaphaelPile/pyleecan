from numpy import linspace, array
from SciDataTool.Functions.Plot.plot_2D import plot_2D


def plot_losses(self, N0_array=None):
    """Plot the losses as a fct of speed

    Parameters
    ----------
    self : OutLoss
        An OutLoss object
    N0_array : ndarray
        speed array to use as X axis [rpm]
    """

    if N0_array is None:
        N0_array = linspace(10, 8000, 100)
    if self.parent is None:
        raise Exception("Error: OutLoss is not in Output object")

    p = self.parent.simu.machine.get_pole_pair_number()

    array_list = [
        array([out_loss.get_loss_scalar(speed / 60 * p) for speed in N0_array])
        for out_loss in self.loss_list
    ]

    plot_2D(
        [N0_array],
        array_list,
        xlabel="Speed [rpm]",
        ylabel="Losses [W]",
        legend_list=[out_loss.name for out_loss in self.loss_list],
    )
