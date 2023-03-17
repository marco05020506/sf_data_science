'''  Угадай число
Компьютер сам загадывает и отгадывает '''

import numpy as np


def random_predict(number: int=1) -> int:
    """ Случайно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        
        if number == predict_number:
            break
    
    return count

print(f'количество попыток {random_predict(23)}')


def score_game(random_predict) -> int:
    """ Среднее количество попыток угадывания из 1_000 подходов

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number)) 
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score
    
if __name__ == '__main__':
    score_game(random_predict) 
    
    
    