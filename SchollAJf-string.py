#makes variables for pet name, type, and pronoun
pet_type="dog"
pet_pronoun="his"
pet_name="winston"
#prints the variables inti a sentence
print(f"I have a {pet_type} and {pet_pronoun} name is {pet_name}.")
#asks your Name and makes it a variable
name=input("Enter your first name: ")
#asks your age and makes it a variable
age=int(input("Enter your age: "))
#asks your yearly savings and makes it a variable
savings=int(input("Enter your yearly savings: "))
#tells you your current age and how old you'll be in 10 years, and how much you will have saved in 5 years and monthly savings
print(f"Hello {name}! You are currently {age} years old. In 10 years you will be {age+10}. If you save ${savings} each year, in five years you will have saved ${savings*5}. Your average monthly savings is ${savings/12}.")
#makes a variable for number of days
days=int(31)
#tells you number of seconds in January
print(f"The number of seconds in January is {days*24*60*60}")
#asks you to enter a number of eggs then makes that a variable
eggs=int(input("Enter the number of eggs: "))
#gives you how many dozens of eggs you have and how many are left over
print(f"This makes {eggs//12} dozen eggs with {eggs%12} left over.")