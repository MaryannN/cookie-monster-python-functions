# Define your functions here

# 1. Define a function that returns the string "GET BACK ON YOUR DIET!" if Cookie Monster has eaten any cookies.
#    If he has eaten zero cookies, return the string "Good job, Cookie Monster."

# def perfect_day(cookies):
#   if cookies > 0:
#     return "GET BACK ON YOUR DIET!"
#   elif cookies == 0:
#    return "Good job, Cookie Monster."
# print(perfect_day(1))
# print(perfect_day(0))


# 2. Not every day can be a perfect day. Let's write a function for a good_day of dieting.
#    If Cookie Monster has eaten fewer than three cookies, it should return a string that congratulates him.
#    If Cookie Monster has eaten exactly three cookies, let's return a string telling him to stop now.
#    If Cookie Monster has eaten more than three cookies, let's return a string scolding him for eating too many.

# def good_day(cookies):
#   if cookies > 3:
#     return "You ate too many!"
#   elif cookies == 3:
#     return "STOP"
#   else:
#     return "Good Job! You ate less than 3 cookies"
# print (good_day(2))

# 3. The longer Cookie Monster is on this diet, the more we feel we can trust him. Let's write a flex_day function.
#    Let's write a function that takes in two arguments - a goal number of cookies and current number of cookies.
#    It will do the same as the previous function did, so calling flex_day(2, 3) should return a scolding string, since he ate one more than his goal.

# def flex_day(goal, cookies):
#   if goal > cookies:
#     return "Good Job!"
#   elif cookies == goal:
#     return "You're right on goal"
#   else:
#     return "Noo, thats too many!"
# print (flex_day(2, 3))
# print (flex_day(2, 2))

# 4. CHALLENGE: Dieting isn't all about cutting out unhealthy foods; it's also about balance.
#    Let's define a function called balanced_diet that takes in two arguments - a number of cookies and a number of vegetables.

#order matters lol
def balanced_diet(cookies, veggies):
  # If Cookie Monster has eaten some vegetables and NO cookies, give him a special congratulations.
  if cookies == 0 and veggies > 0: 
    return "Wow! You ate no cookies and some veggies!!!"
  # If Cookie Monster has eaten no vegetables and no cookies, encourage him to eat something - preferrably a vegetable.
  elif cookies == 0 and veggies == 0: 
    return "Please Please Please eat something, maybe some veggies"
  # If Cookie Monster has eaten more cookies than vegetables, tell him to get back on his diet.
  elif cookies > veggies: 
    return "GET BACK ON YOUR DIET!"
  # If Cookie Monster has eaten the same amount of each, warn him that he should eat a vegetable next.
  elif cookies == veggies: 
    return "Make sure to eat a veggie next!"
  # If Cookie Monster has eaten more vegetables than he has cookies, congratulate him!
  elif veggies > cookies: 
    return "Good job eating more veggies!"

print(balanced_diet(10, 1))
print(balanced_diet(5, 5))
print(balanced_diet(2, 10))
print(balanced_diet(0, 0))
print(balanced_diet(0, 1))

