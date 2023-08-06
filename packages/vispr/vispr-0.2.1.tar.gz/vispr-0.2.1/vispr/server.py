# coding: utf-8
from __future__ import absolute_import, division, print_function

import re, json

import numpy as np
from flask import Flask, render_template, request, session, abort
from jinja2 import Markup

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/")
def index():
    screen = next(iter(app.screens))
    return render_template("index.html", screens=app.screens, screen=screen)


@app.route("/<screen>")
def index_screen(screen):
    try:
        screen = app.screens[screen]
    except KeyError:
        abort(404)
    return render_template("index.html", screens=app.screens, screen=screen)


@app.route("/targets/<screen>/<condition>/<selection>")
def targets(screen, condition, selection):
    screen = app.screens[screen]
    table_args = request.query_string.decode()

    gorilla = screen.species in GORILLA_SPECIES and screen.is_genes
    targets = ""
    background = ""
    if gorilla:
        overlap_args = get_overlap_args()
        targets = screen.targets[condition][selection][:]["target"]
        if overlap_args:
            overlap = app.screens.overlap(*overlap_args)
            filter = targets.apply(lambda target: target in overlap)
            background = targets[~filter]
            targets = targets[filter]
            background = background.to_csv(None, index=False)
        targets = targets.to_csv(None, index=False)

    return render_template(
        "targets.html",
        screens=app.screens,
        selection=selection,
        condition=condition,
        screen=screen,
        control_targets=screen.control_targets,
        hide_control_targets=session.get("hide_control_targets", True),
        table_args=table_args,
        samples=screen.rnas.samples,
        has_rna_info=screen.rnas.info is not None,
        gorilla=gorilla,
        gorilla_targets=targets,
        gorilla_background=background,
        gorilla_mode="hg" if background else "mhg",
        gorilla_species=screen.species)


@app.route("/qc/<screen>")
def qc(screen):
    screen = app.screens[screen]
    return render_template("qc.html",
                           screens=app.screens,
                           screen=screen,
                           fastqc=screen.fastqc is not None,
                           mapstats=screen.mapstats is not None)


@app.route("/compare/<screen>")
def compare(screen):
    screen = app.screens[screen]
    return render_template("compare.html",
                           screens=app.screens,
                           screen=screen)


@app.route("/plt/pvals/<screen>/<condition>/<selection>")
def plt_pvals(screen, condition, selection):
    screen = app.screens[screen]
    plt = screen.targets[condition][selection].plot_pvals(screen.control_targets)
    return plt


@app.route("/plt/pvalhist/<screen>/<condition>/<selection>")
def plt_pval_hist(screen, condition, selection):
    screen = app.screens[screen]
    plt = screen.targets[condition][selection].plot_pval_hist()
    return plt


@app.route("/tbl/targets/<screen>/<condition>/<selection>", methods=["GET"])
def tbl_targets(screen, condition, selection):
    screen = app.screens[screen]
    offset = int(request.args.get("offset", 0))
    perpage = int(request.args.get("perPage", 20))

    # sort and slice records
    records = screen.targets[condition][selection][:]
    total_count = records.shape[0]
    filter_count = total_count

    filter = np.ones(total_count, dtype=np.bool)

    # restrict to overlap
    overlap_args = get_overlap_args()
    if overlap_args:
        overlap = app.screens.overlap(*overlap_args)
        filter &= records["target"].apply(lambda target: target in overlap)

    # searching
    search = get_search()
    if search:
        filter &= records["target"].str.contains(search)

    if session.get("hide_control_targets", True):
        control_targets = screen.control_targets
        filter &= records["target"].apply(
            lambda target: target not in control_targets)

    # filtering
    if not np.all(filter):
        if np.any(filter):
            records = records[filter]
            filter_count = records.shape[0]
        else:
            return render_template("dyntable.json",
                                   records="[]",
                                   filter_count=0,
                                   total_count=total_count)

    # sorting
    columns, ascending = get_sorting()
    if columns:
        records = records.sort(columns, ascending=ascending)
    records = records[offset:offset + perpage]

    # formatting
    def fmt_col(col):
        if col.dtype == np.float64:
            return col.apply("{:.2g}".format)
        return col

    records = records.apply(fmt_col)

    if screen.rnas.info is not None:
        records["locus"] = ["{}:{}-{}".format(*screen.rnas.target_locus(target)) for target in records["target"]]

    return render_template("dyntable.json",
                           records=records.to_json(orient="records",
                                                   double_precision=15),
                           filter_count=filter_count,
                           total_count=total_count)


@app.route("/tbl/pvals_highlight/<screen>/<selection>/<targets>")
def tbl_pvals_highlight(screen, selection, targets):
    screen = app.screens[screen]
    targets = targets.split("|")
    records = get_targets(screen,
                          selection).get_pvals_highlight_targets(targets)
    return records.to_json(orient="records")


@app.route("/tbl/rnas/<screen>/<target>")
def tbl_rnas(screen, target):
    screen = app.screens[screen]
    table = screen.rnas.by_target(target)
    return table.to_json(orient="records")


@app.route("/igv/session/<screen>.xml")
def igv_session(screen):
    screen = app.screens[screen]
    return render_template("igv/session.xml", screen=screen)


@app.route("/igv/track/rnas/<screen>.gct")
def igv_track_rnas(screen):
    screen = app.screens[screen]
    return screen.rnas.track()


@app.route("/plt/normalization/<screen>")
def plt_normalization(screen):
    screen = app.screens[screen]
    plt = screen.rnas.plot_normalization()
    return plt


@app.route("/plt/pca/<screen>/<int:x>/<int:y>/<int:legend>")
def plt_pca(screen, x, y, legend):
    screen = app.screens[screen]
    plt = screen.rnas.plot_pca(comp_x=x, comp_y=y, legend=legend == 1, )
    return plt


@app.route("/plt/correlation/<screen>")
def plt_correlation(screen):
    screen = app.screens[screen]
    plt = screen.rnas.plot_correlation()
    return plt


@app.route("/plt/gc_content/<screen>")
def plt_gc_content(screen):
    screen = app.screens[screen]
    plt = screen.fastqc.plot_gc_content()
    return plt


@app.route("/plt/base_quality/<screen>")
def plt_base_quality(screen):
    screen = app.screens[screen]
    plt = screen.fastqc.plot_base_quality()
    return plt


@app.route("/plt/seq_quality/<screen>")
def plt_seq_quality(screen):
    screen = app.screens[screen]
    plt = screen.fastqc.plot_seq_quality()
    return plt


@app.route("/plt/mapstats/<screen>")
def plt_mapstats(screen):
    screen = app.screens[screen]
    plt = screen.mapstats.plot_mapstats()
    return plt


@app.route("/plt/zerocounts/<screen>")
def plt_zerocounts(screen):
    screen = app.screens[screen]
    plt = screen.mapstats.plot_zerocounts()
    return plt


@app.route("/plt/readcount_cdf/<screen>")
def plt_readcounts(screen):
    screen = app.screens[screen]
    plt = screen.rnas.plot_readcount_cdf()
    return plt

@app.route("/plt/overlap_chord")
def plt_overlap_chord():
    return app.screens.plot_overlap_chord(*get_overlap_args())


@app.route("/plt/overlap_venn")
def plt_overlap_venn():
    return app.screens.plot_overlap_venn(*get_overlap_args())


@app.route("/set/hide_control_targets/<int:value>")
def set_hide_control_targets(value):
    session["hide_control_targets"] = value == 1
    return ""


def get_overlap_args():
    if "fdr" not in request.values and "overlap-items" not in request.form:
        return None

    fdr = float(request.values.get("fdr", 0.25))
    items = list(map(lambda item: item.split("|"), request.values.getlist("overlap-items")))
    return fdr, items


def get_sorting(pattern=re.compile("sorts\[(?P<col>.+)\]")):
    cols, ascending = [], []
    for arg, val in request.args.items():
        m = pattern.match(arg)
        if m:
            cols.append(m.group("col"))
            ascending.append(int(val) == 1)
    return cols, ascending


def get_search(pattern=re.compile("search\[(?P<target>.+)\]")):
    return request.args.get("queries[search]", None)


def get_targets(screen, selection):
    return screen.targets(selection == "positive")


GORILLA_SPECIES = ("HOMO_SAPIENS ARABIDOPSIS_THALIANA SACCHAROMYCES_CEREVISIAE "
                   "CAENORHABDITIS_ELEGANS DROSOPHILA_MELANOGASTER DANIO_RERIO "
                   "MUS_MUSCULUS RATTUS_NORVEGICUS".split())
