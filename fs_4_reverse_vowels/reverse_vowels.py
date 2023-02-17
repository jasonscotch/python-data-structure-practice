def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    
    chars = list(s)
    
    vowel_positions = [i for i in range(len(chars)) if chars[i] in vowels]
   
    vowel_positions.reverse()
    
    for i, vowel_pos in enumerate(vowel_positions):
        chars[vowel_pos] = s[vowel_positions[-(i+1)]]
    
    return "".join(chars)