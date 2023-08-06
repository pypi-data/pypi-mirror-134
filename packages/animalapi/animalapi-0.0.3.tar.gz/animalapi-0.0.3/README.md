<h1 align="center"> Animalapi </h1>
<p align="center">Animal-api wrapper || <a href="https://discord.gg/4cNJxWAGFA"> Official Discord Server </a></p>
<p align="center">
================================

#### pip install animalapi

## Randomized Animal data

```Python
import animalapi as a
data = a.rand_animals()
img = data["image"]
fact = data["fact"]

```

## Specific animal data

```Python
import animalapi as a
data = a.animal_data("dog")
img = data["image"]
fact = data["fact"]
print(img)
print(fact)

```

> Currently this package supports these animals:- ["dog","cat","panda","fox","kangaroo","raccoon","bird","red_panda","koala"]
