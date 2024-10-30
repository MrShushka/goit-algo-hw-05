import timeit

# Алгоритм Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1

# Алгоритм Боєра-Мура
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return False
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    i = m - 1

    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return True  
            i -= 1
            j -= 1
        i += skip.get(text[i], m)
    return False

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern):
    n, m = len(text), len(pattern)
    p_hash = hash(pattern)
    for i in range(n - m + 1):
        if hash(text[i:i + m]) == p_hash:
            if text[i:i + m] == pattern:
                return True  
    return False


def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def compare_algorithms(text, pattern, non_existing_pattern):
    algorithms = {
        "KMP": lambda: kmp_search(text, pattern),
        "Boyer-Moore": lambda: boyer_moore_search(text, pattern),
        "Rabin-Karp": lambda: rabin_karp_search(text, pattern)
    }

    for name, func in algorithms.items():
        time = timeit.timeit(func, number=10)
        print(f"{name} для існуючого підрядка: {time:.6f} секунд")

    print()

    algorithms_non_existing = {
        "KMP": lambda: kmp_search(text, non_existing_pattern),
        "Boyer-Moore": lambda: boyer_moore_search(text, non_existing_pattern),
        "Rabin-Karp": lambda: rabin_karp_search(text, non_existing_pattern)
    }

    for name, func in algorithms_non_existing.items():
        time = timeit.timeit(func, number=10)
        print(f"{name} для неіснуючого підрядка: {time:.6f} секунд")


def main():
    text1 = load_text('стаття 1.txt')
    text2 = load_text('стаття 2.txt')

    existing_pattern = "алгоритм"
    non_existing_pattern = "немаєтакогослова"

    print("Результати для статті 1:")
    compare_algorithms(text1, existing_pattern, non_existing_pattern)

    print("\nРезультати для статті 2:")
    compare_algorithms(text2, existing_pattern, non_existing_pattern)

if __name__ == "__main__":
    main()