# Don't change the Libraries
import os
import sys

#Your Code Here
class ORFFinder:
    def __init__ (self,file):
        self.file=file
        pass
# Implement code to read fasta file and return sequences
    def read_fasta_file(file):
        file=open(("SeqRandom.txt"),"r")
        file=file.read()
        file=file.rstrip(">")
        file=file[1:]
        file=[i.split("\n",1) for i in file]
        file=[i[1].replace("\n","") for i in file]
        return file

 # Implement code to find the longest DNA ORF in a given sequence
    
    def find_longest_orf(seq):
        seq=seq.upper()
        start_codon="ATG"
        stop_codons=["TAG","TAA","TGA"]
        orfs=[]
        for i in range(len(seq)):
            if seq[i:i+3]==start_codon:
                for j in range(i+3,len(seq),3):
                    if seq[j:j+3] in stop_codons:
                        orfs.append(seq[i:j+3])
                    break
            if orfs==[]:
                return None
            else:
                return max(orfs,key=len)


