class FlattenIterator():
    
    def __iter__(self):
        return self

    def __init__(self, list_input):
        self.list_rev = list(reversed(list_input))  #чтобы  использовать pop и вытаскивать по сути первый O(n)
        
    def __next__(self):
        while self.list_rev:
            cur_symbol = self.list_rev.pop() #достаем по сути первый из листа
            is_list = isinstance(cur_symbol, list)
            if is_list: #нашли вложенный список
                self.list_rev.extend(reversed(cur_symbol))  #добавим в конец список который мы нашли
            else:
                return cur_symbol

        raise StopIteration    #выключаем итер при отсутствии элементов в list_rev
    
nested_list = [1, [2, [3, 4], 5], 6]
flat = FlattenIterator(nested_list)
for num in flat:
    print(str(num))