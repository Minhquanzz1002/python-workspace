'''
Khai báo đối tượng Employee có: 
Các thuộc tính (fields, states) sau
- mã số (code)
- tên (name)
- tuổi (age)
- lương (salary)
Các phương thức (behaviors, methods)
- Tổng thu nhập hằng năm sau thuế (income) biết rằng tax = 10%
- In ra thông tin của nhân viên (display)
- Tăng lương cho nhân viên (increaseSalary), biết rằng số lương tăng phải lớn hơn 0
- (Sinh viên tự viết) Giảm lương cho nhân viên (decreaseSalary), biết rằng số lương giảm phải lớn hơn 0 và không vượt quá 20% lương hiện tại
============= YÊU CẦU CHƯƠNG TRÌNH==============
Khai báo biến danh sách (list) nhân viên (dsNhanVien) để lưu trữ các nhân viên và viết chương trình menu thực hiện các chức năng bên dưới 
- Opt-1: Tải danh sách nhân viên từ file dbemp_input.db
- Opt-2: Thêm nhân viên vào danh sách
- Opt-3: Hiển thị danh sách nhân viên
- Opt-4: Hiển thị thông tin của một nhân viên khi biết mã nhân viên
- Opt-5: Chỉnh sửa thông tin một nhân viên
- Opt-6: Xóa một nhân viên ra khỏi danh sách
- Opt-7: Tăng lương cho một nhân viên
- Opt-8: Giảm lương cho một nhân viên
- Opt-9: Tính số lượng nhân viên (countEmp) và xuất ra màn hình
- Opt-10: Tính tổng tiền lương của công ty phải trả hàng tháng (sumSalary) và xuất ra màn hình
- Opt-11: Tính trung bình lương của nhân viên (avgSalary) và xuất ra màn hình
- Opt-12: Tính độ tuổi trung bình của nhân viên (avgAge) và xuất ra màn hình
- Opt-13: Tính tuổi lớn nhất của các nhân viên (maxAge) và hiển thị danh sách nhân viên có tuổi lớn nhất
- Opt-14: Sắp xếp danh sách nhân viên tăng dần theo lương
- Opt-15: Vẽ biểu đồ tương quan lương theo độ tuổi
- Opt-16: Vẽ biểu đồ so sánh lương trung bình của các nhóm tuổi: nhỏ hơn 35, từ 35 đến 50, hơn 50 trở lên
- Opt-17: Vẽ biểu đồ thể hiện phần trăm tổng lương trên các nhóm tuổi như Opt-16
- Opt-18: Vẽ biểu đồ thể hiện phần trăm số lượng nhân viên theo các nhóm tuổi như Opt-16 
- Opt-19: Lưu danh sách nhân viên xuống file dbemp_output.db, biết rằng mỗi nhân viên là một dòng và các thông tin nhân viên được phân cách bởi dấu '-'
- Opt-Khác: Thoát chương trình
'''
import matplotlib.pyplot as plt
import Employee as emp

menu_options = {
    1:'Load data from file',
    2:'Add new employee',
    3:'Display list of employee',
    4:'Show employee details',
    5:'Update employee information',
    6:'Delete employee',
    7:'Increase salary of employee',
    8:'Decrease salary of employee',
    9:'Show total employee a month',
    10:'Show total salary a month',
    11:'Show average of salary a month',
    12:'Show average of age',
    13:'Show maximum age',
    14:'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16:'Draw average of salary chart by age group',
    17:'Draw percentage of salary by age group',
    18:'Draw percentage of total employee by age group',
    19:'Store data to file',
    'Others': 'Exit program'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# Khai báo biến lưu trữ những nhân viên
dsNhanVien = []

while(True):
        print_menu()
        userChoice = ''
        try:
            userChoice = int(input('Input choice: '))
        except:
            print('Invalid input, try again')
            continue
        #Check what choice was entered and act accordingly
        if userChoice == 1:
            fr = open('dbemp_input.db',mode='r',encoding='utf-8')
            for line in fr:
                stripLine = line.strip('\n')
                ds = stripLine.split(',')
                maso = ds[0]
                ten = ds[1]
                tuoi = int(ds[2])
                luong = float(ds[3])
                nv = emp.Employee(maso,ten,tuoi,luong)
                dsNhanVien.append(nv)
            fr.close()
        elif userChoice == 2:
           maso = input("Input code: ")
           ten = input("Input name: ")
           tuoi = int(input("Input age: "))
           luong = float(input("Input salary: "))
           nv = emp.Employee(maso,ten,tuoi,luong)
           dsNhanVien.append(nv)
        elif userChoice == 3:
            for item in dsNhanVien:
                item.display()
        elif userChoice == 10:
            sumSalary = 0.0
            for item in dsNhanVien:
                sumSalary = sumSalary + item.salary
            print(f'Total salary: {sumSalary}') 
        elif userChoice == 15:
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                arrTuoi.append(item.age)
                arrLuong.append(item.salary)
                
            # Vẽ đồ thị
            plt.figure(figsize=(15,5))

            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")

            plt.plot(arrTuoi,arrLuong, "go")
            plt.show()
        else:
            print('BYE BYE')
            break
