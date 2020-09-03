try:
    import requests
    from tkinter import Label
    from tkinter import Button
    from tkinter import messagebox
    from tkinter import filedialog
    import os
    import tkinter
    import time
    import sys
    import hashlib
    import threading


    root = tkinter.Tk()
    mianframe = tkinter.Frame(root)
    tkinter.Label(mianframe,text = "Pysafe正在保护您的电脑").pack()
    mianframe.pack()
    root.geometry("500x400")
    root.title("Pysafe x 微步扫描")
    rongqi = tkinter.Frame(mianframe)
    print("gui框架加载完成;")
    rongqi2 = tkinter.Frame(mianframe)
    rongqi2.pack()
    rongqi.pack()


    def md5s(filename):
        md5scan = hashlib.md5()
        with open(filename, "rb") as fd:
            fdr = fd.read()
            md5scan.update(fdr)
            fd.close()
        return md5scan.hexdigest()


    def antivirus(file_user_open):
        file_md5 = md5s(file_user_open)
        tkinter.Label(rongqi,text = file_user_open).pack()
        time.sleep(0.7)
        url = 'https://api.threatbook.cn/v3/file/report/multiengines'
        post = {'apikey': 'c3ed3ddbccdd48e083ad47d60038c6e80a6f67a2d8a94879b79801ddaf193765','sha256': file_md5}
        feedback = requests.get(url,post)
        jieguo = feedback.json()
        try:
            if jieguo["data"]["multiengines"]["threat_level"] != "clean":
                os.remove(file_user_open)
                tkinter.Label(rongqi,text = "发现威胁").pack()
                print(jieguo.json)
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
                for file_user_open in dirs:
                    file_user_open = os.path.join(root,file_user_open)



    def clean():
        global rongqi
        rongqi.pack_forget()
        rongqi = tkinter.Frame(root)
        rongqi.pack()


    def quitt(root):
        root.destroy()
        print("退出成功")
        os._exit(0)


    def about():
        tkinter.Label(rongqi,text = "李一冉和孟垂毅制作").pack()
    

    def file_watch(user_computer):
        global rongqi
        messagebox.showinfo("文件监控","请选择需要监控的文件夹")
        file_path = filedialog.askdirectory()
        tkinter.Label(rongqi,text = "文件监控自动运行中").pack()
        print("多线程创建成功")
        while True:
            try:
                file_walk_size = os.path.getsize(file_path)
                time.sleep(5)
                file_walk_sizen = os.path.getsize(file_path)
                if file_walk_sizen != file_walk_size:
                    tkinter.Label(rongqi,text = "检测到文件更改，启动扫描").pack()
                    for root, dirs, files in os.walk(file_path):
                        for name in files:
                            name = os.path.join(root, name)
                            antivirus(name)
                    print(dirs)
                else:
                    pass
            except:
                pass
    

    def thread():
        wenjian = threading.Thread(target = file_watch,args = (user_computer,))
        wenjian.daemon = True
        wenjian.start()

    print("函数加载完成;")
    user_computer = os.name
    if user_computer == "posix":
        user_computer = "Mac os"
    else:
        user_computer = "Windows"
    Button(rongqi2, text = "扫描", command = lambda: scan(messagebox.askyesno("是否扫描文件", "扫描文件还是文件夹，文件选择yes，文件夹选择no"))).pack()
    Button(rongqi2,text = "文件监控",command = thread).pack()
    Button(rongqi2,text="清理输出",command = clean).pack()
    Button(rongqi2,text = "关于我们",command = about).pack()
    Button(rongqi2, text="退出", command = lambda: quitt(root)).pack()
    print("gui界面完全加载完成;\n自检完成，结果：正常")
    root.mainloop()
except:
    import subprocess,time
    print("开始安装程序依赖库,请耐心等待️")
    def commandr(command):
        fanhui = subprocess.run(command,shell = True,encoding = "utf-8")
        if fanhui.returncode == 0:
            print("安装成功！请重启程序")
        else:
            print("自动安装失败，请在终端手动输入\npip3 install requests")
    commandr("pip3 install requests")
