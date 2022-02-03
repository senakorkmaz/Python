while True:
    try:
        x = int(input('x:'))
        y = int(input('y: '))
        print(x/y)
    except Exception as e:
        print('Hata!!:',e)

    else:
        break
    finally:
        print('try except sonlandi.')
        