#Q1
'''
def is_Prime(max_num):
    prime=[]
    for num in range(2,max_num + 1):
        isPrime = True
        divisor = range(2, int(num**0.5) + 1)  #testlist for divisor
        for divisors in divisor: #this repeat for the number in range (2,50) to be divide by the numbers in range (2,50)
            if (num % divisors==0):
                isPrime = False
                break
        
        if isPrime:
            prime.append(num)
    
    return prime

def twin_primes(prime_list):
    twin_primes = []

    for item in range(len(prime_list) - 1):
        if prime_list[item + 1] == (prime_list[item] + 2):
            twin_primes.append((prime_list[item], prime_list[item + 1]))
    
    return twin_primes

max_num = 10
prime_max = is_Prime(max_num)
print("All prime num up until 1000:", prime_max)

twin_prime = twin_primes(prime_max)
print("The twin primes up to 1000:",(twin_prime))
'''

#Q2
'''
def find_prime_factors(givennumber):
  prime=[]
  #to find the prime numbers in the range of the givennumber
  for num in range(2,givennumber + 1):
      isPrime = True
      divisor = range(2, int(num**0.5) + 1)  #testlist for divisor
      for divisors in divisor: #this repeat for the number in range (2,50) to be divide by the numbers in range (2,50)
          if (num % divisors==0):
              isPrime = False
              break
        
      if isPrime:
          prime.append(num)

    #find the prime factors using the prime number list
  factor = []
  for prime_num in prime:
    while givennumber % prime_num == 0:
      factor.append(prime_num)
      givennumber //= prime_num

  return factor

original_number = int(input("Enter a number to find its prime factor: "))
prime_factors = find_prime_factors(original_number)
print(f"The prime factors of {original_number} are ",prime_factors)
'''
def pascaltriangle(rows):
  for i in range(rows):
    print(" "* (rows - i), end = "")

    coef = 1
    for j in range(0, i + 1):
      print(coef, end = " ")
      coef = coef * (i-j)//(j+1)
    print()
n = int(input("Rows: "))
pascaltriangle(n)



'''
n = int(input("Enter the row: "))
pascal_triangles = pascal_triangle(n)
print_pascal_triangle(pascal_triangles)'''