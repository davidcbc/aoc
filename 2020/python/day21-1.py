f = open(r"2020/python/day21-input.txt", "r")

allergens = {}
ingredients = set()
ingredientCount = {}

for line in f:
    tokens = line.strip().split(" (contains ")
    a = tokens[1].replace(")","").split(", ")
    i = tokens[0].split()
    for allergen in a:
        if allergen in allergens:
            allergens[allergen] = allergens[allergen].intersection(set(i))
        else:
            allergens[allergen] = set(i)
    for ingredient in i:
        if ingredient not in ingredients:
            ingredients.add(ingredient)
            ingredientCount[ingredient] = 1
        else:
            ingredientCount[ingredient] += 1

print(allergens)
print(ingredients)

ingredientsWithAllergens = set()

for i in allergens.values():
    for ingredient in i:
        ingredientsWithAllergens.add(ingredient)

ingredientsWithoutAllergens = ingredients.difference(ingredientsWithAllergens)
print(ingredientsWithoutAllergens)

count = 0
for i in ingredientsWithoutAllergens:
    count += ingredientCount[i]

print(count)


done = False
while not done:
    done = True
    for a in allergens.items():
        if len(a[1]) != 1:
            done = False
            continue
        i = list(a[1])[0]
        for a2 in allergens.items():
            if a[0] == a2[0]:
                continue
            if i in a2[1]:
                a2[1].remove(i)

print(allergens)
sortedAllergens = sorted(allergens.keys())
output = ""
for a in sortedAllergens:
    output += "," + list(allergens[a])[0]
print(output[1:])
