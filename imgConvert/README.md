# Imgconvert
This project converts images (JPG, PNG, BMP) into a personal style.
## Effect Examples

## Function
- Support `JPG`, `PNG`, `BMP` and other common image formats.
- You can replace the images in the `imgElement` folder to process them.
## Build env
**Operating System**: `Windows 11 (x86_64)` or `Linux (x86_64)`

**Python**: 3.13.5

**GPU**: NVIDIA GPU (e.g. GTX3050) is recommended for faster processing

## Installation Instructions

1. **clone project**

        git clone project <YOUR_REPOt/6SITORY_URL>

        cd imgConvert

2. **Install dependency packages**

        pip install -r requirement.txt

## How to use

1.  將您想轉換的圖片放入 `imgElement` 資料夾。

2.  修改 `example/main.py` 檔案中的第 25 行，將 `image_path` 的值改為您的圖片路徑：

  line 25
      image_path = "../imgElement/your-image-name.jpg"

3.  執行主程式：

      python example/main.py


4.  轉換後的圖片將會儲存在 `example` 資料夾下，檔名為 `output_anime_shinkai.jpg`，同時會彈出視窗顯示對比結果。
   
## Thanks For
This project  uses a pre-trained model provided by [bryandlee/animegan2-pytorch](https://github.com/bryandlee/animegan2-pytorch) .
