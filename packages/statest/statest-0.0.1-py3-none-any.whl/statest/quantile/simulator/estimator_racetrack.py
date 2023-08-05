from statest.quantile.estimate import *
from statest.quantile.expon_based_estimators import prcntl, prcntl2, prcntl3, prcntl4, prcntl5
from statest.quantile.some_distributions import *
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
        self.rvs_fn = distributions_holder[distr_name][0]
        self.ppf_fn = distributions_holder[distr_name][1]
        
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

    def main1(self):
        prf_results = []
        #fig1, (ax1, ax3) = plt.subplots(2, 1)
        #fig2, (ax2, ax4) = plt.subplots(2, 1)
        fig1, ax1 = plt.subplots(1, 1)
        fig2, ax2 = plt.subplots(1, 1)
        fig3, ax3 = plt.subplots(1, 1)
        fig4, ax4 = plt.subplots(1, 1)

        for ix in range(len(self.prcntl_estimators)):
            prcntl_est = self.prcntl_estimators[ix]
            name = self.names[ix]
            prf1 = PrcntlEstPerfMeasurer(n=self.n,
                                         rvs_fn=self.rvs_fn,
                                         ppf_fn=self.ppf_fn,
                                         qs=self.qs,
                                         prcntl_estimator=prcntl_est,
                                         prll_wrlds=30000)
            prf1.simulate()
            prf_results.append(prf1)
            ax1.plot(self.qs, prf1.u_errs, label="Bias for " + name)
            ax2.plot(self.qs, prf1.u_stds, label="Standard deviation for " + name)
            ax3.plot(self.qs, prf1.u_medians, label="DelMedian for " + name)
            ax4.plot(self.qs, prf1.u_mses, label="MSE for " + name)

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

            print("###############")
            print("Finished processing " + name)
            print("###############")

        make_lines(ax1, ax2, ax3, ax4)
        base_path = self.plots_save_dir + self.distr_name + "/" + name
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        fig1.savefig(self.plots_save_dir + self.distr_name + "/" + name + "/biases.png")
        fig2.savefig(self.plots_save_dir + self.distr_name + "/" + name + "/st_devs.png")
        fig3.savefig(self.plots_save_dir + self.distr_name + "/" +
                    name + "/del_medians.png")
        fig4.savefig(self.plots_save_dir + self.distr_name + "/" + name + "/mses.png")
        plt.xlabel("Percentile (q)")
        plt.show()
        return prf_results

    def make_plots_from_disk(self):
        fig1, ax1 = plt.subplots(1, 1)
        fig2, ax2 = plt.subplots(1, 1)
        fig3, ax3 = plt.subplots(1, 1)
        fig4, ax4 = plt.subplots(1, 1)
        qs = genfromtxt(self.data_save_dir + "/qs.csv", delimiter=",")
        self.res_df = pd.DataFrame()
        self.res_df["qs"] = qs
        for name in self.names:
            u_errs = genfromtxt(self.data_save_dir + self.distr_name + "/" +
                                name + "/u_errs.csv", delimiter=',')
            u_stds = genfromtxt(self.data_save_dir + self.distr_name + "/" +
                                name + "/u_stds.csv", delimiter=',')
            u_medians = genfromtxt(self.data_save_dir + self.distr_name + "/" +
                                   name + "/u_medians.csv", delimiter=',')
            u_mses = genfromtxt(self.data_save_dir + self.distr_name + "/" +
                                name + "/u_mses.csv", delimiter=',')
            self.res_df[name] = u_errs
            ax1.plot(qs, u_errs, label="Bias for " + name)
            ax2.plot(qs, u_stds, label="Standard deviation for " + name)
            ax3.plot(qs, u_medians, label="DelMedian for " + name)
            ax4.plot(qs, u_mses, label="MSE for " + name)
        make_lines(ax1, ax2, ax3, ax4)
        plt.show()


def make_lines(ax1, ax2, ax3, ax4):
    ax1.axhline(0, color="black")
    ax1.axvline(0.5, color="black")
    ax2.axhline(0, color="black")
    ax2.axvline(0.5, color="black")
    ax3.axhline(0, color="black")
    ax3.axvline(0.5, color="black")
    ax4.axhline(0, color="black")
    ax4.axvline(0.5, color="black")
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
