
import subprocess


hashcodeFile = 'listofhashcodes.txt'
intermediateFile='intermediateFile'
outputFile = 'outputFile.txt'

hashcodeList = [line.rstrip('\n') for line in open(hashcodeFile)]

basecommand = 'hashcat -b -O -m '
with open(outputFile, "w") as output_f:
    for code in hashcodeList :
        bashcommand = basecommand + code
        print("Executing: " + bashcommand) 
        print("code: " + '0')
        

        proc = subprocess.Popen(bashcommand.split(),stdout= subprocess.PIPE)
        std_out = proc.stdout.read().decode("utf-8")

        splitted = std_out.splitlines()
        pastHashmode = False
        for spl in splitted :
            if not "Hashmode" in spl and not pastHashmode:
                continue
            pastHashmode = True
            if "Started" in spl :
                break
            output_f.write(spl + '\n')
output_f.close()

    

