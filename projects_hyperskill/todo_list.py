##### TODO LIST #####
## print the required todo
def print_task(option):
    
    ## today's todos
    if option == 1:
        print(f'Today {datetime.datetime.today().date().strftime("%d %b")}:\n')
        today_tasky = session.query(Table).filter(Table.deadline == datetime.datetime.today().date()).all()
        if today_tasky == []:
            print("Nothing to do!")
        else:
            for i in range(len(today_tasky)):
                print(f"{i + 1}. {today_tasky[i].task}")

    ## weekly todos
    elif option == 2:
        begin = datetime.datetime.today().date()
        for i in range(7):
            next_day = begin + datetime.timedelta(days=i)
            week_tasky = session.query(Table).filter(Table.deadline == next_day).all()
            if week_tasky == []:
                print(f"""
{next_day.strftime("%A %d %b")}:
Nothing to do!
""")
            else:
                print(f'{next_day.strftime("%A %d %b")}:')
                for j in range(len(week_tasky)):
                    print(f'{j + 1}. {week_tasky[j].task}')

    ## all todos
    elif option == 3:
        all_tasky = session.query(Table).order_by(Table.deadline).all()
        print("All tasks:")
        for i in range(len(all_tasky)):
            print(f'{i + 1}. {all_tasky[i].task}. {all_tasky[i].deadline.strftime("%d %b")}')


    ## missed todos
    elif option == 4:
        miss_tasky = session.query(Table).filter(Table.deadline < datetime.datetime.today().date()).order_by(Table.deadline).all()
        if miss_tasky == []:
            print("Nothing is missed!")
        else:
            for i in range(len(miss_tasky)):
                print(f'{i + 1}. {miss_tasky[i].task}. {miss_tasky[i].deadline.strftime("%d %b")}')

    session.commit()

## adding a new todo
def add_task():
    tasky = input("Enter task:\n")
    tasky_deadline = input("Enter deadline:\n")
    deadline_date = datetime.datetime.strptime(tasky_deadline, "%Y-%m-%d")
    task_addition = Table(task=tasky, deadline=deadline_date)
    session.add(task_addition)
    print("The task has been added!")

    session.commit()

## deleting a todo
def task_delete():
    all_tasky = session.query(Table).order_by(Table.deadline).all()
    if all_tasky == []:
        print("Nothing to delete")
    else:
        for i in range(len(all_tasky)):
            print(f'{i + 1}. {all_tasky[i].task}. {all_tasky[i].deadline.strftime("%d %b")}')
        del_option = int(input("Choose the number of the task you want to delete:\n"))
        task_to_del = all_tasky[del_option - 1]
        session.delete(task_to_del)
        print("The task has been deleted!")

    session.commit()

## Imports
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

## creating the database with SQLite giving the filename, threading for testing
engine = create_engine('sqlite:///todo.db?check_same_thread=False')

## table creation using a Table class
Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.date.today())

    def __repr__(self):
        return self.task

## create the database with the table as described above by the Table Class
Base.metadata.create_all(engine)

## access the database, establish a connection with the database
## make a session
Session = sessionmaker(bind=engine)
session = Session()

## Main
while True:
    print("""
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
""")
    option = int(input())
    if option == 1 or option == 2 or option == 3 or option == 4:
        print_task(option)
    elif option == 5:
        add_task()
    elif option == 6:
        task_delete()
    elif option == 0:
        print("Bye!")
        break
session.commit()
