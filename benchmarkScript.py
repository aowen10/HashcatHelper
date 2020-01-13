
import subprocess

hashcodeFile = './listofhashcodes'

hashcodeList = [line.rstrip('/n') for line in open(hashcodeFile)]

basecommand = 'hashcat -b -O -m '

for code in hashcodeList :
    bashcommand = basecommand + code
    subprocess.call(bashcommand.split())
