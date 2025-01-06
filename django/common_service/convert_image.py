from PIL import Image
from pathlib import Path

def resize_image(input_path, output_folder, new_size=(120, 100)):
    try:
        # Đảm bảo thư mục lưu ảnh kết quả tồn tại
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        # Kiểm tra xem tệp đầu vào có tồn tại không
        input_file = Path(input_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Tệp không tồn tại: {input_file}")

        # Mở ảnh từ đường dẫn đầu vào
        with Image.open(input_file) as img:
            # Thay đổi kích thước ảnh
            resized_img = img.resize(new_size)

            # Tạo đường dẫn tệp ảnh kết quả
            output_file = output_folder / f"output_{input_file.name}"
            resized_img.save(output_file)

            print(f"Ảnh đã được lưu tại: {output_file.resolve()}")
            return output_file

    except Exception as e:
        print(f"Lỗi: {e}")
        return None

input_path = r"D:\Tải Xuống\MainAfter.jpg"
output_folder = r'D:\jvb\JVB-python\start\project\media\workshop_image'  # Đường dẫn thư mục lưu ảnh sau khi xử lý

resize_image(input_path, output_folder, new_size=(120, 100))

