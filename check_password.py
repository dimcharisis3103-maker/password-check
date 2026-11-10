def check_password():
   while True:
        x = input('Δώσε κωδικό: ')
        d1 = False
        d2 = False
        d3 = False
        if len(x) >= 8:
            d1 = True
        for ch in x:
            if ch.isdigit():
                d2 = True
            if ch.isupper():
                d3 = True
        if d1 and d2 and d3:
            print('Κωδικός αποδεκτός')
            break
        else:
            if d1:
                print('[✓] Ο κωδικός πρέπει να έχει τοθλάχιστον 8 χαρακτήρες')
            else:
                print('[X] Ο κωδικός πρέπει να έχει τοθλάχιστον χαρακτήρες')
            if d2:
                print('[✓] Ο κωδικός πρέπει να περιέχει τουλάχιστον ένα ψηφίο')
            else:
                print('[X] Ο κωδικός πρέπει να περιέχει τουλάχιστον ένα ψηφίο')
            if d3:
                print('[✓] Ο κωδικός πρέπει να περιέχει τουλάχιστον έναν κεφαλαίο χαρακτήρα')
            else:
                print('[X] Ο κωδικός πρέπει να περιέχει τουλάχιστον έναν κεφαλαίο χαρακτήρα')
check_password()
               