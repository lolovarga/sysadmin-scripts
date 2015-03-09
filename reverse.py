def reverse_string(s):
    return s[::-1]

def reverse_sentence(s):
    words = s.split(' ')
    return ' '.join(reversed(words))

'asdf' == reverse_string('fdsa')
s = 'The quick brown fox jumped over the lazy dog.'
'dog. lazy the over jumped fox brown quick The' == reverse_sentence(s)
