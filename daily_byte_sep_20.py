"""
link - mailing list( @thedailybyte )

Stattement - This question is asked by Amazon. Given two strings representing sentences, 
                return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). 
                You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...
    sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]   
    sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
    sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
"""
#idea = union(string1,string2) - and((string1,string2)

def uncommon(string1,string2):
    string1 = list(dict().fromkeys(string1.split()))
    string2 = list(dict().fromkeys(string2.split()))
    dictionary = {}
    dictionary = dictionary.fromkeys(string1,1)
    for i in string2:
        if i in dictionary:
            dictionary[i] -= 1
        else:
            dictionary[i] = dictionary.get(i, 0) + 1
    output = []
    for key,value in dictionary.items():
        if value > 0:
            output.append(key)
    return output



string1 =    "the tortoise beat the haire"   
string2 = "the tortoise lost to the haire"

print(uncommon(string1,string2))