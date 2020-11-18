# from collections import deque
#
# number_organisations = int(input('Enter how many organisations will be: '))
# counter = 0
# org_info = deque()
#
# for i in range(number_organisations):
#     quarter = 1
#     new_org_info = list()
#     name_org = input('Enter a name of organisation: ')
#     new_org_info.append(name_org)
#     for x in range(4):
#         quarter_info = ()
#         quarter_value = int(input(f'Enter value for the quarter: '))
#         new_org_info.append(quarter_value)
#     quarter_sum = new_org_info[1] + new_org_info[2] + new_org_info[3] + new_org_info[4]
#     new_org_info.append(quarter_sum)
#     org_info.append(new_org_info)
# print(*org_info, sep='\n')
#
# # Print the average income for all organisations
# av_income = 0
# for i in range(len(org_info)):
#     av_income += org_info[i][5]
# print(f'The average of all organisations is {av_income / len(org_info)}')
#
# # Determine which organisations in profit and which ones in minus
# profit_list = []
# minus_list = []
# av_income_list = []
#
# for i in range(len(org_info)):
#     if int(org_info[i][5]) > int(av_income):
#         profit_list.append(org_info[i][0])
#     elif int(org_info[i][5]) < int(av_income):
#         minus_list.append(org_info[i][0])
#     else:
#         av_income_list.append(org_info[i][0])
#
# print(f'profit list {profit_list}')
# print(f'minus_list {minus_list}')
# print(f'av_income_list {av_income_list}')

# if len(profit_list) != 0 and len(minus_list) != 0:
#     print(f'The company {i} has a profit.' for i in profit_list)
#     print(f'The company {j} has NO a profit.' for j in minus_list)
# elif (len(profit_list) == 0) or (len(minus_list) == 0):
#     if len(profit_list) == 0:
#         print(f'The company {j} has NO a profit.' for j in minus_list)
#     if len(minus_list) == 0:
#         print(f'The company {i} has a profit.' for i in profit_list)
# elif (len(profit_list) == 0) and (len(minus_list) == 0) and len(av_income_list) != 0:
#     print(f'The company {i} has an average profit.' for z in av_income_list)


# =====================================================================================================================
#  Solution from teacher

# from collections import namedtuple
#
# all_comp = []
#
# Comp = namedtuple('Comp', 'name, p1, p2, p3, p4, total')
# num = int(input('num = : '))
# for i in range(num):
#     name = input('name = ')
#     spam = []
#     for j in range(1, 5):
#         spam.append((int(input(f'{j} = '))))
#     all_comp.append(Comp(name, *spam, sum(spam)))
#
# print(all_comp)

# =====================================================================================================================
from collections import namedtuple, deque

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input('Enter the number of companies: '))
total_profit = 0

for i in range(1, num +1):
    profit = 0
    quarters = []
    name = input(f'Enter the name of company {i}: ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Profit for {j +1} quarter: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'\n The average profit is {average}')

# version 1

print(f'\n Companies with income higher than average:')
for comp in all_companies:
    if comp.profit > average:
        print(f'The company {comp.name} has profit {comp.profit}')
        # print((comp.quarters[0])) # print info about required quarter

print(f'\n Companies with income less than average:')
for comp in all_companies:
    if comp.profit < average:
        print(f'The company {comp.name} has profit {comp.profit}')

# version 2
print('*'*60)
sort_comp = deque([None])
for comp in all_companies:
    if comp.profit > average:
        sort_comp.append(comp)
    elif comp.profit < average:
        sort_comp.appendleft(comp)

text = 'less'

for comp in sort_comp:
    if comp is None:
        text = 'Higher'
    else:
        print(f'The company {comp.name} has got {text}, then average profit - {comp.profit}')





