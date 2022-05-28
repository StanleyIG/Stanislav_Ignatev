job_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(job_name)):
        job_name[i] = job_name[i].split()[-1].capitalize()
        job_name[i] = f'Привет {job_name[i]}'
print(', '.join(job_name))