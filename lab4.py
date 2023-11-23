# Ədədi massiv yaratmaq üçün funksiya
def create_array():
    array = []
    for i in range(1, 11):  # 1-dən 10-a qədər ədədlər
        array.append(i)
    return array

# Fayla ədədi massivi yazmaq üçün funksiya
def write_to_file(array, filename):
    with open(filename, 'w') as file:
        for number in array:
            file.write(str(number) + '\n')

# Fayldan son üç ədədi oxumaq üçün funksiya
def read_last_three_and_sum(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        last_three_numbers = [int(line.strip()) for line in lines[-3:]]  # Fayldan son üç ədədi seçir
        sum_last_three = sum(last_three_numbers)
    return sum_last_three

# Yaradılmış faylı açmaq
filename = 'numbers.txt'

# Ədədi massivi yaratmaq
my_array = create_array()

# Fayla yazmaq
write_to_file(my_array, filename)

# Fayldan oxumaq, son üç ədədi tapmaq və yeni fayla yazmaq
sum_last_three = read_last_three_and_sum(filename)
with open('new_numbers.txt', 'w') as new_file:
    new_file.write(f'Sum of last three numbers: {sum_last_three}\n')

print(f'Ədədi massiv fayla yazıldı və son üç ədədi yeni fayla əlavə olundu.')
