class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        # Якщо сегмент ще не має пари, ініціалізуємо список
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            # Якщо ключ вже існує, оновлюємо значення
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # Інакше додаємо нову пару
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """Видаляє пару (ключ, значення) з хеш-таблиці."""
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for i, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    self.table[key_hash].pop(i)  # Видаляємо пару
                    return True
        return False  # Ключ не знайдено

# Приклад використання
ht = HashTable(10)
ht.insert('apple', 100)
ht.insert('banana', 200)
print(ht.get('apple'))  # 100
ht.delete('apple')
print(ht.get('apple'))  # None
