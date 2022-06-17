#Class to format given amounts of money based on which country the money comes from.
class Currency:
    def __init__(self, symbol,onLeft,usSystem,amount):
        self._symbol = symbol
        self._onLeft = onLeft
        self._usSystem = usSystem
        self._amount = amount

    #Method that formats output based on usSystem and onLeft booleans
    def getFormat(self):
        if self._usSystem == True and self._onLeft == True:
            return "{0:s}{1:,.2f}".format(self._symbol,self._amount)

        elif self._usSystem == False and self._onLeft == True:
            return "{0:s}{1:,.2f}".format(self._symbol,self._amount).replace(",","w").replace(".",",").replace("w",".")

        elif self._usSystem == True and self._onLeft == False:
            return "{0:,.2f}{1:s}".format(self._amount,self._symbol)

        elif self._usSystem == False and self._onLeft == False:
            return "{0:,.2f}{1:s}".format(self._amount,self._symbol).replace(",","w").replace(".",",").replace("w",".")

        else:
            return("Invalid Input")
        
    #Magic method to output results
    def __str__(self):
        return(str(self.getFormat()))
        
