Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#!/usr/bin/env python3
"""简单计算器 - 支持加减乘除四则运算"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "错误：除数不能为零！"
    return x / y

def main():
    print("=" * 40)
    print("       简单计算器")
    print("=" * 40)
    print("\n选择运算：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 退出")
    
    while True:
...         choice = input("\n请输入选择 (1/2/3/4/5): ")
...         
...         if choice == '5':
...             print("👋 再见！")
...             break
...         
...         if choice not in ['1', '2', '3', '4']:
...             print("❌ 无效输入，请重新选择！")
...             continue
...         
...         try:
...             num1 = float(input("请输入第一个数字："))
...             num2 = float(input("请输入第二个数字："))
...         except ValueError:
...             print("❌ 请输入有效的数字！")
...             continue
...         
...         if choice == '1':
...             result = add(num1, num2)
...             symbol = "+"
...         elif choice == '2':
...             result = subtract(num1, num2)
...             symbol = "-"
...         elif choice == '3':
...             result = multiply(num1, num2)
...             symbol = "*"
...         elif choice == '4':
...             result = divide(num1, num2)
...             symbol = "/"
...         
...         if isinstance(result, str):
...             print(f"\n{result}")
...         else:
...             print(f"\n结果：{num1} {symbol} {num2} = {result}")
... 
... if __name__ == "__main__":
...     main()
>>> [DEBUG ON]
>>> [DEBUG OFF]
