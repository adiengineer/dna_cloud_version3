# dna_cloud_version3
A toolbox to convert personal data files of any nature into DNA base strings which can be stored as artificially synthesized DNA and vice versa. It also includes cost calculations (artificial DNA is still expensive) and comparisons between several conversion schemes. The actual process of converting binary data to DNA bases involves a lot of challenges and 
requires a certain degree of intern- disciplinary knowledge from coding theory and biology. 
I think our chief achievement was that we could develop a simple, intuitive yet powerful software which not only could 
generate the appropriate sequences but could also give an estimate of the cost of the process.

Chunk Architecture in New Improved Golay code application:


We limit the amount of data in bytes to store per chunk to 9 bytes as this seems the most optimal and less error prone number.

Definitions :

GOD Chunk: The chunk where data regarding filesize and number of chunks required for storing filename is stored. This should be the very first chunk to be read at the time of decoding. Its length is always bigger than the regular payload chunk.

Regular Payload Chunk: The chunk where actual data of file, filename, extension is stored and has used all 9 bytes. Size is neccessarily to be exactly equal to 9 bytes for a chunk to be called Regular.

Irregular Payload Chunk: The chunk whose data has size < 9 bytes. Maximum possible Irregular chunks=1(file extension chunk) + 1(filename chunk) + 1(fileSize chunk) + 1(GOD chunk)=4

Chunk architecture of Regular/Irregular chunk:

•	1 guard trit
•	At max 99 trits worth 9 bytes of data, (exactly 99 trits in a regular chunk )
•	 Tits required for “File Id” depends on number of files and is assumed to be known for supporting multi file access (default taken as 2)
•	 Trits required for chunkId depends on size of the file
•	1 trit for parity
•	1 guard trit

Chunk architecture of GOD chunk:

•	1 guard trit
•	11 trits (1 byte) to get number of file name chunks
•	2 trits to get maximum number of bytes which is required to store file size. (range 1 to 8)
•	next trits ( no of bytes for filesize * 11 * x, x is the minimum no such that god chunk size becomes greater than regular chunk size)
•	File Id trits
•	1 trit for parity
•	1 guard trit

//////////////////

Encoding example

Explanation of sample.txt.dnac

This is the output of encoding of sample.txt file with File ID 1.

GOD CHUNK :
AGAGTGATCGATAGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTATCGCGAGTGTCGC

File Extension CHUNK :
ATGCATATCGAGCTACGCACGAGCATGCGCTAGACTACG

File Name Chunk (In this case only 1 chunk for file name ) :
ATGCGTATATGTCATCTGTATGCATATCGAGCATGTCGCACTACTCGAGTCTCGTACTGTAGTATCACTCTG

Actual DATA now begins here :
TCATGATGAGCGACTCTACGACTCGTGTAGCTATAGCGACATAGTAGCGACATAGTGCATATCGAGCGACTGCGTGTCGTCGCGCGCTCGATGC

A  ---> Guard Base
G ---> Parity
T ---> Chunk ID
C ---> FILE ID base
Black Color is actual DATA encoded


