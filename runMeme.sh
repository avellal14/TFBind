#!/bin/bash


inputHeader=/home/avellal14/GenData/memeInputs/chr22FASTAS/fasta_segment_
inputEnding=.fa

outputHeader=/home/avellal14/GenData/memeOutputs/chr22/fasta_segment_
outputEnding=.meme

for i in {101..200}
do
	inputDirectory="$inputHeader$i$inputEnding"
	echo ${inputDirectory}
	outputDirectory="$outputHeader$i$outputEnding"
	echo ${outputDirectory}
	meme $inputDirectory -dna -mod anr -pal -oc $outputDirectory
	i = i + 1
done
