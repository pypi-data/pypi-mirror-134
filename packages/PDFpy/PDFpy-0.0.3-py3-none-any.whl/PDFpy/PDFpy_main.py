from PyPDF2 import PdfFileWriter, PdfFileReader

class PDF:
    '''
    A Simple Implementation of a PDF editor based on PyPDF2
    github: https://github.com/JonasHri/PDFpy
    '''
    def __init__(self, path = None):
        self.data = []
        if path != None:
            file = PdfFileReader(open(path, "rb"), strict=False)
            for i in range(file.getNumPages()):
                self.data.append(file.getPage(i))

    def __len__(self):
        return len(self.data)
    
    def __add__(self, other):
        assert isinstance(other, PDF)

        res = PDF()

        res.data = self.data + other.data

        return res

    def __getitem__(self, key):
        res = PDF()

        res.data = self.data[key]
    
        return res

    def __setitem__(self, key, other):
        self.data[key] = other.data

    def __delitem__(self, key):
        del self.data[key]
        
            
    def save(self, path):
        '''Saves the PDF at the designated path or the original Location if no path is given'''
        writer = PdfFileWriter()
        for page in self.data:
            writer.addPage(page)
        with open(path, "wb") as f:
            writer.write(f)
