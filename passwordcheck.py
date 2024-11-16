#Password Checker v1
#by Wuayna
#16AUG2024



#Variables
minLength = 9
complex = False
case = False
needsUpper = False
lengthReq = False
unique = False
pwPass = False


print("----------Test your password strength----------\n")

#Passowrd Requirments
# length
# Complexity (upper, lower, numerical, special)
# Unique (nonrepeating, i.e. aaaaaa, bbbbb)


print("----------Meet the following criteria: ----------")
print("1. Length (min length is 9 characters)")
print("2. Complexity (alphanumerical, 1 special character, 1 upper, 1 lower)")
print("3. Unique (no all repeating characters)")
print("\n")





def checkLength(inputPW):
    global lengthReq
    if len(inputPW) < minLength:
        print("WARNING: Password too short")
    else: 
        lengthReq = True
        # print("Password meets length requirement")
def checkCase(inputPW):
    global case
    if any(char.isupper() for char in inputPW) == False:
        print("WARNING: Needs at least 1 uppercase character")
        needsUpper= True
        if any(char.islower() for char in inputPW) == False:
            needsUpper = False
            print("WARNING: Needs at least 1 lowercase character")
    else:
        case = True
         #print("Meets at least 1 upper character requirement")

        
def checkComplex(inputPW):
    global complex
 
 #possiblilities
 #ALL NUMBERS (isnumeric)
    if inputPW.isnumeric() == True:
        print("WARNING: Cannot be all numbers")
 #ALL ALPHA    (isalpha)
    elif inputPW.isalpha() == True:
        print("WARNING: Cannot be all alphabetic characters")
 #ALL SPECIAL  
    elif (char.isalum for char in inputPW) == False:
        print("WARNING: Cannot be all special characters")
    elif inputPW.isalnum() == True:
        print("WARNING: Need at least 1 special character")
 #ALL UPPER
    elif inputPW.isupper() == True:
        print("WARNING: Need at least 1 lowercase character")
 #ALL LOWER
        if inputPW.islower()==True:
            print("WARNING: Need at least 1 uppercase character")
        else:
            case = True
    else:
        complex = True
      
   
def checkRepeat(inputPW):
    x =0
    global unique
    repeated = 1
    while x < (len(inputPW)-1):
        if inputPW[x] == inputPW[x+1]:
           repeated = repeated + 1
        x= x+ 1
    if repeated == len(inputPW):
        print("WARNING: Password cannot be all repeating characters")
    else:
        unique = True
        # print("Unique")
       
        
def passwordCheck():
    global pwPass
    
    while (pwPass == False):
        inputPW = input("Enter your password: \n")
        checkLength(inputPW)
        checkCase(inputPW)
        checkComplex(inputPW)
        checkRepeat(inputPW)

        if complex and unique and lengthReq and case:
            pwPass = True
            print("CONGRATS YOUR PASSWORD IS STRONG\n")
        else:
            print("TRY AGAIN! Your password does not meet the requirements\n")
       

passwordCheck()




