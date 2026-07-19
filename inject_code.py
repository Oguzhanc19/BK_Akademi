import glob

for filepath in ('dashboard.html', 'dashboard_light.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # HTML insertion
        content = content.replace('id="pemail">—</div></div>', 'id="pemail">—</div><div style="font-size:.85rem;color:var(--ac);margin-top:0.3rem;" id="pcode"></div></div>')
        
        # JS insertion
        old_js = "document.getElementById('pemail').textContent = user.email;"
        new_js = old_js + """
  try { db.collection('accessCodes').where('usedBy', '==', user.uid).get().then(snap => { if(!snap.empty) document.getElementById('pcode').innerHTML = 'Erişim Kodu: <strong>' + snap.docs[0].data().code + '</strong>'; }); } catch(e) {}"""
        content = content.replace(old_js, new_js)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated code display in', filepath)
    except Exception as e:
        print(e)
