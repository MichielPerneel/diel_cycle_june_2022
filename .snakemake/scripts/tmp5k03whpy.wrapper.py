
######## snakemake preamble start (automatically inserted, do not edit) ########
import sys; sys.path.extend(['/data/gent/vo/001/gvo00125/vsc43619/envs/snakemake_7/lib/python3.12/site-packages', '/user/gent/436/vsc43619/.cache/snakemake/snakemake/source-cache/runtime-cache/tmp_ob76_h9/https/github.com/snakemake/snakemake-wrappers/raw/0.27.1/bio/fastqc']); import pickle; snakemake = pickle.loads(b'\x80\x04\x95y\n\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94\x8cI/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/raw/330_6_2.fastq.gz\x94a}\x94(\x8c\x06_names\x94}\x94\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x10\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h\x16)}\x94\x8c\x05_name\x94h\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94(\x8c_/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/quality_control/fastqc/330_6_2_fastqc.html\x94\x8c^/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/quality_control/fastqc/330_6_2_fastqc.zip\x94e}\x94(h\x0c}\x94(\x8c\x04html\x94K\x00N\x86\x94\x8c\x03zip\x94K\x01N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bh(h$h*h%ub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94(\x8c\x05330_6\x94\x8c\x012\x94e}\x94(h\x0c}\x94(\x8c\x06sample\x94K\x00N\x86\x94\x8c\x03num\x94K\x01N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94b\x8c\x06sample\x94hH\x8c\x03num\x94hIub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01M$\x0cM\x95\x0bM$\x0cM\x95\x0b\x8c\x04/tmp\x94e}\x94(h\x0c}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06mem_mb\x94K\x02N\x86\x94\x8c\x07mem_mib\x94K\x03N\x86\x94\x8c\x07disk_mb\x94K\x04N\x86\x94\x8c\x08disk_mib\x94K\x05N\x86\x94\x8c\x06tmpdir\x94K\x06N\x86\x94uh\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bhcK\x01heK\x01hgM$\x0chiM\x95\x0bhkM$\x0chmM\x95\x0bhoh`ub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94\x8cL/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/logs/fastqc/330_6_2.log\x94a}\x94(h\x0c}\x94h\x0e]\x94(h\x10h\x11eh\x10h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x10sNt\x94bh\x11h\x14h\x16\x85\x94R\x94(h\x16)}\x94h\x1ah\x11sNt\x94bub\x8c\x06config\x94}\x94(\x8c\x08home_dir\x94\x8c//data/gent/vo/001/gvo00125/vsc43619/diel_cycles\x94\x8c\x07samples\x94\x8cA/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/samples.xlsx\x94\x8c\traw_reads\x94\x8c8/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/raw\x94\x8c\noutput_dir\x94\x8c4/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data\x94\x8c\x0bscratch_dir\x94\x8c</data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/scratch\x94\x8c\x07log_dir\x94\x8c9/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/logs\x94\x8c\x08k_values\x94]\x94(KKKcK\x7fe\x8c\x08adapters\x94\x8cI/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/illumina-adapters.fa\x94\x8c\x12conda_environments\x94\x8c(/data/gent/vo/001/gvo00125/vsc43619/envs\x94\x8c\x0bERCC_folder\x94\x8c;/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/ERCC92\x94\x8c\tspikefile\x94\x8cE/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/data/ERCC92/ERCC92.fa\x94\x8c\x11scripts_directory\x94\x8c7/data/gent/vo/001/gvo00125/vsc43619/diel_cycles/scripts\x94\x8c\x04pfam\x94\x8c=/data/gent/vo/001/gvo00125/shared/ref_dbs/pfam/Pfam-A.full.gz\x94\x8c\x08pfam_dir\x94\x8c//data/gent/vo/001/gvo00125/shared/ref_dbs/pfam/\x94\x8c\x0eeukprot_ref_fa\x94\x8cL/data/gent/vo/001/gvo00125/shared/ref_dbs/eukprot/eukprot.reference.fasta.gz\x94\x8c\x0feukprot_ref_dir\x94\x8c1/data/gent/vo/001/gvo00125/shared/ref_dbs/eukprot\x94\x8c\x0eeggnog_ref_dir\x94\x8c0/data/gent/vo/001/gvo00125/shared/ref_dbs/eggnog\x94u\x8c\x04rule\x94\x8c\x06fastqc\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cEhttps://github.com/snakemake/snakemake-wrappers/raw/0.27.1/bio/fastqc\x94ub.'); from snakemake.logging import logger; logger.printshellcmds = False; __real_file__ = __file__; __file__ = 'https://github.com/snakemake/snakemake-wrappers/raw/0.27.1/bio/fastqc/wrapper.py';
######## snakemake preamble end #########
"""Snakemake wrapper for fastqc."""

__author__ = "Julian de Ruiter"
__copyright__ = "Copyright 2017, Julian de Ruiter"
__email__ = "julianderuiter@gmail.com"
__license__ = "MIT"


from os import path
from tempfile import TemporaryDirectory

from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=False, stderr=True)

def basename_without_ext(file_path):
    """Returns basename of file path, without the file extension."""

    base = path.basename(file_path)

    split_ind = 2 if base.endswith(".gz") else 1
    base = ".".join(base.split(".")[:-split_ind])

    return base


# Run fastqc, since there can be race conditions if multiple jobs 
# use the same fastqc dir, we create a temp dir.
with TemporaryDirectory() as tempdir:
    shell("fastqc {snakemake.params} --quiet "
          "--outdir {tempdir} {snakemake.input[0]}"
          " {log}")

    # Move outputs into proper position.
    output_base = basename_without_ext(snakemake.input[0])
    html_path = path.join(tempdir, output_base + "_fastqc.html")
    zip_path = path.join(tempdir, output_base + "_fastqc.zip")

    if snakemake.output.html != html_path:
        shell("mv {html_path} {snakemake.output.html}")

    if snakemake.output.zip != zip_path:
        shell("mv {zip_path} {snakemake.output.zip}")
