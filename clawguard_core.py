import os
import sys
import time

# 初始化 Windows 的色彩支持
if sys.platform.startswith('win'):
    os.system('')

# 定义黑客风高级色彩代码
C_CYAN = '\033[96m'   # 科技青 (给LOGO和系统提示)
C_RED = '\033[91m'    # 警报红 (给拦截高亮)
C_GREEN = '\033[92m'  # 安全绿 (给放行提示)
C_YELLOW = '\033[93m' # 警告黄 (给命令确认)
C_RESET = '\033[0m'   # 恢复默认颜色

# ClawGuard 品牌增强版 ASCII LOGO (自带科技青色渲染)
BRAND_LOGO = f"""{C_CYAN}
############################################################
#                                                          #
#   ______ _                _____                      _   #
#  / _____) |              / ___ \                    | |  #
# | /     | | _____ _ _ _ | |   | | _   _ _____  ____ _   | |  #
# | |     | |(____ | | | || |   | || | | (____ |/ ___/ _  | |  #
# | \_____| / ___ | | | || |___| || |_| / ___ | |  | |_| | |  #
#  \______)_\_____|\___/  \_____/  \____\_____|_|   \____|_|  #
#                                                          #
#              Z E R O - T R U S T   A G E N T   O S       #
#                 E N T E R P R I S E   M V P              #
############################################################{C_RESET}
"""

def clawguard_intercept(command):
    # 高危动作黑名单
    dangerous_keywords = ["del", "rm", "curl", "wget", "format", "ftp", "send", "upload"]
    is_dangerous = any(keyword in command.lower() for keyword in dangerous_keywords)

    print(f"\n{C_CYAN}[ClawGuard-Proxy] 正在对指令进行安全审计...{C_RESET}")
    time.sleep(0.5) # 模拟审计耗时，增加专业感

    if is_dangerous:
        print(f"\n{C_RED}🚨 [ClawGuard 高危拦截系统激活] 检测到未经授权的数据外发/系统变更请求！{C_RESET}")
        print(f"{C_YELLOW}⚠️ 目标系统命令: {command}{C_RESET}")
        print("-" * 60)
        choice = input("🛡️ 人类主管 (Root Admin)，是否对该操作授权放行？(Y/放行 / N/拒绝): ").strip().upper()

        if choice == 'Y':
            print(f"{C_GREEN}✅ 身份确认。操作已获临时授权。指令放行...\n{C_RESET}")
        else:
            print(f"{C_RED}🛑 授权拒绝！ClawGuard 已强行阻断该进程，并记录日志。企业数据安全得到保障。\n{C_RESET}")
    else:
        print(f"{C_GREEN}🟢 指令安全，合规性审计通过。放行执行...\n{C_RESET}")

if __name__ == "__main__":
    # 清屏，显示 LOGO
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

    print(BRAND_LOGO)
    print("等待 AI 智能体通过网络层下发指令... (输入 'exit' 退出系统)")
    print("="*60)
    
    while True:
        ai_cmd = input(f"\n🤖 {C_CYAN}[模拟 AI 生成的指令]{C_RESET} > ")
        if ai_cmd.lower() == 'exit':
            print("ClawGuard 企业级引擎已关闭。")
            break
        clawguard_intercept(ai_cmd)
