from statest.quantile.simulator.estimator_racetrack1 import\
        RaceTrack, make_lines
from numpy import genfromtxt
import matplotlib.pyplot as plt


def make_bias_plots_from_disk(names_excl={},
                              names_incl=None):
    rt = RaceTrack()
    fig1, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
    if names_incl is None:
        names_incl = set(rt.names)
    qs = genfromtxt(rt.data_save_dir + "/qs.csv", delimiter=",")
    distribns = ["Normal", "LogNormal", "Weibull", "Lomax"]
    axs = [ax1, ax2, ax3, ax4]
    for ix in range(len(distribns)):
        dist = distribns[ix]
        ax = axs[ix]
        for name in names_incl:
            if name not in names_excl:
                u_errs = genfromtxt(rt.data_save_dir +
                                    dist + "/" +
                                    name + "/u_errs.csv", delimiter=',')
                ax.plot(qs, u_errs, label=name)
                ax.set_title("Distribution: " + dist)
                if ix < 3:
                    ax.set_xticks([])
    make_lines(ax1, ax2, ax3, ax4)
    ax1.set_ylim([-0.19, 0.4])
    ax2.set_ylim([-0.55, 0.3])
    ax3.set_ylim([-0.1, 0.1])
    ax4.set_ylim([-1.5, 0.05])
    plt.xlabel("Quantile (q)")
    plt.show()
