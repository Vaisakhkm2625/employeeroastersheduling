import itertools

employees = [
        "vaisakh",
        "vrishali",
        "prasanth",
        "aasiq",
        "devi",
        "vineeth",
        "likhith",
        "arun"
        ]


weeklist = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        ]

shifts = [
        "morning",
        "noon",
        "night"
        ]


def condition(week,shift,i):
    con = not((week == 'monday' or week == 'friday') and i==1 and shift=='noon')
    return con

def employee_condition(week,shift,i,employee):
    con = not(week == 'monday' and employee== 'vaisakh')
    return con


employees_iter = itertools.cycle(employees)
employee_stack = []

def next_employee(week,shift,i,employee):
    pass






l = list(zip(employees[::2],employees[1::2]))
# for i in l:
#     print(i)


for week in weeklist:
    print("{:<10}".format(week),':', end = '')
    for shift in shifts:
        shiftmembers= ''
        for i in range(2):

            next_emp  = ''
            if len(employee_stack) == 0:
                next_emp = next(employees_iter)
            else:
                next_emp = employee_stack.pop()

            if condition(week,shift,i):
                shiftmembers+=(next_emp+"/")
            else:
                employee_stack.append(next_emp)
            
        print("{:<20}".format(shiftmembers), end = '')
        print(end=' ')
    print()


