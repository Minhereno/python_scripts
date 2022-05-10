#!/usr/bin/env python
# BINF 401 Python MySQL database example

# Bob Brown 16 Nov-17
# output a file of all predefined list of metadata for all sequences
# updated 18Nov18  Dr. B
# spr2020 changed to read a file of info then process
#   optional commented out is Mysql commands to read data from db and store back into db
# read in AA sequences and see if it matches fold type criteria if yes store in output

#Minh Tran
#BINF 402

import os
import sys


# import MySQLdb


# ======================
def Chou_Fasman_Calculations():
    # Chou_Fasman_Calculations(tableName):

    proteinName = 'BRCA Protein'
    proteinAAseq = 'GSQDRKIFRGLEICCYGPFTNMPTDQLEWMVQLCGASVVKELSSFTLGTGVHPIVVVQPDAWTEDNGFHAIGQMCEAPVVTREWVLDSVALYQCQELDTYLIPQIPHSHY'

    status = 0

    try:

        choufasmandatatable = open("/Users/minhe/Desktop/ChouFasman_data.txt", "r")
        results = open("/Users/minhe/Desktop/MinhTran_Output.txt", "w")

        dictTable = {}
        for row in choufasmandatatable:
            row = row.split("\t")
            dictTable[row[0]] = row[1:]

        print("ChouFasmanDict=", dictTable["A"], dictTable["Y"])
        # dbCursor.close()

        # start calculating if helix, betasheet, or turn is likely in protein sequence
        # dbCursor= db.cursor()      # open new cursor for inserts

        lenSeq = len(proteinAAseq)

        helixScore = 0
        betasheetScore = 0
        numbeta = 0
        numalpha = 0
        i = 0
        k = 0
        m = 0

        while (i + 6 < (lenSeq)):

            if (i + 6 < (lenSeq)) == False:
                break

            # Identification of helix and sheet "nuclei"

            # Helix - 4 out of 6 residues with high helix propensity (P > 100)
            AA_values = dictTable[proteinAAseq[i]]
            # print( "while "+str(i)+str(proteinAAseq[i])+str(int(AA_values[0]))+"\n" )

            if int(AA_values[0]) > 100:
                numalpha = numalpha + 1
                helixScore = helixScore + int(AA_values[0])

            if (numalpha >= 4):  # if 4 or more residues P > 100
                AA6_values = dictTable[proteinAAseq[i - 6]]
                if (int(AA6_values[0]) > 100):
                    helixScore = helixScore - int(AA_values[0])

            if helixScore > 399:
                start = i - 6
                if start < 0:
                    start = 0

                # print(proteinName+ "AlphaHelix"+ str(i-start)+ str(proteinAAseq[i-start:i])+str(int(helixScore)))
                printRecord(results, proteinName, "AlphaHelix", i, proteinAAseq[i], helixScore)
            i = i + 1

        while (k + 5 < (lenSeq)):

            if (k + 5 < (lenSeq)) == False:
                break

            AA_values = dictTable[proteinAAseq[k]]

            # Beta sheet - 3 out of 5 residues with high sheet propensity (P > 100)
            if int(AA_values[1]) > 100:
                numbeta = numbeta + 1
                betasheetScore += int(AA_values[1])

            if (numbeta >= 3):  # if 3 or more residues P > 100
                AA5_values = dictTable[proteinAAseq[k - 5]]
                if (int(AA5_values[1]) > 100):
                    betasheetScore = int(AA5_values[1])

            if betasheetScore > 299:
                start = k - 5
                if start < 0:
                    start = 0
                # print(proteinName+ "BetaSheet"+str(i-start)+ str(proteinAAseq[i-start:i])+str(int(betasheetScore)))
                printRecord(results, proteinName, "BetaSheet", k, proteinAAseq[k], betasheetScore)
            k = k + 1

        while (m + 6 < (lenSeq)):
            if (m+6 < (lenSeq)) == False:
                break
            AA_values = dictTable[proteinAAseq[m]]
            # Turn
            # Propagation until termination criteria met Turn prediction
            # 1) p(t) > 0.000075     where p(t) = f(j)f(j+1)f(j+2)f(j+3)

            pturn = float(AA_values[3]) * float(AA_values[4]) * float(AA_values[5]) * float(AA_values[6])

            # 2) P(turn) > 1.00 = 100?
            # 3) P(a) > P(turn) > P(b)

            if (pturn > 0.000075) and (int(AA_values[2]) > 100):  # and (int(AA_values[2]) > int(AA_values[2])) and (int(AA_values[3]) > int(AA_values[1])):
                # print(proteinName+ "Turn_"+str(i)+ str(proteinAAseq[i])+str(float(pturn)))
                printRecord(results, proteinName, "Turn",m , proteinAAseq[m], pturn)
            m = m + 1

        # end of while loop


    except:
        print("2 The following problem occurred with the Chou-Fasman processing causing this error:\t" + "\n")
        status = -1
        #metadataFH.close()
        results.close()

    return status


# ======================
def printRecord(results, proteinName, event, loc, eventAAseq, score):
    try:

        sql = proteinName + "'," + str(int(loc)) + ",'" + event + "','" + eventAAseq + "'," + str(float(score))
        print("sql= " + sql)

        # if writing to a db table  else print line in a fil
        #        dbCursor.execute(sql)
        # else have a file already created with file handle dbCursor and write a line to it
        results.write(sql + "\n")

    except:
        print("The following problem occurred with the Chou-Fasman processing causing this error:\t" + "\n")
        status = -1
        # metadataFH.close()
        results.close()
    return


# ======================
if __name__ == "__main__":
    #    if len(sys.argv) < 2:
    #        print(" ERROR no input parameters found"+ sys.argv )
    #        sys.exit(-1)

    #    cfTable= sys.argv[1]  # name of mysql table that has the chou fasman data we need
    #    print( 'program args= '+cfTable )

    #    status= Chou_Fasman_Calculations(cfTable)
    status = Chou_Fasman_Calculations()

    sys.exit(0)  # the program ends
