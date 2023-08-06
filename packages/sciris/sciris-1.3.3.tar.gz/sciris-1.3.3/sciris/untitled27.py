import sciris as sc

names = [
    'os',
    'sys',
    'pandas',
    'pylab',
    'sciris',
]

a = sc.objdict(defaultdict=sc.autolist)
b = sc.autolist()
c = sc.autolist()

for name in names:
    mod = sc.importbyname(name, output=True)
    attrs = dir(mod)
    for attr in attrs:
        if not attr.startswith('__'):
            a[name] += attr
            if attr not in b:
                b += attr
            else:
                c += attr