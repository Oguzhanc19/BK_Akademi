import os
import re

base_dir = r"c:\Users\ASUS\Desktop\BK_Akademi - Kopya"

# --- 1. Update index.html image ---
index_path = os.path.join(base_dir, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80', 'photo1.jpg')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

# --- 2. Update about.html text and image ---
about_path = os.path.join(base_dir, 'about.html')
if os.path.exists(about_path):
    with open(about_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_about_text = """
    <div style="font-size: 1.05rem; line-height: 1.8; color: var(--text);">
        <h3 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-bottom: 1rem; color: var(--accent);">🚀 EZBERLERİ UNUTUN: ULUSLARARASI STANDARTLARDA İNGİLİZCE REVOLUTION!</h3>
        <p style="margin-bottom: 1.5rem;">Gramer kurallarına boğulup iki kelimeyi yan yana getiremediğiniz o eski, hantal sistemleri ait oldukları yerde, yani geçmişte bırakın! Benim ders sistemimde İngilizceyi "öğrenmiyorsunuz", İngilizceyi yaşıyor ve yönetiyorsunuz.</p>
        <p style="margin-bottom: 2rem;">Dünya standartları neyi gerektiriyorsa, masada o var. İşte sizi sıfırdan zirveye taşıyacak küresel sistemimiz:</p>
        
        <h3 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-bottom: 1rem;"><i class="fa-solid fa-globe" style="color:var(--accent);"></i> CEFR Standartlarında Dil Pasaportunuz Hazır!</h3>
        <p style="margin-bottom: 1rem;">Derslerimizin tamamı, Avrupa Ortak Dil Kriterleri (CEFR - Common European Framework of Reference for Languages) ile %100 uyumludur. Yani benimle katettiğiniz her mesafe, dünyanın her yerinde geçerli bir karşılığa sahip.</p>
        <p style="margin-bottom: 1.5rem; font-style: italic; color: var(--muted);">Peki, bu basamaklarda sizi neler bekliyor? Birlikte nereye koşuyoruz?</p>
        
        <ul style="list-style: none; padding-left: 0; margin-bottom: 2rem;">
            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-check" style="position: absolute; left: 0; top: 5px; color: #10b981;"></i> <strong>A1 - A2 (Survival Mode):</strong> İngilizceyle ilk temas! Buzları kırıyoruz. Kendinizi ifade etmeyi, temel günlük hayatta hayatta kalmayı ve o "anlıyorum ama konuşamıyorum" duvarının ilk tuğlalarını yıkmayı öğreniyorsunuz.</li>
            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-check" style="position: absolute; left: 0; top: 5px; color: #10b981;"></i> <strong>B1 - B2 (Independent User - Akıcılık Evresi):</strong> İşte parladığımız yer! İş toplantılarında sunum yapabilir, yabancı dizileri altyazısız izleyebilir ve fikirlerinizi çatır çatır, takılmadan savunacak akıcılığa ulaşırsınız. Küresel dünyanın vatandaşı olduğunuz evre burası.</li>
            <li style="margin-bottom: 1rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-check" style="position: absolute; left: 0; top: 5px; color: #10b981;"></i> <strong>C1 - C2 (Mastery & Fluency - Profesyonel Zirve):</strong> Dili adeta ana diliniz gibi, tüm incelikleriyle, akademik ve profesyonel düzeyde hatasız kullanma gücü. Sanat, iş, bilim... Alanınız ne olursa olsun liderlik koltuğu sizin!</li>
        </ul>

        <h3 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-bottom: 1rem;"><i class="fa-solid fa-trophy" style="color: #fbbf24;"></i> HEDEFİNİZ HANGİ SINAV? SINAV TİPLERİNDE %100 BAŞARI</h3>
        <p style="margin-bottom: 1.5rem;">Sadece genel İngilizce değil; kariyerinizi ve akademik geleceğinizi uçuracak tüm uluslararası ve ulusal sınav tiplerinde özel strateji ve taktiklerle dersler veriyorum. Sınavların şifrelerini birlikte kırıyoruz!</p>
        
        <h4 style="color: #fff; font-size: 1.1rem; margin-bottom: 0.8rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;"><i class="fa-solid fa-bullseye" style="color: #f43f5e;"></i> Uluslararası Akademik & Göçmenlik Sınavları</h4>
        <ul style="list-style: none; padding-left: 0; margin-bottom: 1.5rem;">
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-angle-right" style="position: absolute; left: 0; top: 5px; color: var(--accent);"></i> <strong>IELTS (Academic / General):</strong> Speaking, Writing, Reading ve Listening... Dört yetenekte de sınav yapıcıların sizden ne beklediğini çok iyi biliyorum. Puan hedefiniz neyse, o stratejiyle oynuyoruz.</li>
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-angle-right" style="position: absolute; left: 0; top: 5px; color: var(--accent);"></i> <strong>TOEFL iBT:</strong> Bilgisayar karşısında dil dökmek gözünüzü korkutmasın. Entegre (integrated) görevlerin, zaman yönetiminin ve şablonların kitabını yazıyoruz.</li>
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-angle-right" style="position: absolute; left: 0; top: 5px; color: var(--accent);"></i> <strong>Cambridge Exams (PET, FCE, CAE, CPE):</strong> Ömür boyu geçerli o prestijli sertifikaları portfolyonuza eklemek için gereken tüm akademik altyapıyı eksiksiz yüklüyoruz.</li>
        </ul>

        <h4 style="color: #fff; font-size: 1.1rem; margin-bottom: 0.8rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem;"><i class="fa-solid fa-bullseye" style="color: #f43f5e;"></i> Ulusal & Kurumsal Sınavlar</h4>
        <ul style="list-style: none; padding-left: 0; margin-bottom: 2rem;">
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-angle-right" style="position: absolute; left: 0; top: 5px; color: var(--accent);"></i> <strong>YDS & YÖKDİL:</strong> Dil bilgisi ve kelime tuzakları, paragraf şifreleri, soru kökü analizleri... Zamanla yarışırken doğru şıkka doğrudan gitmenin yollarını gösteriyorum.</li>
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-angle-right" style="position: absolute; left: 0; top: 5px; color: var(--accent);"></i> <strong>Hazırlık Muafiyet (Proficiency):</strong> Üniversitelerin hazırlık sınıflarını doğrudan atlayıp zaman kazanmanız için okulunuzun formatına özel nokta atışı hazırlık.</li>
        </ul>

        <h3 style="color: #fff; font-family: 'Playfair Display', serif; font-size: 1.3rem; margin-bottom: 1rem;"><i class="fa-solid fa-fire" style="color: #f97316;"></i> VE EN BÜYÜK FARKIMIZ: BİREBİR KOÇLUK SİSTEMİ (1-on-1 Coaching)</h3>
        <p style="margin-bottom: 1rem;">Herkesin öğrenme hızı, algılama biçimi ve hayat ritmi farklıdır. Bu yüzden ben sadece bir öğretmen değil, aynı zamanda sizin Yol Arkadaşınız ve Dil Koçunuzum.</p>
        <p style="margin-bottom: 1rem;">Derslerimizin yanı sıra sunduğum Birebir Koçluk hizmetiyle:</p>
        <ul style="list-style: none; padding-left: 0; margin-bottom: 2rem;">
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-star" style="position: absolute; left: 0; top: 5px; color: #fbbf24;"></i> Size özel, esnek ve hedefe yönelik Kişiselleştirilmiş Öğrenme Planı hazırlıyorum.</li>
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-star" style="position: absolute; left: 0; top: 5px; color: #fbbf24;"></i> Haftalık takipli, motivasyonunuzu her an diri tutan Mentorluk Desteği sağlıyorum.</li>
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-star" style="position: absolute; left: 0; top: 5px; color: #fbbf24;"></i> "Konuşma korkusu", "Hata yapma kaygısı" gibi psikolojik bariyerleri birebir seanslarla tamamen ortadan kaldırıyoruz.</li>
            <li style="margin-bottom: 0.8rem; padding-left: 1.5rem; position: relative;"><i class="fa-solid fa-star" style="position: absolute; left: 0; top: 5px; color: #fbbf24;"></i> 7/24 yaşayan bir feedback (geri bildirim) mekanizmasıyla, takıldığınız her an yanınızda oluyorum.</li>
        </ul>
        
        <!-- Add second image to the bottom of the about text -->
        <div style="margin-top: 3rem; margin-bottom: 2rem; border-radius: 20px; overflow: hidden; box-shadow: 0 15px 40px rgba(0,0,0,0.5);">
            <img src="photo2.jpg" alt="TEDx BKAkademi" style="width: 100%; height: auto; display: block; filter: brightness(0.9);">
        </div>
    </div>
    """
    
    # Replace old image
    content = content.replace('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80', 'photo1.jpg')
    
    # Replace content inside <div class="about-content">
    start_tag = '<div class="about-content">'
    end_tag = '</div>\n        </div>\n    </section>'
    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag) + len(start_tag)
        end_idx = content.find(end_tag, start_idx)
        content = content[:start_idx] + "\n" + new_about_text + "\n" + content[end_idx:]
    
    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(content)

# --- 3. Update anket.html to send email to oguzhan196060@gmail.com ---
anket_path = os.path.join(base_dir, 'anket.html')
if os.path.exists(anket_path):
    with open(anket_path, 'r', encoding='utf-8') as f:
        content = f.read()

    js_logic = """
    <script>
        const totalSteps = 6;

        function selectOption(stepNum, element) {
            const parent = element.parentElement;
            const cards = parent.querySelectorAll('.option-card');
            cards.forEach(c => c.classList.remove('selected'));
            element.classList.add('selected');
            document.getElementById('btn-next-' + stepNum).disabled = false;
        }

        function toggleMultiOption(stepNum, element) {
            element.classList.toggle('selected');
            const parent = element.parentElement;
            const anySelected = parent.querySelectorAll('.option-card.selected').length > 0;
            document.getElementById('btn-next-' + stepNum).disabled = !anySelected;
        }

        function nextStep(stepNum) {
            document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
            document.getElementById('step-' + stepNum).classList.add('active');
            updateProgress(stepNum);
        }

        function prevStep(stepNum) {
            document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
            document.getElementById('step-' + stepNum).classList.add('active');
            updateProgress(stepNum);
        }

        function updateProgress(stepNum) {
            const percent = (stepNum / totalSteps) * 100;
            document.getElementById('p-fill').style.width = percent + '%';
            document.getElementById('p-text').innerText = 'Adım ' + stepNum + ' / ' + totalSteps;
        }

        function showSuccess() {
            document.getElementById('surveyForm').style.display = 'none';
            document.getElementById('progress-container').style.display = 'none';
            document.getElementById('success-state').style.display = 'block';
        }

        async function submitSurvey(e) {
            e.preventDefault();
            
            // Collect Data
            const btn = document.getElementById('submit-btn');
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Gönderiliyor...';
            btn.disabled = true;

            let motivations = [];
            document.querySelectorAll('#step-1 .option-card.selected .oc-text').forEach(e => motivations.push(e.innerText));
            
            const examGoal = document.querySelector('#step-2 .option-card.selected .oc-text')?.innerText || "Belirtilmedi";
            const currentLevel = document.querySelector('#step-3 .option-card.selected .oc-text')?.innerText || "Belirtilmedi";
            const challenge = document.querySelector('#step-4 .option-card.selected .oc-text')?.innerText || "Belirtilmedi";
            const need = document.querySelector('#step-5 .option-card.selected .oc-text')?.innerText || "Belirtilmedi";

            const name = document.getElementById('qName').value;
            const phone = document.getElementById('qPhone').value;
            const email = document.getElementById('qEmail').value;
            const job = document.getElementById('qJob').value;

            const payload = {
                "Ad Soyad": name,
                "Telefon (WhatsApp)": phone,
                "E-Posta": email,
                "Meslek / Eğitim": job,
                "Motivasyon (Çoklu Seçim)": motivations.join(', '),
                "Sınav Hedefi": examGoal,
                "Mevcut Seviye": currentLevel,
                "En Büyük Zorluk": challenge,
                "En Çok İhtiyaç Duyulan": need,
                "_subject": "Yeni Anket Başvurusu: " + name
            };

            try {
                // Submit to FormSubmit.co without refreshing page
                await fetch("https://formsubmit.co/ajax/oguzhan196060@gmail.com", {
                    method: "POST",
                    headers: { 
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify(payload)
                });
                
                showSuccess();
            } catch (err) {
                alert("Gönderim sırasında bir hata oluştu. Lütfen bağlantınızı kontrol edin.");
                btn.innerHTML = 'Değerlendirmeyi Gönder <i class="fa-solid fa-paper-plane"></i>';
                btn.disabled = false;
            }
        }
    </script>
    """
    
    # Add IDs to inputs in Step 6
    content = content.replace('<input type="text" class="form-control" required placeholder="Kısa Yanıt">', '<input type="text" id="qName" class="form-control" required placeholder="Kısa Yanıt">', 1)
    content = content.replace('<input type="tel" class="form-control" required placeholder="Kısa Yanıt">', '<input type="tel" id="qPhone" class="form-control" required placeholder="Kısa Yanıt">', 1)
    content = content.replace('<input type="email" class="form-control" required placeholder="Kısa Yanıt">', '<input type="email" id="qEmail" class="form-control" required placeholder="Kısa Yanıt">', 1)
    content = content.replace('<input type="text" class="form-control" placeholder="Kısa Yanıt">', '<input type="text" id="qJob" class="form-control" placeholder="Kısa Yanıt">', 1)
    
    content = content.replace('<button type="submit" class="btn-next">Değerlendirmeyi Gönder', '<button type="submit" id="submit-btn" class="btn-next">Değerlendirmeyi Gönder')
    
    content = content.replace('<form id="surveyForm" onsubmit="event.preventDefault(); showSuccess();">', '<form id="surveyForm" onsubmit="submitSurvey(event)">')
    
    # Replace old script
    start_sc = '<script>'
    end_sc = '</script>\n</body>'
    if start_sc in content and end_sc in content:
        start_idx = content.find(start_sc)
        end_idx = content.find(end_sc) + len('</script>')
        content = content[:start_idx] + js_logic + content[end_idx:]
    
    with open(anket_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("All requests completed!")
