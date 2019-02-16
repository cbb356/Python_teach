def input_numbers():
    number_list = []
    for i in range(3):
        number_list.append(float(input("Input number: ")))
    return number_list

def average(number_list):
    result = (number_list[0] + number_list[1] + number_list[2]) / 3
    return result
    
def main():
    print("Average: ", average(input_numbers()))    
                    
if __name__ == "__main__":
    main()
        
