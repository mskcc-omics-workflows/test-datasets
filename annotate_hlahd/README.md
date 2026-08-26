# annotate_hlahd Test Datasets

Small synthetic test data for the [`annotate_hlahd` module](https://github.com/mskcc-omics-workflows/modules) —
not derived from any real sample.

- `test_sample_final.result.txt` — synthetic HLA-HD class I primary result (same shape as `<sample>_final.result.txt`)
- `test_sample_{A,B,C}.est.txt` — synthetic per-locus HLA-HD estimation detail files
- `hla_nom_p_demo.txt` — subset of the IMGT `wmda/hla_nom_p.txt` P-group reference table covering the alleles above

These mirror the demo fixtures shipped in [mskcc/HLA_HD_workflow](https://github.com/mskcc/HLA_HD_workflow)'s `demo/` directory.
