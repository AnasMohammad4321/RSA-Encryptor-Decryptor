import tkinter as tk
from tkinter import messagebox
from RSA import RSA  
from PIL import Image, ImageTk  


class RSAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA Encryption/Decryption App")
        self.root.geometry("600x580")
        self.root.configure(bg="#DFDAD9")
        self.root.maxsize(600, 580)  
        png_image = Image.open("icon.png")  
        tk_image = ImageTk.PhotoImage(png_image)
        self.root.iconphoto(True, tk_image)

        # Key Size
        self.key_size_label = tk.Label(root, text="Enter RSA Key Size:", font=("Arial", 14), bg="#DFDAD9")
        self.key_size_label.grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
        self.key_size_entry = tk.Entry(root, font=("Arial", 14), width=10, bg="#F1EBE9")
        self.key_size_entry.grid(row=0, column=1, pady=10, padx=10, sticky=tk.W)
        self.key_size_entry.focus()

        # Generate Keys Button
        self.generate_button = tk.Button(root, text="Generate Keys", font=("Arial", 14),
                                         command=self.generate_keys, bg="#4caf50", fg="white")
        self.generate_button.grid(row=1, column=0, columnspan=1, pady=10, padx=10, sticky=tk.W+tk.E)

        # Public Key
        self.public_key_label = tk.Label(root, text="Public Key:", font=("Arial", 14), bg="#DFDAD9")
        self.public_key_label.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W)
        self.public_key_text = tk.Text(root, height=3, width=35, font=("Arial", 12), bg="#F1EBE9")
        self.public_key_text.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W)

        # Private Key
        self.private_key_label = tk.Label(root, text="Private Key:", font=("Arial", 14), bg="#DFDAD9")
        self.private_key_label.grid(row=3, column=0, pady=10, padx=10, sticky=tk.W)
        self.private_key_text = tk.Text(root, height=3, width=35, font=("Arial", 12), bg="#F1EBE9")
        self.private_key_text.grid(row=3, column=1, pady=10, padx=10, sticky=tk.W)

        # Message Entry
        self.message_label = tk.Label(root, text="Enter Message:", font=("Arial", 14), bg="#DFDAD9")
        self.message_label.grid(row=4, column=0, pady=10, padx=10, sticky=tk.W)
        self.message_entry = tk.Entry(root, font=("Arial", 14), width=25, bg="#F1EBE9")
        self.message_entry.grid(row=4, column=1, pady=10, padx=10, sticky=tk.W)

        # Encrypt and Decrypt Buttons
        self.encrypt_button = tk.Button(root, text="Encrypt", font=("Arial", 14),
                                       command=self.encrypt_message, bg="#2196F3", fg="white")
        self.encrypt_button.grid(row=5, column=0, columnspan=1, pady=10, padx=10, sticky=tk.W+tk.E)
        self.decrypt_button = tk.Button(root, text="Decrypt", font=("Arial", 14),
                                       command=self.decrypt_message, bg="#f44336", fg="white")
        self.decrypt_button.grid(row=6, column=0, columnspan=1, pady=10, padx=10, sticky=tk.W+tk.E)

        # Encrypted Message
        self.encrypted_message_label = tk.Label(root, text="Encrypted Message:", font=("Arial", 14), bg="#DFDAD9")
        self.encrypted_message_label.grid(row=7, column=0, pady=10, padx=10, sticky=tk.W)
        self.encrypted_message_text = tk.Text(root, height=2, width=35, font=("Arial", 12), bg="#F1EBE9")
        self.encrypted_message_text.grid(row=7, column=1, pady=10, padx=10, sticky=tk.W)

        # Decrypted Message
        self.decrypted_message_label = tk.Label(root, text="Decrypted Message:", font=("Arial", 14), bg="#DFDAD9")
        self.decrypted_message_label.grid(row=8, column=0, pady=10, padx=10, sticky=tk.W)
        self.decrypted_message_text = tk.Text(root, height=2, width=35, font=("Arial", 12), bg="#F1EBE9")
        self.decrypted_message_text.grid(row=8, column=1, pady=10, padx=10, sticky=tk.W)

    def generate_keys(self):
        key_size = self.key_size_entry.get()
        if key_size.isdigit():
            key_size = int(key_size)
            rsa = RSA(bitlength=key_size)
            public_key, private_key = rsa.generate_keypair()
            self.public_key_text.delete(1.0, tk.END)
            self.public_key_text.insert(tk.END, f"e: {public_key[0]}\nn: {public_key[1]}")
            self.private_key_text.delete(1.0, tk.END)
            self.private_key_text.insert(tk.END, f"d: {private_key[0]}\nn: {private_key[1]}")
        else:
            messagebox.showerror("Error", "Invalid key size. Please enter a valid integer.")

    def encrypt_message(self):
        message = self.message_entry.get()
        if message:
            e = int(self.public_key_text.get("1.0", tk.END).split()[1])
            n = int(self.public_key_text.get("1.0", tk.END).split()[3])
            encrypted_message = ' '.join(str(ord(char) ** e % n) for char in message)
            self.encrypted_message_text.delete(1.0, tk.END)
            self.encrypted_message_text.insert(tk.END, encrypted_message)
        else:
            messagebox.showerror("Error", "Please enter a message to encrypt.")

    def decrypt_message(self):
        encrypted_message = self.encrypted_message_text.get("1.0", tk.END).strip()
        if encrypted_message:
            d = int(self.private_key_text.get("1.0", tk.END).split()[1])
            n = int(self.private_key_text.get("1.0", tk.END).split()[3])
            decrypted_message = ''.join(chr(int(char) ** d % n) for char in encrypted_message.split())
            self.decrypted_message_text.delete(1.0, tk.END)
            self.decrypted_message_text.insert(tk.END, decrypted_message)
        else:
            messagebox.showerror("Error", "Please enter an encrypted message to decrypt.")

root = tk.Tk()
app = RSAApp(root)
root.mainloop()