'''Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0'''


def longest_palindrome (s):

    """Return list with all palindrome strings within text.

    The base of this algorithm is to start with a given character,
    and then see if the surrounding characters are equal. If they
    are equal then it's a palindrome and is added to results set,
    extend to check if the next character on either side is equal, 
    adding to set if equal, and breaking out of loop if not.

    This needs to be repeated twice, once for palindromes of 
    odd lengths, and once for palindromes of an even length."""


    if(len(s) == 0):
        return 0
    results = set()
    string_length = len(s)
    for i, char in enumerate(s):

        # Check for longest odd palindrome(s)
        start, end = i-1, i+1
        while start >=0 and end < string_length and s[start] == s[end]:
            results.add(s[start:end+1])
            start -= 1
            end += 1

        # Check for longest even palindrome(s)
        start, end = i, i + 1
        while start >= 0 and end < string_length and s[start] == s[end]:
            results.add(s[start:end+1])
            start -= 1
            end += 1

    lst = sorted(list(results), key=len)
    if(len(lst) == 0):
        return 1
    else:
        return len(lst[-1])




'''def longest_palindrome (s):
    longest = 0
    for left in xrange(len(s)):
        for right in xrange(len(s), left, -1):
            if s[left:right] in (s[left:right])[::-1]:
                longest = max(right-left, longest)
                break
    return longest'''




'''def longest_palindrome(s):
    """Manacher algorithm - Complexity O(n)"""
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range (1, n - 1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return maxLen'''