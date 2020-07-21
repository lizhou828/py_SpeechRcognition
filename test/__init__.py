# -*- coding: utf-8 -*-
# /usr/bin/python
# 作者：lizhou828
# 实验日期：2020-07-21
# Python版本：3.7
# 操作系统win10

# 原文地址：https://blog.csdn.net/qq_32643313/article/details/99936268

# 所需依赖如下：
# pip install SpeechRecognition
# pip install  PocketSphinx


# pocketsphinx需要安装的中文语言、声学模型
# 下载地址：http://sourceforge.net/projects/cmusphinx/files/Acoustic and Language Models/
# https://nchc.dl.sourceforge.net/project/cmusphinx/Acoustic%20and%20Language%20Models/Mandarin/cmusphinx-zh-cn-5.2.tar.gz

# 因为安装 PocketSphinx 时候，需要依赖swig.exe，，否则在安装过程会报错：error: command 'swig.exe' failed: No such file or directory
# 下载地址：
# https://nchc.dl.sourceforge.net/project/swig/swigwin/swigwin-4.0.1/swigwin-4.0.1.zip


# 如果报错：  error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/
# 需要下载：visualcppbuildtools_full.exe 下载地址：https://474b.com/file/1445568-239446865

import speech_recognition as sr
r = sr.Recognizer()    #调用识别器
# test = sr.AudioFile(r"C:\Users\lizhou\Desktop\rainbow老师采访.wav")   #导入语音文件
test = sr.AudioFile(r"C:\Users\lizhou\Desktop\zufang.wav")   #导入语音文件

with test as source:
    audio = r.record(source)
type(audio)
c=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
print(c)
# ————————————————
# 版权声明：本文为CSDN博主「kimicren」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_32643313/article/details/99936268