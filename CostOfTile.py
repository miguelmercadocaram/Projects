    
def ask():
        width = float(input('Please enter the width: '))
        height = float(input('Please enter the height: '))
        cost = float(input('Please enter the cost per meter: '))

        return width, height, cost


def main():
    a,b,c = ask()

    #old -> print("The cost is: %.2f " % (float(a * b * c)))
    print('The cost is: {0:.2f}'.format(float(a*b*c)))

if __name__ == '__main__':
    main()