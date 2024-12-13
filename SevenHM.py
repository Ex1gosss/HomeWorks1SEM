###1
def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        print("Пожалуйста, введите положительное целое число.")
        return
    
    try:
        with open(file, 'r') as f:
            all_lines = f.readlines()
            last_lines = all_lines[-lines:]  
            for line in last_lines:
                print(line.strip())  
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


read_last(3, 'article.txt')


###4
def main():
    
    filename = input("Введите имя файла (без расширения): ") + ".txt"
    
    
    with open(filename, 'w', encoding='utf-8') as file:
        print("Введите строки для записи в файл. Для сохранения файла введите пустую строку.")
        
        while True:
            line = input()  # Запись строки
            
            
            if line == "":
                print(f"Файл '{filename}' сохранен.")
                break
            
            
            file.write(line + '\n')

if __name__ == "__main__":
    main()

