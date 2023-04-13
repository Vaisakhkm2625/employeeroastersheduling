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

#employees_iter = itertools.cycle(employees)
employee_stack = []


class track_employees:

    def __init__(self,employees):
        self.employees_list=employees;
        self.itr = 0;

    def inc_itr(self):
        self.itr+=1
        if len(self.employees_list)==self.itr:
            self.itr=0


    def next_employee(self,week,shift,member_num):
        self.inc_itr()
        emp =''
        for i in list(range(self.itr,len(self.employees_list)))+list(range(0,self.itr)):
            if employee_condition(week,shift,member_num,self.employees_list[i]):
                tmpemp=self.employees_list.pop(i)
                self.employees_list.insert(i,tmpemp)
                emp = self.employees_list[self.itr];
                #print(self.employees_list)
                break;
        if emp == '' :
            emp = 'no emp avaiable'

        return emp


    def employee(self,week,shift,member_num):
        if condition(week,shift,member_num):
            emp = self.next_employee(week,shift,member_num)
        else:
            emp = ''

        return emp


# l = list(zip(employees[::2],employees[1::2]))
# for i in l:
#     print(i)
te = track_employees(employees)

for week in weeklist:
    print("{:<10}".format(week),':', end = '')
    for shift in shifts:
        shiftmembers= ''
        for i in range(2):

            # next_emp  = ''
            # if len(employee_stack) == 0:
            #     next_emp = next(employees_iter)
            # else:
            #     next_emp = employee_stack.pop()

            # if condition(week,shift,i):
            next_emp= te.employee(week,shift,i)
            shiftmembers+=(next_emp+"/")
            # else:
            #     employee_stack.append(next_emp)
            
        print("{:<20}".format(shiftmembers), end = '')
        print(end=' ')
    print()


