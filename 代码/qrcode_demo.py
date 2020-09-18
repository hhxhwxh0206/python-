import qrcode  # 引入qrcode模块

while True:
    data = input("\n请输入内容：")  # 调用input函数输入要生成二维码的内容
    img = qrcode.make(data)  # 调用qrcode模块中的make函数将指定内容转化为二维码图像对象
    img.save("dj.jpg")  # 调用img对象的save方法将二维码图像对象保存为图片文件
    print("二维码图片生成成功！")
    img.show()  # 调用img对象的show方法将二维码图像显示出来
