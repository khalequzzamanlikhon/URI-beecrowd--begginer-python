inn=int(input())
fst=['I','II','III','IV','V','VI','VII','VIII','IX']
snd=['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
trd=['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
converted=[]
f=inn%10
if f>0:
    converted.append(fst[f - 1])
inn =int(inn/10)
s=inn%10
if s>0:
    converted.append(snd[s-1])
inn=int(inn/10)
t=inn%10
if t>0:
    converted.append(trd[t - 1])
for x in converted[::-1]:
    print(x,end='')
print("")