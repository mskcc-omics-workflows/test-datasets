#!/usr/bin/env python3
"""Write a synthetic SAM exercising the Illumina/manta PR #288 CIGAR-edge rule.

Fully synthetic: random bases on a made-up contig, no sample data.

Regenerate:
    python3 make_edge_indels_bam.py > edge_indels.sam
    samtools sort -o edge_indels.bam edge_indels.sam
    samtools index edge_indels.bam
"""
import random
import re

random.seed(288)

CONTIG = "chr1"
CONTIG_LEN = 100000
QUERY_OPS = set("MIS=X")

# (qname, read-1 CIGAR). Read 2 of every pair is a plain 100M mate.
# flag_*: first/last two CIGAR ops are ID, DI, SI or SD -> whole pair dropped.
# keep_*: must survive.
CASES = [
    ("flag_start_id", "5I3D95M"),
    ("flag_start_di", "3D5I95M"),
    ("flag_end_di", "92M22D8I"),
    ("flag_end_id", "90M5I3D"),
    ("flag_start_si", "5S3I92M"),
    ("flag_end_sd", "95M2D5S"),
    ("keep_hclip_start", "5H3I92M"),
    ("keep_lone_end", "95M5I"),
    ("keep_lone_start", "5I95M"),
    ("keep_internal_del", "50M5D50M"),
    ("keep_softclip", "5S95M"),
    ("keep_plain", "100M"),
]


def query_len(cigar):
    return sum(int(n) for n, op in re.findall(r"(\d+)([MIDNSHP=X])", cigar) if op in QUERY_OPS)


def bases(n):
    return "".join(random.choice("ACGT") for _ in range(n))


def record(qname, flag, rname, pos, mapq, cigar, rnext, pnext, tlen, length):
    return "\t".join(
        str(x) for x in (qname, flag, rname, pos, mapq, cigar, rnext, pnext, tlen, bases(length), "I" * length)
    )


def main():
    print("@HD\tVN:1.6\tSO:unsorted")
    print(f"@SQ\tSN:{CONTIG}\tLN:{CONTIG_LEN}")
    print("@CO\tSynthetic reads for CUSTOM_FILTEREDGEINDELS tests (Illumina/manta PR #288 rule)")
    pos = 1000
    for qname, cigar in CASES:
        mate_pos = pos + 200
        # 99 = paired, proper, mate reverse, first in pair; 147 = paired, proper, reverse, second
        print(record(qname, 99, CONTIG, pos, 60, cigar, "=", mate_pos, 300, query_len(cigar)))
        print(record(qname, 147, CONTIG, mate_pos, 60, "100M", "=", pos, -300, 100))
        if qname == "flag_end_sd":
            # 2113 = paired, first in pair, supplementary. Its own CIGAR is clean;
            # it must be dropped only because its qname is flagged.
            print(record(qname, 2113, CONTIG, 90000, 60, "50M50H", "=", mate_pos, 0, 50))
        pos += 1000
    # Unmapped pair: 77 / 141 = paired, both unmapped, first / second in pair.
    print(record("keep_unmapped", 77, "*", 0, 0, "*", "*", 0, 0, 100))
    print(record("keep_unmapped", 141, "*", 0, 0, "*", "*", 0, 0, 100))


if __name__ == "__main__":
    main()
