class Worker:
    def __init__(self, first_name, last_name, department, year):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.year = year

    def __str__(self):
        return "Worker: " + self.first_name + " " + self.last_name + ", "\
                + self.department + " department, since " + str(self.year)

    @staticmethod
    def read_worker():
        first_name = input('Input first name1:')
        last_name = input('Input last name:')
        department = input('Input name of department:')
        year = input('Input year when the worker bevgun to work:')
        return Worker(first_name, last_name, department, year)
        
def main():
    worker = Worker.read_worker()
    try:
        print(worker)
    except TypeError as error:
        print("Some type error:", error)
        
        
if __name__ == "__main__":
    main()
