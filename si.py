import sys

if len(sys.argv) == 4:
    script_name = sys.argv[0]
    p= int(sys.argv[1])
    r= int(sys.argv[2])
    t=int(sys.argv[3])
else:
    script_name = "simple interest"
    p = 10
    r = 5
    t = 2

si=(p*r*t)/100

print("Simple interest:", si)
