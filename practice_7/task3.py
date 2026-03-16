corname = "FIFA"
attemts = 3
for attemt in range(1, attemts + 1):
  guess = input("Название игры:\n>>>")
  if guess == corname:
    print(f"Поздравляем! Вы угадали с попытки номер №{answer}")
    break   
else:
  print("Попытки закончились. Правильный ответ: FIFA")
