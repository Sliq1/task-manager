import add
import show
import update
import delete

add_tasks_response = add.add_tasks("sleep")
print(add_tasks_response)

show_tasks_response = update.update_tasks("sleep", "wake up")
print(show_tasks_response)

delete_tasks_response = delete.delete_tasks("wake up")
print(delete_tasks_response)
# Removed incomplete function definition
print("Hello World")
print(2+2)
