class ChoresList() :
    
    MINIMUM_NUMBER_OF_CHORES = 2
    MAXIMUM_NUMBER_OF_CHORES = 5

    def __init__(self, the_chores) :
        self.chores = the_chores

    ## Return the chores attribute.
    #          
    @property
    def chores(self):
        return self._chores


    ## Sets the chores attribute.
    # The chores attribute is a set of Chore objects.
    #
    #  @param chores - the chores        
    @chores.setter
    def chores(self, the_chores) :
        try :
            self.valid_chores(the_chores)
            self._chores = the_chores
        except ValueError as err :
            raise

    def __str__(self):
        length = len(self.chores)
        i = 1
        chore_string = ""
        for chore in self.chores :
            chore_string = chore_string + str(chore)
            if i < length :
                chore_string = chore_string + ", "
            i = i + 1
            
        return chore_string

    ## Check whether a chore name exists in the set of chores.
    #
    # @param chore_name
    # @return True if the chore name exists in the set, False if it does not.
    def chore_exists(self, chore_name) :
        found = False
        for chore in self.chores :
            if chore_name == chore.chore_name :
                found = True
                
        return found


    ## Check the set of chores.
    # Verifies that the set of chores is a valid length.
    # 
    # @param chores the set of chores to be validated
    # @return True if the set conforms to the validation conditions
    #         and raise exception if it does not.
    #
    @staticmethod
    def valid_chores(the_chores) :
        # check that the_chores is a set
        if not isinstance(the_chores, set) :
            raise TypeError("List of chores is not a set.")
                
        try :
            ChoresList.is_valid_length(the_chores)
            ChoresList.is_valid_chores(the_chores)
        except ValueError as err :
            raise
        
        return True
        
    @staticmethod        
    def is_valid_length(the_chores) :    
        if len(the_chores) < ChoresList.MINIMUM_NUMBER_OF_CHORES or \
            len(the_chores) > ChoresList.MAXIMUM_NUMBER_OF_CHORES :
            raise ValueError(("\n\t\tThe number of chores" + 
               " must be more than {} and less than {}.")
               .format(ChoresList.MINIMUM_NUMBER_OF_CHORES - 1, ChoresList.MAXIMUM_NUMBER_OF_CHORES + 1))
        # If we reached this point then the checks passed
        return True
    
    
    @staticmethod    
    def is_valid_chores(the_chores) :
        for chore in the_chores :
            if not isinstance(chore, Chore) :
                raise TypeError("The ChoreList does not contain objects which are Chores.")
        # If we reached this point, the chores are valid.
        return True   


    ## Check whether a chore name exists in a set of chores.
    #
    # @param chore_name the name of the chore
    # @param the_chores the set of chores
    # @return True if the set does not contain a chore with the name chore_name
    #         and raise exception if it does.
    #
    @staticmethod    
    def is_unique(chore_name, the_chores) :
        if not isinstance(the_chores, set) :
            raise TypeError("The ChoreList is not a set.")
        
        found = False
        
        for chore in the_chores :
            if not isinstance(chore, Chore) :
                raise TypeError("The ChoreList does not contain objects which are Chores.")
            if chore_name == chore.chore_name :
                found = True

        if found :
            raise ValueError("\t\tChore: {} already exists in the set".format(chore_name))
        
        return found

        
class Chore():

    ## Constants used for validation
    MINIMUM_NAME_LENGTH = 3     # Used to validate team member's name, household name and chore name
    MAXIMUM_NAME_LENGTH = 20
    
    MINIMUM_CHORE_FREQUENCY = 1
    MAXIMUM_CHORE_FREQUENCY = 20

    def __init__(self, the_chore_name, the_frequency) :
        self.chore_name = the_chore_name
        self.frequency = the_frequency

    ## Return the chore name.
    #          
    @property
    def chore_name(self):
        return self._chore_name


    ## Sets the chore name attribute.
    #  @param the_chore_name - the description of the chore        
    @chore_name.setter
    def chore_name(self, the_chore_name) :
        try :
            self.is_valid_chore_name(the_chore_name)
            self._chore_name = the_chore_name
        except ValueError as err :
            raise 

    ## Return the chore frequency.
    #          
    @property
    def frequency(self):
        return self._frequency


    ## Sets the chore frequency attribute.
    #  @param the_chore_name - the description of the chore        
    @frequency.setter
    def frequency(self, the_frequency) :
        try :
            self.is_valid_frequency(the_frequency)
            self._frequency = the_frequency
        except ValueError as err :
            raise 


    def __eq__(self, otherChore):
        if isinstance(otherChore, Chore) :
            return (self.chore_name == otherChore.chore_name)
        else:
            raise TypeError("Argument must be a Chore object.")


    def __hash__(self):
        return hash((self.chore_name))


    def __str__(self):          
        return self.chore_name +  " (" + str(self.frequency) + ")"


    ## Check the name contains only alphanumeric characters and check that it is the right length.
    # 
    # @param name the string to be validated
    # @param minimum_length the minimum length of the string
    # @param maximum_length the maximum length of the string
    # @return True if the string conforms to the validation conditions.
    #         Raise an exception if invalid.
    #
    @staticmethod
    def is_valid_chore_name(name) :
        if len(name) < Chore.MINIMUM_NAME_LENGTH \
            or len(name) > Chore.MAXIMUM_NAME_LENGTH :
            raise ValueError(("Chore name: {}, is not valid. It should be: " +
                         "more than {} characters long " +
                         "and less than {} characters long.")
                .format(name, Chore.MINIMUM_NAME_LENGTH, Chore.MAXIMUM_NAME_LENGTH))

        name_list = name.split()    

        for word in name_list :
            if not word.isalnum():
               raise ValueError(("{}, is not valid. All words in the chore name should be " +
                                 "alphanumeric.").format(word)) 
            

    ##  Checks whether the chore frequency is greater than or equal to the minimum frequency
    #   and less than or equal to the maximum frequency.
    #
    #   @return True or False.
    #
    @staticmethod
    def is_valid_frequency(frequency):
        try :
            frequency = int(frequency)
        except :
            raise TypeError("Chore frequency must be an integer.")
        
        if frequency < Chore.MINIMUM_CHORE_FREQUENCY or frequency > Chore.MAXIMUM_CHORE_FREQUENCY :
            raise ValueError(("Chore frequency must be greater or equal to " + \
                             "{} and less than or equal to {}") \
                .format(Chore.MINIMUM_CHORE_FREQUENCY, Chore.MAXIMUM_CHORE_FREQUENCY))
        return True
 






def main() :

    print("Test 1: Create a valid chore list")    
    try:
        c1 = Chore("wash up", 4)
        c2 = Chore("vacuum stairs", 2)
        c3 = Chore("dusting", 1)
        c4 = Chore("empty bin", 2)
        cl1 = ChoresList(set([c1, c2, c3, c4]))
        print("\n\tVALID: ", cl1)
    except (ValueError, TypeError) as err:
        print("\tERROR: ", err)

    print("\nTest 2: Create a chore list with invalid frequency")    
    try:
        c1 = Chore("wash up", 4)
        c2 = Chore("vacuum stairs", 2)
        c3 = Chore("dusting", 1)
        c4 = Chore("empty bin", 25)
        cl1 = ChoresList(set([c1, c2, c3, c4]))
        print("\n\tVALID: ", cl1)
    except Exception as err:
        print("\tERROR: ", err)
        
    print("\nTest 3: Create a chore list containing an invalid name")    
    try:
        c1 = Chore("wash up", 4)
        c2 = Chore("vacuum stairs", 2)
        c3 = Chore("dusting", 1)
        c4 = Chore("*", 25)
        cl1 = ChoresList(set([c1, c2, c3, c4]))
        print("\n\tVALID: ", cl1)
    except Exception as err:
        print("\tERROR: ", err)       

    print("\nTest 4: Create a chore list with duplicate entries")    
    try:
        c1 = Chore("wash up", 4)
        c2 = Chore("vacuum stairs", 2)
        c3 = Chore("dusting", 1)
        c4 = Chore("wash up", 3)
        cl1 = ChoresList(set([c1, c2, c3, c4]))
        print("\n\tVALID: ", cl1)
    except Exception as err:
        print("\tERROR: ", err)    

if __name__ == "__main__":
    main()
