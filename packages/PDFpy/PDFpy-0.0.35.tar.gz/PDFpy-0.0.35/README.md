# Examples of How To Use

```python
from PDFpy import PDF

# load two PDFs
a = PDF("example1.pdf")
b = PDF("example2.pdf")

# delete every other page from a
del a[::2]

# delete page 3 4 and 7 from b
del b[[3, 4, 7]]

# replace Page 3 from a with page 5 from b
a[3] = b[5]

# merge the first 10 pages of a with all but the first 13 pages of b
c = a[:10] + b[13:]

# save c as "example3.pdf"
c.save("example3.pdf")
```


github: https://github.com/JonasHri/PDFpy