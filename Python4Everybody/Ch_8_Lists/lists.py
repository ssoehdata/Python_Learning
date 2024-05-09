# lists are mutable

lotto = [2,14,26,41,63]
print("Lotto list:",lotto)
lotto[2] = 28
print("changing a value in lotto:",lotto)


# can concatenate lists 

winner = [1,2, 66]
print(winner)

d = lotto + winner

print("Concatenating list lotto and  winner:", d)