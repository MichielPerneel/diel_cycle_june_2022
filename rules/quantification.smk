rule kallisto_index:
    input:
        fasta = os.path.join(config['output_dir'], 'assembly', 'rnaSPAdes', 'final_metatranscriptome.fasta'),
    output:
        index = os.path.join(config['output_dir'], 'assembly', 'rnaSPAdes', 'final_metatranscriptome.idx'),
    log: os.path.join(config['log_dir'], 'quantification', 'index.log'),
    threads: 1
    wrapper: 'v1.15.0/bio/kallisto/index'

rule kallisto_quant:
    input:
        fastq = [
            os.path.join(config['scratch_dir'], 'cleanup', '{sample}_1.clean.fastq.gz'),
            os.path.join(config['scratch_dir'], 'cleanup', '{sample}_2.clean.fastq.gz')
        ],
        index = os.path.join(config['output_dir'], 'assembly', 'rnaSPAdes', 'final_metatranscriptome.idx'),
    output: directory(os.path.join(config['output_dir'], 'quantification', '{sample}')),
    log: os.path.join(config['log_dir'], 'quantification', '{sample}.log'),
    threads: 1
    wrapper: 'v1.15.0/bio/kallisto/quant'

rule kallisto_index_ERCC:
    input:
       fasta =  config['spikefile'],
    output:
        index = os.path.join(config['ERCC_folder'], 'ERCC92.idx'),
    threads: 1
    log: os.path.join(config['log_dir'], 'spike_quantification', 'index.log')
    wrapper:
        "v1.15.0/bio/kallisto/index"

rule kallisto_quant_ERCC:
    input:
        fastq = [
            os.path.join(config['scratch_dir'], 'cleanup', 
                        '{sample}_1.rRNA_removed.fastq.gz'),
            os.path.join(config['scratch_dir'], 'cleanup',
                        '{sample}_2.rRNA_removed.fastq.gz')],
        index = os.path.join(config['ERCC_folder'], 'ERCC92.idx'),
    output:
        directory(os.path.join(config['output_dir'],  'ERCC92', 'kallisto', '{sample}')),
    params:
        extra='',
    log:
        os.path.join(config['log_dir'], 'spike_quantification', '{sample}.log'),
    threads: 1
    wrapper:
        "v1.15.0/bio/kallisto/quant"