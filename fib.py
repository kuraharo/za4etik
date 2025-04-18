def fibonacci(chislo_iterov):
    chislo_odin=0
    chislo_dva=1
    for i in range(chislo_iterov):
        yield chislo_odin
        chislo_odin, chislo_dva=chislo_dva,chislo_odin+chislo_dva

for num in fibonacci(6):
    print(num)