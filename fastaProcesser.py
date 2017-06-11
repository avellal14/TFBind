#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:43:15 2017

@author: avellal14
"""

import fileinput
def makeSmallFASTA(filename):
    ogFastaFile = open(filename,'r')
    newFastaFile = open('/home/avellal14/GenData/segment1.fa', 'w')
    
    fastaSegment = ogFastaFile.read(50000)
    fastaSegment.replace("N","")
    
    #remove all Ns
  
    newFastaFile.write(fastaSegment)
    ogFastaFile.close()
    newFastaFile.close()



def splitFASTA(filename):
    ogFastaFile = open(filename, 'r')
    ogFasta = ogFastaFile.read(500000)
    ogFastaFile.close()
    
    print("DONE READING FILE")
    newFasta = ogFasta.replace('N','') #remove all Ns
    newFasta = newFasta.replace('\n','')
    newFasta = newFasta.replace('<','')
    newFasta = newFasta.replace('>','')
    newFasta = newFasta.replace('A>','')  
    newFasta = newFasta.replace('0','')    
    newFasta = newFasta.replace('I','')
    newFasta = newFasta.replace('S','')      
    newFasta = newFasta.replace('M','')
    newFasta = newFasta.replace('E','')  
    newFasta = newFasta.replace(':','')
    
    
    newFastaFile = open('/home/avellal14/GenData/processedSeq.fa', 'w')
    newFastaFile.write(newFasta)
    newFastaFile.close()
    
    
    newFastaFile = open('/home/avellal14/GenData/processedSeq2.fa', 'w')
    newFastaFile.write(newFasta)
    #remove all whitespace
    for line in fileinput.FileInput('/home/avellal14/GenData/processedSeq.fa',inplace=1):
        if line.rstrip():
            newFastaFile.write(line)
    newFastaFile.close()
    
    
    processedFastaFile = open('/home/avellal14/GenData/processedSeq2.fa', 'r')
    processedFasta = processedFastaFile.read()
    processedFastaFile.close()
    
    i = 3
    fileIndex = 0
    fileDir = '/home/avellal14/GenData/memeInputs/chip_seq/tfbs_chip_' + str(fileIndex) + '.fastq' 
    
  #  indexOne = 0
  #  indexTwo = 0
                                                                            
  # while(True):
  #      try:
   #         print("we good rn")
    #        indexOne = processedFasta.index('<',indexOne+1)
     #       indexTwo = processedFasta.index('>',indexTwo+1)
      #      fastaSegment = processedFasta[:indexOne] + processedFasta[indexTwo+1:]
      #  except ValueError:
     #       print("done with loop")
     #       break                                                                              
                                                                       
    while i < len(processedFasta):
        currentSegment = open(fileDir, 'w')
        currentSegment.write('>ch22')
        fastaSegment = processedFasta[i:i+30000]
        currentSegment.write(fastaSegment)
        currentSegment.close()
        i = i + 30000
        fileIndex = fileIndex + 1
        fileDir = '/home/avellal14/GenData/memeInputs/chip_seq/tfbs_chip_' + str(fileIndex) + '.fastq' 

splitFASTA('/home/avellal14/GenData/memeInputs/chip_seq/tfbsCHIP.fastq')
#makeSmallFASTA('/home/avellal14/GenData/chrYVar.fa')



"""
def removeNs(filename):
    handle = open(filename, "rU")
    filtered = [record for record in SeqIO.parse(handle, "fasta") if record.seq.count('N') == 0]
    newFastaHandle = open('/home/avellal14/GenData/filtered1.fa', 'w')
    SeqIO.write(filtered, newFastaHandle, "fasta")

    newFastaHandle.close()
    handle.close()
    
    
removeNs('/home/avellal14/GenData/chrYVar.fa')
makeSmallFASTA('/home/avellal14/GenData/filtered1.fa')
"""