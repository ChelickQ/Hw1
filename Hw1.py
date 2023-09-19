# a = int(input('Введите сторону а: '))
# b = int(input('Введите сторону b: '))
# c = int(input('Введите сторону с: '))

# def side_compare(x, y, z):
#     if (x + y > z) and (x + z > y) and (y + z > x): 
#         return True
#     else:
#         return False 
# def triangle_type(x, y, z):
#     if x == y and x == z and z == y:
#         return 0
#     elif x == y or x == z or z == y:
#         return 1
#     else:
#         return 2

# if not side_compare(a, b, c):
#     print('Такой треугольник не существует')
# else:
#     if triangle_type(a, b, c) == 0:
#         print('Треугольник равносторонний')
#     if triangle_type(a, b, c) == 1:
#         print('Треугольник равнобедренный')
#     if triangle_type(a, b, c) == 2:
#         print('Треугольник разносторонний')





# def is_prime(number):
#     count = 0
#     for num in range(1, number + 1):
#         if number % num == 0:
#             count += 1
#     if count == 2:
#         return True
# flag = True    
# while flag:
#     user_num = int(input('Введите число от 1 до 100000: '))
#     if 100000 > user_num > 0:
#         flag = False
#     else:
#         print('Ошибка! Введено неверное число')
# if is_prime(user_num):
#     print('Число простое')
# else:
#     print('Число составное')




# from random import randint
# num = randint(0, 1000)
# count = 10

# K = int(input('Введите число между 0 и 1000 '))

# while count > 0:  
#     print('Попытка', count)
#     count -= 1 
    
#     if K < num:
#         print('Ваше число меньше')
#         K=int(input("Повторите попытку: "))
#     elif K > num:
#         print('Ваше число больше')
#         K = int(input("Повторите попытку: "))
#     else:
#         break

# else:
#     print('Исчерпаны все попытки, загаданное число', num)
#     quit()

# print('Вы угадали число ', num)