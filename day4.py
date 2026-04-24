#coding=utf-8
arr = []
while True:
    print("===== 待办事项清单 =====")
    print("1.查看所有任务")
    print("2.添加任务")
    print("3.删除任务")
    print("0.退出")
    print()
    print("请选择(0-3):")
    n = int(input())
    if n == 2:
        print("请输入新任务:")
        rw = input()
        arr.append(rw)
    elif n == 1:
        print("你的任务:")
        for i in range(len(arr)):
            print(f"{i+1}.{arr[i]}")
    elif n == 3:
        print("请输入要删除任务的编号:")
        bh = int(input())
        name = arr[bh-1]
        arr.pop(bh-1)
        print(f"已删除:{name}")
    elif n == 0:
        exit()

