// Firebase yapılandırma dosyası
// Buradaki alanları kendi Firebase projenizin ayarlarıyla doldurun.
// Firebase konsolundan (Project settings > General) kopyalayabilirsiniz.

// ÖRNEK (DEĞİŞTİRİN):
// Aşağıdaki firebaseConfig içindeki değerler Firebase konsolundan kopyalanmıştır.
// Bu dosya, HTML'de CDN ile yüklenen "compat" sürümleriyle (firebase-app-compat.js vb.) birlikte çalışır.
// Bu yüzden burada "import" kullanmıyoruz, doğrudan global firebase nesnesini kullanıyoruz.

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC2iKtrT8sET4kWgGvZBfwm1HJiWFaJhPg",
  authDomain: "bkakademi-5177f.firebaseapp.com",
  projectId: "bkakademi-5177f",
  // ÖNEMLİ: Storage bucket alanı firebase konsolunda genelde *.appspot.com şeklindedir.
  // Konsolda "Storage" sekmesinden gördüğünüz bucket ismini bire bir buraya yazın.
  storageBucket: "bkakademi-5177f.firebasestorage.app",
  messagingSenderId: "1052989546166",
  appId: "1:1052989546166:web:302602fde140c2bfa91017",
  measurementId: "G-3KGQ65EKBE"
};

if (typeof firebase === 'undefined') {
  console.error('Firebase SDK yüklenmeden firebase-config.js çağrıldı. HTML içinde önce Firebase CDN scriptlerini eklediğinizden emin olun.');
} else {
  if (!firebase.apps.length && typeof firebaseConfig !== 'undefined') {
    firebase.initializeApp(firebaseConfig);
  }

  // Global referanslar
  window.auth = firebase.auth();
  window.db = firebase.firestore();
  window.storage = firebase.storage();

  // Basit admin kontrolü için admin e-posta listesi.
  // BURAYA kendi admin hesabınızın e-postasını ekleyin.
  window.ADMIN_EMAILS = [
    'oguzhan606019@gmail.com',
    'admin@bkakademi.com',
    'admin2@gmail.com'
  ];
}

// --- SİBER GÜVENLİK (XSS KORUMASI) ---
// Kullanıcı girdilerini ekrana basarken zararlı kodları etkisiz hale getirir
window.escapeHTML = function(str) {
  if (typeof str !== 'string') return str;
  return str.replace(/[&<>'"]/g, function(tag) {
    const charsToReplace = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    };
    return charsToReplace[tag] || tag;
  });
};
