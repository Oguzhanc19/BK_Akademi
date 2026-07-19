import glob

def update_dashboards():
    for filepath in ('dashboard.html', 'dashboard_light.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        old_code = "const n = user.displayName || user.email.split('@')[0];"
        
        new_code = """try {
    const blocked = await db.collection('blockedUsers').doc(user.email).get();
    if (blocked.exists) {
      auth.signOut();
      window.location.href = 'login';
      return;
    }
  } catch(e) {}
  
  const n = user.displayName || user.email.split('@')[0];"""
        
        content = content.replace(old_code, new_code)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

update_dashboards()
print("Updated dashboards.")
