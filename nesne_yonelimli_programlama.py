import tkinter as tk
from tkinter import messagebox

class Inventory:
    def __init__(self):
        self.items = {}  # Envanteri saklamak için bir sözlük

    def add_item(self, item_name, quantity):
        # Ürünü envantere ekleme fonksiyonu
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        # Ürünü envanterden çıkarma fonksiyonu
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                raise ValueError("Yeterli miktar yok.")
        else:
            raise ValueError("Ürün bulunamadı.")

    def update_item(self, item_name, quantity):
        # Ürünün miktarını güncelleme fonksiyonu
        if item_name in self.items:
            self.items[item_name] = quantity
        else:
            raise ValueError("Ürün bulunamadı.")

    def view_inventory(self):
        # Mevcut envanteri görüntüleme fonksiyonu
        return self.items

class App:
    def __init__(self, root):
        self.inventory = Inventory()  # Envanter nesnesini oluşturma

        self.root = root
        self.root.title("Envanter Yönetim Sistemi")  # Pencere başlığı

        # Girdi alanları
        self.item_name_label = tk.Label(root, text="Ürün Adı:")
        self.item_name_label.grid(row=0, column=0)
        self.item_name = tk.Entry(root)
        self.item_name.grid(row=0, column=1)

        self.quantity_label = tk.Label(root, text="Miktar:")
        self.quantity_label.grid(row=1, column=0)
        self.quantity = tk.Entry(root)
        self.quantity.grid(row=1, column=1)

        # Butonlar
        self.add_button = tk.Button(root, text="Ürün Ekle", command=self.add_item)
        self.add_button.grid(row=2, column=0)

        self.remove_button = tk.Button(root, text="Ürün Çıkar", command=self.remove_item)
        self.remove_button.grid(row=2, column=1)

        self.update_button = tk.Button(root, text="Ürünü Güncelle", command=self.update_item)
        self.update_button.grid(row=2, column=2)

        self.view_button = tk.Button(root, text="Envanteri Görüntüle", command=self.view_inventory)
        self.view_button.grid(row=2, column=3)

        # Çıktı alanı
        self.output_area = tk.Text(root, height=10, width=50)
        self.output_area.grid(row=3, column=0, columnspan=4)

    def add_item(self):
        # Ürün ekleme işlemi
        try:
            item_name = self.item_name.get()
            quantity = int(self.quantity.get())
            self.inventory.add_item(item_name, quantity)
            messagebox.showinfo("Başarılı", f"{quantity} adet {item_name} eklendi.")
            self.clear_fields()  # Giriş alanlarını temizle
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz giriş. Lütfen geçerli bir miktar girin.")

    def remove_item(self):
        # Ürün çıkarma işlemi
        try:
            item_name = self.item_name.get()
            quantity = int(self.quantity.get())
            self.inventory.remove_item(item_name, quantity)
            messagebox.showinfo("Başarılı", f"{quantity} adet {item_name} çıkarıldı.")
            self.clear_fields()  # Giriş alanlarını temizle
        except ValueError as e:
            messagebox.showerror("Hata", str(e))

    def update_item(self):
        # Ürün güncelleme işlemi
        try:
            item_name = self.item_name.get()
            quantity = int(self.quantity.get())
            self.inventory.update_item(item_name, quantity)
            messagebox.showinfo("Başarılı", f"{item_name} {quantity} olarak güncellendi.")
            self.clear_fields()  # Giriş alanlarını temizle
        except ValueError as e:
            messagebox.showerror("Hata", str(e))

    def view_inventory(self):
        # Mevcut envanteri görüntüleme
        inventory = self.inventory.view_inventory()
        output = "Mevcut Envanter:\n"
        for item, quantity in inventory.items():
            output += f"{item}: {quantity}\n"
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, output)

    def clear_fields(self):
        # Giriş alanlarını temizleyen fonksiyon
        self.item_name.delete(0, tk.END)
        self.quantity.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()  # Tkinter penceresini oluşturma
    app = App(root)  # Uygulamayı başlatma
    root.mainloop()  # Tkinter olay döngüsünü başlatma
