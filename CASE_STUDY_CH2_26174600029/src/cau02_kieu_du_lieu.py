# 5 & 6 Tạo các biến theo quy tắc snake_case và đúng kiểu dữ liệu
ma_phien = "LAB026"
ma_may = "PC12"
cong_suat = 250.0
thoi_gian = 90
trang_thai = True
ghi_chu = None

# 7. In từng giá trị và dùng type() để kiểm tra kiểu dữ liệu
print("---Kiểm tra dữ liệu  ---")
print("Mã phiên:", ma_phien, "| Kiểu:", type(ma_phien))
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))
print("Công suất:", cong_suat, "| Kiểu:", type(cong_suat))
print("Thời gian:", thoi_gian, "| Kiểu:", type(thoi_gian))
print("Trạng thái:", trang_thai, "| Kiểu:", type(trang_thai))
print("Ghi chú:", ghi_chu, "| Kiểu:", type(ghi_chu))
print("\n----")

# 8Thay thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian = 120
print("Thời gian sử dụng mới:", thoi_gian)