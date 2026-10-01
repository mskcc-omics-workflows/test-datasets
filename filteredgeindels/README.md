# filteredgeindels test datasets

Synthetic test data for the [`custom/filteredgeindels`](https://github.com/mskcc-omics-workflows/modules) module, which drops read pairs whose CIGAR begins or ends with an unanchored indel (Illumina/manta PR #288 rule: first/last two ops are `ID`, `DI`, `SI` or `SD`).

- `filteredgeindels/edge_indels.bam` (+ `.bai`) — 13 synthetic read pairs plus one supplementary record on a made-up `chr1`; no sample data. 6 pairs carry a flagged CIGAR edge, 7 are controls that must survive (hard-clip edge, lone edge indels, internal deletion, soft clip, plain match, unmapped pair).
- `filteredgeindels/make_edge_indels_bam.py` — deterministic generator. Regenerate with:

      python3 make_edge_indels_bam.py > edge_indels.sam
      samtools sort -o edge_indels.bam edge_indels.sam
      samtools index edge_indels.bam
