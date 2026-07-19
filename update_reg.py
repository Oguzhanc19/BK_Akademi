import os

with open('register.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_catch = "  catch(e){ err.textContent = norm(e); }"

new_catch = """  catch(e){ 
    if(e.code === 'auth/email-already-in-use') {
      try {
        const c = await auth.signInWithEmailAndPassword(em, pw);
        
        // Remove from blockedUsers if they are recovering a deleted account
        try { await db.collection('blockedUsers').doc(em).delete(); } catch(err) {}
        
        await c.user.updateProfile({displayName: fname + ' ' + lname});
        await verifyAndEnter(c.user, err, codeDoc.id);
      } catch(signInErr) {
        err.textContent = 'Bu e-posta adresi kullanımda. Sildiğiniz bir hesabı yeniden açıyorsanız lütfen eski şifrenizi doğru girdiğinizden emin olun.';
      }
    } else {
      err.textContent = norm(e); 
    }
  }"""

content = content.replace(old_catch, new_catch)

old_google = "    await verifyAndEnter(r.user, err, codeDoc.id);"
new_google = "    try { await db.collection('blockedUsers').doc(r.user.email).delete(); } catch(err) {}\n    await verifyAndEnter(r.user, err, codeDoc.id);"
content = content.replace(old_google, new_google)

with open('register.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated register flow.')
