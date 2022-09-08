import matplotlib.pyplot as plt
import numpy as np
import Employee as emp

menu_options = {
    1: 'Load data from file',
    2: 'Add new employee',
    3: 'Display list of employee',
    4: 'Show employee details',
    5: 'Upload employee information',
    6: 'Delate employee',
    7: 'Increase salary of employee',
    8: 'Decrease salary of employee',
    9: 'Show total employee a month',
    10: 'Show total salary a month',
    11: 'Show average of salary a month',
    12: 'Show average of age',
    13: 'Show maximum of age',
    14: 'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16: 'Draw average of salary chart by age group',
    17: 'Draw percentage of salary by age group',
    18: 'Draw percentage of total employee by age group',
    19: 'Store data to file',
    'Others': 'Exit program',
}


def print_menu():
    for key in menu_options.keys():
        print(key, ':', menu_options[key])


def search_employee_by_code(code):
    for item in list_emp:
        if item.code == code:
            item.display()
            return True
    return False

def calculate_mean(arr):
    if arr:
        return np.mean(arr)
    else:
        return 0
    
list_emp = []

while (True):
    print_menu()
    user_choice = ''
    try:
        user_choice = int(input('Input choice:'))
    except:
        print('Invalid input, try again.')
        continue

    match user_choice:
        case 1:
            fr = open('dbemp_input.db', mode='r', encoding='utf-8')
            for line in fr:
                stripLine = line.strip('\n')
                emp_data = stripLine.split(',')
                code = emp_data[0]
                name = emp_data[1]
                age = int(emp_data[2])
                salary = float(emp_data[3])
                employee = emp.Employee(code, name, age, salary)
                list_emp.append(employee)
            fr.close()
        case 2:
            code = input('Input code:')
            name = input('Input name:')
            age = int(input('Input age:'))
            salary = float(input('Input salary:'))
            employee = emp.Employee(code, name, age, salary)
            list_emp.append(employee)
        case 3:
            for item in list_emp:
                item.display()
        case 4:
            code = input('Input code:')
            if search_employee_by_code(code) == False:
                print('Nothing here.')
        case 5:
            code = input('Input code:')
            search_result = False
            for item in list_emp:
                if item.code == code:
                    item.name = input('Input name:')
                    item.age = int(input('Input age:'))
                    item.salary = float(input('Input salary:'))
                    search_result = True
                    break
            if search_result == False:
                print('Nothing here.')
        case 6:
            code = input('Input code:')
            search_result = False
            for item in list_emp:
                if item.code == code:
                    list_emp.remove(item)
                    search_result = True
                    break
            if search_result == False:
                print('Nothing here.')
        case 7:
            code = input('Input code:')
            search_result = False
            for item in list_emp:
                if item.code == code:
                    amount = float(input('Input amount:'))
                    item.increaseSalary(amount)
                    search_result = True
                    break
            if search_result == False:
                print('Nothing here.')
        case 8:
            code = input('Input code:')
            search_result = False
            for item in list_emp:
                if item.code == code:
                    amount = float(input('Input amount:'))
                    item.decreaseSalary(amount)
                    search_result = True
                    break
            if search_result == False:
                print('Nothing here.')
        case 9:
            print(f'Number of employees: {len(list_emp)}')
        case 10:
            total_salary = 0
            for item in list_emp:
                total_salary += item.salary
            print(f'Total salary a month: {total_salary}')
        case 11:
            total_salary = 0
            for item in list_emp:
                total_salary += item.salary
            print('Average salary a month: {:.2f}'.format(total_salary/len(list_emp)))
        case 12:
            total_age = 0
            for item in list_emp:
                total_age += item.age
            print('Average of age:',round(total_age/len(list_emp)))
        case 13:
            max_age = 0
            for item in list_emp:
                if item.age > max_age:
                    max_age = item.age
            print('Maximum of age:',max_age)
        case 14:
            list_emp.sort(key=lambda x: x.salary)
        case 15:
            list_age = []
            list_salary = []
            for item in list_emp:
                list_age.append(item.age)
                list_salary.append(item.salary)

            plt.figure(figsize=(15,5))
            plt.title('Age and salary chart')
            plt.xlabel('Ox: age')
            plt.ylabel('Oy: salary')
            plt.plot(list_age, list_salary, 'g+')
            plt.show()
        case 16:
            x = ['less than 35', 'from 35 to 50', 'more than 50']
            list_salary_1 = []
            list_salary_2 = []
            list_salary_3 = []
            for item in list_emp:
                if item.age < 35:
                    list_salary_1.append(item.salary)
                elif item.age > 50:
                    list_salary_3.append(item.salary)
                else:
                    list_salary_2.append(item.salary)
            y = []
            y.append(calculate_mean(list_salary_1))
            y.append(calculate_mean(list_salary_2))
            y.append(calculate_mean(list_salary_3))

            plt.title('Average of salary chart by age group')
            plt.xlabel('Levels of age')
            plt.ylabel('Average of salary')
            plt.bar(x, y)
            plt.show()
        case 17:
            x = ['less than 35', 'from 35 to 50', 'more than 50']
            noibac = [0, 0.1, 0]
            list_salary_1 = []
            list_salary_2 = []
            list_salary_3 = []
            for item in list_emp:
                if item.age < 35:
                    list_salary_1.append(item.salary)
                elif item.age > 50:
                    list_salary_3.append(item.salary)
                else:
                    list_salary_2.append(item.salary)
            list_salary = []
            list_salary.append(sum(list_salary_1))
            list_salary.append(sum(list_salary_2))
            list_salary.append(sum(list_salary_3))
            
            plt.pie(list_salary, explode=noibac, labels=x, shadow=True, startangle=45)
            plt.title('Percentage of salary by age group')
            plt.legend(title='Levels of age')
            plt.show()
        case 18:
            x = ['less than 35', 'from 35 to 50', 'more than 50']
            noibac = [0, 0.1, 0]
            age_35 = 0
            age_35_to_50 = 0
            age_50 = 0
            for item in list_emp:
                if item.age < 35:
                    age_35 += 1
                elif item.age > 50:
                    age_50 += 1
                else:
                    age_35_to_50 += 1
            list_age = []
            list_age.append(age_35)
            list_age.append(age_35_to_50)
            list_age.append(age_50)
            
            plt.pie(list_age, explode=noibac, labels=x, shadow=True, startangle=45)
            plt.title('Percentage of salary by age group')
            plt.legend(title='Levels of age')
            plt.show()
        case 19:
            fw = open('output.db', mode='w', encoding='utf-8')
            for item in list_emp:
                fw.write(f'{item.code},{item.name},{item.age},{item.salary}\n')
            print('Store file successfully')
            fw.close()
        case default:
            print('BYE')
            break
