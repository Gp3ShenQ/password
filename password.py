# password = 'a123456'

# key = input('請輸入密碼: ')

x = 2
while x+1:
    password = 'a123456'
    key = input('請輸入密碼: ')
    if x == 0:
        break
    elif key != password :
        print('密碼錯誤!還有', x ,'次機會')
        x -= 1
    elif key == password:
        print('登入成功!!!!')
        break

