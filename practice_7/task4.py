while True:
  action = input("Введите номер действия (1, 2 или off):\n>>>")
  if action == "1":
    preference = input("Введите предпочтение:\n>>>")
    if prefernce == "спорт":
      print("рекомендация: подкаст убойный спорт")
    else:
      print("рекомендация: новый альбом канье уэста")
  elif action == "2":
    attemts = 3
    for attemt in range(1, attemts +1):
      guess = input(название музыкальной группы:\n>>>")
      if guess == "quenn":
        print("вы выиграли билет на концерт!")
        break
    else: 
      print("Попытки закончились. Правильный ответ: Queen")
  elif action == "off":
    print("Програма завершена")
    break 
else:
  print("Неверный ввод. Попробуйте снова")
