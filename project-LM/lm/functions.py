import winsound
import student
import faculty
import book
import pickle
import datetime
import time
import sys
import pyttsx3 


def load_student():
    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break
    return curr_students


def load_faculty():
    curr_emps = []
    with open('faculty_data.pkl', 'rb') as f:
        while True:
            try:
                curr_emps.append(pickle.load(f))
            except EOFError:
                break
    return curr_emps


def load_books():
    get_books = []
    with open('books_data.pkl', 'rb') as f:
        while True:
            try:
                get_books.append(pickle.load(f))
            except EOFError:
                break
    return get_books




def dump_students(curr_students):
    for i in range(0, len(curr_students)):
        if i == 0:
            with open('student_data.pkl', 'wb') as f:
                pickle.dump(curr_students[i], f)
        else:
            with open('student_data.pkl', 'ab') as f:
                pickle.dump(curr_students[i], f)


def dump_faculty(curr_emps):
    for i in range(0, len(curr_emps)):
        if i == 0:
            with open('faculty_data.pkl', 'wb') as f:
                pickle.dump(curr_emps[i], f)
        else:
            with open('faculty_data.pkl', 'rb') as f:
                pickle.dump(curr_emps[i], f)


def search_book(mode, data):
    books = load_books()
    if mode == 'i':
        for it in books:
            if it.isbn == data:
                print(f'Book details are: \nAuthor:{it.author}\nTitle:{it.title}\nCopies Available:{it.num_copies}')
                return
        print('Book not available.')
    elif mode == 't':
        for it in books:
            if it.title.lower() == data.lower():
                print(f'Book details are: \nAuthor:{it.author}\nTitle:{it.title}\nCopies Available:{it.num_copies}')
                return
        print('Book not available.')
        
#          elif mode == 't':
#         for it in books:
#             if it.title == data.lower():
#                 print(f'Book details are: Title:{it.title}\nCopies Available:{it.num_copies}')
#                 return
#         print('Book not available.')
        
    elif mode == 'a':
        flag = 0
        for it in books:
            if it.author.lower() == data.lower():
                print(f'Book details are: \nAuthor:{it.author}\nTitle:{it.title}\nCopies Available:{it.num_copies}')
                flag = 1
        if flag == 0:
            print('Book not available.')


def modify_std_on_return(book_isbn, roll):
    curr_students = load_student()
    for st in curr_students:
        if st.roll_no == roll:
#            for j in st.books_issued:
#            if
            for it in st.books_issued:
                if it['isbn'] == book_isbn:
                    st.num_books_issued -= 1
                    st.books_issued.remove(it)

    dump_students(curr_students)


    
#why not working shyam!!!!!!    
def calc_fine(roll, book_isbn):
    curr_students = load_student()
    dor = 0
    doi = 0
    for s in curr_students:
        if s.roll_no == roll:
            for it in s.books_issued:
                if it['isbn'] == book_isbn:
                    doi = it['doi']
                    dor = datetime.datetime.now()
                    break
    diff_days = dor - doi
    if diff_days.days > 14:
        fine = 2 * (diff_days.days - 14)
        print(f'Fine amount: Rs.{fine}')
    else:
        print('Thank you !')


def modify_faculty_on_return(book_isbn, emp_id):
    curr_emps = load_faculty()
    nc = 0
    for e in curr_emps:
        if e.eid == emp_id:
            for it in e.books_issued:
                if it['isbn'] == book_isbn:
                    nc = it['nc']
                    e.books_issued.remove(it)
    dump_faculty(curr_emps)
    return nc



def issued_faculty(book_isbn, emp_id):
    curr_emps = load_faculty()
    for emp in curr_emps:
        if emp.eid == emp_id:
            for it in emp.books_issued:
                if it['isbn'] == book_isbn:
                    return True
    return False



def check_avail_faculty(isbn, cp):
    get_books = load_books()
    for it in get_books:
        if it.isbn == isbn and it.num_copies >= cp:
            return True
    return False



def modify_faculty(emp_id, issued):
    curr_emps = load_faculty()
    for fac in curr_emps:
        if fac.eid == emp_id:
            fac.books_issued.append(issued)
            break
    dump_faculty(curr_emps)


def modify_book(isbn, num_copies=1, mode=0):
    get_books = load_books()
    for i in range(0, len(get_books)):
        if get_books[i].isbn == isbn and mode == 0:
            get_books[i].num_copies -= num_copies
            break
        if get_books[i].isbn == isbn and mode == 1:
            get_books[i].num_copies += num_copies
    for j in range(0, len(get_books)):
        if j == 0:
            with open('books_data.pkl', 'wb') as fi_it:
                pickle.dump(get_books[j], fi_it)
        else:
            with open('books_data.pkl', 'ab') as fi_it:
                pickle.dump(get_books[j], fi_it)


#this too......!!                
def check_if_already_issued_to_student(isbn, std_roll):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll:
            for it in std.books_issued:
                if it['isbn'] == isbn:
                    return False
    return True


def modify_student(std_roll, it_issued):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll:
            std.books_issued.append(it_issued)
            std.num_books_issued += 1
    dump_students(curr_students)


    
def check_available(isbn, std_roll):
    curr_data_books = load_books()
    for it in curr_data_books:
        if it.isbn == isbn and it.num_copies > 0:
            return check_if_already_issued_to_student(it.isbn, std_roll)
    return False



def check_std_limit(std_roll):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll and std.num_books_issued <= 4:
            return True
    return False



def check_if_isbn_present(isbn):
    curr_data_books = load_books()
    for it in curr_data_books:
        if it.isbn == isbn:
            return True
    return False



def check_if_eid_present(eid):
    curr_emps = load_faculty()
    for emp in curr_emps:
        if emp.eid == eid:
            return True
    return False



def verify_authentication(eid):
    return check_if_eid_present(eid)


def std_present(std_roll):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll:
            return True
    return False


def add_faculty():
    try:
        ename = input('Enter faculty name: ')
        while True:
            eid = input('Enter faculty id (5 digits): ')
            if len(eid) != 5:
                print('employee id has to be 5 digits long, try again.')
            else:
                break
    except ValueError:
        print('Invalid Input')
    else:
        if check_if_eid_present(eid):
            print('Faculty with this eid already exists. Cannot add Faculty.')
            return
        f = faculty.FacultyClass(ename, eid)
        faculty.faculty_list.append(f)
        with open('faculty_data.pkl', 'ab') as fi_fac:
            pickle.dump(f, fi_fac)


def add_student():
    branch_roll_mapping = {'COE': 'CO','IT': 'IT','ECE': 'EC','ICE': 'IC','MPAE': 'MP','ME': 'ME','BT': 'BT','CSE':'CS'}
    
    try:
        name = input('Enter name of Student: ')
        while True:
            year_of_admn = input('Enter the Year of Admission of Student: ')
            if int(year_of_admn) > datetime.datetime.now().year:
                print(f'Year of admission cannot be greater than {datetime.datetime.now().year}')
            else:
                break
                
        branch = input('Enter branch of student: ')
        while True:
            admn_id_no = input('Enter roll number (only 4 digits): ')
            if len(admn_id_no) != 4:
                print('roll number has to be 4 digits long.')
            else:
                break
        std_roll = "0187" + branch_roll_mapping[branch] + admn_id_no
    except ValueError and KeyError:
        print('Invalid Input. Try again')
        return
    else:
        if std_present(std_roll):
            print('A student with the same details already exists. Cannot Add Student.')
        else:
            s = student.StudentClass(name, year_of_admn, branch, admn_id_no)
            student.student_list.append(s)
            with open('student_data.pkl', 'ab') as fi_std:
                pickle.dump(s, fi_std)
            print(f'Student with name {name} and roll no {std_roll} has been added.')


def add_book():
    try:
        title = input('Enter Book Title: ')
        author = input('Enter Name of Author: ')
        while True:
            isbn = int(input('Enter Book ISBN (13 digit ISBN is followed by this library): '))
            check_isbn = str(isbn)
            if len(check_isbn) == 13:
                break
            else:
                print('Length of ISBN has to be 13. Try again.')
        num_copies_to_add = int(input('Enter number of copies of this book to be added: '))
    except ValueError:
        print('Invalid Input, ISBN/Number of copies has to be a number. Try again.')
        return
    else:
        if check_if_isbn_present(isbn):
            print('Book with same ISBN and title already exists, Book details have been updated')
            get_books = load_books()
            for i in range(0, len(get_books)):
                if get_books[i].isbn == isbn:
                    cp = get_books[i].num_copies
                    get_books.pop(i)
                    it_new = book.BookClass(title, author, isbn, num_copies_to_add + cp)
                    book.book_list.append(it_new)
                for j in range(0, len(book.book_list)):
                    if j == 0:
                        with open('books_data.pkl', 'wb') as fi_it:
                            pickle.dump(book.book_list[j], fi_it)
                    else:
                        with open('books_data.pkl', 'ab') as fi_it:
                            pickle.dump(book.book_list[j], fi_it)
        else:
            it_new = book.BookClass(title, author, isbn, num_copies_to_add)
            book.book_list.append(it_new)
            with open('books_data.pkl', 'ab') as fi_it:

                pickle.dump(it_new, fi_it)
    print('Book details updated in system..')


def print_student_details():

    student_details = load_student()
    for st in student_details:
        print('Name : ' + st.name)
        print('Roll No :' + st.roll_no)
        print('Books Issued : ' + str(st.num_books_issued))
        for it in st.books_issued:
            print(f"Book ISBN : {it['isbn']}")
            print(f"Date Of Issue : {it['doi']}")
        print('-'*25)


def print_faculty_details():
    faculty_details = load_faculty()
    for fc in faculty_details:
        print('Faculty Name : ' + fc.ename)
        print('Faculty ID : ' + fc.eid)
        for it in fc.books_issued:
            print(f"Book ISBN : {it['isbn']}")
            print(f"Date Of Issue : {it['doi']}")
            print(f"{it['nc']} copies of book having ISBN {it['isbn']}")
            print('*'*25)
                  
def archive():
    print("")
    print("")  
    engine = pyttsx3.init()  
    engine.say("welcome to library management system .") 
    engine.say("loading data") 
                  
    engine.runAndWait()                


    blah ="loading data....."
                  
    blah2="reading book data....."
    blah3="                      : book data(.pkl) collected....."
    blah4="reading student data....."
    blah5="                      : student data(.pkl) collected....."
    blah6="reading faculty data....."
    blah7="                      : faculty data(.pkl) collected....."
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n") 
    frequency = 1400  
    duration = 1000  
    winsound.Beep(frequency, duration)               
    for i in blah2:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")    
    for i in blah3:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")    
    for i in blah4:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")    
    for i in blah5:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")    
    for i in blah6:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")    
    for i in blah7:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")
                 
    engine.say("thanks for your patience!")
    engine.runAndWait()           
    print("thanks for your patience!......here you go !")
     
  
    
   # engine.say("hello world") 
   # engine.say("Thank you, stackoverflow") 
   
    engine.say("here you go !")              
    engine.runAndWait()              
            
    
       
            
    
    
    curr_std = load_student()
    for std in curr_std:
        diff = datetime.datetime.now().year - int(std.year_of_admn)
                  
        if diff > 4:
            print(f' {std.name} with roll no {std.roll_no}')
            for it in std.books_issued:
                modify_book(it['isbn'], 1, 1)
            std.books_issued.clear()
            std.num_books_issued = 0
                  
            with open('passed.pkl', 'ab') as file:
                pickle.dump(std, file)
            curr_std.remove(std)
            print(f'{std.name} with roll no {std.roll_no} passed !')
    dump_students(curr_std)
    




def print_book_details():
    book_details = load_books()
    for i in book_details:
        print('Title : ' + i.title)
        print('Author : ' + i.author)
        print(f'ISBN {i.isbn}')
        print(f'Copies available are : {i.num_copies}')
        print('-'*25)


def issue_book_student():
    std_roll = input('Enter Student Roll No To Whom Book Has To Be Issued : ')
    if std_present(std_roll):
        if check_std_limit(std_roll):
            book_isbn = int(input('Enter ISBN of Book That Has To Be Issued : '))
            if check_available(book_isbn, std_roll):
                issue_obj = {
                    'isbn': book_isbn,
                    'doi': datetime.datetime.now()
                }
                modify_student(std_roll, issue_obj)
                print('Book Issued To Student With ' + std_roll + ' Successfully.')
                modify_book(book_isbn)
            else:
                print('Book Not Available....! Cannot Issue.')
        else:
            print('Cannot Issue Book.')
    else:
        print('Student not found. Cannot Issue Book.')


def issue_book_facutly():
    emp_id = input('Enter Faculty ID To Whom Book Has To Be Issued: ')
    if check_if_eid_present(emp_id):
        book_isbn = int(input('Enter Book ISBN That Has To Be Issued: '))
        num_copies = int(input('Enter Number Of Copies To Be Issued: '))
        if check_avail_faculty(book_isbn, num_copies):
            issue_obj = {
                'isbn': book_isbn,
                'doi': datetime.datetime.now(),   
                'nc': num_copies
            }
            modify_faculty(emp_id, issue_obj)
            modify_book(book_isbn, num_copies)
            print(f'Book with {book_isbn} has been issued to employee with eid {emp_id}')
        else:
            print(f'Book with {book_isbn} not available. Cannot issue book')
    else:
        print(f'Employee with {emp_id} not present. Can not issue book.')


def return_book_facutly():
    emp_id = input('Enter Faculty ID: ')
    if check_if_eid_present(emp_id):
        book_isbn = int(input('Enter Book ISBN to be Returned: '))
        if issued_faculty(book_isbn, emp_id):
            num_copies = modify_faculty_on_return(book_isbn, emp_id)
            modify_book(book_isbn, num_copies, 1)
        print(f'This Book Was Not Issued To Employee With ID {emp_id}.')
    print('Employee ID Not Found.')


def return_book_student():
    std_roll = input('Enter Student Roll No Who Is Returning The Book: ')
    if std_present(std_roll):
        book_isbn = int(input('Enter Book ISBN To Be Returned: '))
        if not check_if_already_issued_to_student(book_isbn, std_roll):
            calc_fine(std_roll, book_isbn)
            modify_book(book_isbn, 1, 1)
            modify_std_on_return(book_isbn, std_roll)
        else:
            print(f'Book with ISBN: {book_isbn} has not been issued to this student.')
    else:
        print('try again !')


