---
title: Sequencing
tags:
  - Python
  - R
  - HPC
  - Nextflow
  - Docker
---
# RNA Sequencing

**RNA sequencing pipeline for processing large volumes of biological data, developed by Jack Gisby.**

## About

This repository is part of the REsearch COmputing and Data science Exemplars (ReCoDE) project. ReCoDE exemplars are annotated high-quality research software projects that aim to support teaching and learning in research computing and data science. Courses on these topics usually focus on a single topic at a time, so ReCoDE exemplars help students understand how this knowledge can be integrated into a functional project.

This exemplar involves the development of a pipeline for processing large volumes of biological data. The development of next generation sequencing technologies has facilitated a systems-level approach to biological and biomedical research. In particular, RNA sequencing (RNA-seq) has become a ubiquitous method for gene expression profiling. However, the colossal datasets produced by this method pose a new challenge for life science researchers, who commonly have little statistical or computational training. The processing of sequencing data commonly requires the development of custom workflows that can run in parallel on university computing clusters. Furthermore, the quality control and statistical analysis of these data requires specialist knowledge and purpose-built software packages.

This project demonstrates the development of a pipeline for processing RNA-seq datasets on the computing clusters, such as the Imperial College Research Computing Service (RCS), and basic statistical analysis of the normalised data. This will involve:

- Quality control and trimming of raw RNA-seq reads
- Alignment of reads to the human reference genome
- Conversion of aligned reads to a matrix of gene counts
- Downstream statistical analysis:
- Data normalisation
- Unsupervised analysis (e.g. PCA)
- Differential expression and enrichment using edgeR

We will write scripts, using bash and the R programming language, that can execute these steps in parallel on computing clusters Developed by Jack Gisby.

## Link to material

Start working through the material using the online [Documentation](https://imperialcollegelondon.github.io/ReCoDE_rnaseq_pipeline/).
The full source code for this project is on [GitHub](https://github.com/ImperialCollegeLondon/ReCoDE_rnaseq_pipeline).
