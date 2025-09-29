# To-Do List Manager

def display_menu():
    print("\nTo-Do List Manager")
    print("1. 添加新任务")
    print("2. 显示所有任务")
    print("3. 标记任务已完成")
    print("4. 退出")

def add_task(tasks):
    task = input("请输入新任务：")
    tasks.append({"task": task, "completed": False})
    print(f"任务 '{task}' 已添加！")

def show_tasks(tasks):
    if not tasks:
        print("当前没有任务。")
    else:
        print("\n任务清单：")
        for i, task in enumerate(tasks, start=1):
            status = "已完成" if task["completed"] else "未完成"
            print(f"{i}. {task['task']} [{status}]")

def mark_task_completed(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("请输入要标记完成的任务编号："))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print(f"任务 '{tasks[task_number - 1]['task']}' 已标记为完成！")
            else:
                print("无效的任务编号。")
        except ValueError:
            print("请输入有效的数字。")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("请选择操作：")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("退出程序。")
            break
        else:
            print("无效的选择，请重试。")

if __name__ == "__main__":
    main()