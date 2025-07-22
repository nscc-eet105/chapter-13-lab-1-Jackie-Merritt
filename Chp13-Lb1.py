#Jackie-Merritt_Chp13-Lab1_7/20/2025

total = []
def main():
    print('Repeater Program\n')
    character = input('What character would you like to repeat? ')
    amount = int(input(f"How many {character}'s would you like?: "))
    repeat(amount, character)
    print(''.join(total))

def repeat(amount, character):
    if amount == 0:
        return amount
    else:
        total.append(character)
        return amount + repeat(amount - 1, character)


    
if __name__ == '__main__':
    main()
    
