import ctypes
from ctypes import *

class Student(Structure):
	_fields_ = [("name",c_char * 30),
			("fScore", c_float * 3),
			("age",c_int)
			]


su = Student()
su.name = b"test-sdk"
su.fScore = (18,2,3)
su.age = 16

def test_Display_Student():
	ll = ctypes.cdll.LoadLibrary   
	lib = ll("./libpycall.so") 
	# lib.Display.restype = c_float
	# lib.Display.argtypes = [Student]    
	lib.Display_Student(su)  
	print('----- finish -----\n') 



class Books(Structure):
	_fields_ = [("title",c_char * 50),
			("author", c_char * 50),
			("subject",c_char *100),
			("book_id",c_int)
			]
	
book = Books()
book.title = b"C Programming"
book.author = b"Nuha Ali"
book.subject = b"C Programming Tutorial"
book.book_id = 6495407


def test_Display_Books():
	ll = ctypes.cdll.LoadLibrary   
	lib = ll("./libpycall.so") 
	# lib.Display.restype = c_float
	# lib.Display.argtypes = [Student]    
	lib.Display_Books(book)  
	print('----- finish -----') 


if __name__ == '__main__':
	test_Display_Student()
	test_Display_Books()
	