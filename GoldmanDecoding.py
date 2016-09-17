# -*- coding: utf-8 -*-
import ExtraModules
import huffman
import io
import os
import HuffmanDecodeManager


def decode(filename):
 generateTrits(filename)
 huffmanDecode(filename)
 

 # first generate dna string out of the encoded file input
def generateTrits(filename):

 with io.open(filename,"r") as fileToRead, io.open(filename[:-5]+'.temp',"w") as OutputFile:
  first=True
  prevBase='A'
  rc=1
  for chunk in fileToRead:
   
   if chunk[0] == 'G' or chunk[0]=='C':
    chunk=ExtraModules.reverseComplement(chunk)

   end=25
   lengthOfChunk=len(chunk)
   
   if lengthOfChunk <= 117:
       end = (lengthOfChunk-18)%25
       if end == 0:
        end = 25  
   temp=chunk[1:lengthOfChunk-17]
   
   if rc == 0:
    temp=ExtraModules.reverseComplement(temp)
   rc=rc^1
     
         
   if first is False :
    OutputFile.write(unicode(getTrits(temp[-1*end:],prevBase)))
   else :
    first = False
    OutputFile.write(unicode(getTrits(temp,prevBase)))
   prevBase=temp[-1]


def getTrits(payload,prevBase):
 outputList=[]
 
 for base in payload:
  outputList.append(str(ExtraModules.diffEncDict[prevBase].index(base)))
  prevBase=base
 
 return ''.join(outputList)

def huffmanDecode(filename):
 tempfile=filename[:-5]+'.temp'
 with io.open(filename[:-5],"wb") as OutputFile,io.open(tempfile,"rb") as tempFileToRead:
     y=HuffmanDecodeManager.HuffmanDecodeManager(OutputFile)
     y.readFromFile(tempFileToRead,lengthfromS2(tempFileToRead))
     y.close()
 os.remove(tempfile)

def lengthfromS2(tempFileToRead):
 tempFileToRead.seek(-20,os.SEEK_END)
 lenghtOfS1=ExtraModules.base3ToInt(tempFileToRead.read())
 tempFileToRead.seek(0)
 return lenghtOfS1

decode(raw_input())
