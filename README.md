# Text Reader

## Gereklilikler

### Anaconda

```cmd
conda install -c mcs07 tesseract
conda install -c jim-hart pytesseract
```

### Türkçe dili ekleme

* Türkçe dil paketini [buraya](https://github.com/tesseract-ocr/tessdata/raw/3.04.00/tur.traineddata) tıklayarak indirin.
* `image_to_string(img, lang="tur")` yazdığınızda hatanın geldiği yola kopyalayın.