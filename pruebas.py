import re
import itertools
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import scipy.integrate as integrate
import scipy as sp
from scipy.stats import norm
from scipy.stats import poisson
from scipy.stats import bernoulli
from typing import Callable



#5.2
def bits_to_string(bit_message: str) -> str:
    unicodes_in_binary = [ bit_message[i:i+8] for i in range(0, len(bit_message), 8) ]
    unicodes = ...
    strings = list(map(chr, unicodes))
    return ''.join(strings)


frase='010010000110111101101100011000010010000001100011011010000110100101100011010000000111001100100001001000000100010101110011011100000110010101110010011011110010000001100101011100110111010011101001011011100010000001100010011010010110010101101110'

lista=['01001000', '01101111', '01101100', '01100001', '00100000', '01100011', '01101000', '01101001', '01100011', '01000000', '01110011', '00100001', '00100000', '01000101', '01110011', '01110000', '01100101', '01110010', '01101111', '00100000', '01100101', '01110011', '01110100', '11101001', '01101110', '00100000', '01100010', '01101001', '01100101', '01101110']

unicodes=(int('0b'+lista[0], 2))
#print(unicodes)
#print(bits_to_string(frase))


a=[ int('0b'+lista[i], 2) for i in range(0, len(lista)) ]
#print(a)
lista=list(map(chr,a))
#print(''.join(lista))


#5.3

t='0000000000'
p=0.2
t_array = np.fromiter(t, dtype=int)
print(t_array)
noise = bernoulli.rvs()
#t_masked = t_array ^ noise # XOR
#r = ''.join(...) 
#print(r)


