def count_letters(lis):
    countu=0
    count1=0
    for i in lis:
        if i.isupper():
            countu+=1
        elif i.islower():
            count1+=1
        print("No of uppercase characters :",countu)
        print("No of lowercase characters",count1)
string="The quick Brow Fox"
list1=(string)
count_letters(list1)
