import pylab as pl
import sciris as sc
# import covasim as cv

pl.figure()
pl.plot([1,4,3])

fn ='boo1.svg'
comments = {'ohmy':23, 'boo':'foo'}
sc.savefig(fn, comments=comments, freeze=True)

md = sc.loadmetadata(fn)

sc.pp(md)

# pl.savefig('boo1.jpg', metadata={'ohmy':str(23), 'boo':'foo'})
# metadata = {'ohmy':str(23), 'boo':'foo'}
# sc.savefig('boo1.svg', comments=)

# cv.Sim().run().plot()
# cv.savefig('boo2.png')

# svg = sc.loadtext('boo1.svg').splitlines()
# for line in svg:
#     if 'sciris_metadata' in line:
#         break

# m1p = sc.loadmetadata('boo1.png')
# m1j = sc.loadmetadata('boo1.jpg')
# # m1s = sc.loadmetadata('boo1.svg')
# # m2 = sc.loadmetadata('boo2.png')

# print(m1p)
# print(m1j)
# print(m1s)
# # print(m2)