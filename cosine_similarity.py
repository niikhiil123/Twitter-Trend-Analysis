import numpy as np
import matplotlib.pyplot as plt

import re
import math
import string
from string import punctuation
import collections
from collections import Counter

file=open("economy.txt")
economy_related_words = file.read()
file.close()

file=open("social.txt")
social_related_words = file.read()
file.close()

file=open("culture.txt")
culture_related_words  = file.read()
file.close()

file=open("health.txt")
health_related_words =file.read()
file.close()

economy_list=0
a=0
social_list=0
b=0
culture_list=0
c=0
health_list=0
d=0

WORD = re.compile(r"\w+")

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

    
token_economy=vector1 = text_to_vector(economy_related_words)
token_social=text_to_vector(social_related_words)
token_culture=text_to_vector(culture_related_words)
token_health=text_to_vector(health_related_words)

file=open('Tweet.txt','r')
lines=file.readlines()

c=0

for line in lines:
    c+=1
    s=line.strip()

    s=s.lower()
    s=re.sub('['+punctuation+']+','',s)
    s=re.sub('([0-9]+)','',s)


    s=re.sub(r'[^\w\s]','',s)
    s=re.sub(r'http\S+','',s)
    s=re.sub(r'bit.ly/\S+','',s)
    s=re.sub(r'http\S+','',s)
    s=s.strip('[link]')

    s=re.sub('(RT[A-Za-z]+[A-Za-z0-9-_]+)','',s)
    s=re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)','',s)
    s=re.sub('(#[A-Za-z]+[A-Za-z0-9-_]+)','',s)
    
    s=text_to_vector(s)

    a=get_cosine(token_economy,s)
    b=get_cosine(token_social,s)
    c=get_cosine(token_culture,s)
    d=get_cosine(token_health,s)

    if a!=0 or b!=0 or c!=0 or d!=0:
        if a>b and a>c and a>d:
            economy_list=economy_list+1
        if b>a and b>c and b>d:
            social_list=social_list+1
        if c>a and c>b and c>d:
            culture_list=culture_list+1
        if d>a and d>b and d>c:
            health_list=health_list+1

file.close()

s1="hello world"
s2="hello a b world"

vector1 = text_to_vector(s1)
vector2 = text_to_vector(s2)
cosine = get_cosine(vector1, vector2)

print("Cosine Similarity")

# print("\nCosine similarity: ", cosine)

ep=float(economy_list)/float((economy_list+social_list+culture_list+health_list))
ep=ep*100
sp=float(social_list)/float((economy_list+social_list+culture_list+health_list))
sp=sp*100
cp=float(culture_list)/float((economy_list+social_list+culture_list+health_list))
cp=cp*100
hp=float(health_list)/float((economy_list+social_list+culture_list+health_list))
hp=hp*100

print("\nPercentage: ")


print("Economy: ",ep)
print("Social: ",sp)
print("Culture: ",cp)
print("Health: ",hp)

tweets = ['Economy','Social','Culture','Health']
data = [ep,sp,cp,hp]

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(data, labels=tweets, autopct='%.1f%%')
ax.set_title('Trend Analysis')
plt.show()
