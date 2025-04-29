#!/bin/bash

echo "[+] Instalando dependências para Mu Auto Attack..."

# Atualiza pacotes
if command -v apt >/dev/null; then
    sudo apt update && sudo apt install -y nmap gobuster nikto whatweb wfuzz sqlmap python3
elif command -v pkg >/dev/null; then
    pkg update && pkg install -y nmap gobuster nikto whatweb wfuzz sqlmap python
else
    echo "[!] Gerenciador de pacotes não suportado. Instale manualmente as ferramentas necessárias."
    exit 1
fi

echo "[+] Instalação concluída com sucesso!"
