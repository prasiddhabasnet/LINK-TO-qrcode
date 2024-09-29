#Prasiddha basnet
#sept 29 2024
import qrcode
import image

qr = qrcode.QRCode(
    version = 15,  #it's means the version of the qr code higher the bigger the code and complicated picture
    box_size = 10, #it's means the size of the qr box diplay in screen is 15
    border = 5, #border means the white stuff in the box of qr

)
data = "https://www.instagram.com/prashudffx07/"
#as i have given the path of my insragram link the same way we can generate every link
#if you don't want to redirect and creadte normal
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", black_color = "white")
img.save("test.png")


