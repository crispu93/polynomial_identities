import math # isclose
import random # randint(a,b)
import time
from decimal import *

"""
def read_input():
    canonical = [int(x) for x in input().split()]
    product = [int(x) for x in input().split()]
    return canonical,product
"""

def generate_random_test(degree, num_tests):
    """ Generate canonical and product representation of polynomials
    and save them in a file. All numbers are integers between -20 and 20
    """
    f = open("test_cases.txt", "w") #overwrite any existing content
    for i in range(num_tests):
        can = [random.randint(-20,20) for x in range(degree+1) ]
        
        sign = [-1,1]
        prod = [random.randint(-20,20) for x in range(degree)]
        random.shuffle(sign)
        prod.insert(0,sign[0])
        
        s_can = ' '.join([str(x) for x in can])
        s_prod = ' '.join([str(x) for x in prod])
        f.write(s_can+"\n")
        f.write(s_prod+"\n")
    f.close()
    return 0

def read_input(file_name):
    """ Read test cases file and return 
    two arrays with the canonical and product 
    form of each test respectively 
    """
    f = open(file_name,"r")
    lines = [line.rstrip('\n') for line in f]
    i=0
    c = []
    p = []
    for line in lines:
        if i%2 == 0:
            c.append([float(x) for x in line.split()])
        else:
            p.append([float(x) for x in line.split()])
        i+=1
    return c,p


def evaluate_canonical(num, cform):
    sum = 0
    for i in range(0, len(cform)):
        sum += (cform[i]*(num)**i)
    return sum

def evaluate_product(num, pform):
    prod = pform[0]
    for i in range(1, len(pform)):
        prod *= (num + pform[i])
    return prod

def rand_polynomial_id(cform, pform):
    r = random.randint(1, 100*len(pform)-1)
    cr = evaluate_canonical(r, cform) 
    pr = evaluate_product(r, pform) 

    return math.isclose(cr,pr)

def kth_rand_polynomial(cform, pform, k):
    """ select at most k random numbers to see 
        if polynomials are the same
    """
    while k and rand_polynomial_id(cform, pform):
        k-=1
    if k==0:
        return True
    else:
        return False

def test_cases(cforms, pforms, max_tests):
    for i in range(len(cforms)):
        cform = cforms[i]
        pform = pforms[i]

        if kth_rand_polynomial(cform, pform, max_tests):
            print(i+1, ") Polynomials are equal")
        else:
            print(i+1, ") Polynomials are different")

if __name__ == '__main__':
    """Generate test cases in the file test_cases.txt
    
    num_tests = 1000
    pol_degree = 70
    generate_random_test(pol_degree, num_tests)
    """
    file_name = "test_cases.txt"
    cforms,pforms = read_input(file_name)
    num_tests = len(cforms)
    pol_degree = len(cforms[0]) 
    max_tests = pol_degree   # Max number of times that evaluates each polynomial
    t1 = time.clock()
    test_cases(cforms, pforms, max_tests)
    print("El tiempo total con", num_tests, "casos es", time.clock()-t1, "seg")