# Step 1. Process input
eq = '4x^2 +4x +    (-8) =  0' 

# User can accidentally put an extra space or omit a space too! 
# We adhere to the idea that replay should be universal
# Remove all spaces in eq string:
eqws = eq.replace(' ', '')

# Remove curved brackets function
def removeCurvedBrackets(str: str):
    return str.replace('(', '').replace(')', '')

# Let's start by extracting a, b, c from user input and storing it to variables.
a = int(removeCurvedBrackets(eqws.split('x^2')[0]))
b = int(removeCurvedBrackets(eqws.split('x+')[0].split('+')[1]))
c = int(removeCurvedBrackets(eqws.split('=0')[0].split('x+')[1]))

print(a, b, c) # 4 4 -8

# Step 2. Calculate answer 

# Now, once we have all the coefficients, let's remind ourselves of the quadratic formula:
# (-b ± (b ** 2 - 4 * a * c)) / (2 * a)
# Let's find x1 and x2!
x1 = int((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
x2 = int((-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))

print(x1, x2) # -2 1