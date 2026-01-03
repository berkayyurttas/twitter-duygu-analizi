# 🐦 Türkçe Twitter (X) Duygu Analizi Projesi

Bu proje, Makine Öğrenmesi (Machine Learning) ve Doğal Dil İşleme (NLP) tekniklerini kullanarak Türkçe tweetlerin duygu durumunu **(Pozitif, Negatif, Nötr)** analiz eden bir web uygulamasıdır.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Sklearn](https://img.shields.io/badge/Library-Scikit--Learn-orange)

## 🎯 Projenin Amacı
Sosyal medyada paylaşılan Türkçe metinlerin arkasındaki duyguyu otomatik olarak tespit etmek. Özellikle Türkçe'nin yapısal zorluklarını (olumsuzluk ekleri, ironi vb.) aşarak yüksek doğruluklu bir sınıflandırma modeli geliştirmek.

## 🚀 Proje Süreci: Adım Adım Ne Yaptık?

Bu proje 4 ana aşamadan oluşmaktadır:

### 1. Veri Ön İşleme (Data Preprocessing)
Ham Twitter verisi gürültülüdür. Modelin daha iyi öğrenmesi için şu temizlik işlemleri yapıldı:
* **Temizlik:** Linkler (`http`), kullanıcı adları (`@user`), noktalama işaretleri ve sayılar Regex kullanılarak temizlendi.
* **Stopwords (Etkisiz Kelimeler):** *ve, ama, ile* gibi anlam taşımayan kelimeler atıldı.
* **💡 Özel Dokunuş:** NLTK kütüphanesinin standart listesindeki **"değil"** ve **"yok"** kelimeleri, cümlenin anlamını tersine çevirdiği için (örn: *iyi değilim*) koruma altına alındı ve silinmedi.

### 2. Özellik Çıkarımı (Feature Extraction)
Metinleri bilgisayarın anlayacağı sayılara çevirmek için **TF-IDF (Term Frequency - Inverse Document Frequency)** yöntemi kullanıldı.
* **N-Grams Tekniği:** Modelin sadece kelimelere tek tek bakması yerine, kelime gruplarına da bakması sağlandı (`ngram_range=(1,2)`).
* *Örnek:* Model artık sadece "iyi" kelimesini değil, **"iyi değil"** kalıbını da bir bütün olarak görüp Negatif olarak algılayabiliyor.

### 3. Modelleme (Machine Learning)
* **Algoritma:** Lojistik Regresyon (Logistic Regression) kullanıldı.
* **Eğitim:** Veri seti %80 Eğitim ve %20 Test olarak ayrıldı.
* **Dengesiz Veri Çözümü:** Negatif ve Nötr verilerin azınlıkta kalmaması için `class_weight='balanced'` parametresi ve Stratified Split kullanıldı.

### 4. Web Arayüzü (Deployment)
* Model, son kullanıcının rahatça test edebilmesi için **Streamlit** kütüphanesi ile modern bir web arayüzüne dönüştürüldü.
* Arka plan ve yazı renkleri CSS ile özelleştirilerek "Dark Mode" görünümü kazandırıldı.

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için şu adımları izleyin:

1. **Repoyu klonlayın:**
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/twitter-duygu-analizi.git](https://github.com/KULLANICI_ADIN/twitter-duygu-analizi.git)
   cd twitter-duygu-analizi
