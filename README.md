Test datasets for local MSK modules or subworkflows added into modules repo

#### Branches
1. dmp_demux (raw fastq files and metadata from sequencing for demultiplexing used in DMP)
2. argos (test datasets for Argos Pipeline)
3. neoantigen (test datasets for Neoantigen)
4. hg37 (downsized reference files for hg37, and downsized chromosome 22)
5. hla (test datasets for hla)
6. chr22 (downsized chromosome 22)?

#### Rules
1. Master branch should stay empty. Actual test datasets are categories into different branches.
2. Each test file should be LESS than 25 MB based on the requirement of GitHub
3. Each branch contains datasets specifically for a pipeline (e.g. argos), project (e.g. dmp_demux), module/sub-workflow (e.g. neoantigen), or references (e.g. hg37)
4. Each branch contains README file with brief introduction of the test datasets, prefer to have a link with the corresponding workflow repo (if applicable)
5. If a new test dataset does not belong to all existing branches, create a `feature/<test-dataset>` branch based on `master` branch. Once the test dataset is ready to publish, contact our Review Team to do the final review and create new official branch.
