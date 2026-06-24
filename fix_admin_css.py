import os
import re

original_path = r"C:\Users\ASUS\Desktop\BK_Akademi\admin.html"
current_path = r"C:\Users\ASUS\Desktop\BK_Akademi - Kopya\admin.html"

# Read original file
with open(original_path, 'r', encoding='utf-8') as f:
    orig_content = f.read()

# Extract original <style> block
match = re.search(r'<style>.*?</style>', orig_content, flags=re.DOTALL)
if match:
    orig_style = match.group(0)
    
    # We want to insert our new overrides at the end of the original style block
    theme_overrides = """
/* BKAkademi Premium Dark Theme Override for Admin Panel */
:root {
  --bg: #0a0e27;
  --sur: rgba(15, 23, 42, 0.7);
  --sur2: rgba(30, 41, 59, 0.5);
  --ink: #f8fafc;
  --ink2: #cbd5e1;
  --mu: #94a3b8;
  --bdr: rgba(255, 255, 255, 0.1);
  --bdr2: rgba(255, 255, 255, 0.05);
  --ac: #6366f1;
  --ac2: #8b5cf6;
  --al: rgba(99, 102, 241, 0.15);
  --rd: #f43f5e;
  --rl: rgba(244, 63, 94, 0.15);
  --grn: #10b981;
  --gl: rgba(16, 185, 129, 0.15);
  --gld: #fbbf24;
  --sh: 0 10px 30px rgba(0,0,0,0.5);
  --sh3: 0 0 20px rgba(99,102,241,0.3);
}
body { background-color: var(--bg); background-image: radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 30px 30px; }
aside { background: rgba(10, 14, 39, 0.8) !important; backdrop-filter: blur(20px) !important; border-right: 1px solid var(--bdr) !important; }
.topbar { background: rgba(10, 14, 39, 0.5) !important; backdrop-filter: blur(15px) !important; border-bottom: 1px solid var(--bdr) !important; }
.panel, .stat, .ucrd { background: var(--sur) !important; backdrop-filter: blur(12px) !important; border: 1px solid var(--bdr) !important; box-shadow: var(--sh) !important; }
.panel:hover, .stat:hover, .ucrd:hover { border-color: var(--ac) !important; box-shadow: 0 10px 40px rgba(99,102,241,0.2) !important; }
"""
    
    # Inject overrides before </style>
    new_style = orig_style.replace('</style>', theme_overrides + '\n</style>')

    # Now replace the broken style block in current_path with new_style
    with open(current_path, 'r', encoding='utf-8') as f:
        curr_content = f.read()
    
    # Replace the current <style> block
    curr_content = re.sub(r'<style>.*?</style>', new_style, curr_content, flags=re.DOTALL)
    
    with open(current_path, 'w', encoding='utf-8') as f:
        f.write(curr_content)
    
    print("Fixed admin.html CSS!")
else:
    print("Original style block not found.")
