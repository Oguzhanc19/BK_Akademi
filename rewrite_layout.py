import os

with open('bengu-karakurt.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 4rem;">'
end_marker = '<div style="text-align: center; margin-top: 5rem;">'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = '''<style>
  .bio-grid {
    display: grid;
    gap: 2.5rem;
    align-items: center;
    margin-bottom: 4rem;
  }
  @media (min-width: 900px) {
    .bio-grid {
      grid-template-columns: 1fr 1.6fr 1fr;
    }
  }
  @media (max-width: 899px) {
    .bio-grid {
      grid-template-columns: 1fr;
    }
  }
  .bio-img {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  }
  .bio-img img {
    width: 100%;
    height: auto;
    object-fit: cover;
    display: block;
  }
  .bio-text {
    color: var(--ink2);
    font-size: 1.1rem;
    line-height: 1.9;
    text-align: justify;
    padding: 0 1rem;
  }
</style>

    <div class="bio-grid">
      <div class="bio-img">
        <img src="bengu_tedx1.jpg" alt="Bengü Karakurt TEDx Sahnesi">
      </div>
      
      <div class="bio-text">
        <p style="margin-bottom: 1.5rem;">
          Merhaba, ben Bengü Karakurt! Dijital dünyada beni <strong>'Anlat Bengü'</strong> olarak da tanıyor olabilirsiniz. İngiliz Dili ve Edebiyatı mezunu bir İngilizce öğretmeni ve içerik üreticisiyim.
        </p>
        <p>
          Çalışmalarıma ağırlıklı olarak Samsun'da devam ediyor; her seviyeden öğrenciye genel İngilizce eğitimlerinin yanı sıra ileri düzey <strong>SAT sınavına hazırlık</strong> dersleri veriyorum.
        </p>
      </div>

      <div class="bio-img">
        <img src="bengu_tedx2.jpg" alt="Bengü Karakurt Ödül">
      </div>
    </div>

    <div class="bio-grid">
      <div class="bio-img">
        <img src="bengu_tedx3.jpg" alt="Bengü Karakurt TEDx Konuşması">
      </div>
      
      <div class="bio-text">
        <p style="margin-bottom: 1.5rem;">
          Eğitim felsefemin temelinde, İngilizceyi sıkıcı dilbilgisi kurallarından kurtarıp günlük hayatın eğlenceli bir parçası haline getirmek yatıyor. Toplumumuzdaki yabancı dil öğrenme önyargılarını kırmak amacıyla Ondokuz Mayıs Üniversitesi'nde <em>'Kim Tutar Seni'</em> başlıklı seminerler düzenledim.
        </p>
        <p>
          Bu vizyonumu 20 Nisan 2026'da <strong>TEDxEBYÜ</strong> sahnesine taşıyarak <em>'Neden İngilizce'yi anlıyoruz ama konuşamıyoruz?'</em> konulu bir konuşma gerçekleştirdim. Ayrıca Şubat 2024'te <strong>'Kim Milyoner Olmak İster?'</strong> yarışmasına katılarak bu heyecanımı ekranlarda da paylaştım. Gelin, İngilizce ile aranızdaki psikolojik bariyerleri birlikte aşalım!
        </p>
      </div>

      <div class="bio-img">
        <img src="bengu_tedx4.jpg" alt="Bengü Karakurt TEDxEBYÜ Plaketi">
      </div>
    </div>

    '''

    final_content = content[:start_idx] + new_content + content[end_idx:]
    with open('bengu-karakurt.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print('Updated layout successfully!')
else:
    print('Could not find markers.')
