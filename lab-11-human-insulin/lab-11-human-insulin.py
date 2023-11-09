# Exercise 1
#import regex module
import re

#specify file paths
originalFile = "/home/ec2-user/environment/lab-11-human-insulin/preproinsulin.txt"
cleanedFile = "/home/ec2-user/environment/lab-11-human-insulin/cleaned-prepro.txt"


# Function to clean the text using regex by importing re module
def stripText(text):
    stripText = re.sub(r'[\d\s\r\n]+|//|ORIGIN', '', text)
    return stripText

# open uncleaned file in read mode
with open(originalFile, 'r') as file:
    # read the content
    data = file.read()

# clean the original file using the function stripText
toCleanData = stripText(data) 
    
# write the cleaned data in the output file
with open(cleanedFile, 'w') as file:
    cleanedData = file.write(toCleanData)
     
print(cleanedData)

#convert explicitly the cleaneData to string and count the characters
numCharacters = len(str(cleanedData))
print(numCharacters) 

# Exercise 2
# confirm number of characters
# preproinsulin_seq_clean = 'malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn'

# print(len(preproinsulin_seq_clean))

# #print amino acids 1-24
# l_insulin = preproinsulin_seq_clean[:24]
# print(l_insulin)
# print(len(l_insulin))

# #print amino acids 1-24
# b_insulin = preproinsulin_seq_clean[24:54]
# print(b_insulin)
