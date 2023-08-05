============
**metameta**
============

*Purpose*
-----------
metameta is a toolset for analyzing metatranscriptome data that has been mapped to metagenomic data.

*Requirements*
------------------
- Python 3.4 or higher
- pysam 0.8.2.1 or higher

*Installation*
---------------
''pip install metameta''

*Usage*
----------
metameta <tool name> [arguments for tool]

"metameta" without arguments will give help on the metameta package.
"metameta <tool>" without any arguments will give the help for that tool.

*Tools*
--------
generate_fastr.py [--log_file] [--verbose] [--version] [--verify] <fastaq> <bsam> <fastr>

filter_fastr.py [--log_file] [--verbose] [--version] [--verify] [--min_length] [--max_length] <fastr>

annotate_clusters.py [--log_file] [--verbose] [--version] [--verify] <stats> <gff>

annotate_clusters.py [--log_file] [--verbose] [--version] [--verify] <table> <gff> <[ann]>


