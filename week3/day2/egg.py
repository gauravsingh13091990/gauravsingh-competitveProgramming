import random


def fut(i):
    co=0
    m=15
    
    n=0
    while(n<i):
        
        l=n
        n=n+m
        
        m  =m-1
        
        co=co+1
        
    if(l==n):
        return co
    co=co+(i-l)
    
    return co

for k in range(1,101):
    print(k,'leds to',fut(k))