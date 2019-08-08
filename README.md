# Monkey操作指引

一：测试前提：
本地AndroidSdk环境
一台设备连接电脑

二：adb脚本：
adb shell monkey -p com.xiaomi.smarthome -s 2333 --pct-touch 70 --pct-motion 30 --ignore-crashes --ignore-timeouts --monitor-native-crashes --throttle 200 -v -v -v 500 >/Users/lumi/Documents/monkey_test/monkey_log.log

参数说明: 
-s 8888 指定序列值
--pct-touch 70： 70%触摸事件
--pct-motion 30: 30%滑动事件
--ignore-crashes ：闪退后继续执行
--ignore-timeouts：超时后继续执行
--monitor-native-crashes：跟踪本地方法的崩溃问题
--throttle 200：指定事件之间的间隔为200ms
-v -v：输出日志信息 
500：一共执行500次
com.xiaomi.smarthome：包名

三：文件目录：
monkey_config.xml：存放Activity信息
monkey_shell.py: python脚本
monkey_log.log: 记录日志

四：注意事项：
1、关掉快捷卡片
因为有快捷卡片的时候monkey很难进入到设备插件页面，此时需要把这个功能关掉最快进入插件页面进行测试
2、运行python脚本之前需要将读取xml的文件目录切换为自己的xml本地目录
3、monkey脚本日志保存目录自行设置
4、可自行设置轮询次数：
比如设置每30s轮循一次，1个小时轮询120次，假设monkey执行10小时，那么你的轮询次数就要设置1200次

五：执行顺序：
1、执行adb命令将monkey跑起来
2、执行python脚本


六：达到效果：
1、monkey只会随机操作主页面和插件页面
主页面：米家、有品、智能、我的的Tab页面都属于主页面
插件页面：从主页面进去的设备插件也都属于插件页面
2、如果随机操作跳转到了主页面和插件页面之外的其他界面，
python脚本在执行时检测到了当前页面在这个范围之内，会把他拉回到主页面

七：相关命令：
1、获取app的主Activity：
aapt dump badging*路径
eg：aapt dump
badging /Users/lumi/Desktop/apk/SmartHome_Dev_5.5.21.1_localscene.apk
 


或者
windows：adb logcat | findstr
linux：adb logcat | grep START
再点击带测试应用出现Activcity
 
 


2、查看当前页面Activity
windows：adb shell dumpsys activity |findstr "mResumedActivity" 
linux：adb shell dumpsys activity |grep "mResumedActivity"

3、获取当前正在运行的所有的activity
Linux:adb shell dumpsys activity activities | grep "Run"
windows：adb shell dumpsys activity |findstr "Run"

4、回到某个指定的activity
adb shell am start -n package/.XXXactivity
eg：adb shell am start -n com.xiaomi.smarthome/.SmartHomeMainActivity

5、禁用和取消通知栏
adb shell settings put global policy_control immersive.full=*
adb shell settings put global policy_control null


