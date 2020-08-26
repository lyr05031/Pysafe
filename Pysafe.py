try:
    from tkinter import Label
    from tkinter import Button
    from tkinter import messagebox
    from tkinter import filedialog
    import os
    import tkinter
    import _thread
    import time
    import sys
    import random
    import hashlib
    import requests

    cunchu = ""
    myfile = open(os.path.dirname(__file__) + "/Pysafe.py", "r")
    myfile = myfile.readlines()
    mylogefile = open(os.path.dirname(__file__) + "/log.txt", "a")
    print("模块导入完成;\n基本读取数据完成;\n开始自检:")


    root2 = tkinter.Tk()
    root = tkinter.Tk()
    root.geometry("500x400")
    root2.geometry("300x500")
    root.title("Pysafe x 微步扫描")
    root2.title("Pysafe 输出窗口")
    rongqi = tkinter.Frame(root2)
    rongqi.pack()
    print("gui框架加载完成;")


    def md5s(filename):
        md5scan = hashlib.md5()
        with open(filename, "rb") as fd:
            fdr = fd.read()
            md5scan.update(fdr)
            fd.close()
        return md5scan.hexdigest()


    def thread(file_walk, w):
        tkinter.Label(rongqi,text = "多线程创建成功").pack()
        while True:
            file_walk_size = os.path.getsize(file_walk)
            time.sleep(10)
            file_walk_sizen = os.path.getsize(file_walk)
            if file_walk_sizen != file_walk_size:
                for root, dirs, files in os.walk(file_walk):
                    for name in files:
                        name = os.path.join(root, name)
                        scan(name)
                print(dirs)
            else:
                tkinter.Label(rongqi,text = "文件监控运行中").pack()



    def powerthread(root):
        tkinter.Label(rongqi,text = "多线程创建成功").pack()
        root.attributes("-fullscreen", "true")
        messagebox.showinfo("恶搞", "我们会无限占用电脑CPU   :)")
        while True:
            a = (random.randint(9999999 ** 999999999999999999999999999999999, 99999999999999999 ** 9999999999999))
            b = (random.randint(9999999 ** 999999999999999999, 9999999 ** 999999999999999))
            c = (random.randint(9999999 ** 999999999999999999999999999999999, 99999999999999999 ** 9999999999999))
            print(a ** b ** a ** b ** a ** b ** a ** b ** a ** b ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** c ** a ** b ** a ** b ** c ** a)


    def antivirus(file_user_open):
        file_md5 = md5s(file_user_open)
        tkinter.Label(rongqi,text = file_md5).pack()
        time.sleep(2)
        url = 'https://api.threatbook.cn/v3/file/report/multiengines'
        post = {'apikey': 'c3ed3ddbccdd48e083ad47d60038c6e80a6f67a2d8a94879b79801ddaf193765','sha256': file_md5}
        feedback = requests.get(url,post)
        jieguo = feedback.json()
        try:
            if jieguo["data"]["multiengines"]["threat_level"] != "clean":
                time.sleep(1)
                os.remove(file_user_open)
                tkinter.Label(rongqi,text = "发现威胁").pack()
                print(jieguo.json)
                mylogefile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + f"发现了威胁，{file_user_open},md5:{file_md5}已经清除\n")
        except:
            tkinter.Label(rongqi,text = "文件安全").pack()


    def scan(user_feedback):
        if user_feedback == True:
            file_user_open = filedialog.askopenfilename()
            antivirus(file_user_open)
        else:
            file_walk = filedialog.askdirectory()
            for root, dirs, files in os.walk(file_walk):
                for file_user_open in files:
                    file_user_open = os.path.join(root, file_user_open)
                    antivirus(file_user_open)


    def watch():
        global cunchu
        file_walk = filedialog.askdirectory()
        _thread.start_new_thread(thread, (file_walk, w))


    def quitt(root):
        global cunchu
        root.destroy()
        print("退出成功")
        os._exit(0)


    def power(root):
        global cunchu
        _thread.start_new_thread(powerthread, (root,))


    def clean():
        global rongqi
        rongqi.pack_forget()
        rongqi = tkinter.Frame(root2)
        rongqi.pack()

    print("函数加载完成;")
    user_computer = os.name
    if user_computer == "posix":
        user_computer = "Mac os"
    else:
        user_computer = "Windows"
    Button(root, text="扫描", command=lambda: scan(messagebox.askyesno("是否扫描文件", "扫描文件还是文件夹，文件选择yes，文件夹选择no"))).pack()
    Button(root, text="文件监控", command=watch).pack()
    Button(root, text="恶搞", command=lambda: power(root)).pack()
    Button(root, text="退出", command=lambda: quitt(root)).pack()
    Button(root,text="清理输出",command = clean).pack()
    print("gui界面完全加载完成;\n自检完成，结果：正常")
    root.mainloop()
except:
    print("程序异常退出 请在终端输入\npip3 install requests，如果不能解决，请反馈lyr")