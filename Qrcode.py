import qrcode

url = "https://site-namorada-1-h3ds.onrender.com"  # Substitua pelo seu link real
img = qrcode.make(url)
img.save("qr_code.png")
