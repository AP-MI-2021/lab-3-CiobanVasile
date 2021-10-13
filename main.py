from typing import List

def arata_meniu():
    print('1. Citire lista')
    print('2. Afisare cea mai lunga subsecventa cu toate numerele prime')
    print('3. Afisare cea mai lunga subsecventa cu toate numerele care au cifrele prime')
    print('4. Afisare cea mai lunga subsecventa cu toate numerele neprime')
    print('x. Quit')


def citire_list() -> List[int]:
    list = []
    list_str = input('Cititi numerele separate printr-un spatiu:')
    list_str_split = list_str.split(' ')
    for num_str in list_str_split:
        list.append(int(num_str))
    return list


def is_prime(n: int) -> bool:
    '''
    (Am folosit subprogramul aratat de dumneavoastra la seminar)
    Determina daca un numar dat este prim.
    Input:
    -Un numar intreg n,natural
    Output:
    -True daca n este prim,false contrar
    '''
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

def is_digit_prime(n: int) ->bool:
    '''
    Determina daca un numar are toate cifrele prime
    Input:
    -un numar intreg n,pozitiv
    Output:
    True daca n are cifrele prime,false contrar
    '''
    while n > 0:
        if is_prime(n%10) == False:
            return False
        n = n//10
    return True


def get_longest_all_primes(lst: list[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate elementele sunt numere prime.
    Input:
    - O lista de numere intregi,strict pozitive
    Output:
    - Cea mai lunga subsevcenta de numere prime, printr-o lista
    '''

    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            all_prime = True
            for numar in lst[st:dr+1]:
                if is_prime(numar) == False:
                    all_prime = False
                    break
            if all_prime == True:
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result

def get_longest_all_not_prime(lst: list[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa in care toate numerel sunt neprime
    Input:
    -O lista de numere intregi, naturale
    Output:
    -Cea mai lunga subsecventa de numere care sunt neprime,returnata printr-o lista
    '''
    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            all_non_prime = True
            for numar in lst[st:dr + 1]:
                if is_prime(numar) == True:
                    all_non_prime = False
                    break
            if all_non_prime == True:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def get_longest_prime_digits(lst: list[int]) -> List[int]:
    '''
        Determina cea mai lunga subsecventa in care toate numerele au cifrele prime.
        Input:
        - O lista de numere intregi,strict pozitive
        Output:
        - Cea mai lunga subsevcenta de numere care au cifrele prime ,printr-o lista
        '''

    lungime = len(lst)
    result = []
    for st in range(lungime):
        for dr in range(st, lungime):
            all_digit_prime = True
            for numar in lst[st:dr + 1]:
                if is_digit_prime(numar) == False:
                    all_digit_prime = False
                    break
            if all_digit_prime == True:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_is_prime():
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(18) == False
    assert is_prime(23) == True


def test_get_longest_all_primes():
    assert get_longest_all_primes([1,2,2,2,2,4]) == [2,2,2,2]
    assert get_longest_all_primes([1,2,3,5,4]) == [2,3,5]
    assert get_longest_all_primes([12,4,6,8,10]) == []
    assert get_longest_all_primes([10,11,13,17,19,20]) == [11,13,17,19]

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([222,333,444,555,777,222,333]) == [555,777,222,333]
    assert get_longest_prime_digits([44,44,22,22,22,66,55,33]) == [22,22,22]
    assert get_longest_prime_digits([333,333,444,222,222,555,888]) == [222,222,555]

def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([1,2,3,4,6])==[4,6]
    assert get_longest_all_not_prime([2,2,2,4,4,2,2,2,4,4,4])==[4,4,4]
    assert get_longest_all_not_prime([5,5,5,6,6,5,6,5,6,6,6,5,6,6,6,6])==[6,6,6,6]

def test_is_digit_prime():
    assert is_digit_prime(2222) == True
    assert is_digit_prime(12345) == False
    assert is_digit_prime(4689) == False
    assert is_digit_prime(357) == True

def main():
    list = []
    while True:
        arata_meniu()
        option = input('Alegerea dumneavoastra: ')
        if option == '1':
            list = citire_list()
        elif option == '2':
            print('Cea mai lunga subsecventa cu toate numerele prime:', get_longest_all_primes(list))
        elif option == '3':
            print("Cea mai lunga subsecventa cu toate numerele care au cifrele prime este:", get_longest_prime_digits(list))
        elif option == '4':
            print("Cea mai lunga subsecventa cu toate numerele neprime:",get_longest_all_not_prime(list))
        elif option == 'x':
            break
        else:
            print('Alegere invalida.')


if __name__ == '__main__':
    test_get_longest_prime_digits()
    test_get_longest_all_primes()
    test_get_longest_all_not_prime()
    test_is_prime()
    test_is_digit_prime()
    main()