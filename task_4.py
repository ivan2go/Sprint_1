new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(-1)) #смена статуса

new_tasks.remove('task_007') #удоляем

print(new_tasks[-1]) #асап таска


#print(new_tasks, 'новые')
#print(completed_tasks, 'готовые')