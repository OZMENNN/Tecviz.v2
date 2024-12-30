import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def hesapla_alan_degeri(m2):
    """
    Verilen m² (alan) değeri için kademeli katsayılarla toplam değer hesaplar.
    """
    try:
        m2 = float(m2)
        toplam_deger = 0

        if m2 > 25000:
            toplam_deger += (m2 - 25000) * 0.0015
            m2 = 25000
        if m2 > 5000:
            toplam_deger += (m2 - 5000) * 0.003
            m2 = 5000
        if m2 > 1000:
            toplam_deger += (m2 - 1000) * 0.004
            m2 = 1000
        if m2 > 500:
            toplam_deger += (m2 - 500) * 0.005
            m2 = 500
        if m2 > 100:
            toplam_deger += (m2 - 100) * 0.01
            m2 = 100
        if m2 > 10:
            toplam_deger += (m2 - 10) * 0.02
            m2 = 10
        toplam_deger += m2 * 0.05

        return toplam_deger
    except ValueError:
        return None

def ekle_button_click():
    m2_input = entry_m2.get().strip()
    if not m2_input:
        messagebox.showerror("Hata", "Metrekare değeri boş bırakılamaz!")
        return
    
    sonuc = hesapla_alan_degeri(m2_input)

    if sonuc is None:
        messagebox.showerror("Hata", "Lütfen geçerli bir metrekare değeri giriniz!")
        return
    
    # Eklenen ve çıkarılan değerleri hesapla
    m2 = float(m2_input)
    topladigimiz_deger = sonuc + m2
    cikardigimiz_deger = sonuc - m2

    # Verileri listeye ekle
    data_list.append((m2, sonuc, topladigimiz_deger, cikardigimiz_deger))
    update_data_listbox()
    entry_m2.delete(0, tk.END)

def update_data_listbox():
    listbox_data.delete(0, tk.END)
    for idx, (m2, sonuc, topladigimiz_deger, cikardigimiz_deger) in enumerate(data_list):
        listbox_data.insert(
            tk.END,
            f"{idx + 1}. Girdi: {m2} m², Sonuç: {sonuc:.2f}, +Girdi: {topladigimiz_deger:.2f}, -Girdi: {cikardigimiz_deger:.2f}"
        )

def kaydet_button_click():
    if not data_list:
        messagebox.showinfo("Bilgi", "Kaydedilecek bir veri bulunmuyor!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            for m2, sonuc, topladigimiz_deger, cikardigimiz_deger in data_list:
                f.write(
                    f"Girdi: {m2} m², Sonuç: {sonuc:.2f}, +Girdi: {topladigimiz_deger:.2f}, -Girdi: {cikardigimiz_deger:.2f}\n"
                )
        messagebox.showinfo("Başarılı", f"Sonuçlar başarıyla {file_path} dosyasına kaydedildi!")

def temizle_button_click():
    data_list.clear()
    update_data_listbox()

# Tkinter arayüzü oluşturma
window = tk.Tk()
window.title("Arşiv Onaylı Koordinat Doğruluğu Hesaplama")

data_list = []

# Arayüz bileşenleri
label_m2 = tk.Label(window, text="Alan Miktarı Metrekare (m²):")
label_m2.grid(row=0, column=0, padx=10, pady=10)

entry_m2 = tk.Entry(window)
entry_m2.grid(row=0, column=1, padx=10, pady=10)

button_ekle = tk.Button(window, text="Ekle", command=ekle_button_click)
button_ekle.grid(row=1, column=0, padx=5, pady=5)

button_temizle = tk.Button(window, text="Temizle", command=temizle_button_click)
button_temizle.grid(row=1, column=1, padx=5, pady=5)

listbox_data = tk.Listbox(window, width=80, height=10)
listbox_data.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

button_kaydet = tk.Button(window, text="Kaydet", command=kaydet_button_click)
button_kaydet.grid(row=3, column=0, columnspan=2, pady=10)

# Arayüzü çalıştır
window.mainloop()
