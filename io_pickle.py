import pickle
listfile = 'shoplist'
shoplist = ['iphone','ipad','moto','xiaomi']

f = open(listfile,'wb')
pickle.dump(shoplist,f)
f.close()

del shoplist

f = open(listfile,'rb')
list = pickle.load(f)

print(list)