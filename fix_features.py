import glob

for ext in ('*.html', '*.js'):
    for filepath in glob.glob(ext):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content.replace('href="/features"', 'href="/#features"')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print('Updated features link in', filepath)
        except Exception as e:
            print("Error processing", filepath, e)
