from optparse import OptionParser
import json
import numpy as np
import pandas as pd
from anndata import AnnData
from rpy2.robjects import r, pandas2ri
from rpy2.robjects.conversion import localconverter
import rpy2.robjects as ro
import sys

def normalize_Dino(adata):
    df_counts = pd.DataFrame(
        data=adata.X.todense(),
        index=adata.obs.index,
        columns=adata.var.index
    )
    df_counts = df_counts.transpose()

    # TODO REMOVE!!!!!
    #df_counts = df_counts.loc[['RPS10', 'ILF2', 'CALML5', 'PECAM1']]
    df_counts = df_counts.iloc[:400]
    #df_counts.to_csv('test.tsv', sep='\t')
    print(df_counts)

    print("Converting Python object to rpy2 object...")
    with localconverter(ro.default_converter + pandas2ri.converter):
        r_counts = ro.conversion.py2rpy(df_counts)
    print("Done.")
    rstring="""
        function(raw_mat) {
            library(Dino)
            print(raw_mat)
            norm_mat <- Dino(as.matrix(raw_mat))
            norm_mat <- as.dataframe(norm_mat)
            norm_mat
        }
    """
    r_func = ro.r(rstring)
    r_res = r_func(r_counts)
    with localconverter(ro.default_converter + pandas2ri.converter):
        df_norm = ro.conversion.rpy2py(r_norm)
    adata_norm = AnnData(df_norm.transpose())
    return adata_norm

