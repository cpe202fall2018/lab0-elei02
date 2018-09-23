def weight_on_planets():
   # write your code here
   print ("What do you weigh on earth? ", end='')
   age = input()
   weightOnMars = 0.38 * double(age)
   weightOnJupiter = 2.34 * double(age)
   print("On Mars you would weigh ", weightOnMars, " pounds.")
   print("On Jupiter you would weigh ", weightOnJupiter, " pounds.")
   
if __name__ == '__main__':
   weight_on_planets()
