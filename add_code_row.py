import glob

for filepath in ('dashboard.html', 'dashboard_light.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Insert the row into the Profilim table
        old_html = '<div class="ir"><span class="ik">E-posta</span><span class="iv" id="pe">—</span></div>'
        new_html = old_html + '\n          <div class="ir"><span class="ik">Erişim Kodu</span><span class="iv" id="pe-code" style="font-weight:bold;color:var(--ac);">—</span></div>'
        content = content.replace(old_html, new_html)
        
        # Update the javascript to also update pe-code
        old_js = "document.getElementById('pcode').innerHTML = 'Erişim Kodu: <strong>' + snap.docs[0].data().code + '</strong>';"
        new_js = "document.getElementById('pcode').innerHTML = 'Erişim Kodu: <strong>' + snap.docs[0].data().code + '</strong>'; document.getElementById('pe-code').textContent = snap.docs[0].data().code;"
        content = content.replace(old_js, new_js)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated UI in', filepath)
    except Exception as e:
        print(e)
