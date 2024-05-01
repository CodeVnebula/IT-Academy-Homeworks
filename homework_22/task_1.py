def handle_data(data, small, high):
    with open(small, "w") as result_file_small, \
         open(high, "w") as result_file_huge, \
         open(data, "r") as file:
        for line in file:
                line = line.strip()
                price = line.split(',')[-1]
                
                if float(price) < 10:
                    result_file_small.write(line + "\n")
                else:
                    result_file_huge.write(line + "\n")
                    
def main():
    data_file_path = "homework_22/Assets/data.txt"
    small_file_path = "homework_22/Results/small.txt"
    high_file_path = "homework_22/Results/high.txt"
    handle_data(data_file_path, small_file_path, high_file_path)     

if __name__ == "__main__":
    main()
