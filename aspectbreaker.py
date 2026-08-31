import os
import sys
from PIL import Image

def resize_image(image_path, ratio, output_path=None):
    """Растягивает картинку до указанного соотношения"""
    if not os.path.exists(image_path):
        print(f"Файл не найден: {image_path}")
        return False
    
    img = Image.open(image_path)
    orig_w, orig_h = img.size
    
    if ratio == "1:1":
        size = max(orig_w, orig_h)
        target_size = (size, size)
    elif ratio == "4:3":
        width = max(orig_w, int(orig_h * 4 / 3))
        height = int(width * 3 / 4)
        target_size = (width, height)
    else:
        print(f"❌ Неизвестное соотношение: {ratio}")
        return False
    
    resized = img.resize(target_size, Image.Resampling.LANCZOS)
    
    if output_path is None:
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_{ratio.replace(':', 'x')}{ext}"
    
    resized.save(output_path, quality=95)
    print(f"{os.path.basename(image_path)} -> {os.path.basename(output_path)} [{target_size[0]}x{target_size[1]}]")
    return True

def main():
    if len(sys.argv) < 3:
        print("Принудительное растягивание картинок")
        print("\nИспользование:")
        print(f"  python {sys.argv[0]} --ratio 4:3 image1.jpg image2.png")
        print(f"  python {sys.argv[0]} --ratio 1:1 avatar.jpg")
        print("\nДоступные соотношения: 1:1, 4:3")
        return
    
    if sys.argv[1] == "--ratio":
        ratio = sys.argv[2]
        files = sys.argv[3:]
    else:
        ratio = "4:3"
        files = sys.argv[1:]
    
    if ratio not in ["1:1", "4:3"]:
        print(f"Неверное соотношение: {ratio}. Доступно: 1:1, 4:3")
        return
    
    if not files:
        print("Нет файлов для обработки")
        return
    
    print(f"Соотношение: {ratio}")
    print(f"Файлов: {len(files)}\n")
    
    for file_path in files:
        resize_image(file_path, ratio)

if __name__ == "__main__":
    main()
