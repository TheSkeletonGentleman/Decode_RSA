"""
Authors:    Nikolic Stefan, Rouiller Cyril, Lapaire Sabrina, Marty Hugo
Project:    Decode RSA
Date:       14.12.2023
File:       program.py
Summary:    Main file for the RSA project
"""

# Imports
import utils as utl

# Public key
n=511636457
e=4493

# Message
messages = [
211183711,
446786007,
357923975,
281749153,
12017582,
23000371,
446786007,
295431008,
23000371,
72571259,
180409797,
403705150,
29559188,
347821675,
87253785,
191661894,
196261151,
446786007,
357923975,
281749153,
335347341,
23000371,
446786007,
295431008,
23000371,
347821675,
118097858,
400315772,
60629211,
117016026,
481113344,
29559188,
85798646,
167404802,
402504809,
85798646,
480199951,
209970459,
313368049,
29229558,
226739394,
482581869,
237652899,
94552886,
406106888,
496773658,
9148111,
377434482,
103906785,
86505617,
263435422,
240270618,
354241201,
282007950,
502503165
]

# For each block, decode it 
def RSA_decode(_n, _e, msg):
    result = []
    d = utl.find_d(_n, _e)
    for block in msg:
        result.append(utl.exponentiation(block, d, n))
    return result

resp = ""

# For each decoded block concat it in rep
for decoded_block in RSA_decode(n,e,messages):
    resp += utl.decodemsg(decoded_block)

# Print rep
print(resp)