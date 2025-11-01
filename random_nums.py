from time import time_ns

def ruler_nums(
        len_ruler: int # сколько чисел сгененерировать
        # order: bool # сгенерировать числа в порядке (True) или сгенерировать числа в случайном порядке (False)
    ):
    seed = time_ns()

    fifty_percent_from_seed = seed / 2 # 50% от суммы (seed)

    # --защита (усложняем)--
    one = seed - fifty_percent_from_seed
    # -----
    if len_ruler > len(str(one))-2:
        return "ошибка, [ len_ruler > len(str(one)) (True) ] вы не можете поставить длину числа больше чем длина которая получилась в переменной result."

    else:
        if len_ruler <= one:
            total = int(one) ^ seed

            return str(total)[0:len_ruler]
        else:
            return "ошибка, [ len_ruler <= one (False) ] вы не можете поставить длину числа больше чем длина которая получилась в result"

# тест (успешный)
# for i in range(1, 51):
#     print(f"{i} - {ruler_nums(i)}")
