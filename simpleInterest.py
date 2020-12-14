# Compute simple interest for the user inputs p, n and r
#!/usr/bin/python

def calculate_simple_interest(p, n, r):
    si = 0.0
    si = float(p*n*r)/float(100);
    return si;

if __name__ == '__main__':
    p = 25000.00;
    n = 60;
    r = 4.9;
    simple_interest = calculate_simple_interest(p, n, r);
    print("Simple interest value: %.2f" % simple_interest);
