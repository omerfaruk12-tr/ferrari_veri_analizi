import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Veriler işleniyor, motor ısınıyor... 🏎️")

# 1. VERİYİ İÇERİ AL
dosya_yolu = "/Users/omerfarukbolat/Downloads/Sport car price.csv"
df = pd.read_csv(dosya_yolu)

# 2. VERİ TEMİZLİĞİ (İstatistikçi Dokunuşu)
# Fiyatlarda "101,200" gibi virgüller var, Python bunu metin sanar. Biz onu saf sayıya (float) çeviriyoruz.
df['Price (in USD)'] = df['Price (in USD)'].astype(str).str.replace(',', '', regex=False).astype(float)
df['Horsepower'] = pd.to_numeric(df['Horsepower'], errors='coerce')

# 3. FERRARI FİLTRESİ
ferrari_df = df[df['Car Make'] == 'Ferrari'].copy()

# 4. GÖRSEL ŞOV (LinkedIn'i Sallayacak Kısım)
plt.style.use('dark_background') # Veri bilimcilerin en sevdiği o havalı koyu tema
plt.figure(figsize=(12, 7))

# Saçılım grafiği: Beygir gücü fiyatı nasıl etkiliyor?
sns.scatterplot(
    data=ferrari_df, 
    x='Horsepower', 
    y='Price (in USD)', 
    hue='Car Model', # Noktalar modellere göre farklı renk olsun
    s=200, # Noktaların büyüklüğü
    palette='magma' # Ateşli renk paleti
)

# Grafiği süsleyelim
plt.title('Ferrari: Beygir Gücü ve Fiyat İlişkisi', fontsize=18, color='gold', fontweight='bold')
plt.xlabel('Beygir Gücü (HP)', fontsize=14)
plt.ylabel('Fiyat (USD)', fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Model isimlerini sağa al
plt.grid(True, alpha=0.2)
plt.tight_layout()

# Grafiği hem Mac'ine kaydet hem de ekranda göster
kayit_yolu = "/Users/omerfarukbolat/Downloads/ferrari_analiz_grafik.png"
plt.savefig(kayit_yolu, dpi=300)
print(f"BAM! Grafik çizildi ve şuraya kaydedildi: {kayit_yolu}")

plt.show()