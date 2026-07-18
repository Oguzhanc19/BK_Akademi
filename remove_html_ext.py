import os, re, glob

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    original_content = content

    # Replace window.location.href='index.html' -> window.location.href='/'
    content = re.sub(r'window\.location\.href\s*=\s*[\'"`]index\.html[\'"`]', 'window.location.href="/"', content)
    # Replace other window.location.href='xxx.html' -> window.location.href='xxx'
    content = re.sub(r'window\.location\.href\s*=\s*[\'"`]([a-zA-Z0-9_-]+)\.html[\'"`]', r'window.location.href="\1"', content)

    # Replace href='index.html' -> href='/'
    content = re.sub(r'href=[\'"`]index\.html#?([^\'"`]*)[\'"`]', r'href="/\1"', content)
    
    # Replace href='xxx.html' -> href='xxx'
    content = re.sub(r'href=[\'"`]([a-zA-Z0-9_-]+)\.html#?([^\'"`]*)[\'"`]', lambda m: 'href="' + m.group(1) + (('#'+m.group(2)) if m.group(2) else '') + '"', content)

    # Also check for window.location = '...'
    content = re.sub(r'window\.location\s*=\s*[\'"`]index\.html[\'"`]', 'window.location="/"', content)
    content = re.sub(r'window\.location\s*=\s*[\'"`]([a-zA-Z0-9_-]+)\.html[\'"`]', r'window.location="\1"', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', filepath)

for ext in ('*.html', '*.js'):
    for filepath in glob.glob(ext):
        process_file(filepath)
