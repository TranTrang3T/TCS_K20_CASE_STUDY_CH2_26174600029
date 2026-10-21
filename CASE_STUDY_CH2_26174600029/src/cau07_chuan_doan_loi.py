ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Ép kiểu dữ liệu sang float
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
#Các lỗi đã phát hiện 
# 1 Lỗi TypeError: Biến cong_suat_w nhận giá trị str từ hàm input() nên không thể nhân với số phút.
# 2Khắc phục: Sử dụng float() hoặc int() để chuyển đổi giá trị nhập vào của cong_suat_w thành số trước khi tính toán.