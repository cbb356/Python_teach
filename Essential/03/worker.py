import datetime

class Worker:
    def __init__(self, first_name, last_name, department, year):
        if not first_name:
            raise ValueError('first name cannot be empty')
        if not first_name:
            raise ValueError('last name cannot be empty')
        if not first_name:
            raise ValueError('department cannot be empty')
        




        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.year = year

    def __str__(self):
        return "Worker: " + self.first_name + " " + self.last_name + ", "\
                + self.department + " department, since " + str(self.year)

    @staticmethod
    def read_worker():
        first_name = input('Input first name:')
        last_name = input('Input last name:')
        department = input('Input name of department:')
        year = int(input('Input year when the worker begun to work:'))
        return Worker(first_name, last_name, department, year)

def found_year_f():
    while True:
        try:
            found_year = int(input('Input year when company was founded:'))
            break
        except ValueError:
            print('Enter correct year')
    return found_year            
        
def main():
    found_year = found_year_f()
    workers = []
    while True:
        workers.append = Worker.read_worker()
    try:
        print(worker)
    except ValueError as error:
        print("Error:", error)
    # print(found_year)
        
        
if __name__ == "__main__":
    main()
