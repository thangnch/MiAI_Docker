# Dựa trên image cơ bản nào
FROM python:3

# Khai báo thư mục làm việc
WORKDIR /Volumes/Data/00.Source/Python/MiAI_Docker_Sample

# Copy toàn bộ file mã nguồn và các file khác vào image
COPY . .

# Cài đặt Flask
RUN pip install -r setup.txt

# Thực hiện lệnh chạy
CMD ["python","./example03.py"]