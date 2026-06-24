import os
import re

base_dir = r"c:\Users\ASUS\Desktop\BK_Akademi - Kopya"

# --- 1. Update index.html (Nasıl Çalışır section) ---
index_path = os.path.join(base_dir, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1
    content = content.replace('<h3>Hesap Oluşturun</h3>', '<h3>Ön Değerlendirme</h3>')
    content = content.replace('<p>Ücretsiz hesabınızı saniyeler içinde oluşturun ve platforma giriş yapın.</p>', '<p>Kısa bir anketle hedeflerinizi ve seviyenizi belirleyin.</p>')
    
    # Step 2
    content = content.replace('<h3>Seviyenizi Belirleyin</h3>', '<h3>Uzman Görüşmesi</h3>')
    content = content.replace('<p>Kısa bir seviye tespit sınavı ile size en uygun içerikleri sunalım.</p>', '<p>Eğitim danışmanlarımızla ihtiyaçlarınızı analiz edelim.</p>')
    
    # Step 3
    content = content.replace('<h3>Öğrenmeye Başlayın</h3>', '<h3>Eğitime Başlayın</h3>')
    content = content.replace('<p>Günlük hedeflerinizi tamamlayın, kelime haznenizi genişletin ve puanlar kazanın.</p>', '<p>Size özel tanımlanan erişim koduyla paneline giriş yap ve başla.</p>')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html steps")


# --- 2. Update iletisim.html (Logo fix) ---
iletisim_path = os.path.join(base_dir, 'iletisim.html')
if os.path.exists(iletisim_path):
    with open(iletisim_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # The logo is already styled with Playfair Display in CSS:
    # .nav-logo { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; text-decoration: none; color: #fff; }
    # But wait, looking at index.html, maybe the class name is different?
    # In index.html, logo is <a href="#" class="logo">BKAkademi<span>.</span></a>
    # Let me check index.html logo class just to be sure... I will change .nav-logo to match exactly.
    # Actually, in iletisim.html, I used <em> instead of <span> and the CSS is there. The user said it "looks plain text".
    # I will replace the logo HTML in iletisim.html to match index.html exactly if needed, but wait, index.html logo is:
    # <a href="#" class="logo">BKAkademi<span>.</span></a> 
    # And index.css has: .logo { font-family: 'Playfair Display', serif; font-size: 1.8rem; ... }
    # Let's just update the logo HTML and CSS in iletisim.html directly using regex.
    content = re.sub(r'<a href="index.html" class="nav-logo">.*?</a>', '<a href="index.html" class="logo" style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; font-weight: 700; color: #fff; text-decoration: none;">BKAkademi<span style="color: #6366f1; font-style: italic;">.</span></a>', content)
    
    with open(iletisim_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated iletisim.html logo")


# --- 3. Update login.html (Add 3D Image & Dynamic Code logic) ---
login_path = os.path.join(base_dir, 'login.html')
if os.path.exists(login_path):
    with open(login_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add image to login left panel
    # Find a good place, maybe inside <div class="quote-section">
    img_html = '<div style="text-align:center; margin: 2rem 0;"><img src="login_img.png" alt="Login 3D" style="max-width: 80%; border-radius: 20px; animation: float 6s ease-in-out infinite; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));"></div>'
    if 'login_img.png' not in content:
        content = content.replace('<div class="quote-section">', f'<div class="quote-section">\n{img_html}')
    
    # Update logic script for access code to check localStorage
    old_script = 'const VALID_CODE = "BKA2026"; // Sabit erişim kodu'
    new_script = """
    function getValidCodes() {
        let codes = localStorage.getItem("bka_access_codes");
        return codes ? JSON.parse(codes) : ["BKA2026"]; // Varsayılan bir kod ekleyelim
    }
    """
    
    content = content.replace(old_script, new_script)
    content = content.replace('if (code === VALID_CODE)', 'const validCodes = getValidCodes();\n        if (validCodes.includes(code))')
    
    with open(login_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated login.html")


# --- 4. Update register.html (Add 3D Image & Dynamic Code logic) ---
register_path = os.path.join(base_dir, 'register.html')
if os.path.exists(register_path):
    with open(register_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    img_html = '<div style="text-align:center; margin: 2rem 0;"><img src="register_img.png" alt="Register 3D" style="max-width: 80%; border-radius: 20px; animation: float 6s ease-in-out infinite; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.5));"></div>'
    if 'register_img.png' not in content:
        # Put it in the visual panel
        content = content.replace('<div class="benefits">', f'{img_html}\n<div class="benefits">')
        
    # Update logic script for access code to check localStorage
    content = content.replace(old_script, new_script)
    content = content.replace('if (code === VALID_CODE)', 'const validCodes = getValidCodes();\n        if (validCodes.includes(code))')
    
    with open(register_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated register.html")


# --- 5. Update admin.html (Add Code Generator Panel) ---
admin_path = os.path.join(base_dir, 'admin.html')
if os.path.exists(admin_path):
    with open(admin_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    admin_panel_html = """
    <!-- Code Generator Panel -->
    <div class="panel" id="code-generator-panel" style="margin-bottom: 2rem; background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(15,23,42,0.8)); border-color: rgba(99,102,241,0.3);">
        <div class="ph">
            <h3><i class="fa-solid fa-key"></i> Öğrenci Erişim Kodu Üret</h3>
        </div>
        <div style="display: flex; gap: 1rem; align-items: center;">
            <button onclick="generateAccessCode()" class="btn-up" style="width: auto; margin-top: 0; padding: 0.8rem 1.5rem;"><i class="fa-solid fa-plus"></i> Yeni Kod Üret</button>
            <div id="generated-code-display" style="font-family: monospace; font-size: 1.5rem; color: #fff; background: rgba(0,0,0,0.3); padding: 0.8rem 1.5rem; border-radius: 8px; border: 1px dashed rgba(99,102,241,0.5); letter-spacing: 2px;">---</div>
        </div>
        <p style="color: #94a3b8; font-size: 0.8rem; margin-top: 1rem;">Bu kodları öğrencilere vererek sisteme kayıt olmalarını / giriş yapmalarını sağlayabilirsiniz. Kodlar tarayıcının hafızasında tutulur.</p>
        
        <script>
        function generateAccessCode() {
            const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
            let code = 'BKA-';
            for(let i=0; i<5; i++) {
                code += chars.charAt(Math.floor(Math.random() * chars.length));
            }
            
            document.getElementById('generated-code-display').innerText = code;
            
            // Save to localStorage
            let codes = localStorage.getItem('bka_access_codes');
            let codesArray = codes ? JSON.parse(codes) : ["BKA2026"];
            codesArray.push(code);
            localStorage.setItem('bka_access_codes', JSON.stringify(codesArray));
            
            // Show toast
            const toast = document.getElementById('toast');
            if(toast) {
                toast.innerText = "Yeni kod üretildi ve kaydedildi!";
                toast.className = "show s";
                setTimeout(() => toast.className = "", 3000);
            }
        }
        </script>
    </div>
    """
    
    if "code-generator-panel" not in content:
        # Insert at the beginning of the overview section content
        content = content.replace('<div id="overview" class="sec active">', f'<div id="overview" class="sec active">\n{admin_panel_html}')
        with open(admin_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated admin.html with Code Generator")

