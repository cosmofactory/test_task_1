def reverse_string(string_to_reverse: str) -> str:
    chars = list(string_to_reverse)
    left, right = 0, len(chars) - 1

    while left < right:
        # Обмен местами
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


string_to_reverse = "123456abcd"
print(reverse_string(string_to_reverse))
