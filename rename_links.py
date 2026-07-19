import os, glob

replacements = {
    '"iletisim"': '"contact"',
    "'iletisim'": "'contact'",
    '"anket"': '"survey"',
    "'anket'": "'survey'",
    '"sikca-sorulan-sorular"': '"faq"',
    "'sikca-sorulan-sorular'": "'faq'",
    "'admin.html'": "'admin'",
    '"admin.html"': '"admin"',
    "'dashboard.html'": "'dashboard'",
    '"dashboard.html"': '"dashboard"',
    "'dashboard_light.html'": "'dashboard_light'",
    '"dashboard_light.html"': '"dashboard_light"',
    "'login.html'": "'login'",
    '"login.html"': '"login"',
    "'register.html'": "'register'",
    '"register.html"': '"register"',
    "'index.html'": "'/'",
    '"index.html"': '"/"',
    "'iletisim.html'": "'contact'",
    '"iletisim.html"': '"contact"',
    "'anket.html'": "'survey'",
    '"anket.html"': '"survey"',
    "'sikca-sorulan-sorular.html'": "'faq'",
    '"sikca-sorulan-sorular.html"': '"faq"',
    '"/features"': '"/#features"', # just in case I missed it somewhere
}

for ext in ('*.html', '*.js'):
    for filepath in glob.glob(ext):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print('Updated', filepath)
        except Exception as e:
            pass
