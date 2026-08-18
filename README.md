<p align="center">
  <img src="criptamo.png" width="180" alt="CriptAmo">
</p>

# CriptAmo

Herramienta experimental de DesarrollAMO para **generar y visualizar claves/direcciones de distintas criptomonedas**.

## Estado

**Histórico / experimental.** Se conserva por su valor técnico y de aprendizaje. No ha sido auditado como wallet, custodia ni software financiero de producción.

## Qué contiene

- variantes históricas `CriptAmo.py`, `CriptAmo1.py` y `CriptAmo2.py`;
- derivación/generación para varias redes;
- interfaz Tkinter;
- experimentos adicionales en `Version2/` y `web3/`;
- `requirements.txt`;
- licencia MIT incluida en el repositorio.

## Instalación histórica

```bash
git clone https://github.com/amoedo7/CriptAmo.git
cd CriptAmo
pip install -r requirements.txt
python CriptAmo.py
```

En Linux puede ser necesario instalar Tkinter mediante el gestor de paquetes de la distribución.

## Seguridad crítica

CriptAmo trabaja con material criptográfico. Por eso:

- **nunca** uses claves privadas que protejan fondos reales para probar el proyecto;
- no pegues seeds, frases mnemónicas ni claves privadas reales en Issues, logs o capturas;
- no asumas que la generación aleatoria o derivación implementada aquí ha sido auditada criptográficamente;
- prueba únicamente con claves desechables y redes/test wallets controladas por vos;
- una dirección pública puede compartirse; una clave privada o seed no.

Este repositorio no recupera fondos ni otorga acceso legítimo a wallets de terceros.

## Relación con DesarrollAMO

CriptAmo representa una etapa de experimentación con criptografía y apps de escritorio. No es actualmente una pieza central de DAMO/IAMO, pero se conserva como proyecto AMO independiente y como referencia técnica.

## Versionado

Las múltiples variantes históricas se mantienen para preservar evolución. Si se retoma el proyecto, el primer trabajo debería ser elegir una única entrada canónica, agregar tests deterministas y separar claramente librería, UI y soporte de redes.

---

**DesarrollAMO** · tus claves privadas deben permanecer bajo tu control.
