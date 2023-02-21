def count(name):
    vowel = 0
    consonent = 0
    for i in range(len(name)):
        if name[i] in ['a','e','i','o','u']:
            vowel = vowel+1
        else:
            consonent = consonent+1
    print("count of vowel is",vowel)
    print("count of consonent is",consonent)
a = input("enter the name")
count(a)