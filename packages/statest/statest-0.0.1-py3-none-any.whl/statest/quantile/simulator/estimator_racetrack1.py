from statest.quantile.estimate import est_1, est_2, est_3,\
                                      est_4, est_5, est_6,\
                                      est_7, est_8, est_9
from statest.quantile.expon_based_estimators import prcntl, prcntl2,\
                                                    prcntl3, prcntl4
from statest.quantile.some_distributions import rvs_fn1, rvs_fn2,\
                                                rvs_fn3, rvs_fn4,\
                                                rvs_fn5, rvs_fn6,\
                                                ppf_fn1, ppf_fn2,\
                                                ppf_fn3, ppf_fn4,\
                                                ppf_fn5, ppf_fn6,\
                                                distributions_shelf
from statest.quantile.perf_measurer import PrcntlEstPerfMeasurer
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import pandas as pd
import os


class RaceTrack():
    def __init__(self, distr_name="LogNormal", n=15):
        # Set these parameters manually before running the code.
        self.data_save_dir = "./sim_data/"
        self.plots_save_dir = "./plots/"
        self.distr_name = distr_name
        self.n = n
        self.rvs_fn = distributions_shelf[distr_name][0]
        self.ppf_fn = distributions_shelf[distr_name][1]
        # The number of parallel worlds to simulate. Higher is better.
        self.prll_wrlds = 300000

        # The percentiles to compare performance for.
        self.qs = np.arange(0.01, 1.0, 0.03)
        # Enumerate the estimators.
        self.prcntl_estimators = [prcntl, est_1, est_7,
                                  est_2, est_3, est_4,
                                  est_5, est_6,
                                  est_8, est_9, prcntl2, prcntl3,
                                  prcntl4]

        self.names = ["expon_bias", "r_strat1",
                      "r_strat7",
                      "r_strat2", "r_strat3",
                      "r_strat4", "r_strat5",
                      "r_strat6",
                      "r_strat8", "r_strat9", "expon_bias_m=2",
                      "expon_mle", "expon_bias_max_m"]

    def race(self):
        self.init_axes()
        self.prf_results = []
        for ix in range(len(self.prcntl_estimators)):
            prcntl_est = self.prcntl_estimators[ix]
            name = self.names[ix]
            prf1 = PrcntlEstPerfMeasurer(n=self.n,
                                         rvs_fn=self.rvs_fn,
                                         ppf_fn=self.ppf_fn,
                                         qs=self.qs,
                                         prcntl_estimator=prcntl_est,
                                         prll_wrlds=self.prll_wrlds)
            prf1.simulate()
            self.prf_results.append(prf1)
            self.write_date_to_disk(name, prf1)
            self.plot_figs(name, prf1)
            print("###############")
            print("Finished processing " + name)
            print("###############")

        make_lines(self.ax1, self.ax2, self.ax3, self.ax4)
        self.save_figs()
        plt.show()

    def write_date_to_disk(self, name, prf1):
        if not os.path.exists(self.data_save_dir):
            os.makedirs(self.data_save_dir)
        np.savetxt(self.data_save_dir + "/qs.csv", self.qs, delimiter=",")
        base_path = self.data_save_dir + self.distr_name + "/" + name
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        np.savetxt(self.data_save_dir + self.distr_name + "/" +
                   name + "/u_errs.csv", prf1.u_errs, delimiter=",")
        np.savetxt(self.data_save_dir + self.distr_name + "/" +
                   name + "/u_stds.csv", prf1.u_stds, delimiter=",")
        np.savetxt(self.data_save_dir + self.distr_name + "/" +
                   name + "/u_medians.csv", prf1.u_medians, delimiter=",")
        np.savetxt(self.data_save_dir + self.distr_name + "/" +
                   name + "/u_mses.csv", prf1.u_mses, delimiter=",")

    def plot_figs(self, name, prf1):
        self.ax1.plot(self.qs, prf1.u_errs, label="Bias for " + name)
        self.ax2.plot(self.qs, prf1.u_stds,
                      label="Standard deviation for " + name)
        self.ax3.plot(self.qs, prf1.u_medians,
                      label="DelMedian for " + name)
        self.ax4.plot(self.qs, prf1.u_mses, label="MSE for " + name)

    def save_figs(self):
        base_path = self.plots_save_dir + self.distr_name + "/"
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        self.fig1.savefig(self.plots_save_dir +
                          self.distr_name + "/biases.png")
        self.fig2.savefig(self.plots_save_dir +
                          self.distr_name + "/st_devs.png")
        self.fig3.savefig(self.plots_save_dir +
                          self.distr_name + "/del_medians.png")
        self.fig4.savefig(self.plots_save_dir +
                          self.distr_name + "/mses.png")

    def make_plots_from_disk(self,
                             names_excl={},
                             names_incl=None):
        self.init_axes()
        if names_incl is None:
            names_incl = set(self.names)
        qs = genfromtxt(self.data_save_dir + "/qs.csv", delimiter=",")
        self.res_df = pd.DataFrame()
        self.res_df["qs"] = qs
        for name in names_incl:
            if name not in names_excl:
                u_errs = genfromtxt(self.data_save_dir +
                                    self.distr_name + "/" +
                                    name + "/u_errs.csv", delimiter=',')
                u_stds = genfromtxt(self.data_save_dir +
                                    self.distr_name + "/" +
                                    name + "/u_stds.csv", delimiter=',')
                u_medians = genfromtxt(self.data_save_dir +
                                       self.distr_name + "/" +
                                       name + "/u_medians.csv", delimiter=',')
                u_mses = genfromtxt(self.data_save_dir +
                                    self.distr_name + "/" +
                                    name + "/u_mses.csv", delimiter=',')
                self.res_df[name] = u_errs
                self.ax1.plot(qs, u_errs, label="Bias for " + name)
                self.ax2.plot(qs, u_stds,
                              label="Standard deviation for " + name)
                self.ax3.plot(qs, u_medians, label="DelMedian for " + name)
                self.ax4.plot(qs, u_mses, label="MSE for " + name)
        make_lines(self.ax1, self.ax2, self.ax3, self.ax4)
        plt.show()

    def init_axes(self):
        # fig1, (ax1, ax3) = plt.subplots(2, 1)
        # fig2, (ax2, ax4) = plt.subplots(2, 1)
        self.fig1, self.ax1 = plt.subplots(1, 1)
        self.fig2, self.ax2 = plt.subplots(1, 1)
        self.fig3, self.ax3 = plt.subplots(1, 1)
        self.fig4, self.ax4 = plt.subplots(1, 1)


def make_lines(ax1, ax2, ax3, ax4):
    for ax in [ax1, ax2, ax3, ax4]:
        #ax.xlabel("Percentile (q)")
        ax.axhline(0, color="black")
        ax.axvline(0.5, color="black")
        ax.legend()
