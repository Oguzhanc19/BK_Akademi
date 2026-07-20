import os

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_split = content.split('<main')
header = head_split[0]

footer_split = head_split[1].split('</main>')
footer = '</main>' + footer_split[1]

# Make sure title is updated
header = header.replace('<title>Hakkında | BKAkademi</title>', '<title>Bengü Karakurt Kimdir? | BKAkademi</title>')

main_content = ''' style="flex: 1 0 auto; width: 100%; display: flex; flex-direction: column;">
<section style="padding: 5rem 5%; background: #fff;">
  <div style="max-width: 1200px; margin: 0 auto;">
    
    <div style="text-align:center; margin-bottom: 4rem;">
      <div class="eyebrow"><i class="fas fa-star"></i> Hakkımda</div>
      <h1 style="font-family: 'Playfair Display', serif; font-size: 3rem; color: var(--ink);">Bengü Karakurt Kimdir?</h1>
      <p style="font-size: 1.1rem; color: var(--ink2); max-width: 700px; margin: 1rem auto; line-height: 1.8;">
        İngilizceyi bir ders olmaktan çıkarıp, hayatınızın merkezine yerleştiren, kalıpları yıkan eğitim ve gelişim vizyoneri.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">
      <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
        <img src="bengu_tedx1.jpg" alt="Bengü Karakurt TEDx Sahnesi" style="width: 100%; height: 100%; object-fit: cover; display: block;">
      </div>
      <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
        <img src="bengu_tedx2.jpg" alt="Bengü Karakurt Ödül" style="width: 100%; height: 100%; object-fit: cover; display: block;">
      </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 2rem; max-width: 900px; margin: 0 auto; color: var(--ink2); font-size: 1.1rem; line-height: 1.8;">
      <p>
        <strong>Erzincan Binali Yıldırım Üniversitesi'nde</strong> düzenlenen TEDxEBYÜ sahnesinde "Yengeç Sepeti" başlıklı konuşmasıyla kalıplara meydan okuyan Bengü Karakurt, klasik eğitim sistemlerinin dayattığı sınırları aşmayı hedefleyen yenilikçi bir vizyona sahiptir.
      </p>
      <p>
        İngilizce eğitiminde sadece gramer kurallarını ezberletmek yerine, dili yaşayarak ve hissederek öğrenme felsefesini savunur. <em>"İngilizceyi öğrenmiyorsunuz, yaşıyor ve yönetiyorsunuz"</em> mottosuyla yola çıkarak, uluslararası standartlarda, CEFR uyumlu ve birebir öğrenci odaklı eğitim modelleri geliştirmiştir.
      </p>
      <p>
        TEDx sahnesindeki duruşundan da anlaşılacağı üzere, o sadece bir İngilizce öğretmeni değil; aynı zamanda öğrencilerine ilham veren, potansiyellerini ortaya çıkarmalarını sağlayan bir yol göstericidir. BK Akademi'nin kurucusu olarak, öğrencilerin potansiyelini maksimize etmek ve onları küresel dünyada özgüvenle iletişim kurabilecek bireyler haline getirmek için çalışır.
      </p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 4rem;">
      <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
        <img src="bengu_tedx3.jpg" alt="Bengü Karakurt TEDx Konuşması" style="width: 100%; height: 100%; object-fit: cover; display: block;">
      </div>
      <div style="border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
        <img src="bengu_tedx4.jpg" alt="Bengü Karakurt TEDxEBYÜ Plaketi" style="width: 100%; height: 100%; object-fit: cover; display: block;">
      </div>
    </div>

    <div style="text-align: center; margin-top: 5rem;">
      <a href="survey" class="btn-p">Tanışma Dersi Ayarla <i class="fas fa-calendar-check"></i></a>
    </div>

  </div>
</section>
'''

full_html = header + '<main' + main_content + footer

with open('bengu-karakurt.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print('bengu-karakurt.html generated successfully!')
