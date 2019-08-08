#coding=utf8
import os
import re
import xml.dom.minidom as xmldom
import time
 
class Mtest():
    def __init__(self):
        # 此处注意dir要切换到xml正确的路径
        dir = '/Users/lumi/Documents/monkey_test/monkey_config.xml'
        dom = xmldom.parse(dir)
        root = dom.documentElement

        # 获取xml中的package_name
        self.package_name = root.getElementsByTagName('packagename')[0].firstChild.data
        print(self.package_name)

        # 获取xml中的main_activity
        self.main_activity = root.getElementsByTagName('mainactivity')[0].firstChild.data
        print(self.main_activity)

        # 获取xml中的interval
        self.interval = int(root.getElementsByTagName('interval')[0].firstChild.data)
        print(self.interval)

        # 获取xml中的count
        self.count = int(root.getElementsByTagName('count')[0].firstChild.data)
        print(self.count)

        # 获取xml中的white_activity
        self.white_activity = root.getElementsByTagName('whiteactivity')[0].firstChild.data.replace('\n','').replace(' ','').split(',')
        print('self.white_activity:', self.white_activity)


    # 获取当前的activity，判断是否在白名单内，如果在就做操作，如果不在就拉回主页面
    def get_now_activity(self):
        # 获取当前连接的手机设备信息
        os.system("adb devices")

        # 获取当前页面的activity
        content = os.popen('adb shell dumpsys activity activities | grep  "Run"').read()
        print('当前页面activity:',content)


        # 过滤掉不必要的信息/.[a-zA-Z0-9]+
        pattern = re.compile(r'/[a-zA-Z0-9\.]+') 
        print('pattern:',str(pattern))

        # 过滤后的activity
        activity_list = pattern.findall(content)
        print('alist:',activity_list)

        # 拼接：
        current_activity = self.package_name + activity_list[0]
        print('currentActivity',current_activity)


        excute_shell = 'adb shell am start -n '+ self.main_activity
        print('excuteshell:',excute_shell)

        if len(activity_list) > 0:
            if current_activity not in self.white_activity:
                print('当前activity:' + activity_list[0])
                print('--------------开始返回主activity----------------')
                # 可拉回主页面
                os.system(excute_shell)
            else:
                print('当前activity:' + activity_list[0] + '不需要返回')


    def checkActivity(self):
        for _ in range(self.count):
            time.sleep(5)
            self.get_now_activity()
 
if __name__ == '__main__':
    test = Mtest()
    test.checkActivity()
