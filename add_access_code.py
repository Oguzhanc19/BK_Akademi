import os
import re

base_dir = r"c:\Users\ASUS\Desktop\BK_Akademi - Kopya"
files_to_check = ['login.html', 'register.html']

code_wall_html = """
    <!-- ACCESS CODE WALL -->
    <style>
    #access-wall {
        position: fixed; inset: 0; background: rgba(10,14,39,0.95); backdrop-filter: blur(10px);
        z-index: 9999; display: flex; align-items: center; justify-content: center; flex-direction: column;
    }
    .aw-box {
        background: rgba(15,23,42,0.8); border: 1px solid rgba(99,102,241,0.3); border-radius: 16px;
        padding: 3rem; text-align: center; max-width: 400px; width: 90%; box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }
    .aw-box h2 { font-family: 'Playfair Display', serif; color: #fff; margin-bottom: 1rem; }
    .aw-box p { color: #94a3b8; font-size: 0.9rem; margin-bottom: 2rem; line-height: 1.5; }
    .aw-input {
        width: 100%; padding: 1rem; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1);
        border-radius: 8px; color: #fff; font-size: 1rem; text-align: center; letter-spacing: 2px;
        margin-bottom: 1rem; outline: none; transition: all 0.3s;
    }
    .aw-input:focus { border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99,102,241,0.2); }
    .aw-btn {
        width: 100%; padding: 1rem; background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: #fff; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;
        transition: all 0.3s;
    }
    .aw-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(99,102,241,0.4); }
    #aw-error { color: #f87171; font-size: 0.8rem; margin-top: 1rem; display: none; }
    </style>
    
    <div id="access-wall">
        <div class="aw-box">
            <h2>Öğrenci Girişi</h2>
            <p>Lütfen eğitmeniniz tarafından size verilen erişim kodunu girin.</p>
            <input type="password" id="awCode" class="aw-input" placeholder="Erişim Kodu" autocomplete="off">
            <button class="aw-btn" onclick="checkAccessCode()">Doğrula</button>
            <div id="aw-error">Geçersiz erişim kodu. Lütfen tekrar deneyin.</div>
        </div>
    </div>
    
    <script>
    const VALID_CODE = "BKA2026"; // Sabit erişim kodu
    
    document.addEventListener("DOMContentLoaded", () => {
        if (sessionStorage.getItem("bka_access_granted") === "true") {
            document.getElementById("access-wall").style.display = "none";
        }
    });
    
    function checkAccessCode() {
        const code = document.getElementById("awCode").value;
        if (code === VALID_CODE) {
            sessionStorage.setItem("bka_access_granted", "true");
            document.getElementById("access-wall").style.display = "none";
        } else {
            document.getElementById("aw-error").style.display = "block";
            document.getElementById("awCode").value = "";
        }
    }
    </script>
    <!-- /ACCESS CODE WALL -->
"""

for f in files_to_check:
    path = os.path.join(base_dir, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if "id=\"access-wall\"" not in content:
            # Insert right after <body>
            new_content = content.replace("<body>", f"<body>\n{code_wall_html}")
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Added access wall to {f}")

