# GitHub'a Yükleme Rehberi

Bu rehber, projenizi GitHub'a yüklemek için gereken tüm adımları içerir.

## Ön Hazırlık

### 1. Git Kurulumu Kontrolü

```bash
git --version
```

Eğer Git yüklü değilse, [git-scm.com](https://git-scm.com/) adresinden indirin.

### 2. Git Yapılandırması

```bash
git config --global user.name "Adınız Soyadınız"
git config --global user.email "email@example.com"
```

## GitHub'da Repository Oluşturma

1. [GitHub](https://github.com) hesabınıza giriş yapın
2. Sağ üst köşeden **"+"** > **"New repository"** seçin
3. Repository bilgilerini girin:
   - **Repository name:** `bigisayar_goru_odev3`
   - **Description:** "Temel görüntü işleme algoritmalarının Python implementasyonu"
   - **Public** veya **Private** seçin
   - **README**, **.gitignore**, ve **license** eklemeyin (zaten var)
4. **"Create repository"** butonuna tıklayın

## Projeyi GitHub'a Yükleme

### Yöntem 1: Komut Satırından (Önerilen)

Proje klasörüne gidin:

```bash
cd "c:\Users\USER\Desktop\projeler1\gite yüklenecekler\bigisayar_görü_ödev3"
```

Git repository'sini başlatın:

```bash
git init
```

Tüm dosyaları staging area'ya ekleyin:

```bash
git add .
```

İlk commit'i oluşturun:

```bash
git commit -m "İlk commit: Görüntü işleme kütüphanesi v1.0.0"
```

Ana branch'i main olarak ayarlayın:

```bash
git branch -M main
```

GitHub repository'nizi remote olarak ekleyin (KULLANICI_ADI yerine kendi kullanıcı adınızı yazın):

```bash
git remote add origin https://github.com/KULLANICI_ADI/bigisayar_goru_odev3.git
```

Kodu GitHub'a push edin:

```bash
git push -u origin main
```

### Yöntem 2: GitHub Desktop ile

1. [GitHub Desktop](https://desktop.github.com/) indirin ve kurun
2. Uygulamayı açın ve GitHub hesabınızla giriş yapın
3. **File** > **Add Local Repository** seçin
4. Proje klasörünü seçin
5. **Publish repository** butonuna tıklayın
6. Repository adını ve açıklamasını girin
7. **Publish Repository** butonuna tıklayın

## Doğrulama

GitHub'daki repository sayfanızı ziyaret edin:
```
https://github.com/KULLANICI_ADI/bigisayar_goru_odev3
```

Tüm dosyaların yüklendiğini kontrol edin.

## Sonraki Adımlar

### README'yi Özelleştirme

README.md dosyasındaki şu bölümleri güncelleyin:

1. **İletişim Bilgileri:**
   ```markdown
   - 📧 Email: [gerçek_email@example.com]
   - 🐙 GitHub: [@gerçek_kullanici_adi](https://github.com/gerçek_kullanici_adi)
   ```

2. **Proje Linki:**
   ```markdown
   **Proje Linki:** [https://github.com/gerçek_kullanici_adi/bigisayar_goru_odev3]
   ```

3. **Lisans Sahibi:**
   LICENSE dosyasındaki copyright bilgisini güncelleyin.

Değişiklikleri commit edin:

```bash
git add README.md LICENSE
git commit -m "İletişim bilgileri güncellendi"
git push
```

### Repository Ayarları

GitHub repository sayfasında:

1. **Settings** > **General**:
   - Description ekleyin
   - Website ekleyin (varsa)
   - Topics ekleyin: `computer-vision`, `image-processing`, `python`, `numpy`, `opencv`

2. **Settings** > **Pages** (GitHub Pages için):
   - Source: `main` branch seçin
   - Dokümantasyonu web'de yayınlayın

### Badges Ekleme

README.md'ye daha fazla badge ekleyebilirsiniz:

```markdown
[![GitHub stars](https://img.shields.io/github/stars/KULLANICI_ADI/bigisayar_goru_odev3)](https://github.com/KULLANICI_ADI/bigisayar_goru_odev3/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/KULLANICI_ADI/bigisayar_goru_odev3)](https://github.com/KULLANICI_ADI/bigisayar_goru_odev3/network)
[![GitHub issues](https://img.shields.io/github/issues/KULLANICI_ADI/bigisayar_goru_odev3)](https://github.com/KULLANICI_ADI/bigisayar_goru_odev3/issues)
```

## Gelecekteki Güncellemeler

Değişiklik yaptığınızda:

```bash
# Değişiklikleri görüntüle
git status

# Değişiklikleri ekle
git add .

# Commit oluştur
git commit -m "Açıklayıcı commit mesajı"

# GitHub'a push et
git push
```

## Sorun Giderme

### "Permission denied" Hatası

SSH key oluşturun:

```bash
ssh-keygen -t ed25519 -C "email@example.com"
```

Public key'i GitHub'a ekleyin:
- Settings > SSH and GPG keys > New SSH key

### "Remote already exists" Hatası

```bash
git remote remove origin
git remote add origin https://github.com/KULLANICI_ADI/bigisayar_goru_odev3.git
```

### Büyük Dosya Uyarısı

100MB'den büyük dosyalar için Git LFS kullanın:

```bash
git lfs install
git lfs track "*.zip"
git add .gitattributes
git commit -m "Git LFS eklendi"
```

## İyi Pratikler

1. **Anlamlı Commit Mesajları:**
   ```bash
   git commit -m "feat: Yeni özellik eklendi"
   git commit -m "fix: Hata düzeltildi"
   git commit -m "docs: Dokümantasyon güncellendi"
   ```

2. **Düzenli Push:**
   - Her önemli değişiklikten sonra push edin
   - Günlük çalışmanızın sonunda push edin

3. **Branch Kullanımı:**
   ```bash
   # Yeni özellik için branch oluştur
   git checkout -b feature/yeni-ozellik
   
   # Değişiklikleri commit et
   git commit -m "Yeni özellik eklendi"
   
   # Main branch'e merge et
   git checkout main
   git merge feature/yeni-ozellik
   git push
   ```

## Yardım ve Kaynaklar

- [Git Dokümantasyonu](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub Desktop Dokümantasyonu](https://docs.github.com/en/desktop)

---

**Başarılar! 🚀**

Projeniz artık GitHub'da ve dünya ile paylaşılmaya hazır!
