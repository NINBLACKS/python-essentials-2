"""
You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -- everytime 
you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block for each letter (direction) and 
you know it takes you one minute to traverse one city block, so create a function that will return true 
if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, 
of course, return you to your starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
    It will never give you an empty array (that's not a walk, that's standing still!).
"""
walk = ['n', 'w', 'e', 's', 'e', 'w', 'n', 'w' 'e', 's']

if len(walk) != 10:
    print('This walk won\'t take you exactly 10 min')
    north = 0
    south = 0
    east = 0
    west = 0
    for i in walk:
        if i == 'n':
            north += 1
            print('There\'s a north')
        elif i == 's':
            south += 1
            print('There\'s a south')
        elif i == 'e':
            east += 1
            print('There\'s an east')
        elif i == 'w':
            west += 1
        print('There\'s a west')
    print('norths=', north)
    print('souths=', south)
    print('easts=', east)
    print('wests=', west)
    if south - north == 0 and west - east == 0:
        print('youll get to the starting point')
    else:
        print('youll get late to you appointment')
"""else:
    print('This walk will take you 10 min')
    fhalf = walk[:5]
    lhalf = walk[5:]
    print(fhalf)
    lhalf.reverse()
    print(lhalf)
    opposites = {'n': 's', 'w': 'e', 's': 'n', 'e': 'w'}
    for i in range(5):
        if opposites[fhalf[i]] != lhalf[i]:
            print('You won\'t return on time')
        else:
            print('You will return in time')
"""
