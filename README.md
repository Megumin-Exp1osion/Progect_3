# Progect_3
Третий проект в Яндекс Лицее 
 
Описание:
 Данный проект включает в себя код для бота в Discord :).
 
Функции и команды: 
 Данный бот несёт под собой префикс "$$":
 
 "$$new" - функция, создающая новую игру.
     Не принимает никаких аргументов. При вызове создаёт выплывающий список, создающий новую игру:
      Доступные игры:
       1) "Подброс монетки 1 на 1"',
       2) "Камень, ножницы, бумага",
       3) "Подброс двух кубиков"
       
     После создания игры будет написано, кто создал игру и с каким id.
 
 "$$join <id>" - функция, присоединяющая пользователя к игре.
     Принимает аргумент <id> - id игры, к которой нужно подключиться.
     Если лимит игроков достигнут, начинается процесс игры
  
  "$$choice <id>" - функция, используемая для игры "Камень, ножницы, бумага".
     Принимает аргумент <id> - id игры, в которой нужно сделать выбор.
     После вызова создаёт всплывающий список, в котором нужно сделать выбор.
  
  "$$del <col>" - вспомогательная функция.
     Принимает аргумент <col> - количество строк которые нужно удалить (БЕЗВОЗВРАТНО).
  
  "$$cat" - функция для котиков.
     Не принимает никаких аргументов, а только выводит вам котика для поднятия настроения :)
  
  "$$dog" - функция для котиков.
     Не принимает никаких аргументов, а только выводит вам собачку для поднятия настроения :)
  
  
  
 
