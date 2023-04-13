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


print("----- condition: 'monday' or 'friday' 'noon' only 1st member necessary")
print("----- condition: employee:'vaisakh' leave on week:'monday'")
def condition(week,shift,i):
    con = not((week == 'monday' or week == 'friday') and i==1 and shift=='noon')
    return con

def employee_condition(week,shift,i,employee):
    con = True 
    con = not(week == 'monday' and employee== 'vaisakh')
    return con




#employees_iter = itertools.cycle(employees)
employee_stack = []


class track_employees:

    def __init__(self,employees):
        self.employees_list=employees;
        self.itr = -1;

    def inc_itr(self):
        self.itr+=1
        if len(self.employees_list)==self.itr:
            self.itr=0


    def next_employee(self,week,shift,member_num):
        self.inc_itr()
        emp =''
        for i in list(range(self.itr,len(self.employees_list)))+list(range(0,self.itr)):
            #print('|n|',end='')
            #print(employee_condition(week,shift,member_num,self.employees_list[i]),end='')
            if employee_condition(week,shift,member_num,self.employees_list[i]):
                tmpemp=self.employees_list.pop(i)
                self.employees_list.insert(self.itr,tmpemp)
                emp = self.employees_list[self.itr];
                #print(tmpemp,end='')
                #print(self.itr,':',i,end='')
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

            next_emp= te.employee(week,shift,i)
            shiftmembers+=(next_emp+"/")
            
        print("{:<25}".format(shiftmembers), end = '')
        print(end=' ')
    print()


