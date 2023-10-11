from helperFunctions import printErr


class MoveValidator:
    @staticmethod
    def validate(args):
        amount_of_args = len(args)
        if amount_of_args != len(set(args)):
            printErr("There Are Duplicate Arguments!\nExample: rock paper scissors (EVERY ONE OF THEM ARE UNIQUE)")
        elif amount_of_args < 3:
            printErr("At Least 3 Arguments Should Be Passed!\nExample: rock paper scissors lizard spock (ARGUMENTS ARE MORE THAN 3)")
        elif amount_of_args % 2 == 0:
            printErr("Amount of Arguments Should be Odd!\nExample: scissors paper rock (NUMBER OF ARGUMENTS ARE EVEN)")
        else:   
            return True
        return False
    
    
