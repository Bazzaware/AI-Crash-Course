import numpy as np

conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000
d = len(conversionRates)
X = np.zeros((N,d))

for row in range(d):
   for cell in range(d):
       if np.random.rand() < conversionRates[cell]:
            X[row][cell] = 1


# Holds the results of our losses and wins.
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

#  Iterrates through each row in results array
for i in range(N):
    selected = 0
    maxRandom = 0

# Thompson Sampling Model
# With a selected row from results selects cell 0 to 4
    for j in range(d):

        randomBeata = np.random.beta(nPosReward[j] + 1, nNegReward[j] +1 )
        if randomBeata > maxRandom:
            maxRandom = randomBeata
            selected = j

    if X[i] [selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

nSelected = nPosReward + nNegReward
for i in range(d):
    print('Machine number ' + str(i + 1) + ' was selected ' + str( nSelected[i]) + ' times.')

print('Conclusion: Best machine is ' +  str(np.argmax(nSelected) + 1 ))
