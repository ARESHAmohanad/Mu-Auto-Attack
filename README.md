# 🧠 Mu Auto Attack

Ferramenta automática de pentest em Python para reconhecimento e ataque básico a aplicações web.  
Baseado nos labs do projeto [Ethical Hacking Labs](https://github.com/Samsar4/Ethical-Hacking-Labs).

---

## ⚙️ Funcionalidades

- 🔍 Fingerprint do alvo (`whatweb`)
- 🔎 Scan completo de portas (`nmap`)
- 📂 Descoberta de diretórios (`gobuster`)
- 🧪 Teste de vulnerabilidades conhecidas (`nikto`)
- 📊 Fuzzing de parâmetros (`wfuzz`)
- 💉 Ataque SQL Injection básico (`sqlmap`)
- 🧾 Relatórios organizados por ferramenta

---

## 🚀 Como usar

```bash
git clone https://github.com/ARESHAmohanad/Mu-Auto-Attack
cd Mu-Auto-Attack
chmod +x *
pip install -r requirements.txt
sudo ./install.sh
python3 mu_auto_attack.py http://example.com

🧰 Instalação das ferramentas necessárias
🐧 Linux (Kali, Ubuntu, Debian)

# Atualize os pacotes
sudo apt update && sudo apt upgrade -y

# Instale ferramentas principais
sudo apt install -y whatweb nmap gobuster nikto wfuzz sqlmap

# Instale Python e pip
sudo apt install -y python3 python3-pip

# Instale dependências Python do projeto
pip3 install -r requirements.txt


📱 Termux (com root ou proot)


pkg update && pkg upgrade -y
pkg install -y python git nmap wget

# Instale ferramentas via fsociety ou manualmente
wget https://raw.githubusercontent.com/Manisso/fsociety/master/install.sh
bash install.sh

# Baixe e execute o projeto
git clone https://github.com/ARESHAmohanad/Mu-Auto-Attack
cd Mu-Auto-Attack
chmod +x *
pip install -r requirements.txt
python3 mu_auto_attack.py http://example.com

💡 Algumas ferramentas podem ser instaladas via pip:

pip install wfuzz
git clone https://github.com/sqlmapproject/sqlmap.git




📂 Estrutura de Saída
Relatórios serão salvos automaticamente em diretórios separados para cada alvo, organizados por ferramenta.



⚠️ Aviso Legal
Esta ferramenta é educacional. Use apenas em sistemas que você tem permissão para testar.
O uso indevido pode violar leis locais e resultar em consequências legais.
