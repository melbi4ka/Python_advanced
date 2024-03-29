def palindrome(word, n):
    if n == len(word) // 2:
        return f"{word} is a palindrome"

    left = word[n]
    right = word[len(word)-n-1]

    if left != right:
        return f"{word} is not a palindrome"

    return palindrome(word, n+1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
