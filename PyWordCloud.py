from wordcloud import WordCloud
from tkinter import *
import jieba
from imageio import imread
tkwindow = Tk()
TxtPath = StringVar()
ImgPath = StringVar()
ImgWidth = StringVar()
ImgHeight = StringVar()
BgImgPath = StringVar()
FontPath = StringVar()
tkwindow.minsize(600,350)
tkwindow.maxsize(600,350)
tkwindow.title("PyWordCloud 1.0(GUI)")
msg1 = Label(text="TXT文件路径(完整或相对路径):")
msg1.pack()
TxtPathInput = Entry(tkwindow,width=400,textvariable=TxtPath)
TxtPathInput.pack()
msg2 = Label(text="输出图片路径(完整或相对路径):")
msg2.pack()
ImgPathInput=Entry(tkwindow,width=400,textvariable=ImgPath)
ImgPathInput.pack()
msg3 = Label(text="输出图片宽:")
msg3.pack()
ImgWidthInput=Entry(tkwindow,width=400,textvariable=ImgWidth)
ImgWidthInput.pack()
msg4 = Label(text="输出图片高:")
msg4.pack()
ImgHeightInput=Entry(tkwindow,width=400,textvariable=ImgHeight)
ImgHeightInput.pack()
msg5 = Label(text="背景轮廓图片路径(完整或相对路径，可选):")
msg5.pack()
BgImgPathInput=Entry(tkwindow,width=400,textvariable=BgImgPath)
BgImgPathInput.pack()
msg6 = Label(text="字体文件路径(完整或相对路径):")
msg6.pack()
FontPathInput=Entry(tkwindow,width=400,textvariable=FontPath)
FontPathInput.pack()
def Text_Filter(content):
    replace_dict={"的":"","了":"","和":"","是":"","从":"","有":"","而":"","年":"","月":"","日":"","让":"","要":"","就":"","is":"","am":"","are":"","were":"","was":""}
    for element in replace_dict:
        content = content.replace(element,replace_dict[element])
    return content
def OutputWordCloud():
    file_content = " ".join(jieba.cut(open(TxtPathInput.get(),"r").read(),cut_all=False))
    if(BgImgPathInput.get() == ""):
        wcl_img = WordCloud(font_path=FontPathInput.get(),background_color="white",width=int(ImgWidthInput.get()),height=int(ImgHeightInput.get()),margin=2).generate(Text_Filter(file_content))
        wcl_img.to_file(ImgPathInput.get())
    else:
        wcl_img = WordCloud(font_path=FontPathInput.get(),background_color="white",width=int(ImgWidthInput.get()),height=int(ImgHeightInput.get()),margin=2,mask=imread(BgImgPathInput.get())).generate(Text_Filter(file_content))
        wcl_img.to_file(ImgPathInput.get())
OutputImgButton  = Button(tkwindow,text="输出词云图片",command=OutputWordCloud)
OutputImgButton.pack()
OutputImgButton  = Button(tkwindow,text="退出",command=exit)
OutputImgButton.pack()
msg7 = Label(text="(C)2022 Kxz All Rights Reserved")
msg7.pack()
tkwindow.mainloop()
