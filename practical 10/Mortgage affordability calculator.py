def evaluate (house_value,annual_salary): #Define a function 'evaluate' that has two input values, the first for housing prices and the second for annual income
    if 5*annual_salary-house_value >0: #Use if statements to verify compliance with the fivefold standard
        print ("Yes")
    else:
        print ("No")
evaluate(67000,16000) #Call the function to obtain the output value, which can also be changed, and the output value will also change accordingly
