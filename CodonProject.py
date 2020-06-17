# DNA sequence attributes.
print("Input your DNA sequence below:")
dnaSeq = input()
print("Confirmation: Your DNA sequence is " + dnaSeq)
print("Is this correct? Type yes or no.")
correct = input()
if correct == "yes":
    for j in range(len(dnaSeq)):
        if dnaSeq[j] == "A" or dnaSeq[j] == "T" or dnaSeq[j] == "G" or dnaSeq[j] == "C":
            correct = correct
        else:
            print("INCORRECT BASES USED : PLEASE CHECK YOUR BASES")
            correct = "no"
            break
# Program Main Body
if correct == "yes":
    dnaLength = len(dnaSeq)
    print("The length of the DNA sequence is " + str(dnaLength) + ".")
    count = 0
    for i in range(dnaLength):
        if dnaSeq[i] == 'A' or dnaSeq[i] == "T":
            count += 1
    print("The AT count is " + str(count) + ".")
    percentAT = count / dnaLength * 100
    print("The AT content percentage is " + str(round(percentAT, 2)) + " %.")

# Complimentary DNA sequence and template mRNA sequence.
    mrnaSeq = ""
    dnaComp = ""
    for k in range(dnaLength):
        if dnaSeq[k] == 'A':
            dnaComp = dnaComp + "T"
        elif dnaSeq[k] == 'T':
            dnaComp = dnaComp + "A"
        elif dnaSeq[k] == 'C':
            dnaComp = dnaComp + "G"
        elif dnaSeq[k] == 'G':
            dnaComp = dnaComp + "C"
        if dnaSeq[k] == 'A':
            mrnaSeq = mrnaSeq + "A"
        elif dnaSeq[k] == 'T':
            mrnaSeq = mrnaSeq + "U"
        elif dnaSeq[k] == 'C':
            mrnaSeq = mrnaSeq + "C"
        elif dnaSeq[k] == 'G':
            mrnaSeq = mrnaSeq + "G"

    print("The complimentary DNA sequence is " + dnaComp)
    print("The mRNA sequence is " + mrnaSeq)

# Codons & Splicing out introns.
    count = 0
    cycle = 0
    startcod = 0
    stopcod = 0
    SeqCod = ""
    for r in range(0, dnaLength, 3):
        if dnaSeq[r] == "A" and dnaSeq[r + 1] == "T" and dnaSeq[r + 2] == "G":
            for x in range(r+3, dnaLength, 3):
                if dnaSeq[x] == "T" and dnaSeq[x + 1] == "A" and dnaSeq[x + 2] == "A":
                    count += 1
                    for w in range(r+3, x, 3):
                        if dnaSeq[w] == "A" and dnaSeq[w + 1] == "T" and dnaSeq[w + 2] == "G":
                            count -= 1
                            break
                    break
                elif dnaSeq[x] == "T" and dnaSeq[x + 1] == "A" and dnaSeq[x + 2] == "G":
                    count += 1
                    for w in range(r+3, x, 3):
                        if dnaSeq[w] == "A" and dnaSeq[w + 1] == "T" and dnaSeq[w + 2] == "G":
                            count -= 1
                            break
                    break
                elif dnaSeq[x] == "T" and dnaSeq[x + 1] == "G" and dnaSeq[x + 2] == "A":
                    count += 1
                    for w in range(r+3, x, 3):
                        if dnaSeq[w] == "A" and dnaSeq[w + 1] == "T" and dnaSeq[w + 2] == "G":
                            count -= 1
                            break
                    break
    if dnaLength % 3 == 0:
        while (cycle < count):
            for q in range(stopcod, dnaLength, 3):
                if dnaSeq[q] == "A" and dnaSeq[q+1] == "T" and dnaSeq[q+2] == "G":
                    print("START CODON AT BASE " + str(q+1))
                    startcod = q+1
                    for n in range(q, dnaLength, 3):
                        if dnaSeq[n] == "T" and dnaSeq[n + 1] == "A" and dnaSeq[n + 2] == "A":
                            print("STOP CODON AT BASE " + str(n+1))
                            stopcod = n+3
                            break
                        elif dnaSeq[n] == "T" and dnaSeq[n + 1] == "A" and dnaSeq[n + 2] == "G":
                            print("STOP CODON AT BASE " + str(n+1))
                            stopcod = n+3
                            break
                        elif dnaSeq[n] == "T" and dnaSeq[n + 1] == "G" and dnaSeq[n + 2] == "A":
                            print("STOP CODON AT BASE " + str(n+1))
                            stopcod = n+3
                            break
                if dnaSeq[q] == "A" and dnaSeq[q + 1] == "T" and dnaSeq[q + 2] == "G":
                    break
            for l in range(startcod - 1, stopcod):
                if dnaSeq[l] == 'A':
                    SeqCod = SeqCod + "A"
                elif dnaSeq[l] == 'T':
                    SeqCod = SeqCod + "U"
                elif dnaSeq[l] == 'C':
                    SeqCod = SeqCod + "C"
                elif dnaSeq[l] == 'G':
                    SeqCod = SeqCod + "G"
            cycle += 1
        if startcod != 0 and stopcod != 0:
            print("Complete mRNA sequence with spliced out introns: " + SeqCod)
    else:
        print("Missing full-length codons (non-divisible by 3) or out-of-frame.")

# Amino Acid Sequence
    AA1 = ""
    AA3 = ""
    LenCod = len(SeqCod)
    for b in range(0, LenCod, 3):
        if SeqCod[b] == "A" and SeqCod[b+1] == "U" and SeqCod[b+2] == "G":
            AA1 = AA1 + "M"
            AA3 = AA3 + "Met"
        elif (SeqCod[b] == "U" and SeqCod[b+1] == "A" and SeqCod[b+2] == "A"
                or SeqCod[b] == "U" and SeqCod[b+1] == "A" and SeqCod[b+2] == "G"
                or SeqCod[b] == "U" and SeqCod[b+1] == "G" and SeqCod[b+2] == "A"):
            AA1 = AA1 + " "
            AA3 = AA3 + "   "
        elif (SeqCod[b] == "U" and SeqCod[b+1] == "U" and SeqCod[b+2] == "U"
                or SeqCod[b] == "U" and SeqCod[b+1] == "U" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "F"
            AA3 = AA3 + "Phe"
        elif (SeqCod[b] == "U" and SeqCod[b+1] == "A" and SeqCod[b+2] == "U"
                or SeqCod[b] == "U" and SeqCod[b+2] == "A" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "Y"
            AA3 = AA3 + "Tyr"
        elif (SeqCod[b] == "U" and SeqCod[b+1] == "G" and SeqCod[b+2] == "U"
                or SeqCod[b] == "U" and SeqCod[b+1] == "G" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "C"
            AA3 = AA3 + "Cys"
        elif SeqCod[b] == "U" and SeqCod[b+1] == "G" and SeqCod[b+2] == "G":
            AA1 = AA1 + "W"
            AA3 = AA3 + "Trp"
        elif (SeqCod[b] == "U" and SeqCod[b+1] == "C" and SeqCod[b+2] == "U"
                or SeqCod[b] == "U" and SeqCod[b+1] == "C" and SeqCod[b+2] == "C"
                or SeqCod[b] == "U" and SeqCod[b+1] == "C" and SeqCod[b+2] == "A"
                or SeqCod[b] == "U" and SeqCod[b+1] == "C" and SeqCod[b+2] == "G"
                or SeqCod[b] == "A" and SeqCod[b+1] == "G" and SeqCod[b+2] == "U"
                or SeqCod[b] == "A" and SeqCod[b+1] == "G" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "S"
            AA3 = AA3 + "Ser"
        elif (SeqCod[b] == "U" and SeqCod[b+1] == "U" and SeqCod[b+2] == "A"
                or SeqCod[b] == "U" and SeqCod[b+1] == "U" and SeqCod[b+2] == "G"
                or SeqCod[b] == "C" and SeqCod[b+1] == "U" and SeqCod[b+2] == "U"
                or SeqCod[b] == "C" and SeqCod[b+1] == "U" and SeqCod[b+2] == "C"
                or SeqCod[b] == "C" and SeqCod[b+1] == "U" and SeqCod[b+2] == "A"
                or SeqCod[b] == "C" and SeqCod[b+1] == "U" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "L"
            AA3 = AA3 + "Leu"
        elif (SeqCod[b] == "C" and SeqCod[b+1] == "C" and SeqCod[b+2] == "U"
                or SeqCod[b] == "C" and SeqCod[b+1] == "C" and SeqCod[b+2] == "C"
                or SeqCod[b] == "C" and SeqCod[b+1] == "C" and SeqCod[b+2] == "A"
                or SeqCod[b] == "C" and SeqCod[b+1] == "C" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "P"
            AA3 = AA3 + "Pro"
        elif (SeqCod[b] == "C" and SeqCod[b+1] == "A" and SeqCod[b+2] == "U"
                or SeqCod[b] == "C" and SeqCod[b+1] == "A" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "H"
            AA3 = AA3 + "His"
        elif (SeqCod[b] == "C" and SeqCod[b+1] == "A" and SeqCod[b+2] == "A"
                or SeqCod[b] == "C" and SeqCod[b+1] == "A" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "Q"
            AA3 = AA3 + "Gln"
        elif (SeqCod[b] == "C" and SeqCod[b+1] == "G" and SeqCod[b+2] == "U"
                or SeqCod[b] == "C" and SeqCod[b+1] == "G" and SeqCod[b+2] == "C"
                or SeqCod[b] == "C" and SeqCod[b+1] == "G" and SeqCod[b+2] == "A"
                or SeqCod[b] == "C" and SeqCod[b+1] == "G" and SeqCod[b+2] == "G"
                or SeqCod[b] == "A" and SeqCod[b+1] == "G" and SeqCod[b+2] == "A"
                or SeqCod[b] == "A" and SeqCod[b+1] == "G" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "R"
            AA3 = AA3 + "Arg"
        elif (SeqCod[b] == "A" and SeqCod[b+1] == "U" and SeqCod[b+2] == "U"
                or SeqCod[b] == "A" and SeqCod[b+1] == "U" and SeqCod[b+2] == "C"
                or SeqCod[b] == "A" and SeqCod[b+1] == "U" and SeqCod[b+2] == "A"):
            AA1 = AA1 + "I"
            AA3 = AA3 + "Ile"
        elif (SeqCod[b] == "A" and SeqCod[b+1] == "C" and SeqCod[b+2] == "U"
                or SeqCod[b] == "A" and SeqCod[b+1] == "C" and SeqCod[b+2] == "C"
                or SeqCod[b] == "A" and SeqCod[b+1] == "C" and SeqCod[b+2] == "A"
                or SeqCod[b] == "A" and SeqCod[b+1] == "C" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "T"
            AA3 = AA3 + "Thr"
        elif (SeqCod[b] == "A" and SeqCod[b+1] == "A" and SeqCod[b+2] == "U"
                or SeqCod[b] == "A" and SeqCod[b+1] == "A" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "N"
            AA3 = AA3 + "Asn"
        elif (SeqCod[b] == "A" and SeqCod[b+1] == "A" and SeqCod[b+2] == "A"
                or SeqCod[b] == "A" and SeqCod[b+1] == "A" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "K"
            AA3 = AA3 + "Lys"
        elif (SeqCod[b] == "G" and SeqCod[b+1] == "U" and SeqCod[b+2] == "U"
                or SeqCod[b] == "G" and SeqCod[b+1] == "U" and SeqCod[b+2] == "C"
                or SeqCod[b] == "G" and SeqCod[b+1] == "U" and SeqCod[b+2] == "A"
                or SeqCod[b] == "G" and SeqCod[b+1] == "U" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "V"
            AA3 = AA3 + "Val"
        elif (SeqCod[b] == "G" and SeqCod[b+1] == "C" and SeqCod[b+2] == "U"
                or SeqCod[b] == "G" and SeqCod[b+1] == "C" and SeqCod[b+2] == "C"
                or SeqCod[b] == "G" and SeqCod[b+1] == "C" and SeqCod[b+2] == "A"
                or SeqCod[b] == "G" and SeqCod[b+1] == "C" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "A"
            AA3 = AA3 + "Ala"
        elif (SeqCod[b] == "G" and SeqCod[b+1] == "A" and SeqCod[b+2] == "U"
                or SeqCod[b] == "G" and SeqCod[b+1] == "A" and SeqCod[b+2] == "C"):
            AA1 = AA1 + "D"
            AA3 = AA3 + "Asp"
        elif (SeqCod[b] == "G" and SeqCod[b+1] == "A" and SeqCod[b+2] == "A"
                or SeqCod[b] == "G" and SeqCod[b+1] == "A" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "E"
            AA3 = AA3 + "Glu"
        elif (SeqCod[b] == "G" and SeqCod[b+1] == "G" and SeqCod[b+2] == "U"
                or SeqCod[b] == "G" and SeqCod[b+1] == "G" and SeqCod[b+2] == "C"
                or SeqCod[b] == "G" and SeqCod[b+1] == "G" and SeqCod[b+2] == "A"
                or SeqCod[b] == "G" and SeqCod[b+1] == "G" and SeqCod[b+2] == "G"):
            AA1 = AA1 + "G"
            AA3 = AA3 + "Gly"

    print("1-letter amino acid sequence: " + AA1)
    print("3-letter amino acid sequence: " + AA3)
elif correct == "no":
    print("PLEASE START PROGRAM OVER")
else:
    print("INCORRECT COMMAND : PLEASE START PROGRAM OVER")