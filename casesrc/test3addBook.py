# -*- coding: utf-8 -*-
from addBook import AddBook
from getBookList import GetBookList
import  unittest

class addBookList(unittest.TestCase):
    def testaddbooklist(self):
        # addbook
        filename = 'caseAdd.xlsx'
        begincase = '00101'
        casenum = 2
        addbooklist = AddBook()
        booklist = addbooklist.add_book(filename, begincase, casenum)
        # query
        filenameq = 'caseData.xlsx'
        casenumq = 1
        for book in booklist:
            inbookid = int(book['id'])
            begincase = book['caseid']
            print int(inbookid)
            if inbookid > 0:
                books = GetBookList()
                books.get_book_list(filenameq, begincase, casenumq, inbookid)

#if __name__ == '__main__':
#    testunit = unittest.TestSuite()
#    testunit.addTest(addBookList("addbooklist"))



