# 🧠 Mu Auto Attack

Ferramenta automática de pentest em Python para reconhecimento e ataque básico a aplicações web. Baseado nos labs do projeto [Ethical Hacking Labs](https://github.com/Samsar4/Ethical-Hacking-Labs).

## ⚙️ Funcionalidades

- Fingerprint do alvo (`whatweb`)
- Scan completo de portas (`nmap`)
- Descoberta de diretórios (`gobuster`)
- Teste de vulnerabilidades (`nikto`)
- Fuzzing de parâmetros (`wfuzz`)
- Ataque SQL Injection básico (`sqlmap`)
- Relatórios organizados por ferramenta

## 🚀 Como usar

```bash
git clone https://github.com/ARESHAmohanad/Mu-Auto-Attack
cd Mu-Auto-Attack
chmod +x *
pip install -r requirements.txt
sudo ./install.sh
python3 mu_auto_attack.py http://example.com


