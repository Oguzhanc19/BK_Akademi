import os
import re

base_dir = r"c:\Users\ASUS\Desktop\BK_Akademi - Kopya"

# Files that already have a <style> block to replace
standard_files = ['index', 'about', 'login', 'register', 'dashboard', 'admin']

for f in standard_files:
    html_path = os.path.join(base_dir, f"{f}.html")
    css_path = os.path.join(base_dir, f"{f}.css")
    
    if os.path.exists(html_path) and os.path.exists(css_path):
        with open(html_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        with open(css_path, 'r', encoding='utf-8') as css_file:
            new_css = css_file.read()
            
        # Replace the first <style>...</style> block
        new_content = re.sub(r'<style>.*?</style>', new_css, content, flags=re.DOTALL, count=1)
        
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}.html")

# Files where we inject the CSS before </head>
tailwind_files = ['payment', 'resources']

for f in tailwind_files:
    html_path = os.path.join(base_dir, f"{f}.html")
    css_path = os.path.join(base_dir, f"{f}.css")
    
    if os.path.exists(html_path) and os.path.exists(css_path):
        with open(html_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        with open(css_path, 'r', encoding='utf-8') as css_file:
            new_css = css_file.read()
            
        # Insert before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', f'{new_css}\n</head>', 1)
            with open(html_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}.html")
        else:
            print(f"Could not find </head> in {f}.html")

