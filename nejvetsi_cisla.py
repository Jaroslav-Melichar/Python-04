list = [];
def my_function(list):
  return list[::-1];
number = int(input('Kolik čísel chcete napsat: '));
for n in range(number):
    numberbers = int(input('Zadejte číslo: '));
    list.append(numberbers);
print("Největší číslo je:", max(list));

my_function(list);