import os
import re

base_dir = r"c:\Users\ASUS\Desktop\BK_Akademi - Kopya"
files_to_check = ['index.html', 'about.html']

for f in files_to_check:
    path = os.path.join(base_dir, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original = content
        
        # Replace only when it has CTA button classes
        content = content.replace('href="iletisim.html" class="btn-primary"', 'href="anket.html" class="btn-primary"')
        content = content.replace('href="iletisim.html" class="btn-nav"', 'href="anket.html" class="btn-nav"')
        content = content.replace('href="iletisim.html" class="btn-p"', 'href="anket.html" class="btn-p"')
        
        # If there are any other specific buttons in about.html or index.html
        content = content.replace('href="iletisim.html" class="btn-secondary"', 'href="anket.html" class="btn-secondary"')
        
        if content != original:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")

