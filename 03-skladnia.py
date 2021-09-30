usser_choice  = -1
tasks = []
def show_tasks():
    task_index = 0
    for task in tasks:
        print( str(task_index) + '.' + task )
        task_index += 1

def add_task():
    task = input('Wpisz trasć zadania: ')
    tasks.append(task)
    print('Dodano zadanie!')

def del_task():
    task_index = int(input('Podaj index zadania: '))
    if task_index < 0 or task_index > len(tasks)-1:
        print('Indeks poza zakresem')
        return
    tasks.pop(task_index)
    print('Zadanie zostałusunięty')

def save_task_to_file():
    file = open("tasks.txt", "w", encoding="utf-16")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def lode_task_from_file():
    try:
        file = open("tasks.txt", "r", encoding="utf-16")
        for line in file.readline():
            tasks.append(line.strip())
        file.close()
    except:
        return
lode_task_from_file()
while usser_choice !=5:
    if usser_choice == 1:
        show_tasks()
    
    if usser_choice == 2: 
        add_task()
    if usser_choice == 3: 
        del_task()
    if usser_choice == 4: 
        save_task_to_file()
    print()        
    print('1. Pokż zadania')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Zapisz zadania do pliku')
    print('5. Wyjdź!')
    print()
    usser_choice = int(input('Wybierze opcje: '))

