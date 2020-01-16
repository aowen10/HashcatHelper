
import subprocess

hashcodeFile = './listofhashcodes'
outputFile = 'outputFile.txt'

hashcodeList = [line.rstrip('/n') for line in open(hashcodeFile)]

basecommand = 'hashcat -b -O -m '
postcommand = ' >> ' + outputFile
for code in hashcodeList :
    bashcommand = basecommand + code + postcommand
    subprocess.call(bashcommand.split())
