
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/data/gent/vo/001/gvo00125/vsc43619/envs/snakemake_7/lib/python3.12/site-packages', '/user/gent/436/vsc43619/.cache/snakemake/snakemake/source-cache/runtime-cache/tmpw42j8m4k/https/github.com/snakemake/snakemake-wrappers/raw/v1.15.0/bio/kallisto/quant']); import pickle; snakemake = pickle.loads(b'\x80\x04\x95\x17\x0b\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94(\x8c[/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/scratch/cleanup/330_4_1.clean.fastq.gz\x94\x8c[/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/scratch/cleanup/330_4_2.clean.fastq.gz\x94\x8cc/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/assembly/rnaSPAdes/final_metatranscriptome.idx\x94e}\x94(\x8c\x06_names\x94}\x94(\x8c\x05fastq\x94K\x00K\x02\x86\x94\x8c\x05index\x94K\x02N\x86\x94u\x8c\x12_allowed_overrides\x94]\x94(h\x12\x8c\x04sort\x94eh\x12h\x0ch\x16\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x1b)}\x94\x8c\x05_name\x94h\x16sNt\x94bh\x10h\x06\x8c\tNamedlist\x94\x93\x94)\x81\x94(h\nh\x0be}\x94(h\x0e}\x94h\x14]\x94(h\x12h\x16eh\x12h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x12sNt\x94bh\x16h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x16sNt\x94bubub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8cI/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/quantification/330_4\x94a}\x94(h\x0e}\x94h\x14]\x94(h\x12h\x16eh\x12h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x12sNt\x94bh\x16h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x16sNt\x94bub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94}\x94(h\x0e}\x94h\x14]\x94(h\x12h\x16eh\x12h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x12sNt\x94bh\x16h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x16sNt\x94bub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94\x8c\x05330_4\x94a}\x94(h\x0e}\x94\x8c\x06sample\x94K\x00N\x86\x94sh\x14]\x94(h\x12h\x16eh\x12h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x12sNt\x94bh\x16h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x16sNt\x94b\x8c\x06sample\x94hRub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M@/M\x10-M@/M\x10-\x8c\x04/tmp\x94e}\x94(h\x0e}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94uh\x14]\x94(h\x12h\x16eh\x12h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x12sNt\x94bh\x16h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x16sNt\x94bhiK\x01hkK\x01hmM@/hoM\x10-hqM@/hsM\x10-huhfub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8cR/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/logs/quantification/330_4.log\x94a}\x94(h\x0e}\x94h\x14]\x94(h\x12h\x16eh\x12h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x12sNt\x94bh\x16h\x19h\x1b\x85\x94R\x94(h\x1b)}\x94h\x1fh\x16sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x08home_dir\x94\x8c//data/gent/vo/001/gvo00125/vsc43619/diel_cycles\x94\x8c\x07samples\x94\x8cA/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/samples.xlsx\x94\x8c\traw_reads\x94\x8c8/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/raw\x94\x8c\noutput_dir\x94\x8c4/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data\x94\x8c\x0bscratch_dir\x94\x8c</data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/scratch\x94\x8c\x07log_dir\x94\x8c9/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/logs\x94\x8c\x08k_values\x94]\x94(KKKcK\x7fe\x8c\x08adapters\x94\x8cI/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/illumina-adapters.fa\x94\x8c\x12conda_environments\x94\x8c(/data/gent/vo/001/gvo00125/vsc43619/envs\x94\x8c\x0bERCC_folder\x94\x8c;/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/ERCC92\x94\x8c\tspikefile\x94\x8cE/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/ERCC92/ERCC92.fa\x94\x8c\x11scripts_directory\x94\x8c7/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/scripts\x94\x8c\x04pfam\x94\x8c=/data/gent/vo/001/gvo00125/shared/ref_dbs/pfam/Pfam-A.full.gz\x94\x8c\x08pfam_dir\x94\x8c//data/gent/vo/001/gvo00125/shared/ref_dbs/pfam/\x94\x8c\x0eeukprot_ref_fa\x94\x8cL/data/gent/vo/001/gvo00125/shared/ref_dbs/eukprot/eukprot.reference.fasta.gz\x94\x8c\x0feukprot_ref_dir\x94\x8c1/data/gent/vo/001/gvo00125/shared/ref_dbs/eukprot\x94\x8c\x0eeggnog_ref_dir\x94\x8c0/data/gent/vo/001/gvo00125/shared/ref_dbs/eggnog\x94u\x8c\x04rule\x94\x8c\x0ekallisto_quant\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cNhttps://github.com/snakemake/snakemake-wrappers/raw/v1.15.0/bio/kallisto/quant\x94ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = 'https://github.com/snakemake/snakemake-wrappers/raw/v1.15.0/bio/kallisto/quant/wrapper.py';
######## snakemake preamble end #########
"""Snakemake wrapper for Kallisto quant"""

__author__ = "Joël Simoneau"
__copyright__ = "Copyright 2019, Joël Simoneau"
__email__ = "simoneaujoel@gmail.com"
__license__ = "MIT"

from snakemake.shell import shell

# Creating log
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# Placeholder for optional parameters
extra = snakemake.params.get("extra", "")

# Allowing for multiple FASTQ files
fastq = snakemake.input.get("fastq")
assert fastq is not None, "input-> a FASTQ-file is required"
fastq = " ".join(fastq) if isinstance(fastq, list) else fastq

shell(
    "kallisto quant "  # Tool
    "{extra} "  # Optional parameters
    "--threads={snakemake.threads} "  # Number of threads
    "--index={snakemake.input.index} "  # Input file
    "--output-dir={snakemake.output} "  # Output directory
    "{fastq} "  # Input FASTQ files
    "{log}"  # Logging
)
