In most cases, we follow the following steps.

Build diploid genome and transcriptome
""""""""""""""""""""""""""""""""""""""
Seqnature incorporates known polymorphisms and short indels from genetically diverse and heterozygous model organisms
into reference genomes, and can construct individualized haploid or diploid transcriptomes suitable for read alignment
by common aligners.

Align reads against diploid transcriptome
"""""""""""""""""""""""""""""""""""""""""
EMASE has been extensively used with the aligner bowtie1. RNA-seq reads need to be aligned simultaneously to a diploid
transcriptome. Use bowtie aligner with the following option::

    bowtie -q -a --best --strata --sam -v 3

Create alignment profile
""""""""""""""""""""""""
Our EM algorithm runs on 3-dimensional incidence matrix of |transcripts|x|haplotypes|x|reads|. Once alignment file in
bam format is available, we need to convert it into the matrix format.

Run EM Algorithm
""""""""""""""""

Here, we list several real application scenarios.


.. image:: https://travis-ci.org/jax-cgd/emase.png?branch=master
        :target: https://travis-ci.org/jax-cgd/emase

