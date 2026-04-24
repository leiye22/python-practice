#coding=utf-8
import json
file_name =r"D:\pycharm\PyCharm Community Edition 2021.3\一周小任务\task_list.json"
def load_task():
    with open(file_name,'r',encoding='utf-8') as f:
        return json.load(f)

def save_task(tasks):
    with open(file_name,"w",encoding='utf-8') as f:
        json.dump(tasks,f,ensure_ascii=False,indent=2)

def show_task(tasks):
    if not tasks:
        print("暂无任务")
    else:
        print("你的任务：")
        for idx,t in enumerate(tasks,1):
            print(f"{idx},{t}")

def add_task(tasks):
    print("请输入要添加的任务:")
    new = input()
    tasks.append(new)
    save_task(tasks)

def del_task(tasks):
    print("请输入要删除任务的编号:")
    num = int(input())
    name = tasks[num-1]
    tasks.pop(num-1)
    print("已删除:"+name)

def main():
    tasks = load_task()
    while True:
        print("===== 待办任务清单 =====")
        print("1.查看所有任务")
        print("2.添加任务")
        print("3.删除任务")
        print("0.退出")
        print("请输入(0-3):")
        choice = int(input())
        if choice == 1:
            show_task(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            del_task(tasks)
        elif choice == 0:
            exit()
if __name__ == '__main__':
    main()



