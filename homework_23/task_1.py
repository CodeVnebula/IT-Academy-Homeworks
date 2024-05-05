import json

def open_json(mode: str, data = {}) -> dict:
    """Opens json file in different mode for different tasks such as reading
    its content and returning it and receiving dict for writing results into
    another json file

    Args:
        mode (str): This argument is for deciding in which mode to open file
        'w' for writing, 'r' for reading. 
        data (dict, optional): For receiving results dict after handling the data.
        Defaults to {}.

    Returns:
        dict: after opening json in 'r' mode and loading its content into 'departments'
        dict
    """
    
    if mode == "r":
        path = "homework_23/data/departments.json"
        try:
            with open(path, mode) as file:
                departments = json.load(file)
                
            return departments
        
        except FileNotFoundError:
            print("File does not exist Or could not be opened!")
            return None
    
    elif mode == "w":
        results_file_path = "homework_23/results/avg_salary.json"
        try:
            with open(results_file_path, mode) as json_file:
                json.dump(data, json_file, indent=2)
                
                print(f"Successfully moved data into '{results_file_path.split("/")[-1]}'")
                print("Saved errors into 'errors-log.txt' file")
                
        except Exception as e:
            print(f"An error occurred: {e}")
    
    else:
        print(f"Error occured! Specified mode - '{mode}' is not supported yet!")
        exit()
  

def error_log(errors: str):
    """Writes received errors into the 'errors-log.txt' file

    Args:
        errors (str): Receives errors found while running the code 
    """
    
    path = "homework_23/errors-log.txt"
    try:
        with open(path, "a") as file:
            file.write(errors + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")
                 
    
def handle_data(departments_data: dict) -> dict:
    """Function to handle data as needed, receives dict of content and returns dict of results

    Args:
        departments_data (dict): Receives dict for handling its content

    Returns:
        dict: After collecting needed data it's moved into dict and returned
    """
    
    results = {}
    
    for department in departments_data:
        department_name = departments_data[department]["name"]
        employees = departments_data[department]["employees"]
        
        if len(employees) == 0:
            error = f"Department - '{department_name}' Employees field is empty!"
            print("Employees list empty error saved.")
            error_log(error)
            continue
        
        count_non_digit_chars = 0
        average_salary = 0
        for employee in employees:
            try:
                employee_salary = employee["salary"]
                try:
                    average_salary += int(employee_salary)
                except ValueError:
                    count_non_digit_chars += 1
                    error = f"Employee {employee['name']} Contains non-digit characters!"
                    print("Non-digit characters error saved.")
                    error_log(error)
            except:
                pass
        try:
            average_salary = average_salary / (len(employees) - count_non_digit_chars)
        except ZeroDivisionError:
            error = f"Zero division error occured for calculating average salary for {department_name}"
            print("Zero division error saved.")
            error_log(error)
            continue
            
        results[department_name] = str(average_salary)
            
    return results
                
    
def main():
    print()
    
    departments = open_json("r")
    
    results = handle_data(departments)
    
    open_json("w", results)
    
    print()
if __name__ == "__main__":
    main()
