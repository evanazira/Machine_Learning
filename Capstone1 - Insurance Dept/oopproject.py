import time
from datetime import datetime

class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def read_lines(self):
        with open(self.filename, "rt") as file:
            return file.readlines()
    
    def write_lines(self, lines):
        with open(self.filename, "wt") as file:
            file.writelines(lines)
    
    def append_line(self, line):
        with open(self.filename, "at") as file:
            file.write(line + "\n")

class UserInput:
    # @staticmethod
    def get_input(datatype, caption, error_message, default_value=None):
        value = None
        while True:
            try:
                input_value = input(caption)
                if default_value is None:
                    value = datatype(input_value)
                else:
                    value = default_value if input_value.strip() == "" else datatype(input_value)
            except Exception:
                print(error_message)
            else:
                break
        return value
class CarInsurance:
    def __init__(self, car_file, car_insurance_file):
        self.car_file = FileManager(car_file)
        self.car_insurance_file = FileManager(car_insurance_file)

    def print_insurance(self):
        print("-" * 120)
        print(" " * 53, "\033[1mCAR INSURANCE\033[0m\n", " " * 53)
        lines = self.car_file.read_lines()
        for index, line in enumerate(lines):
            data = line.strip().split(" | ")
            if index == 0:
                print(f"{'No.':>4}{data[0]:>12}{data[1]:>12}{data[2]:>9}{data[3]:>5}{data[4]:>19}{data[5]:>8}{data[6]:>18}{data[7]:>23}{data[8]:>9}")
                print("=" * 120)
            else:
                print(f"{index:>4}{data[0]:>12}{data[1]:>12}{data[2]:>9}{data[3]:>5}{data[4]:>19}{data[5]:>8}{data[6]:>20}{data[7]:>19}{data[8]:>11}")

        datas = [line.strip().split(" | ") for line in lines]
        index = UserInput.get_input(int, "Enter a number: ", "Number must be an integer")
        if index > 0 and index < len(datas):
            car_plate, make, model, year, vin, mileage, expiry_date, status = datas[index]
            print(f"\nCar plate number: {car_plate}\nMake: {make}\nModel: {model}\nYear: {year}\nVIN: {vin}\nMileage: {mileage}\nInsurance expiry date: {expiry_date}\nStatus: {status}")
            if status.strip() == "Active":
                print("\nThe insurance has been active")
            else:
                print("\nThe insurance has been expired")
                confirm = UserInput.get_input(str, "\nDo you want to renew this car insurance (y/n)? ", "Confirm must be in String")
                if confirm == "y":
                    self.find_and_update_insurance(car_plate)

    def find_and_update_insurance(self, car_plate):
        car_plate = car_plate.replace(" ", "")
        lines = self.car_insurance_file.read_lines()
        datas = [line.strip().split(" | ") for line in lines]

        for i, data in enumerate(datas):
            if data[0].replace(" ", "") == car_plate:
                new_company = UserInput.get_input(str, f"Company[{data[4]}]: ", "Company must be in string ", data[4])
                new_policy_number = UserInput.get_input(str, f"Policy number[{data[5]}]: ", "Policy number must be in string", data[5])
                new_coverage_type = UserInput.get_input(str, f"Coverage Type[{data[7]}]: ", "Coverage type must be in string", data[7])
                new_premium_amount = UserInput.get_input(str, f"Premium amount[{data[8]}]: ", "Premium amount must be in integer", data[8])
                new_status = UserInput.get_input(str, f"Status[{data[9]}]: ", "Status must be in string", data[9])
                new_expiry_date = UserInput.get_input(str, f"Expiry date[{data[10]}]: ", "Expiry date must be in string", data[10])
                new_claim_amount = UserInput.get_input(int, f"Claim amount[{data[11]}]: ", "Claim amount must be in integer", data[11])
                datas[i] = [data[0], data[1], data[2], data[3], new_company, new_policy_number, data[6], new_coverage_type, new_premium_amount, new_status, new_expiry_date, new_claim_amount]
                break

        new_lines = [" | ".join(map(str, item)) + "\n" for item in datas]
        self.car_insurance_file.write_lines(new_lines)
        self.update_car_file(car_plate)

    def update_car_file(self, car_plate):
        car_plate = car_plate.replace(" ", "")
        car_lines = self.car_file.read_lines()
        insurance_lines = self.car_insurance_file.read_lines()
        
        car_data = [line.strip().split(" | ") for line in car_lines]
        insurance_data = [line.strip().split(" | ") for line in insurance_lines]

        for i, car in enumerate(car_data):
            for insurance in insurance_data:
                if car[0].replace(" ", "") == car_plate and insurance[0].replace(" ", "") == car_plate:
                    car_data[i][6] = insurance[-2]
                    car_data[i][7] = insurance[-3]

        new_lines = [" | ".join(map(str, item)) + "\n" for item in car_data]
        self.car_file.write_lines(new_lines)
        print("\nThe car insurance was successfully renewed.")

class DriverInsurance:
    def __init__(self, driver_file, driver_insurance_file):
        self.driver_file = FileManager(driver_file)
        self.driver_insurance_file = FileManager(driver_insurance_file)

    def print_insurance(self):
        print("-" * 120)
        print(" " * 52, "\033[1mDRIVER INSURANCE\033[0m\n", " " * 52)
        lines = self.driver_file.read_lines()
        for index, line in enumerate(lines):
            data = line.strip().split(" | ")
            if index == 0:
                print(f"{'No.':<8}{data[0]:<12}{data[1]:<19}{data[2]:<8}{data[3]:<12}{data[4]:<22}{data[5]:<19}{data[6]:<14}")
                print("=" * 120)
            else:
                print(f"{index:<8}{data[0]:<12}{data[1]:<19}{data[2]:<8}{data[3]:<12}{data[4]:<22}{data[5]:<19}{data[6]:<14}")

        datas = [line.strip().split(" | ") for line in lines]
        index = UserInput.get_input(int, "Enter a number: ", "Number must be an integer")
        if index > 0 and index < len(datas):
            driver_id, driver_name, driver_age, gender, license_number, expiry_date, status = datas[index]
            print(f"\nDriver ID: {driver_id}\nName: {driver_name}\nAge: {driver_age}\nGender: {gender}\nLicense number: {license_number}\nInsurance expiry date: {expiry_date}\nInsurance status: {status}")
            if status.strip() == "Active":
                print("\nThe insurance has been active")
            else:
                print("\nThe insurance has been expired")
                confirm = UserInput.get_input(str, "\nDo you want to renew this driver insurance (y/n)? ", "Confirm must be in String")
                if confirm == "y":
                    self.find_and_update_insurance(driver_id)

    def find_and_update_insurance(self, driver_id):
        driver_id = driver_id.replace(" ", "")
        lines = self.driver_insurance_file.read_lines()
        datas = [line.strip().split(" | ") for line in lines]

        for i, data in enumerate(datas):
            if data[0].replace(" ", "") == driver_id:
                new_company = UserInput.get_input(str, f"Company[{data[5]}]: ", "Company must be in string ", data[5])
                new_policy_number = UserInput.get_input(str, f"Policy number[{data[6]}]: ", "Policy number must be in string", data[6])
                new_coverage_type = UserInput.get_input(str, f"Coverage Type[{data[7]}]: ", "Coverage type must be in string", data[7])
                new_premium_amount = UserInput.get_input(str, f"Premium amount[{data[8]}]: ", "Premium amount must be in integer", data[8])
                new_status = UserInput.get_input(str, f"Status[{data[9]}]: ", "Status must be in string", data[9])
                new_expiry_date = UserInput.get_input(str, f"Expiry date[{data[10]}]: ", "Expiry date must be in string", data[10])
                new_claim_amount = UserInput.get_input(int, f"Claim amount[{data[11]}]: ", "Claim amount must be in integer", data[11])
                datas[i] = [data[0], data[1], data[2], data[3], new_company, new_policy_number, data[6], new_coverage_type, new_premium_amount, new_status, new_expiry_date, new_claim_amount]
                break

        new_lines = [" | ".join(map(str, item)) + "\n" for item in datas]
        self.driver_insurance_file.write_lines(new_lines)
        self.update_driver_file(driver_id)

    def update_driver_file(self, driver_id):
        driver_id = driver_id.replace(" ", "")
        driver_lines = self.driver_file.read_lines()
        insurance_lines = self.driver_insurance_file.read_lines()
        
        driver_data = [line.strip().split(" | ") for line in driver_lines]
        insurance_data = [line.strip().split(" | ") for line in insurance_lines]

        for i, driver in enumerate(driver_data):
            for insurance in insurance_data:
                if driver[0].replace(" ", "") == driver_id and insurance[0].replace(" ", "") == driver_id:
                    driver_data[i][6] = insurance[-2]
                    driver_data[i][7] = insurance[-3]

        new_lines = [" | ".join(map(str, item)) + "\n" for item in driver_data]
        self.driver_file.write_lines(new_lines)
        print("\nThe driver insurance was successfully renewed.")

class InsuranceApp:
    def __init__(self):
        self.car_insurance = CarInsurance("car_data.txt", "car_insurance_data.txt")
        self.driver_insurance = DriverInsurance("driver_data.txt", "driver_insurance_data.txt")

    def run(self):
        while True:
            print("\n1. Car Insurance\n2. Driver Insurance\n3. Exit")
            choice = UserInput.get_input(int, "Enter your choice: ", "Choice must be an integer")
            if choice == 1:
                self.car_insurance.print_insurance()
            elif choice == 2:
                self.driver_insurance.print_insurance()
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = InsuranceApp()
    app.run()



