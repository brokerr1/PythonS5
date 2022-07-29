#Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#Пример:
#[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
#[1, 5, 2, 3, 4, 1, 7] => [1, 5]

nums = [1, 5, 2, 3, 4, 6, 1, 7]

# Первый вариант

def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))

# Второй вариант

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups

print(get_up(nums))