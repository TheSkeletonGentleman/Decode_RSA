# Notes
Vous pouvez mettre des notes ici :

##### Le code qui était présent dans énnoné court et long
Code int to string (version python)

def decodemsg(M):
    return M.to_bytes((M.bit_length() + 7) // 8, "little").decode("utf-8")

def encode_msg(m):
    m.encode('utf-8')
    tmp = bytes(m, 'utf-8')
    str = int.from_bytes(tmp, "little")
    return str
    
##### RSA
p et q sont des nombres premiers

n = p*q
phi(n) = (p-1)*(q-1)
1 = e * d + phi(n) * y
d = x * mod(phi(n))

pgdc(8, 9) = 1 = (-1) * 8 + 1 * 9
    e = 8
    phi(n) = 9

##### Indicatrice d'Euler
a^phi(n) ≡n 1    ->    si pgdc(a,n) = 1
M = Π^e mod(n)   ->    si pgdc(M,n) = 1
(Π^e mod(n))^d mod(n) ≡n (Π^e)^d = Π^(e*d) = Π^(1-phi(n)*-y')
≡n Π(Π^phi(n) mod(n))^-y'
≡n Π(1^-y') ≡n M

##### Bernstein
si n = p*q alors (Π^e)^d ≡n M  pourtout M < nq

##### Fermat
a^k mod(n) = 1
(n-1)^2k ≡n 1
----A----             ----B----
si p est premier alors a^(p-1) ≡p 1
A -> B oui
B -> A non
mais !B -> !A

test 1: a = 4
4^15-1 ≡15 1

test 2: a = 11
11^15-1 ≡15 1

test 3: a = 3
3^15-1 ≡15 9

donc 15 n'est pas premier

P(négatif avec P pas premier) =~ 1/4
K test nég -> P(être premier) =~ 1-1/4^k

-> on tire aléatoirement un nombre a € [2,p-2]

##### Miller-Rabin
p premier ?
p-1 = 2^s * i
a^i ≡ p 1
a^(2^r * i) ≡p -1