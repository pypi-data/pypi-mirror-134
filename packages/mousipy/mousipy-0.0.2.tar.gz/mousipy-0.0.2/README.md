# mousipy
Translates an AnnData object from scanpy with mouse gene symbols into one with human gene symbols by mapping orthologs from biomart.

# Why?
Many people just uppercase a mouse gene symbol to get the human ortholog. This works in most cases, but fails for some.
For example, there is no Cd8b gene in mice since the correct mouse ortholog to the human gene CD8B is Cd8b1. The gene CD8B is the defining marker for CD8+ T cells
which would get lost by just uppercasing gene symbols but is correctly retained by mapping gene symbols with mousipy.

# Usage example
```
import scvelo as scv
from mousipy import translate
adata = scv.datasets.pancreas()  # mouse scRNA-seq dataset
humanized_adata = translate(adata)
```

# How it works
In mousipy/biomart are lists of mouse (GRCm39) and human (GRCh38.p13) orthologs exported from [biomart](https://www.ensembl.org/biomart/).
First, for all mouse gene symbols in adata.var_names we check if there is an ortholog in the list.
- if there is exactly one human ortholog, the gene symbol is translated directly
- if there is an entry for that gene in the list explicitly mapping it to no ortholog, it will be discarded
- if there are multiple different human orthologs, the gene's expression counts are added to **all** its orthologs
- if the gene is not found in the list, we make it uppercase (and hope that that is the ortholog)
