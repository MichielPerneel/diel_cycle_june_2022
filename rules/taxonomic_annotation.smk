rule create_eukprot_db:
    """
    This rule turns the EukProt sequences into a mmseqs DB
    """
    input: config['eukprot_ref_fa']
    output: os.path.join(config['eukprot_ref_dir'], 'eukprot')
    shell:'''
    unset OMP_PROC_BIND

    module load MMseqs2

    mmseqs createdb {input} {output}
    '''

rule create_metatranscriptome_db:
    """
    This rule turns the metatranscriptome sequences into a mmseqs DB
    """
    input: os.path.join(config['output_dir'], 'assembly', 'protein', 'metatranscriptome.pep')
    output: os.path.join(config['output_dir'], 'assembly', 'protein', 'metatranscriptome_mmseqsDB')
    shell:'''
    unset OMP_PROC_BIND

    module load MMseqs2

    mmseqs createdb {input} {output}
    '''

rule eukprot_annotation:
    input:
        metatranscriptome_mmseqsDB=os.path.join(config['output_dir'], 'assembly', 'protein', 'metatranscriptome_mmseqsDB'),
        eukprot_mmseqsDB=os.path.join(config['eukprot_ref_dir'], 'eukprot'),
    output:
        os.path.join(config['output_dir'], 'annotation', 'taxonomy_eukprot', 'eukprot_annotation.m8')
    params:
        eukprot_out_dir=os.path.join(config['output_dir'], 'annotation', 'taxonomy_eukprot'),
        tmp=config['scratch_dir']
    threads: 60
    resources:
        mem_mb=250000
    shell:'''
    unset OMP_PROC_BIND

    module load MMseqs2

    # Query assembly against reference
    mmseqs search {input.metatranscriptome_mmseqsDB} {input.eukprot_mmseqsDB} {params.eukprot_out_dir}/resultDB {params.tmp} -s 6

    # Extract first hit
    mmseqs filterdb {params.eukprot_out_dir}/resultDB {params.eukprot_out_dir}/resultDB.firsthit --extract-lines 1
    mmseqs convertalis {input.metatranscriptome_mmseqsDB} {input.eukprot_mmseqsDB} {params.eukprot_out_dir}/resultDB.firsthit {output}
    '''