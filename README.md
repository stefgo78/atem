# atem

Panel do zmiany adresu RTMP w ATEM Mini Pro uruchamiany na Androidzie (Termux), bez Node.js, bez npm, bez kompilacji.

## 1. Instalacja w Termux

```bash
pkg update
pkg install python git
pip install -r requirements.txt

START:
python server.py

http://IP_ANDROID:3000

