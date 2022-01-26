import sys
import re

def q2941():
    ss = sys.stdin.readline().strip()
    result = re.sub("c=|c-|dz=|d-|lj|nj|s=|z=", "0", ss)
    print(len(result))
    
q2941()