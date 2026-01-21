#aks for some to enter their name then assigns that input to a variable
name = input('What is your name?')
#says hello and the input
print('Hello ' + name)
#asks for an age then makes that input a variable
age =int(input('What is your age?'))
#prints your age plus 5 years, make sure x is defined as an integer otherwise you will get an error
print('In 5 years you will be', age+5)
#asks user how many years to add to their age then makes it a variable
y=int(input('How many years do you want to add to your age?'))
#prints user age in y years
print('In', str(y), 'years you will be', str(age + y), 'years old')
#asks user for hours worked in a week, then makes it a floating point value and assigns it to a variable
hours = float(input('Enter hours worked: '))
#asks user for their hourly wage, then makes it a floating point value and assigns it to a variable
wage = float(input('Enter your hourly wage, without the $: '))
#prints pay for week
print('Your gross pay this week is $',round(hours*wage, 2))
#prints estimated annual earnings
print('Your estimated annual gross pay is $',round(hours*wage*52, 2))