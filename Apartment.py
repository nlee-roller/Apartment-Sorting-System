class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.metersFromUCSB}m, Condition: {self.condition}"

    def __lt__(self, rhs):
        if self.rent != rhs.rent:
            return self.rent < rhs.rent
        elif self.metersFromUCSB != rhs.metersFromUCSB:
            return self.metersFromUCSB < rhs.metersFromUCSB
        else:
            if self.condition == "excellent" and rhs.condition != "excellent":
                return True
            elif self.condition == "bad" and rhs.condition != "bad":
                return False
            elif self.condition == "average" and rhs.condition != "average":
                if rhs.condition == "excellent":
                    return False
                elif rhs.condition == "bad":
                    return True
            else:
                return False

    def __gt__(self, rhs):
        if self.rent != rhs.rent:
            return self.rent > rhs.rent
        elif self.metersFromUCSB != rhs.metersFromUCSB:
            return self.metersFromUCSB > rhs.metersFromUCSB
        else:
            if self.condition == "excellent" and rhs.condition != "excellent":
                return False
            elif self.condition == "average" and rhs.condition != "average":
                if rhs.condition == "excellent":
                    return True
                elif rhs.condition == "bad":
                    return False
            elif self.condition == "bad" and rhs.condition != "bad":
                return True
            else:
                return False
            
                

    def __eq__(self, rhs):
        if (self.rent == rhs.rent) and (self.metersFromUCSB == rhs.metersFromUCSB) and (self.condition == rhs.condition):
            return True
        else:
            return False
