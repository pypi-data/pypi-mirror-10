import numpy as np
import pandas as pd
from flask import render_template

from vispr.results.common import AbstractResults

class Results(AbstractResults):
    def __init__(self, dataframe):
        super(Results, self).__init__(dataframe)
        self.df.columns = self.df.columns.str.lower()

    def plot_mapstats(self):
        data = self.df.loc[:, ["label", "reads", "mapped"]]
        data["unmapped_percentage"] = ((self.df["reads"] - self.df["mapped"]) / self.df["reads"]).apply("{:.1%}".format)

        width = 20 * data.shape[0]
        return render_template("plots/mapstats.json",
                               data=data.to_json(orient="records"),
                               width=width)

    def plot_zerocounts(self):
        data = self.df.loc[:, ["label"]]
        data["zerocounts"] = np.log10(self.df["zerocounts"])

        width = 20 * data.shape[0]
        return render_template("plots/zerocounts.json",
                               data=data.to_json(orient="records"),
                               width=width)

    def plot_gini_index(self):
        data = self.df[["label", "giniindex"]]

        width = 20 * data.shape[0]
        return render_template("plots/gini_index.json",
                               data=data.to_json(orient="records"),
                               width=width)
