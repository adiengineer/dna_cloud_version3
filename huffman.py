# -*- coding: utf-8 -*-
reverseHuffmanDict = dict()
huffmanDict = {0:'22201' ,            #0-> NULL CHARACTER
                   85:'22200' ,           #85-> U
                   170:'22122' ,          #170-> ª
                   127:'22121',           #127 ->
                   253:'22120' ,          #253 -> ý
                   52:'22112' ,           #52 -> 4
                   138:'22111' ,          #138 ->
                   41:'22110' ,            #41 -> )
                   86:'22102' ,           #86 -> V
                   42:'22101' ,           #42 -> *
                   100:'22100' ,          #100 -> d
                   44:'22022' ,           #44 -> ,
                   250:'22020' ,          #250 -> ú
                   132:'22021' ,          #132 ->
                   161:'22012' ,          #161 -> i
                   98:'22010' ,           #98 -> b
                   8:'22002' ,            #8 -> ^H 
                   34:'22011' ,           #34 -> 
                   10:'22001' ,           #10 -> [NL]
                   149:'22000' ,          #149 ->
                   87:'21222' ,           #87 -> W
                   21:'21221' ,           #21 ->
                   74:'21220' ,           #74 -> J
                   36:'21212' ,           #36 ->$
                   69:'21210' ,           #69 -> E
                   177:'21202' ,          #177 -> ±
                   20:'21211' ,           #20 ->
                   213:'21200' ,          #213 -> Õ
                   163:'21201' ,          #163 -> £
                   229:'21121' ,          #229 -> å
                   255:'21122' ,         #255 -> ÿ
                   197:'21120' ,          #197 -> Å
                   133:'21112' ,          #133 ->
                   252:'21110' ,          #252 -> ü
                   26:'21111' ,           #26 -> 
                   173:'21101' ,          #173 -> ­
                   151:'21102' ,          #151 -> 
                   82:'21100' ,           #82 -> R
                   75:'21022' ,           #75 -> K
                   37:'21021' ,           #37 -> %
                   166:'21011' ,          #166 -> ¦
                   191:'21020' ,          #191 -> ¿
                   88:'21012' ,           #88 -> X
                   63:'21010' ,           #63 -> ?
                   68:'21001' ,           #68 -> D
                   150:'21002' ,          #150 ->
                   76:'21000' ,           #76 -> L
                   4:'20222' ,            #4 -> 
                   154:'20221' ,          #154 ->
                   234:'20212' ,          #234 -> ê
                    22:'20220' ,          #
                    162:'20211' ,         #¢
                    105:'20210' ,        #i
                    102:'20202' ,        #f
                    171:'20201' ,         #«
                    104:'20200' ,         #h
                    169:'20122' ,         #©
                    196:'20121' ,         #Ä
                    208:'20120' ,         #Ð
                    84:'20112' ,          #T
                    130:'20111' ,
                    146:'20102' ,         #
                    72:'20110' ,          #H
                    16:'20101' ,          #
                    66:'20100' ,          #B
                    24:'20022' ,          #
                    106:'20012' ,         #j
                    223:'20020' ,         #ß
                    58:'20021' ,          #:
                    137:'20011' ,
                    73:'20010' ,          #I
                    101:'20001' ,         #e
                    168:'20002' ,         #¨
                    181:'12221' ,         #µ
                    175:'12222' ,         #¯
                    251:'20000' ,#û       
                    40:'12220',#(
                    140:'12212',#<8c>
                    17:'12211',#^Q
                    83:'12210',#S
                    254:'12202',#þ
                    240:'12201',#ð
                    214:'12200',#Ö
                    53:'12122',#5
                    202:'12112',#Ê
                    25:'12121',#^Y
                    18:'12120',#^R
                    247:'12111',#÷
                    174:'12110',#®
                    112:'12102',#p
                    89:'12101',#Y
                    210:'12100',#Ò
                    217:'12012',#Ù
                    248:'12020',#ø
                    194:'12021',#Â
                    182:'12022',#¶
                    80:'12011',#P
                    79:'12002',#O
                    195:'12010',#Ã
                    12:'12001',#Form Feed
                    209:'12000',#Ñ
                    165: '11222',#¥
                    245:'11221',#õ
                    2:'11220',#^B
                    81:'11212',#Q
                    38:'11211',#&
                    141:'11202',#<8d>
                    211:'11210',#Ó
                    239:'11200',#ï
                    95:'11201',#_
                    43:'11122',#+
                    224:'11121',#à
                    203:'11112',#Ë
                    145:'11120',#<91>
                    147:'11110',#<93>
                    19:'11111',#^S
                    50:'11101',#2
                    136:'11102',#<88>
                    107:'11100',#k
                    134:'11022',#<86>
                    109:'11021',#m
                    153:'11020',#<99>
                    148:'11002',#<94>
                    205:'11010',#Í
                    212:'11011',#Ô
                    54:'11012',#6
                    241:'11000',#ñ
                    156:'11001',#<9c>
                    115:'10222',#s
                    116:'10221',#t
                    78:'10220',#N
                    67:'10211',#C
                    70:'10212',#F
                    178:'10210',#²
                    159:'10202',#<9f>
                    142:'10201',#<8e>
                    92:'10200',#\
                    48:'10122',#0
                    90:'10120',#Z
                    218:'10121',#Ú
                   126:'10112',#~
                   39:'10111',#'
                   219:'10102',#Û
                   167:'10110',#§
                   114:'10101',#r
                   172:'10022',#¬
                   14:'10100',#^N
                   120:'10020',#x
                   139:'10021',#<8b>
                   160:'10012',
                   33:'10011',#!
                   179:'10010',#³
                   117:'10002',#u
                   225:'10001',#á
                   129:'10000',#<81>
                   183:'02222',#·
                   230:'02220',#æ
                   35:'02221',##
                   93:'02210',#]
                   6:'02211',#^F
                   32:'02212',#0
                   56:'02201',#8
                   158:'02202',#<9e>
                   185:'02121',#¹
                   47:'02122',#/
                   143:'02200',#<8f>
                   123:'02111',#{
                   204:'02120',#Ì
                   242:'02112',#ò
                   111:'02110',#o
                   103:'02102',#g
                   108:'02101',#l
                   9:'02100',#[TAB]
                   65:'02022',#A
                   249:'02020',#ù
                   13:'02021',#^M
                   180:'02012',#´
                   226:'02001',#â
                   144:'02002',#<90>
                   15:'02010',#^O
                   57:'02011',#9
                   128:'02000',#<80>
                   135:'01220',#<87>
                   243:'01221',#ó
                   190:'01222',#¾
                   207:'01212',#Ï
                   77:'01211',#M
                   45:'01210',#-
                   91:'01202',#[
                   192:'01201',#À
                   186:'01122',#º
                   216:'01200',#Ø
                   97:'01112',#a
                   118:'01120',#v
                   246:'01121',#ö
                   215:'01111',#×
                   51:'01102',#3
                   206:'01110',#Î
                   184:'01100',#¸
                   227:'01101',#ã
                   233:'01022',#é
                   237:'01021',#í
                   188:'01020',#¼
                   113:'01012',#q
                   49:'01011',#1
                   201:'01010',#É
                   155:'01002',#<9b>
                   222:'01000',#Þ
                   231:'01001',#ç
                   5:'00222',#^E
                   27:'00221',#^[
                   131:'00212',#<83>
                   164:'00220',#¤
                   3:'00211',#^C
                   46:'00210',#.
                   119:'00201',#w
                   28:'00202',#^\
                   176:'00200',#°
                   23:'00122',#^W
                   64:'00121',#@
                   157:'00120',#<9d>
                   187:'00112',#»
                   244:'00110',#ô
                   238:'00111',#î
                   96:'00102',#`
                   235:'00101',#ë
                   60:'00022',#<
                   1:'00100',#^A
                   110:'00021',#n
                   200:'00011',#È
                   221:'00020',#Ý
                   99:'00012',#c
                   31:'00010',#^_
                   198:'00002',#Æ
                   193:'00001',#Á
                   125:'00000',#}
                   124:'222222',#|
                   152:'222221',#<98>
                   122:'222220',#z
                   71:'222212',#G
                   94:'222211',#^
                   220:'222210',#Ü
                   29:'222202',#^]
                   199:'222201',#Ç
                   61:'222200',#=
                   11:'222122',#^K
                   228:'222121',#ä
                   62:'222120',#>
                   55:'222112',#7
                   121:'222111',#y
                   7:'222110',#^G
                   30:'222102',#^^
                   232:'222101',#è
                   189:'222100',#½
                   59:'222021',#;
                   236:'222022',#ì
                   }
def encode(num):
  global huffmanDict
  return huffmanDict[ord(num)]

def setReverseHuffman():
  global reverseHuffmanDict
  for key in huffmanDict:
    reverseHuffmanDict[huffmanDict[key]]=key

def decode(tritString):
  return reverseHuffmanDict.get(tritString,-1)

