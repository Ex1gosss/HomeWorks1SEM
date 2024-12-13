###1
import re

def check_license_plate(plate):
    
    plate = plate.upper()
    plate = re.sub(r'[^АВЕKMНОРСТУХ0123456789]', '', plate)  # Оставляем только корректные символы
    
   
    private_car_pattern = r'^[АВЕKMНОРСТУХ]{1}\d{3}[АВЕKMНОРСТУХ]{2}\d{2,3}$'
    taxi_pattern = r'^[АВЕKMНОРСТУХ]{2}\d{3}\d{2,3}$'

    
    if re.match(private_car_pattern, plate):
        return "Частный легковой автомобиль"
    elif re.match(taxi_pattern, plate):
        return "Такси"
    else:
        return "Неверный номер"


if __name__ == "__main__":
    license_plate = input("Введите номер: ")
    result = check_license_plate(license_plate)
    print(result)


###2
with open('text.txt',) as file:
    word_count = sum(len(line.split()) for line in file)

print(word_count)

###3
import re

text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
updated_text = re.sub(r'\b(2[0-3]|[01]?[0-9]):([0-5][0-9])(:([0-5][0-9]))?\b', '(TBD)', text)

print(updated_text)

###4
import re

text = "Владимир устроился на работу в одно очень важное место. И в первом же документе ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п."
abbreviations = re.findall(r'\b[A-ZА-Я]{2,}(?:\s+[A-ZА-Я]{2,})*\b', text)

print(abbreviations)
