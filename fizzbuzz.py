def fizzbuzz(i):
    if i % 3 == 0:
        if i % 5 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    if i % 5 == 0:
        return "Buzz"
    return str(i)

def fizzbuzz_csv(n):
    s = '"'
    for i in xrange(1, n+1):
        if i == n:
            s = s + "'" + fizzbuzz(i) + "'"
        else:
            s = s + "'" + fizzbuzz(i) + "', "
    s += '"'
    return s
        
        
print fizzbuzz(15) == "FizzBuzz"
print fizzbuzz(3) == "Fizz"
print fizzbuzz(2) == "2"
print fizzbuzz(5) == "Buzz"
s = fizzbuzz_csv(5)
print s
fizzbuzz_csv(5) == s
