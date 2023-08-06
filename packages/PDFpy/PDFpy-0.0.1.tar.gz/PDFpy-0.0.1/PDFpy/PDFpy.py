from PyPDF2 import PdfFileWriter, PdfFileReader
from collections.abc import Iterable

class PDF:
    '''A Simple Implementation of a PDF editor based on PyPDF2'''
    def __init__(self, path = None):
        self.data = PdfFileWriter()
        if path != None:
            file = PdfFileReader(open(path, "rb"))
            for i in range(file.getNumPages()):
                self.data.addPage(file.getPage(i))

    def __len__(self):
        return self.data.getNumPages()
    
    def __add__(self, other):
        assert isinstance(other, PDF)

        res = PDF()
        for i in range(len(self)):
            res.data.addPage(self.data.getPage(i))
        
        for i in range(len(other)):
            res.data.addPage(other.data.getPage(i))

        return res

    def __getitem__(self, key):
        res = PDF()

        if isinstance(key, int):
            res.data.addPage(self.data.getPage(key))

        elif isinstance(key, Iterable):
            for i in key:
                res.data.addPage(self.data.getPage(i))
        
        elif isinstance(key, slice):
            key = key.indices(len(self))
            for i in range(key[0], key[1], key[2]):
                res.data.addPage(self.data.getPage(i))
    
        return res

    def __setitem__(self, key, other):
        assert isinstance(other, PDF)

        if isinstance(key, int):
            self.__setitem__([key], other)
            return
        elif isinstance(key, slice):
            key = key.indices(len(self))
            self.__setitem__(list(range(key[0], key[1], key[2])), other)
            return
        
        assert len(key) == len(other)

        res = PdfFileWriter()
        idx = 0
        for i in range(len(self)):
            if idx < len(key) and key[idx] == i:
                res.addPage(other.data.getPage(idx))
                idx += 1
            else:
                res.addPage(self.data.getPage(i))
        
        self.data = res
            
    def save(self, path):
        '''Saves the PDF at the designated path or the original Location if no path is given'''
        with open(path, "wb") as f:
            self.data.write(f)
