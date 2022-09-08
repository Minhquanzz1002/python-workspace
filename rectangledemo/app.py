'''
(*) Sinh viên tự thực hành
Viết chương trình menu
1- Đọc dữ liệu từ file input.db
2- Thêm mới hình chữ nhật
3- Hiển thị danh sách hình chữ nhật
4- Lưu danh sách hình chữ nhật xuống file demo4output.db
Others- Thoát
'''
import Rectangle as rect
menu_options = {
    1: 'Đọc dữ liệu từ file input.db',
    2: 'Thêm mới hình chữ nhật',
    3: 'Hiển thị danh sách hình chữ nhật',
    4: 'Lưu danh sách hình chữ nhật xuống file demo4output.db',
    'Others': 'Thoát'
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


rectList = []

while(True):
    print_menu()
    userChoice = ''
    try:
        userChoice = int(input('Nhập tùy chọn: '))
    except:
        print('Nhập sai định dạng, hãy nhập lại.....')
        continue

    if userChoice == 1:
        fr = open('..\\rectangledemo\\input.db',
                  mode='r', encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            lst = stripLine.split(',')
            width = float(lst[0])
            length = float(lst[1])   
            rectangle = rect.Rectangle(width, length)
            rectList.append(rectangle)
        fr.close()

    elif userChoice == 2:
        width = float(input('Nhập chiều rộng: '))
        length = float(input('Nhập chiều dài: '))
        rectangle = rect.Rectangle(width, length)
        rectList.append(rectangle)
    elif userChoice == 3:
        if rectList.count == 0:
            print('List is empty')
        else:
            for item in rectList:
                item.display()

    elif userChoice == 4:
        fw = open('..\\rectangledemo\\output.db',mode='w',encoding='utf-8')
        for item in rectList:
            fw.write(f'{item.width} - {item.length} - {item.calculate_perimeter()} - {item.calculate_area()}\n')
        fw.close()
    else:
        print('EXIT')
        break
