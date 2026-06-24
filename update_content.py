import os
import re

base_dir = r"c:\Users\ASUS\Desktop\BK_Akademi - Kopya"
files_to_check = ['index.html', 'about.html', 'login.html', 'register.html', 'dashboard.html', 'admin.html', 'payment.html', 'resources.html']

replacements = [
    ("Ücretsiz Bilgi Alın", "Hemen Bilgi Al"),
    ("Ücretsiz Dene", "Hemen Dene"),
    ("İlk Ders Ücretsiz", "Deneme Dersi Alın"),
    ("Ücretsiz Başla", "Hemen Başla"),
    ("Ücretsiz", ""), # catch-all for any stray ones
    ("padding: 7rem 3rem;", "padding: 4rem 3rem;"),
    ("padding: 8rem 3rem 4rem;", "padding: 5rem 3rem 2rem;"),
    ("padding: 5rem 3rem;", "padding: 3rem 3rem;"),
    ("margin-top: 4rem;", "margin-top: 2rem;"),
    ("padding: 4rem 3rem;", "padding: 3rem 2rem;"), # further compress stats strip
    ('href="register.html"', 'href="iletisim.html"'),
    # For login buttons that are meant to be CTA (like "Ücretsiz Dene" which went to login)
    ('href="login.html" class="btn-primary"', 'href="iletisim.html" class="btn-primary"'),
    ('href="login.html" class="btn-p"', 'href="iletisim.html" class="btn-p"'),
]

for f in files_to_check:
    path = os.path.join(base_dir, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        original = content
        
        # We don't want to break the actual login links in navbars. 
        # Only CTA buttons usually have specific classes.
        
        for old, new in replacements:
            content = content.replace(old, new)
            
        # Specific fix for "Ücretsiz" leaving empty spaces or weird grammar
        content = content.replace(" Hemen Başla", "Hemen Başla")
        content = content.replace(" Hemen Dene", "Hemen Dene")
        content = content.replace(" Hemen Bilgi Al", "Hemen Bilgi Al")
        
        if content != original:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")

