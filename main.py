# Güçlü Parolanın Özellikleri
# 1 En az 8 karakterden oluşur.
# 2 Harflerin yanı sıra, rakam ve “?, @, !, #, %, +, -, *, %” gibi özel karakterler içerir.
# 3 Büyük ve küçük harfler bir arada kullanılır.

import tkinter as tk # GUI Modülü
import random # Rastgele sayı üretmek için kullanılan modül
import pyperclip # Kopyalama Modülü

window = tk.Tk() # Pencere oluşturuldu.
window.geometry("500x300") # Boyutları belirlendi.
window.resizable(False, False) # Pencere boyutları sabitlendi.
window.configure(bg="#e6e6fa") # Arkaplan rengi oluşturuldu.

label = tk.Label(window, text="") # Label oluşturuldu.
label.pack()

# Kullanılacak olan karakter oluşturuldu ve diziye aktarıldı.
alfabe_kucuk = "abcdefghijklmnoprstuvyzqwx"
alfabe_buyuk = "ABCDEFGHIJKLMNOPRSTUVYZQWX"
rakamlar = "1234567890"
ozel_karakterler = "?@!#%+-*%"

dizi_p = alfabe_buyuk + alfabe_kucuk + rakamlar + ozel_karakterler


# Parola oluşturma butonu oluşturuldu.
def write_text():
    password = ""
    random_int = random.randint(12, 20) # 12-20 karakter boyutunda oluşturuldu.

    # Burada oluşturulan diziden rastgele eleman seçilip password kelimesine eklendi.
    i = 0
    while i < random_int:
        password += random.choice(dizi_p)
        i += 1

    # Ekrana yazdırılma işlemi burada yapıldı.
    label.config(text=password)
    label.place(relx=0.32, rely=0.4)
    label.configure(bg="#e6e6fa", font=("Times New Roman", 16))

# Butonun büyüklüğü rengi vs. gibi özellikleri belirlendi.
button = tk.Button(window, text="Rastgele Parola Oluştur", command=write_text, width=50, height=5, font=("Times New Roman",10))
button.place(relx=0.15, rely=0.6)
button.configure(bg="#ff6a6a")

# Kopyalama butonu  oluşturuldu.
def panoya_kopyala():
    text = label.cget("text")
    pyperclip.copy(text)

# Kopyalama butonunun büyüklüğü rengi vs. gibi özellikleri belirlendi.
copy_button = tk.Button(window, text="Panoya Kopyala", command=panoya_kopyala, font=("Times New Roman",10))
copy_button.place(relx=0.15, rely=0.6)
copy_button.configure(bg="#ff6a6a")
copy_button.pack()

window.mainloop()
