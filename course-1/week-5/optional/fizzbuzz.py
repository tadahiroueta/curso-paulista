def fizzbuzz(x):
    if x%3==0:
        if x%5==0:
            return ("FizzBuzz")
        return("Fizz")
    if x%5==0:
        return ("Buzz")
    return x
