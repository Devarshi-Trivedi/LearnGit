# hello, git learers

## project setup

### so we have three branches,

- featurex -> sum of the even numbers in given range
- featurey -> reverse string
- featureZ -> list operation

### we have folder structure,

- Feature -> all folders about feature inside it
- Feature/FeatureX -> saperate folder for developing FeatureX
- Feature/FeatureY -> saperate folder for developing FeatureY
- Feature/FeatureZ -> saperate folder for developing FeatureZ

- assets -> all common assets are in this folder

### we have file as,

- main.py -> driver file
- feature(c).py -> driver file for perticular feature 

## commit history be like ...

A -> main -> initial commit
B -> main -> modify setup files as per requirement

>B -> main -> [ featurex, featurey, featurez ] create branch

C -> featurex -> add input method
D -> featurey -> add input method
E -> featurez -> add input method

>E -> featurez -> [ subfeaturez ] create branch

F -> featurey -> complete module (with Bug)

G -> featurex -> add calculation mentod for two cases 

>G -> featurex -> [ sol2featurex ] create branch

H -> subfeaturez -> add feature 'clear, push, shift'

I -> sol2featurex -> second solution for feature , add calculation method for two cases

J -> featurex -> add calcuation method for third case, complete

K -> sol2featurex -> add calcuation method for third case, complete

L -> subfeaturez -> add feature 'pop, unshift, insert'

M -> subfeaturez -> add feature 'countdix'

>B -> main -> [ updatereadme ] create branch 

OO -> updatereadme -> update readme.md

N -> subfeaturez -> change arg[ 0 ] to opcode and change related info  



