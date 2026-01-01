def remove_null_bytes(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    # Null byte'ları temizle
    cleaned_content = content.replace(b'\0', b'')  # b'\0' ile null byte karakterini hedefliyoruz

    # Temizlenen içeriği tekrar dosyaya yaz
    with open(file_path, 'wb') as file:
        file.write(cleaned_content)

# Temizleme işlemini her dosya için yapalım
files_to_clean = [
    'main.py', 
    'code/brightness_adjustment.py', 
    'code/contrast_adjustment.py', 
    'code/negative_image.py', 
    'code/thresholding.py', 
    'code/histogram_analysis.py', 
    'code/image_statistics.py', 
    'code/contrast_stretching.py', 
    'code/histogram_equalization.py', 
    'code/gamma_correction.py'
]

for file in files_to_clean:
    remove_null_bytes(file)
    print(f"Null byte temizlendi: {file}")
