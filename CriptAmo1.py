import tkinter as tk
from tkinter import messagebox
from bitcoin import *
import binascii

# ==== Funciones ====

def hex_to_wif(hex_key):
    return encode_privkey(hex_key, 'wif')

def wif_to_address(wif):
    return privtoaddr(wif)

def mostrar_direccion():
    hex_key = entry_priv.get().strip()
    if len(hex_key) != 64:
        messagebox.showerror("Error", "La clave debe tener 64 caracteres HEX.")
        return

    try:
        wif = hex_to_wif(hex_key)
        addr = wif_to_address(wif)
        entry_wif.delete(0, tk.END)
        entry_wif.insert(0, wif)
        entry_address.delete(0, tk.END)
        entry_address.insert(0, addr)
        messagebox.showinfo("✔️ Éxito", "Clave convertida correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo convertir: {e}")

def firmar_transaccion():
    try:
        wif = entry_wif.get().strip()
        addr_from = entry_address.get().strip()
        utxo_txid = entry_utxo.get().strip()
        utxo_index = int(entry_index.get().strip())
        script_pubkey = entry_script.get().strip()
        dest_address = entry_dest.get().strip()
        amount = float(entry_amount.get().strip())
        fee = float(entry_fee.get().strip())

        # Construir inputs y outputs
        tx_ins = [{
            'output': f'{utxo_txid}:{utxo_index}',
            'value': int((amount + fee) * 1e8),
            'address': addr_from,
            'script': script_pubkey,
        }]
        tx_outs = [{
            dest_address: int(amount * 1e8)
        }]

        # Crear y firmar
        tx = mktx(tx_ins, tx_outs)
        signed = sign(tx, 0, wif)

        txt_resultado.config(state='normal')
        txt_resultado.delete(1.0, tk.END)
        txt_resultado.insert(tk.END, f"🔏 Transacción firmada (hex):\n{signed}")
        txt_resultado.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"❌ Falló la firma: {e}")

# ==== Interfaz gráfica ====

root = tk.Tk()
root.title("🧠 CriptAmo TX Builder - by El3imm")
root.configure(bg="#111111")
root.geometry("880x680")

style_label = {"bg": "#111111", "fg": "lime", "font": ("Courier", 10)}
style_entry = {"font": ("Courier", 10), "width": 70}

tk.Label(root, text="🔐 Clave privada (HEX):", **style_label).pack()
entry_priv = tk.Entry(root, **style_entry)
entry_priv.pack()

btn_convert = tk.Button(root, text="🔁 Convertir a WIF y Dirección", command=mostrar_direccion, bg="#1f1f1f", fg="cyan", font=("Courier", 11))
btn_convert.pack(pady=5)

tk.Label(root, text="🔑 Clave privada (WIF):", **style_label).pack()
entry_wif = tk.Entry(root, **style_entry)
entry_wif.pack()

tk.Label(root, text="📬 Dirección BTC (Origen):", **style_label).pack()
entry_address = tk.Entry(root, **style_entry)
entry_address.pack()

tk.Label(root, text="🧱 UTXO TXID:", **style_label).pack()
entry_utxo = tk.Entry(root, **style_entry)
entry_utxo.pack()

tk.Label(root, text="🔢 Índice del UTXO:", **style_label).pack()
entry_index = tk.Entry(root, **style_entry)
entry_index.pack()

tk.Label(root, text="🛡️ ScriptPubKey del UTXO:", **style_label).pack()
entry_script = tk.Entry(root, **style_entry)
entry_script.pack()

tk.Label(root, text="🎯 Dirección de destino:", **style_label).pack()
entry_dest = tk.Entry(root, **style_entry)
entry_dest.pack()

tk.Label(root, text="💰 Monto a enviar (BTC):", **style_label).pack()
entry_amount = tk.Entry(root, **style_entry)
entry_amount.pack()

tk.Label(root, text="📉 Fee (BTC):", **style_label).pack()
entry_fee = tk.Entry(root, **style_entry)
entry_fee.pack()

btn_sign = tk.Button(root, text="✍️ Firmar Transacción", command=firmar_transaccion, bg="#2b2b2b", fg="gold", font=("Courier", 12))
btn_sign.pack(pady=10)

txt_resultado = tk.Text(root, height=10, width=105, font=("Courier", 9), bg="#1a1a1a", fg="white")
txt_resultado.pack(pady=10)
txt_resultado.config(state='disabled')

root.mainloop()
