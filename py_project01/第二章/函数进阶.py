import utils.tools

def  main(**kwargs):
    print(kwargs.get('a'))
    if kwargs.get('a'):
        print('a')

main()

area = utils.tools.calc_circle_area(5)
print(area)

# if __name__ == "__main__":



    