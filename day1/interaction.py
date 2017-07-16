# Author:Scott She

name = input("name ")
age = int(input("age "))
job = input("job ")
salary = float(input("salary "))
print(type(name), type(age), type(job), type(salary))

info1 = """ 
---------------- info of %s ------------------
Name: %s
Age: %d
Job: %s
Salary: %.1f
""" % (name, name, age, job, salary)
print(info1)

info2 = '''
---------------- info of {_name} ------------------
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)
print(info2)

info3 = '''
---------------- info of {0} ------------------
Name: {0}
Age: {1}
Job: {2}
Salary: {3}
'''.format(name,
           age,
           job,
           salary)
print(info3)

# 以上三种字符串格式化, 一般都会用第二种



