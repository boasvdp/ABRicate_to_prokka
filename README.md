# Goal

Find Prokka locus tags which correspond to hits found with ABRicate

# Method

User is asked to provide one ABRicate output file and one Prokka output .gff file to match. CONTIG NAMES SHOULD BE THE SAME (meaning prokka should not have renamed contig names using e.g. `--compliant`). Contig names and gene start and end are compared, and locus tags are printed (one per hit).


