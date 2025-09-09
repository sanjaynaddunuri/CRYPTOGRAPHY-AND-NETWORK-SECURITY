def matrix(keyword):
    k = "".join(dict.fromkeys(keyword.upper().replace("J", "I").replace(" ", "")))
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    s = k + "".join([c for c in alpha if c not in k])
    return [list(s[i:i+5]) for i in range(0, 25, 5)]

def digraphs(text):
    t = text.upper().replace("J", "I").replace(" ", "")
    out, i = [], 0
    while i < len(t):
        a = t[i]; b = t[i+1] if i+1 < len(t) else "X"
        if a == b: out.append(a+"X"); i += 1
        else: out.append(a+b); i += 2
    return out

def pos(m, ch):
    for r in range(5):
        for c in range(5):
            if m[r][c] == ch: return r, c

def encrypt(text, m):
    res = ""
    for a,b in digraphs(text):
        r1,c1 = pos(m,a); r2,c2 = pos(m,b)
        if r1 == r2: res += m[r1][(c1+1)%5] + m[r2][(c2+1)%5]
        elif c1 == c2: res += m[(r1+1)%5][c1] + m[(r2+1)%5][c2]
        else: res += m[r1][c2] + m[r2][c1]
    return res

if __name__ == "__main__":
    p = input("Enter plaintext: ")
    k = input("Enter keyword: ")
    print("Encrypted Message:", encrypt(p, matrix(k)))
