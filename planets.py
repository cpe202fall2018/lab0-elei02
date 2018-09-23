def weight_on_planets():
   # write your code here
   print ("What do you weigh on earth? ", end='')
   age = int(input())
   weightOnMars = 0.38 * age
   weightOnJupiter = 2.34 * age
   print("\nOn Mars you would weigh", weightOnMars, "pounds.","\nOn Jupiter you would weigh", weightOnJupiter, "pounds.", end='')
   
if __name__ == '__main__':
   weight_on_planets()
