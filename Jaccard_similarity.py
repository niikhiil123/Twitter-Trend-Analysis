import numpy as np
import matplotlib.pyplot as plt

import re
from string import punctuation

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

def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    a=(float)(len(intersection))
    b=(float)(len(union))
    return (a/b)


def get_scores(group,tweets):
    scores = []
    for tweet in tweets:
        s = jaccard_similarity(group, tweet)
        scores.append(s)
    return scores

economy_list=0
a=0
social_list=0
b=0
culture_list=0
c=0
health_list=0
d=0

token_economy=economy_related_words.split()
token_social=social_related_words.split()
token_culture=culture_related_words.split()
token_health=health_related_words.split()

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
    
    #print(s)

    s=s.split()

    a=jaccard_similarity(token_economy,s)
    b=jaccard_similarity(token_social,s)
    c=jaccard_similarity(token_culture,s)
    d=jaccard_similarity(token_health,s)

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

s1="hello world".split()
s2="hello a b world".split()

e=jaccard_similarity(s1,s2)
print("Jaccard Similarity")
# print("\nJaccard similarity:",e)

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

