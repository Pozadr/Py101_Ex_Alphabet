user_decision = 'y'

while user_decision == 'y':
    try:
        step = input('Type step for alphabet printing loop: ')
        step = int(step)
        
    except ValueError:
        print('\nThis is not a valid data. Try again!\n')
        continue

    print('Alphabet in normal order: \n')
    x = 0
    for i in range(65, 91, step):  # range(65,91) -> capital alphabet letters in ASCII 
        letter = chr(i)  # chr(ascii_code) - return string of sign from ascii table
        x += 1
        print(letter, '=>', letter.lower(), ' ', end='')
        if i > 65 and x == 5:  # Every 5 iterations go to the new line '\n'
            x = 0
            print('\n', end='')



    print('\n\nAlphabet in reverse order: \n')
    x = -1 
    for i in range(122, 96, -step):  # range(122,96) -> small alphabet letters in ASCII    letter = chr(i)
        letter = chr(i)
        x +=1
        if x == 5:
            x = 0
            print('\n', end='')
        print(letter.upper(), '=>', letter, end='  ')
        
    user_decision = input("\nOnce again? (y/n)?")
