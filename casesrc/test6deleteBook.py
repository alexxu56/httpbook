# -*- coding: utf-8 -*-
from deleteBook import deleteBook
from getBookList import GetBookList
import unittest

class testDeleteBook(unittest.TestCase):
    def testdeletebook(self):
        # addbook
        filename = 'caseDelete.xlsx'
        begincase = '00601'
        casenum = 2

        deletebooklist = deleteBook()
        booklist = deletebooklist.delete_book(filename, begincase, casenum)
        print booklist

        # query
        filenameq = 'caseData.xlsx'
        casenumq = 1
        for book in booklist:
            inbookid = int(book['id'])
            begincase = book['caseid']
            print begincase
            print int(inbookid)
            if inbookid > 0:
                books = GetBookList()
                books.get_book_list(filenameq, begincase, casenumq, inbookid)

#if __name__ == '__main__':

