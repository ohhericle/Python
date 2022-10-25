""" BISECTION SEARCH """
""" Bisection Search to Find a Square Root """

x = float(input("enter a number:"))

epsilon = 0.00001
num_guesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

# If x is less than 1 ; the square root will always be bigger than x
if x > 1:
    ans = (high + low)/2.0
else:
    ans = 1
while high - low >= 2 * epsilon:
    print("low =",low,"high =", high)
    num_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0

print('Number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)