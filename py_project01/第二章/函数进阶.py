def  main(**kwargs):
    print(kwargs.get('a'))
    if kwargs.get('a'):
        print('a')

main()