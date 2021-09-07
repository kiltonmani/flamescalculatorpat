print("\nThis flames calculator assesses and predicts the outcome of a relationship based on an algorithm of two given names.")
print("\nPlease enter the two names you are interested in!\n")
name1 = input("Enter Name 1 : ").lower()
name2 = input("Enter Name 2 : ").lower()
set1 = []  # make list of name1 as set1
count1 = {}  # dict to count occurance of letters of name1
set2 = []  # make list of name1 as set2
count2 = {}  # dict to count occurance of letters of name2
set1.extend(name1)  # add letters of name1 as elements of set1
set2.extend(name2)  # add letters of name1 as elements of set2
for i in "abcedfghijklmnopqrstuvwxyz":
    count1.update({i: (set1.count(i))})  # count occurance of letters of name1 and store it as a dict
for i in "abcedfghijklmnopqrstuvwxyz":
    count2.update({i: (set2.count(i))})  # count occurance of letters of name2 and store it as a dict
count3 = {}  # dict of letters and occurance after cutting common letters
for i in "abcedfghijklmnopqrstuvwxyz":
    count3.update({i: (abs((count1[i]) - (count2[i])))})  # decloccurance after cutting common letters
tot = int()  # flame number
for i in "abcedfghijklmnopqrstuvwxyz":
    tot += count3[i]  # find flames number
flames = ["f", "l", "a", "m", "e", "s"]
flames2 = []
while len(flames) > 1:
    rem = ((tot % (len(flames))) - 1)
    del flames[rem]
    if rem > 0:
        flames2 = flames[rem:] + flames[:rem]
        flames = flames2
    else:
        flames2 = flames
answer=flames[0]
meaning={"f":"Friendship",
         "l":"Love",
         "a":"Affection",
         "m":"Marriage",
         "e":"Enemy",
         "s":"Siblings"}
print("\nThe relationship between",name1.upper(),"and",name2.upper(),"will end in",meaning[answer].upper()+".")
