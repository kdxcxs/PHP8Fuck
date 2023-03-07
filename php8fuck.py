s      = "('['^'(')"
t      = "(')'^']')"
r      = "('['^')')"
q      = "(','^']')"
p      = "('.'^'^')"
strstr = ".".join([s, t, r, s, t, r])
sqrt   = ".".join([s, q, r, t])
s_zero = f"(({sqrt})(({strstr})('.',',')).'')"
n      = f"('^'^{s_zero})"
strspn = ".".join([s, t, r, s, p, n])
num    = lambda x:f"({strspn})('{'.' * x}','.')"
c      = f"('['^{num(8)}.'')"
h      = f"('['^{num(3)}.'')"
phpchr = lambda x:f"({'.'.join([c, h, r])})({num(ord(x))})"
phpstr = lambda s:'.'.join([phpchr(c) for c in s])

if __name__ == "__main__":
    print(f"({phpstr('phpinfo')})()")
