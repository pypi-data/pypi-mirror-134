import sciris as sc

fn, ln = sc.getcaller(frame=1, tostring=False).values()
print(fn, ln)
print(sc.loadtext(fn).splitlines()[ln]) # See the line that called this function