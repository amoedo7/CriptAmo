<p align="center">
  <img src="criptamo.png" width="180" alt="CriptAmo Logo">
</p>

# CriptAmo

**CriptAmo** es una aplicación de escritorio en Python que te permite generar claves privadas y direcciones públicas para múltiples criptomonedas de forma sencilla, rápida y visual, usando una interfaz gráfica con `Tkinter`.

### 🚀 Características

- Generación automática de:
  - Clave privada (formato hexadecimal)
  - Direcciones para: Bitcoin, Ethereum, Dogecoin, Litecoin, Dash, BitcoinCash, Zcash, BNB, Clams
- Opción para ingresar tu propia clave privada y derivar direcciones
- Interfaz visual clara, moderna y en modo oscuro
- Botón de donaciones con direcciones del autor 😄

### 🖼️ Captura

![Captura de pantalla](https://via.placeholder.com/700x540.png?text=CriptAmo+UI)

### 🛠️ Requisitos

- Python 3.8 o superior
- Dependencias del archivo `requirements.txt`

### 📦 Instalación

```bash
git clone https://github.com/El3imm/CriptAmo.git
cd CriptAmo
pip install -r requirements.txt
python CriptAmo.py

❤️ Donaciones
Si esta herramienta te ayudó, podés invitarme un cafecito cripto ☕:

makefile
Copiar
Editar
Bitcoin: 17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv
Ethereum: 0x548702ecce06cbc6991c86de390bc008459cdf5a
Dogecoin: DBsxS8VfMVpPt5qjEW68BBCyh5KAsCNYec
Y más dentro de la app...
🧑‍💻 Autor
El3imm — explorando la frontera entre código y criptografía.
GitHub • Twitter (si tenés uno)

📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver LICENSE para más información.

yaml
Copiar
Editar

---

### 📦 `requirements.txt`

```txt
ecdsa==0.18.0
base58==2.1.1
Tkinter viene por defecto en Python (si no, instalar con sudo apt install python3-tk en Linux).