========================
README for SMART (1.4.2)
========================
Time-stamp: <2015-05-17 11:28:37 Hongbo Liu>

Introduction
============

It is known that DNA methylation plays important roles in regulation
of cell development and differentiation. DNA methylation/unmethylation
mechanisms are common in all tissue/cell. However, different cell 
types with the same genome have different methylomes. Recently,
high-throughput sequencing combining bisulfite treatment (Bisulfite
-Seq) have been used to generate DNA methylomes from a wide range of
human tissue/cell types at a genome-wide perspective. To characterize
the genome regions that consist of continuous CpGs with similar 
methylation specificity, we developed the Specific Methylation Analysis
and Report Tool (SMART) based on the quantified methylation specificity,
Euclidean distance and similarity entropy, for identifying and 
characterizing sets of genome segments comprising continuous CpGs with 
similar methylation specificities. For a given set of multiple methylomes 
profiled using BS-Seq, entropy-based procedures facilitated the quantification 
of methylation specificity for each CpG and the determination of the 
Euclidean distance and similar entropy for each pair of neighboring CpGs. 
Subsequently, continuous scanning based on these quantified parameters 
segments the genome into primary segments comprising CpG sites with high 
methylation similarities across all cell types. Further, the 
primary segments in close proximity and sharing similar methylation 
patterns were merged into larger segments of different types, including 
high specificity (HighSpe), low specificity (LowSpe) and almost no 
cell-specificity (NoSpe) segments. Eventually, the High/LowSpe segments 
with specific hypo-/hypermethylation in the minority of cell types, 
cell-type-specific hypomethylation marks (HypoMarks) and cell-type-specific 
hypermethylation marks (HyperMarks), were identified using a statistical 
method. To facilitate the mining of methylation marks (MethyMarks) across 
cell types and species, all algorithms used in this procedure were 
integrated into a Specific Methylation Analysis and Report Tool (SMART), 
which is also available at http://fame.edbc.org/smart.

Install
=======

Please check the file 'INSTALL' in the distribution.

Usage of SMART
==============

:usage: SMART MethyDir CytosineDir [-h] [-n PROJECTNAME] [-o OUTPUTFOLDER] [-v]  



positional arguments
-----------------------
MethyDir
```````````````
The directory (such as /liuhb/BSSeq/) of the folder including methylation data files formated in wig.gz (such as H1.wig.gz). REQUIRED.

CytosineDir
``````````````````
The directory (such as /liuhb/CLoc_hg19/) of the folder including cytosine location files for all chromesomes formated in txt.gz (such as chr1.txt.gz). REQUIRED.

optional arguments
----------------------
-h, --help
``````````````````
show this help message and exit

-n PROJECTNAME
`````````````````````````````
Project name, which will be used to generate output file names. DEFAULT: "SMART"

-o OUTPUTFOLDER
````````````````````````````````
If specified all output files will be written to that directory. Default: the directory named using projectname and currenttime (such as SMART20140801132559) in the current working directory.

-v, --version
```````````````````
show program's version number and exit

Example
==============

Example data
---------------

The example data can be found in the directory Example under the installation directory of SMART. It should be noted that the location of installation directory of SMART may be different in different Operating System. The Cytosines and their methylation level in 50kb regions from chr3 and chr6 were extracted for test of SMART. User can use following command to test SMART.

Example command
---------------------
:For Linux: 

The main function SMART may be in /usr/local/bin/, and example data may be in ../python2.7/dist-packages/SMART/Example. The following referece may be useful for test of SMART::

  SMART /usr/local/lib/python2.7/dist-packages/SMART/Example/BSSeq_fortest/ /usr/local/lib/python2.7/dist-packages/SMART/Example/CLoc_hg19_fortest/ -n Test -o /usr/local/lib/python2.7/dist-packages/SMART/Example/Example_Results/



:For windows: 

The main function SMART may be in ..\\Python27\\Scripts\\, and example data may be in ..\\Python27\\Lib\\site-packages\\SMART\\Example. The following referece may be useful for test of SMART::

  cd  ..\Python27\Scripts\
  python SMART ..\Python27\Lib\site-packages\SMART\Example\BSSeq_fortest\ ..\Python27\Lib\site-packages\SMART\Example\CLoc_hg19_fortest\ -n Test -o ..\Python27\Lib\site-packages\SMART\Example\Example_Results\


Output Files 
==============
1. Folder SplitedMethy is a a output directory to store the splited Methylation data.
   The methylation data are stored in different chromosome sub-folders. In each
   sub-folder, the methylation data for all samples are included. 
2. Folder MethylationSpecificity is a output directory to store the methylation
   levels and specifity for each C which is common across all samples. These files are
   stored in chromosomes. In this folder, MethylationSpecificity.wig.gz includes
   the methylation specifity of all common C. And this file can be uploaded to UCSC
   browser for visualization.
3. Folder MethylationSegment includes three sub-folders: GenomeSegment, GenomeSegmentMethy,
   and MergedGenomeSegment. The sub-folder GenomeSegment stores all small segments
   identified by SMART in each chromosome. And the sub-folder GenomeSegmentMethy stores
   the methylation levels of each small segments across all samples which may be useful for
   users' local further analysis. The sub-folder MergedGenomeSegment stores the larger 
   segments merged based on the small segments in each chromosome. The final results are
   generated based on these merged segments.
4. Folder FinalResults includes all intresting results which may be concerned by users.
   In this folder, there are six files. 

   -The first file 1SmallSegmentBed.txt.gz stores all small segments in bed format,  which  can be uploaded to UCSC browser for visualization.

   -The second file 2MergedSegmentBed.txt.gz stores all merged segments in bed format, which  can be uploaded to UCSC browser for visualization.

   -The third file 3MergedSegment.txt stores all merged segments in txt format, which is useful  for local further analysis.

   -The fourth file 4MergedSegmentwithmethylation.txt stores the methylation levels of all  merged segments across all samples, which is useful for local further analysis.

   -The fifth file 5MergedHighLowSpeSegmentwithspecificity.txt stores the methylation specificity and p values of t-test for each merged HighSpe/LowSpe segement, which is useful for further analysis on cell-type-specificity for each HighSpe/LowSpe segement. The positive p value represents the segment is hyper-methylated in the corresbonding cell-type, while the negative p value represents the segment is hypo-methylated in the corresbonding cell-type.

   -The sixth file 6CellTypeSpecificMethymarkPvalue.txt is a reformated file for the fifth file. In this file, only the HighSpe/LowSpe segements which show significant hypo- or hyper-methylation in some cell-types are remained. This file is usefull for users to select and analyze cell-type-specific methylation marks including HypoMarks and HyperMarks.

Other useful links
==================
:Predefined C locations in various species and other resources: http://fame.edbc.org/smart/
:QDMR: http://bioinfo.hrbmu.edu.cn/qdmr/
:UCSC Genome browser:  http://genome.ucsc.edu/

Contact 
==================
:For any help:  you are welcome to write to Hongbo Liu (hongbo919@gmail.com).