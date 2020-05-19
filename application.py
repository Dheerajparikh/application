import sqlite3 as lite

#funtionallity goes here

class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            conn = lite.connect('Courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCRIMENT, name TEXT, discription TEXT, prise TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
            pass
        except Exception:
            print("Unable to create a DB")


# TODO:create data
def insert_data(self,data):
    try:

        with con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO course(name,discription, prise, is_private) VALUES (?,?,?,?)", data
            )
    except Exception:
            return False


 


# TODO: read data
def fetch_data(self):
    try:

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM courses")
            return cur.fetchall()
    except Exception:
            return False



# TODO: delete data
def delete_data(self):
    try:

        with con:
            cur = con.cursor()
            sql = "DELETE FROM course WHERE id = ?"
            cur.execute(sql, [id])            
            
    except Exception:
            return False
    






# TODO:provide interface to user

def main():
    print("*"*40)
    print("\n:: COURSE MANAGMENT :: \n")
    print("*"*40)


    db = DatabaseManage()
    

    print("#"*40)
    print("\n :: User manaul :: \n")
    print("#"*40)

    print ("\nPress 1. Insert a new course")
    print ("\nPress 2. Show all the courses")
    print ("\nPress 3. Delete a course (NEED ID OF COURSE)")
    print("#"*40)
    print ("\n")


    choice = input("\n Enter the choice")

    if choice == "1":
        name = input("\n enter course name: ")
        discription = input("\n enter course discription: ")
        prise = input("\n enter course prise: ")
        private = input("\n Is this course private(0/1): ")

        if db.insert_data([name, discription, price,private]):
            print(" course was inserted succesfully")
        else:
            print("OOPS something is wrong")


    elif choice == "2":
        print("\n:: Course Lise ::\n")

        for index, item in enumerate(db.fetch_data()):
            print("\n SL no:" + str(index +1))
            print(" Course ID:" + str(item[0]))
            print(" Course Name:" + str(item[1]))
            print(" Course discription:" + str(item[2]))
            print(" Course prise:" + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print(" IS private:" +private)
            print("\n")


    elif choice == "3":
        record_id= input(" ENter the course ID")

        if db.delete_data(record_id):
            print("Course was deleted with a success")
                
        else:
            print("SOMETING WENT WORNG")
    else:
        print("\n BAD CHOISE")  


if __name__== '__main__':
    main()

               
