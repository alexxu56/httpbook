# -*- coding: utf-8 -*-
from updateBook import UpdateBook
from getBookList import GetBookList
import unittest

class testUpdateBook(unittest.TestCase):
    def testupdatebook(self):
        # addbook
        filename = 'caseUpdate.xlsx'
        begincase = '00301'
        casenum = 2

        updatebooklist = UpdateBook()
        booklist = updatebooklist.update_book(filename, begincase, casenum)

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

