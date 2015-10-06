# [Genomic Data Science Specialization (Johns Hopkins University and Coursera)] (https://www.coursera.org/specialization/genomics/41)


### Incentives & Benefits
High-throughput experimental techniques have enabled the Data Science revolution in modern biology. People with skills in biology, computations and statistics are fundamental to this change. This Specialization will help you be a part of the new wave of Big Data Science in Genomics. These skills are in high demand across modern biology, from bench scientists in industry and academia to data scientists working with healthcare analytics.

### Courses
This specialization will teach you to understand, analyze, and interpret data from next-generation sequencing experiments. You will learn common tools of genomic data science, including Python, R, Bioconductor, and Galaxy. These courses can serve as a stand-alone introduction to genomic data science or can compliment to a primary degree or postdoc in biology, molecular biology, or genetics. The Specialization concludes with a Capstone project that allows you to apply the skills you've learned throughout the courses.

### Projects

#### Project1 -- Concepts of Genomic Data Science

In this project you will be reading a genomic data science paper and answering some questions to help you learn about how the different fields in genomic data science work together and to evaluate your understanding of some of the concepts we have learned throughout the course. The paper we are reading is called: “Microbial Genes in the Human Genome: Lateral Transfer or Gene Loss?” You can access the paper from the Science Magazine site here: http://www.sciencemag.org/content/292/5523/1903.full.

[Project Solution](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course1_Introduction%20to%20Genomic%20Technologies/Course%20Project_test2.pdf)

#### Project2 -- Identify DNA Polymorphic Sites with Galaxy

[Published Page]( https://usegalaxy.org/u/coursera/p/genomic-data-science-with-galaxyidentify-polymorphic-sites)

This page includes description about analyses of DNA polymorphic sites of father-mother-child sequencing samples:

step 1: load data - the data are loaded from local files, set "fastqsanger" format and "hg19" database on the starting page

step 2: check quality of all sequencing files - use FastQC tool (version: 0.63) to check quality of the sequencing

step 3: mapping - use BWA-MEM tool (version: 0.1) to map sequence to reference genome (choose hg19 as reference), paired end

step 4: add or replace read groups - label each group (the mapping file) using AddOrReplaceReadGroup (version: 1.126.0)

step 5: merge 3 individual mapping files - use MergeSamFiles (version: 1.126.0)

step 6: filter - using filter tools: Filter (version: 1.126.0, remove low quality mapping), MarkDuplicates (version: 1.126.0, filter out duplicated mapping), CleanSam (version: 1.126.0)

step 7: identify polymorphic sites - using FreeBayes tool (version: 0.4) to identify polymorphic sites base on hg19 genome

step 8: filter out false positive sites - using VCFfilter (version: 0.0.3) to select sites where the chance of a false positive call is 1 in 10,000 or better.

step 9: extract workflow and download final vcf file for further analyses.

Stage 2 - analyze data of polymorphic sites based on vcf file

step 10: load data - set format as "vcf", genomic database as hg19

step 11: identify number of snp, mnp, del, ins or complex - using VCFfilter tool (version:0.0.3 ) to select different types of polymorphism (for example: -f "TYPE = snp", select snp only), then using Filter tool (version: 1.1.0) to find duplicated polymorphisms

step 12: identify genes with polymorphic sites - using ANNOVAR Annotate VCF tool (version: 0.1) to annotate the  vcf file in step 10

step 13: count polymorphic sites for each gene - using Group tool (version: 2.1.0, by gene name) to count number of polymorphic sites for each gene

step 14: sort results in step 13 using Sort tool (version: 1.0.3, by descending).

[WorkFlow](https://usegalaxy.org/workflow/display_by_username_and_slug?username=coursera&slug=workflow-constructed-from-history-genomic-data-science-with-galaxy-project---completed)

[History for Analyses](https://usegalaxy.org/u/coursera/h/workflow-constructed-from-history-genomic-data-science-with-galaxy-project---completed)

#### Project3 - Develop Python Bioinformatics Tools to Analyze DNA Sequence 

In this project, a python program that takes as input a file containing DNA sequences in multi-FASTA format was developed. The program includes a set of tools for dna sequence analyses (a. check records in file (count_records), b. compute the length of each DNA sequence (check_length), c. identify open read frame in each DNA sequence (orf_identifier), d. identify repeated motif in sequence (repeats_identifier)). To use the tool  sets, please assign the path and file name to the class function. For example: dna_tools = dna_tool_sets ("../data/dna.example.fasta"). Then, call the functions in the class, e.g call function to check length of dna sequence: length = dna_tools.check_length()

[Python code](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course3_Python%20for%20Genomic%20Data%20Science/Python%20Project/script/dna_tools.py)

[Project solution] (https://github.com/lanttern/Genomic-Data-Science/blob/master/Course3_Python%20for%20Genomic%20Data%20Science/Python%20Project/final_project_results.pdf)

#### Project4 - Develop Pipeline for Next Generation Sequencing: Analyze DNA Alignment, DNA Assembly, Genetic Variants and RNA Sequencing in Linux

##### Project_A (Exam1)

Assume you sequenced and assembled the genome of Malus domestica (apple), and performed gene annotation. You then collected samples and ran RNA-seq experiments to determine sets of genes that are expressed in the various tissues. This information was stored, respectively, in the following files: “apple.genome”, “apple.genes”, “apple.condition{A,B,C}”.

NOTE: The apple genome and the apple gene annotations for this project were extracted from the Rosaceae Genome Database (RGD). Actual data have then been modified, and hence may not directly reflect the information in the original RGD records. Answer each question separately. Where multiple values are required, separate them by ‘,’ only, with no spaces. Do not use ‘,’ within numbers.

[Project_A Code](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam1/project_exam1.pdf)

[Project_A Solution](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam1/Exam1.pdf)

##### Project_B (Exam2)

As part of a larger project cataloging genetic variation in the plant Arabidopsis thaliana, you sequenced and assembled the genome of one strain (‘wu_0_A’), then mapped back the reads to the assembled genome. The resulting BAM file is included in the package ‘gencommand_proj2_data.tar.gz’. Using SAMtools and BEDtools as well as other Unix commands introduced in this course, examine the files and answer the following questions.

NOTE: Input data have been obtained and modified from those generated by the 1001 Genomes Project, accession ‘Wu_0_A’.

[Project_B Code](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam2/project_exam2.pdf)

[Project_B Solution](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam2/Exam2.pdf)

##### Project_C (Exam3)

As part of the effort to catalog genetic variation in the plant Arabidopsis thaliana, you resequenced the genome of one strain (‘wu_0_A’; genome file: ‘wu_0.v7.fas’), to determine genetic variants in this organism. The sequencing reads produced are in the file ‘wu_0_A_wgs.fastq’. Using the tools bowtie2, samtools and bcftools, develop a pipeline for variant calling in this genome. 

NOTE: Genome and re-sequencing data have been obtained and modified from those generated by the 1001 Genomes Project, accession ‘Wu_0_A’.

[Project_C Code](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam3/project_exam3.pdf)

[Project_C Solution](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam3/Exam3.pdf)

##### Project_D (Exam4)

You are performing an RNA-seq experiment to determine genes that are differentially expressed at different stages in the development of Arabidopsis thaliana shoot apical meristem. You collected samples at day 8 and day 16 (files “Day8.fastq” and “Day16.fastq”), extracted and sequenced the cellular mRNA, and are now set to perform the bioinformatics analysis. The reference genome you will need for the analysis is “athal_chr.fa” and the reference gene annotations are in “athal_genes.gtf”. Use default parameters unless otherwise specified. Sample command files that you can modify to create your own pipeline are provided in the file “commands.tar.gz”. All files are provided in the archive gencommand_proj4.tar.gz.

NOTE: The genome and annotation data were obtained and modified from the Arabidopsis Information Resources (TAIR) Database, and the RNA-seq reads were extracted from GenBank’s Short Read Archive (SRA).

[Project_D Code](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam4/project_exam4.pdf)

[Project_D Solution](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam4/Exam4.pdf)

[Commands](https://github.com/lanttern/Genomic-Data-Science/blob/master/Course4_Command%20Line%20Tools%20for%20Genomic%20Data%20Science/Project_Exam4/commands.pdf)
