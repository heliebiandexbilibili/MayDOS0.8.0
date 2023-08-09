"""
colorama现已弃用

字体样式 -->
Font.BLACK     : 黑色
Font.RED       : 红色
Font.GREEN     : 绿色
Font.YELLOW    : 黄色
Font.BLUE      : 蓝色
Font.VIOLET    :
Font.BEIGE     : 青蓝色
Font.WHITE     : 白色

字体背景样式 -->
Font.BLACK     : 黑色
Font.RED       : 红色
Font.GREEN     : 绿色
Font.YELLOW    : 黄色
Font.BLUE      : 蓝色
Font.VIOLET
Font.WHITE     : 绿色

字体特性/特效 -->
Font.END       : 终端默认设置
Font.BOLD      : 高亮显示
Font.ITALIC    : 斜体文本
Font.URL       : 下划线
Font.BLINK     : 闪烁
Font.BLINK2    : 未知
Font.SELECTED  : 反显

系统颜色表示说明 -->
绿色：提示，正确
红色：警告，错误
黄色：警告，错误（比红色弱一点）
浅蓝色/青蓝色/蓝色：信息，属性
紫红色：暂定
黑色：无（黑色哪看得见？）
"""
try:
    import wget, json, requests
    import os, sys, asyncio, tkinter.messagebox
    import base64
    from time import sleep
except Exception as e:
    print(f"{e}\n")
    os.system(r'install.bat')
    os.system(r'cls')
    quit()
    
os.system(r'title MayDOS') # 更改标题

# 环境设置
if os.name == "nt":
    os.system("")
    
# 自动生成/补全 部分文件
DIR_LIST = ['MayDOS_Login/', 'important/', 'important/Applications', 'important/log', 'important/download', 'important/download/per.txt']
for dir in DIR_LIST:
    if dir != DIR_LIST[-1]: 
        if os.path.isdir(dir) == False:
            os.makedirs(dir)
    else:
        if os.path.isdir(dir) == False:
            with open('important/download/per.txt','w') as f:
                f.write('root')

# 彩色自定义文本
class Style:
    END = '\33[0m'
    BOLD = '\33[1m'
    ITALIC = '\33[3m'
    URL = '\33[4m'
    BLINK = '\33[5m'
    BLINK2 = '\33[6m'
    SELECTED = '\33[7m'

class Font:
    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'

class Background:
    BLACK = '\33[40m'
    RED = '\33[41m'
    GREEN = '\33[42m'
    YELLOW = '\33[43m'
    BLUE = '\33[44m'
    VIOLET = '\33[45m'
    BEIGE = '\33[46m'
    WHITE = '\33[47m'

# 系统权限API
class SysPerAPI():
    def __init__(self,Per : str = 'sys') -> None:
        self.Per = Per
        return None

    def cls(self) -> int:
        try:
            os.system('cls')
            return 200
        except Exception as e:
            print(f'{Font.RED}MayDOS/ROOT/ERROR>>>{e}{Font.WHITE}')
            return 400

    def CreatSysFile(self,path : str = '',context : str = 'Test') -> int:
        try:
            if self.Per == 'sys':
                with open(path,'w',encoding='utf-8') as f:
                    f.write(f'SYS_FILE\n{context}')
                    f.close()
                return 200
            elif self.Per != 'sys':
                print(f'{Font.YELLOW}权限不足{Font.WHITE}')
                return 201
            else:
                print(f'{Font.YELLOW}Unknown permissions: {self.Per}{Font.WHITE}')
                return 202
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}{Font.WHITE}')
            return 400

    def JsonFileRead(self,path):
        try:
            with open(path,'r') as f:
                __date = f.read()
                f.close()
                return __date
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}')

# 创建更新检测函数
async def check_update_bar():
    task = asyncio.create_task(check_update())
    for i in range(1, 101):
        print("\r", end="")
        print("检测更新中: {}%: ".format(i), "▋" * (i // 2), end="")
        sys.stdout.flush()
    await task    
    
async def check_update():
    # 读取更新日志
    Update = json.loads(requests.get("https://buelie.github.io/MayDOS/config.json").text)

    # 比较版本号
    if Update["latest"]["default"] != CODE:
        Y_N_U = tkinter.messagebox.askyesno(title='更新提示',message=f'有可用更新，是否下载?\n当前版本: {CODE} -> {Update["latest"]["default"]}\n稍等一下，马上就好，在important/download/找到更新程序并运行即可')
        
        if Y_N_U == True:   # 如果条件为真则执行该线程

            # 检测文件是否存在,如果存在则执行销毁操作
            if os.path.isfile('update.py'):
                os.remove("update.py")
            else:
                pass

            # 下载更新文件并运行
            wget.download("https://buelie.github.io/MayDOS/Update/update.py","")
            os.system("START update.py")
            print("\n")
            
            # 退出线程
            quit()
        else:
            os.system("cls")
    else:
        os.system("cls")

# 变量设置
error_version_file_not_found = False
error_account_file_not_found = False
PYTHON_PROGRAM = "python3.11.exe"

try:
    ver_open= open('important/Version.ver', mode='r')
    ver_open.seek(0, 0)
    CODE = ver_open.read()
except FileNotFoundError:
    error_version_file_not_found = True

# 以asyncio调用check_update_bar函数
asyncio.run(check_update_bar())

# 打印动画
with open("important/icon.txt", "r") as icon:
    for text in icon.readlines():
        print(text)

try:
    account_open = open('important/account.user',mode='r')
    account_info = account_open.readlines()

    un_username = account_info[0]
    username = un_username[0:-1]

    un_password = account_info[1]
    password = un_password[0:-1]

    account_open.close()
    
    try:
        username = str(base64.b64decode(username),'utf-8')
        password = str(base64.b64decode(password),'utf-8')
    except Exception as e:
        print(f'{Font.RED}ERROR: 账户信息加载失败，账户文件可能损坏，请尝试注销并重新注册{Font.WHITE}')
        print(f'{Font.RED}错误信息：{Font.WHITE}')
        print(e)
        input('按下回车键退出. . .')
        quit()
    
except FileNotFoundError:
    error_account_file_not_found = True

if error_account_file_not_found == True and error_version_file_not_found == False:
    print(f'{Font.RED}未注册或账户文件异常丢失,可尝试启动OOBE修复{Font.WHITE}')
    input('按下回车键退出. . .')
    quit()
elif error_version_file_not_found == True and error_account_file_not_found == False:
    print(f'{Font.RED}系统版本文件被移动或异常丢失，请尝试联系我们以修复,可尝试启动OOBE修复{Font.WHITE}')
    input('按下回车键退出. . .')
    quit()
elif error_account_file_not_found  and error_version_file_not_found == True:
    print(f'{Font.RED}未找到系统版本文件及账户文件,可尝试启动OOBE修复{Font.WHITE}')
    print(f'{Font.RED}请确认是否注册并尝试联系我们,可尝试启动OOBE修复{Font.WHITE}')
    input('按下回车键退出. . .')
    quit()
    
print(f'{Font.GREEN}欢迎{Font.WHITE}')

while True:
    if username == 'TEST':
        print(account_info)
        print(f'{Font.BLUE}测试账户登录{Font.WHITE}')
    else:
        print(f'{Font.BEIGE}登录{username}的电脑{Font.WHITE}')
    
    if username == 'TEST':
        break
    else:
        userspassword = input('密码>')

    if userspassword == password:
        print(f'{Font.GREEN}密码正确{Font.WHITE}')
        break
    else:
        print(f'{Font.RED}密码错误！{Font.WHITE}')
        pass

sleep(0.25)
SysPerAPI().cls()

print(f'{Font.GREEN}正在准备你的MayDOS命令行......{Font.WHITE}')
print(f'{Font.GREEN}请输入"usebook"以打开MayDOS{CODE}的使用手册和帮助{Font.WHITE}')

while True:
    cmd = input('MayDOS/Root>>>')

    if cmd.lower() == 'calc':
        os.system(f"{PYTHON_PROGRAM} important/Applications/calc.py")

    elif cmd[0:3].lower() == 'sof':
        try:
            if cmd[4:-1] == 'json':
                print(f"{Font.RED}MayDOS/Root>>>该文件您无权访问")
            elif cmd[4:-1] == 'api' or cmd[4:-1] == 'api.py':
                print(f"{Font.RED}MayDOS/Root>>>该文件您无权访问")
            else:
                if os.path.isfile(f'important/Applications/{cmd[4:-1]}/{cmd[4:-1]}.json') == False or os.path.isfile(f'important/Applications/{cmd[4:-1]}/{cmd[4:-1]}/MAIN.txt') == False:
                    print(f'{Font.YELLOW}MayDos/Root/SOF>>>应用程序"{cmd[4:-1]}"可能已被恶意篡改,请谨慎运行。（Y/N)')
                    Warn_0 = input()
                    Warn_0 = Warn_0.lower()
                    if Warn_0 == 'y' or Warn_0 == 'yes':
                        try:
                            os.system(f'START /MAX "important/Applications/{cmd[4:-1]}/{cmd[4:-1]}.bat"')
                        except Exception as e:
                            print(f'{Font.RED}MayDOS/Root>>>{e}')
                    elif Warn_0 == 'n' or Warn_0 == 'not':
                        pass
                    else:
                        print("未知操作，已自动退出...")
        except Exception as e:
            print(f'{Font.RED}MayDOS/Root>>>{e}')

    elif cmd[0:4].lower() == 'down':
        print("=======================================")
        print("|请选择下载源                         |            \n|1.STORE 默认的应用商店 2.HTTP网络渠道|\n|3.退出                               |")
        print("=======================================")
        DOWN_INPUT = input("MayDOS/download>>>")
        if DOWN_INPUT == '1':
            print("======================================================")
            print("已选择下载源<STORE>,可下载已上传的应用,输入EXIT以退出|")
            print("======================================================")
            while True:
                D_I_0 = input("MayDOS/Download/STORE>>>")
                D_I_0 = D_I_0.lower()
                if D_I_0 == 'exit':
                    break

        elif DOWN_INPUT == '2': 
            print("=========================================================")
            print("已选择下载源<HTTP>,可下载任何网络上的应用,输入EXIT以退出|")
            print("=========================================================")
            while True:
                D_I_0 = input("MayDOS/Download/STORE>>>")
                if D_I_0.lower() == 'exit':
                    break
                else:
                    wget.download(f'{D_I_0}',"important/download/")

        elif DOWN_INPUT == '3' or DOWN_INPUT == '': 
            pass
        else:
            print("未知操作,已自动退出......")
            print("===================================================")

    elif cmd.lower() == "":
        pass

    elif cmd[0:6].lower() == 'search':
        search_cmd = r'START https://cn.bing.com/search?q='+cmd[7:]+'&cvid=aff84598b5bf4a62acc130c33917054f&aqs=edge..69i57j0l3j69i59l2j69i60l3.1183j0j4&FORM=ANAB01&PC=U531'
        try:
            try:
                os.popen(search_cmd)
            except Exception as e:
                os.popen(search_cmd)
                print(" ")
            else:
                print(" ")
        except Exception as e:
            os.popen(search_cmd)
            print(" ")

    elif cmd.lower() == 'usebook' or cmd.lower() == 'help':
        with open("important/usebook.txt", "r", encoding="utf-8") as menu:
            for text in menu.readlines():
                print(f"{Font.GREEN}{text}{Font.WHITE}")

    elif cmd.lower() == 'close':
        quit()

    elif cmd.lower() == 'menu':
        pass

    elif cmd.lower() == 'shut':
        if input("{Font.RED}确认关机（这可不是闹着玩的）？{Font.WHITE}[Y/N]") == "Y":
            if sys.platform == 'win32':
                os.system('shutdown -p')
            elif sys.platform == 'linux':
                os.system('shutdown –h now')
            elif sys.platform == 'darwin':
                os.system('sudo shutdown -h now')
            else:
                os.system('shutdown -p')
        else:
            break

    elif cmd.lower() == 'notepad':
        try:
            ENCO_FILE = 'w'

            print('\n选择编辑模式 -->')
            print('1.正常写入')
            print('2.系统权限写入')
            print('3.特殊文件写入')

            print(f'{Font.YELLOW}================')
            print(f'{Font.BEIGE}exit        退出')
            print(f'{Font.BEIGE}path    文件路径{Font.WHITE}\n')
            print(f'{Font.BEIGE}enco    读取方式{Font.WHITE}\n')

            Notepad = input('MayDOS/Apply/NOTEPAD>>>')

            if Notepad == 'exit':
                print('\n')
            elif Notepad == '1':
                print(f'模式:正常写入\n')
                CFILE = input("MayDOS/Apply/NOTEPAD/CreatFile>>>")
                with open(CFILE,ENCO_FILE,encoding='utf-8') as f:
                    f.write(CFILE)
                    f.close()
            #SysPerAPI().cls()
            #os.system('python important/Applications/Notepad/Notepad.py')

        except Exception as e:
            print(f'{Font.RED}MayDOS/Root/ERROR>>>{e}{Font.WHITE}')

    elif cmd.lower() == 'explorer':
        try:
            SysPerAPI().cls()
            os.system('python important/Applications/Explorer/Explorer.py')
        except:
            print(f'{Font.RED}找不到{cmd}应用程序{Font.WHITE}')

    elif cmd.lower() == 'cls':
        SysPerAPI().cls()

    elif cmd == username:
        List_RAN = ['MayDOS有摸鱼部门和搞事部门！','0.4.1是0.4.2之前最多BUG的版本',
        'MayDOS其实从0.4.0开始就有可安装版本了呢~','MayDOS的安装版本自动更新会报错！',
        'MayDOS现在已经有很多人参与开发了呢','MayDOS的开发人员似乎对MayDOS没有激情',
        'MayDOS的软件API其实和TinOS一样','MayDOS的软件可以无缝移植到TinOS哦!~',
        '其实OOBE中的更新通道仔细一看就感觉不对劲','你知道MayDOS其实在0.4以后有了阁小小的GUI吗？']
        for text in List_RAN:
            print(text)
    
    elif cmd.lower() =='sysver':
        print(f'系统版本：MayDOS {CODE}')
        print('\n开发：MayDOS开发团队 版权所有2023(C)')
    else:
        print(f"{Font.YELLOW}未定义的指令，请输入'usebook'以查看使用手册和帮助{Font.WHITE}")