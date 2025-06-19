#!/usr/bin/env python3

import subprocess
import sys
import os
from datetime import datetime

if len(sys.argv) != 2:
    print("Uso: python mu_auto_attack.py http://example.com")
    sys.exit(1)

alvo = sys.argv[1]
data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
diretorio_saida = f"mu_recon_{alvo.replace('http://','').replace('https://','').replace('/', '')}_{data}"
os.makedirs(diretorio_saida, exist_ok=True)

# Função para rodar comandos e salvar saída

def executar(comando, nome_saida):
    print(f"[+] Executando: {comando}")
    try:
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, timeout=300)
    except subprocess.CalledProcessError as e:
        resultado = e.output
    except subprocess.TimeoutExpired:
        resultado = b"[!] Tempo limite excedido"

    with open(os.path.join(diretorio_saida, nome_saida), "wb") as f:
        f.write(resultado)

# 1. WhatWeb
executar(f"whatweb {alvo}", "1_whatweb.txt")

# 2. Nmap nas 1000 portas
host = alvo.replace("http://", "").replace("https://", "").split("/")[0]
executar(f"nmap -sS -Pn -T4 -p- -oN - {host}", "2_nmap.txt")

# 3. Gobuster para diretórios
executar(f"gobuster dir -u {alvo} -w /usr/share/wordlists/dirb/common.txt -q", "3_gobuster.txt")

# 4. Nikto para vulnerabilidades básicas
executar(f"nikto -host {alvo}", "4_nikto.txt")

# 5. Wfuzz para parâmetros GET
executar(f"wfuzz -c -u {alvo}/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt --hc 404", "5_wfuzz.txt")

# 6. Sqlmap simples
executar(f"sqlmap -u {alvo} --batch --random-agent --level=1 --risk=1", "6_sqlmap.txt")

print(f"\n[+] Recon finalizado. Relatórios salvos em: {diretorio_saida}")
