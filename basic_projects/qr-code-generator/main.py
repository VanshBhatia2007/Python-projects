import qrcode

data = input("enter the text or url : ").strip()
filename = input("enter the file name : ").strip()

qr = qrcode.QRCode(box_size= 10 , border= 4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"qr code saved as {filename}")

# output :
# enter the text or url : https://github.com/VanshBhatia2007
# enter the file name : git.jpg
# qr code saved as git.jpg
