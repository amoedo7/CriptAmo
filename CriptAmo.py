import tkinter as tk
import os, ecdsa, hashlib, base58

# ========= INFO DE AUTOR =========
AUTHOR = "El3imm"

DONATION_ADDRESSES = {
    "Bitcoin": "17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv",
    "Litecoin": "LRxpA5rr8kAAbtMHg45ruS7929x9gsnEsv",
    "Dogecoin": "DBsxS8VfMVpPt5qjEW68BBCyh5KAsCNYec",
    "BitcoinCash": "17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv",
    "Clams": "xF3VnkPVKoQ9PTkzrPjE4bLA33t718KGLG",
    "Zcash": "t1QcTuCyA2Qhhwii2SLugmE9J4bmxMxwMZN",
    "Dash": "XhRhj8Cv1o8hW2FiMoQnUwjAeHAZfvCAdp",
    "Ethereum": "0x548702ecce06cbc6991c86de390bc008459cdf5a",
    "BNB": "0x548702ecce06cbc6991c86de390bc008459cdf5a"
}

# ========= FUNCIONES =========

def generate_private_key():
    return os.urandom(32).hex()

def private_to_public_key(priv_key_hex):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(priv_key_hex), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return b'\x04' + vk.to_string()

def ripemd160(data):
    return hashlib.new('ripemd160', data).digest()

def base58_address(prefix, pub_key_hash):
    payload = prefix + pub_key_hash
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return base58.b58encode(payload + checksum).decode()

def generate_addresses(pub_key):
    pub_key_sha = hashlib.sha256(pub_key).digest()
    pub_key_ripemd = ripemd160(pub_key_sha)

    addresses = {
        "Bitcoin": base58_address(b'\x00', pub_key_ripemd),
        "Litecoin": base58_address(b'\x30', pub_key_ripemd),
        "Dogecoin": base58_address(b'\x1e', pub_key_ripemd),
        "BitcoinCash": base58_address(b'\x00', pub_key_ripemd),
        "Dash": base58_address(b'\x4c', pub_key_ripemd),
        "Clams": base58_address(b'\x89', pub_key_ripemd),
        "Zcash": base58_address(b'\x1c\xb8', pub_key_ripemd),
    }

    eth_hash = hashlib.new('sha3_256', pub_key[1:]).digest()
    eth_address = "0x" + eth_hash[-20:].hex()
    addresses["Ethereum"] = eth_address
    addresses["BNB"] = eth_address

    return addresses

def mostrar_salida(texto):
    text_output.config(state='normal')
    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, texto)
    text_output.config(state='disabled')

def generar():
    priv_key = generate_private_key()
    pub_key = private_to_public_key(priv_key)
    addresses = generate_addresses(pub_key)

    output = f"🔑 Clave Privada:\n{priv_key}\n\n🏦 Direcciones:\n"
    for name, addr in addresses.items():
        output += f" - {name}: {addr}\n"

    mostrar_salida(output)

def mostrar_donaciones():
    salida = f"🙏 ¡Gracias por tu apoyo!\n\n👤 Autor: {AUTHOR}\n\n🏦 Donaciones:\n"
    for name, addr in DONATION_ADDRESSES.items():
        salida += f" - {name}: {addr}\n"
    mostrar_salida(salida)

def from_existing_key():
    key = key_entry.get().strip()
    if len(key) == 64 and all(c in "0123456789abcdefABCDEF" for c in key):
        status_label.config(text="✅", fg="lime")
        try:
            pub_key = private_to_public_key(key)
            addresses = generate_addresses(pub_key)
            output = f"🔑 Clave Privada:\n{key}\n\n🏦 Direcciones:\n"
            for name, addr in addresses.items():
                output += f" - {name}: {addr}\n"
            mostrar_salida(output)
        except Exception as e:
            mostrar_salida(f"❌ Error al procesar la clave: {str(e)}")
    else:
        status_label.config(text="❌", fg="red")
        mostrar_salida("❌ Clave no válida. Debe tener exactamente 64 caracteres hexadecimales.")

# ========= INTERFAZ =========

root = tk.Tk()
root.title("🧠 CriptAmo - Wallet Generator by El3imm")
root.geometry("750x600")
root.configure(bg="#121212")

tk.Label(root, text="CriptAmo", font=("Courier", 20, "bold"), fg="lime", bg="#121212").pack(pady=10)

# Ingreso de clave existente
key_frame = tk.Frame(root, bg="#121212")
key_frame.pack(pady=5)

tk.Label(key_frame, text="🗝️KEY🗝️:", bg="#121212", fg="white", font=("Courier", 11)).pack(side="left")
key_entry = tk.Entry(key_frame, width=70, font=("Courier", 10))
key_entry.pack(side="left", padx=5)

status_label = tk.Label(key_frame, text="❔", font=("Courier", 14), bg="#121212", fg="white")
status_label.pack(side="left", padx=5)

mi_key_btn = tk.Button(root, text="🗝️ Mi KEY", command=from_existing_key, bg="#1a1a1a", fg="cyan", font=("Courier", 12))
mi_key_btn.pack(pady=4)

# Botones de acción
btn = tk.Button(root, text="🎲 Generar Direcciones Nuevas", command=generar, bg="#1f1f1f", fg="white", font=("Courier", 14), relief="ridge")
btn.pack(pady=10)

donate_btn = tk.Button(root, text="❤️ Donar a El3imm", command=mostrar_donaciones, bg="#1c1c1c", fg="gold", font=("Courier", 12), relief="ridge")
donate_btn.pack(pady=5)

# Área de salida
text_output = tk.Text(root, width=85, height=20, font=("Courier", 10), bg="#1e1e1e", fg="lime", wrap="none")
text_output.pack(padx=10, pady=10)
text_output.config(state='disabled')

root.mainloop()
