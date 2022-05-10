#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# developed by Dr. Brown
# program that accepts a genome or subset of one in an input file
# It looks for a gene start codon then an end codon
# when if finds start then end it prints their location and the gene sequence between them.
# It checks all 3 possible forward reading frames.
"""
@author: minhtran
"""

# Minh Tran   mtran34@masonlive.gmu.edu     2/17/2020
#=========================
# ADD YOUR CODE  HERE

import sys
import os
import Bio.Seq as Seq
 
 
def main():

# started with Johnaton Foox  https://jonfoox.wordpress.com/2014/01/20/python-script-for-amino-acid-translation/
# Protein translator
      
    CodonDict = {'ATT':'I', 'ATC':'I', 'ATA':'I', 'CTT':'L', 'CTC':'L',
    'CTA':'L', 'CTG':'L', 'TTA':'L', 'TTG':'L', 'GTT':'V', 'GTC':'V',
    'GTA':'V', 'GTG':'V', 'TTT':'F', 'TTC':'F', 'ATG':'M', 'TGT':'C',
    'TGC':'C', 'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'GGT':'G',
    'GGC':'G', 'GGA':'G', 'GGG':'G', 'CCT':'P', 'CCC':'P', 'CCA':'P',
    'CCG':'P', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'TCT':'S',
    'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S', 'TAT':'Y',
    'TAC':'Y', 'TGG':'W', 'CAA':'Q', 'CAG':'Q', 'AAT':'N', 'AAC':'N',
    'CAT':'H', 'CAC':'H', 'GAA':'E', 'GAG':'E', 'GAT':'D', 'GAC':'D',
    'AAA':'K', 'AAG':'K', 'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AGA':'R', 'AGG':'R', 'TAA':'X', 'TAG':'X', 'TGA':'X'} #dictionary
    
    protFile = open("/Users/minhe/Documents/wuhansequence.txt").read() #open and read file
      
    print("Original DNA sequence Output;")
    status = yourRoutine(CodonDict, protFile) #using the function
    A_count = protFile.count("A") #counting individual base pairs
    T_count = protFile.count("T")
    C_count = protFile.count("C")
    G_count = protFile.count("G")

    print("A_count is", A_count, "," ,"T_count is", T_count, "," ,"C_count is", C_count, ",","G_count is", G_count,".") #printing individual base pairs
    print("The length of the sequence is:", A_count + T_count + C_count + G_count) #printing length of sequence
    print("\n")

    # print the return status 
    print(status) #print result of function

    
    #Reversed Sequence:
    #print("\n")
    #print("Reversed Sequence Output;")
    #reversed_DNA = protFile[::-1] #reversing sequence
    #status_2 = yourRoutine(CodonDict,reversed_DNA) #using the same function on the reversed seq to get output
    #print(status_2) #printing the result of the function for reversed seq
   
    sys.exit(0)



#========================
def yourRoutine(CodonDict, protFile): #function
   
   AAcountDict: Any = {'I':0, 'L':0, 'V':0, 'F':0, 'M':0, 'C':0,
         'A':0, 'G':0, 'P':0, 'T':0, 'S':0, 'Y':0, 'W':0, 'Q':0,
         'N':0, 'H':0, 'E':0, 'D':0, 'K':0, 'R':0, 'X':0 }
   
   stopCodons= {'TAG':'stop codon', 'TGA':'stop codon', 'TAA':'stop codon'}   #stop codons
    
   status = 'GOOD'
   rowCnt = 0  # there should only be ONE row with the protein bps in your file
   nucleotide_string = ''
   
   

   if protFile == []: #if empty file
       print('empty or bad file name')
       status = 'bad'

   else:
       # read input file first row should be the DNA sequence for your protein

       for rowInfo in protFile: #counting rows
           rowCnt += 1
           nucleotide_string += rowInfo.strip('\n')
           # nucleotide_string += rowInfo
       print("\nrowcnt= " + str(rowCnt))
       #print("The sequence is:",nucleotide_string) #printing the sequence
       print("The length of the sequence is:", len(nucleotide_string)) #printing length of sequence

       lenNS = len(nucleotide_string) #length of sequence
       #print("before AA counts=" +str(AAcountDict))

       startCodonFound = False
       endCodonFound = False
       geneAAseq = ""
          # M = Methionine amino acid
       startLoc = 0
       endLoc = 0

       for position in range(0,lenNS,3): #for every three base pairs = codon
          if position < (lenNS-2):
               threeBasePairs = nucleotide_string[position:position+3]
               threeBasePairs = threeBasePairs.upper() #making seq all uppercase
               
               aaSymbol = CodonDict[threeBasePairs]
               
               
               if aaSymbol == "M": #Finding start codon(M)
                   startCodonFound = True
                   startLoc = position
                   print("*Found start codon for Methionine(ATG) at base pair position:", startLoc)


                   
               elif startCodonFound and (threeBasePairs in stopCodons): #start and stop codon present
                   endLoc = position
                   endCodonFound = True
                   print("  ** Found gene at base pair position "+str(startLoc)+" to "+str(endLoc),":",nucleotide_string[startLoc:endLoc]) #printing base pairs from start loc to end loc
                   print("        -Translated Sequence is:",Seq.translate(nucleotide_string[startLoc:endLoc])) #Using Biopython to translate seq(similar to our codon dict),* means stop codon
                   startLoc = endLoc #starting next codon from end loc
                   # print start end and aa and bp string of gene found
               
               if startCodonFound and not endCodonFound:
                   geneAAseq += aaSymbol
                 
               AAcountDict[aaSymbol] += 1

       print("*** Gene AA sequence is: "+ str(geneAAseq))
              
       print("\nCount of each Amino Acid coded for in the DNA string given is:")
       print(str(AAcountDict)) #returning amount of count of amino acids based on dictionary
       print("\n")

       
       return status #return status to make sure function went through

       


#===================

if __name__ == "__main__": main()