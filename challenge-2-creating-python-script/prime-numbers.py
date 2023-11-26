# """
# Write a Python script to:
#
# - Display all the prime numbers between 1 to 250.
# - Store the results in a results.txt file.
# - Test the script. Verify that it produced the expected results in
# the results.txt file.
#
# - Save the script and make a note of its location (absolute path)
# for future reference.
#
# - Note: Both Python 2 and Python 3 are installed on the Linux Host.
# It is recommended to use Python 3. To run a Python script
# using version 3, run the following command by replacing file.py
# with your file name.
#
# prime numbers:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
# 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
# 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
# 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
# 257, 263, 269, 271, 277, 281, 283, 293.
# """
#

def checkPrime(number):
    if number < 2:
        return False
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True

#test function() for new checking of prime numbers
# def checkPrime(number):
#     prime = True
#     for num in range(2, number):
#         if (number%num == 0):
#             prime = False



def createPrimeNum(startNum, endNum):
    displayPrime = [num for num in range(startingNumber, endingNumber + 1) if checkPrime(num)]
    return displayPrime


def saveAsTxtFile(primes, filename='test1-results.txt'):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')


# define the range of prime numbers
startingNumber = 1
endingNumber = 250

# generate prime numbers
generatePrimeNumbers = createPrimeNum(startingNumber, endingNumber)

# save the prime numbers in a .txt file
saveAsTxtFile(generatePrimeNumbers)

# display this to verify if working
print(f'Prime numbers ranging from {startingNumber} to {endingNumber} are generated! ')
print(f'It is saved to results.txt')
# print(f"Prime numbers from {start} to {end} have been saved to results.txt.")


'''
2	3	5	7	11	13	17	19	23
29	31	37	41	43	47	53	59	61	67
71	73	79	83	89	97	101	103	107	109
113	127	131	137	139	149	151	157	163	167
173	179	181	191	193	197	199	211	223	227
229	233	239	241
'''