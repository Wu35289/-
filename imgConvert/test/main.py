#!/usr/bin/env python3
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image

# 載入模型（新海誠動漫風）
model = torch.hub.load('bryandlee/animegan2-pytorch', 'generator', pretrained='face2paint')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device).eval()

# 圖片轉換
transform = transforms.Compose([
    transforms.Resize((512, 512)),
    transforms.ToTensor(),
])

# 載入你的圖片
image_path = "../imgElement/dog.jpg"  # <-- 換成你的圖片路徑
input_image = Image.open(image_path).convert("RGB")
input_tensor = transform(input_image).unsqueeze(0).to(device)

# 預測
with torch.no_grad():
    output_tensor = model(input_tensor)

# 存檔
output_image = output_tensor.squeeze().cpu()
save_image(output_image, 'output_anime_shinkai.jpg')

# 顯示圖片
plt.subplot(1, 2, 1)
plt.imshow(input_image)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(np.transpose(output_image.numpy(), (1, 2, 0)))
plt.title("大便")
plt.axis('off')

plt.show()
