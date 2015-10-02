# takes in list of values for C, H, and O and then computes the needed ratios
def processElementalData(elementalList):
    # 0 = H:C, 1 = O:C, 2 = N:C
    ratiosList = [[],[],[]]
    
    #Computes all the ratios and adds them to the ratiosList
    for line in elementalList:
        if len(line) == 4:
			
	    HtoC = line[1]/line[0]
            ratiosList[0].append(HtoC)
            OtoC = line[2]/line[0]
            ratiosList[1].append(OtoC)
            NtoC = line[3]/line[0]
	    ratiosList[2].append(NtoC)

       			
    return ratiosList

    
    
