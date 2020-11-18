from sklearn import tree

semen = 0
besi = 1
kg = 0
pcs = 1

tipe = [[20, 1],[30, 1],[50, 0],[90, 0]]
varian = [0, 0, 1, 1]
reaksi= tree.DecisionTreeClassifier()
reaksi= reaksi.fit(tipe, varian)

print('Klasifikasi bangunan maju harapan')
a = input('Berapa kilogram? : ')
b = input('\njenis yang dipilih \nkg atau pcs : ')

jawab = int(a)
if b.lower() == 'kg':
    tk = 0
elif b.lower() == 'pcs':
    tk = 1
else:
    print('Unknown')

c = reaksi.predict([[jawab, tk]])
if c == 0:
    d = 'semen'
else:
    d = 'besi'

print('Berikut pilihan yang anda masukan : {}'.format(d))


