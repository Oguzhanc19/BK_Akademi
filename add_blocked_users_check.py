import os

def update_login():
    with open('login.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_code = """function red(u){
  window.location.href = Array.isArray(window.ADMIN_EMAILS) && window.ADMIN_EMAILS.includes(u.email) ? 'admin' : 'dashboard';
}"""
    
    new_code = """async function red(u){
  try {
    const blocked = await db.collection('blockedUsers').doc(u.email).get();
    if (blocked.exists) {
      await auth.signOut();
      const err = document.getElementById('err');
      if (err) {
        err.style.display='block';
        err.innerHTML='<i class="fas fa-exclamation-triangle"></i> Bu hesap kalıcı olarak silinmiştir.';
      }
      return;
    }
  } catch(e) {}
  window.location.href = Array.isArray(window.ADMIN_EMAILS) && window.ADMIN_EMAILS.includes(u.email) ? 'admin' : 'dashboard';
}"""
    
    content = content.replace(old_code, new_code)
    with open('login.html', 'w', encoding='utf-8') as f:
        f.write(content)


def update_register():
    with open('register.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_code = "auth.onAuthStateChanged(u => { if(u) window.location.href=Array.isArray(window.ADMIN_EMAILS)&&window.ADMIN_EMAILS.includes(u.email)?'admin':'dashboard'; });"
    
    new_code = """auth.onAuthStateChanged(async u => { 
  if(u) {
    try {
      const blocked = await db.collection('blockedUsers').doc(u.email).get();
      if (blocked.exists) {
        await auth.signOut();
        const err = document.getElementById('err');
        if (err) {
          err.style.display='block';
          err.innerHTML='<i class="fas fa-exclamation-triangle"></i> Bu hesap kalıcı olarak silinmiştir.';
        }
        return;
      }
    } catch(e) {}
    window.location.href=Array.isArray(window.ADMIN_EMAILS)&&window.ADMIN_EMAILS.includes(u.email)?'admin':'dashboard'; 
  }
});"""
    
    content = content.replace(old_code, new_code)
    with open('register.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_login()
update_register()
print("Updated login and register to check blockedUsers.")
