# Python script for capturing flanking sequences around an indicated phophosite in a protein
Input:
Excel sheet with the phosphosites mentioned for every peptide accession number. 
File with all the accession numbers of the protein 

Requirements:
Modules: excelrd, pyfaidx and sys

Output:
File with the list of flanking sequences(+7 and -7 around the phospho site)
For the sequences that have insufficient length, X characters are inserted to make up for the unequal length.

