#SELF REFLECTION QUESTIONS

#1. The first bug I saw was the missing colon at the end of the second for loop header 
#I saw it while reading through the script from top to bottom because it would cause a Syntax Wrror 
#It showed me that even 1 thing can majorly through off the code running fully 

#2. apply_discount(price,tier) takes the original price of the item and applies the membership tier
#It applies the 15% for gold, 10% for silver, and 5% for bronze or then no discount for under that.
#Someone could use this function without reading its code by giving it the origional price and the 
#memebership tier. it returns the discounted price 

#3. AI, I used ChatGPT on exercise 5 to tell me what the error means in the code, but I noticed some of the issues 
#based on past assignments and things we have talked about in class such as missing the colan. I 
#also Claude to double check a code line because one of my indents was off which was throwing off the prints


#Exercise 1 

def calculate_tax(price, rate):
    return price * rate 

#Calling the fuction 
tax1 = calculate_tax (100, 0.07)
tax2 = calculate_tax (250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150,0.05):.2f}")

#Exercise 2 

def apply_discount(price, tier):
    if tier == "gold": 
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers  = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print (f"{tier}: ${apply_discount(price, tier):.2f}")


#Exercise 3

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

#The loop used total = sale which replaced the total 
# each time and overrode it. total += adds each sale to the running total 

total = 0
for sale in sales:
    total += sale
    print(f"[Trace] current sale: {sale}, updated total: {total}") 

print(f"Total: {total}")

#The original for sale in sales statement is missing the : 
#which is needed before the loop 
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

#The original condition <= which had invalid index
# but using the < stops the loop before the i reaches the length of the list
i = 0
while i < len(sales):
    print(f"[Trace] current index i = {i}, total elements = {len(sales)}")
    print(sales[i])
    i += 1

#Exercise 6 
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # the global variable so 100 prints here 
print(double_it()) # 1998 prints here because it is using the double it with the 999 as the x 
print(x)           # it is using the first x global value so it prints 100 

#The x inside the function is the local variable so it only applies to the inside 
# double_it. It doesn't change the global x outside of the function which stays constant at 100
