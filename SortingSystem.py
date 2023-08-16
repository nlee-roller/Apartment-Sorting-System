from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2

        # uses additional space to create left/right halves
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        #recursive sorts lefthalf, then righthalf lists
        mergesort(lefthalf)
        mergesort(righthalf)

        #Merge two sorted sublists (lefthalf/righthalf) int a List
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i += 1
            else:
                apartmentList[k] = righthalf[j]
                j += 1
            k += 1

        # put remaining lefthalf elements (if they exist) into aList
        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i += 1
            k += 1
            
        # put remaining righthalf elemtns (if they exist) into aList
        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j += 1
            k += 1

def ensureSortedAscending(apartmentList):
    if len(apartmentList) == 0:
        return True
    ascendingOrder = True
    i = 0
    while ascendingOrder == True and i < len(apartmentList) - 1:
        if apartmentList[i] < apartmentList[i+1]:
            i += 1
            continue
        else:
            ascendingOrder = False
            break
    return ascendingOrder
        

def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[-1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    apptString = ""
    mergesort(apartmentList)
    for i in range(len(apartmentList)):
        if (i + 1) <= (len(apartmentList) - 1):
            if apartmentList[i+1].rent > budget:
                if apartmentList[i].rent <= budget:
                    apptString += apartmentList[i].getApartmentDetails()
                    break
        if apartmentList[i].rent < budget:
            apptString += apartmentList[i].getApartmentDetails() + "\n"
        elif apartmentList[i].rent == budget:
            apptString += apartmentList[i].getApartmentDetails() + "\n"
        else:
            continue
    return apptString
