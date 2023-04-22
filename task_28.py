# def rec_sum(a,b):
#     if a+b <= 100:
#         if a > 0 and b > 0:
#             print(a,b)
#             print(a+b)
#     else:
#         if a < 0:
#             print("Число а является отрицательным и не соотвествует условию задачи")
#         else: 
#             print("Число b является отрицательным и не соотвествует условию задачи")        
# rec_sum(1,2)

a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))

def rec_sum(a, b):
    if a == 0:
        return b
    else:
        return rec_sum(a - 1, b + 1)
    
print(rec_sum(a, b))