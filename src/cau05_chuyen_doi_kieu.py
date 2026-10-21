# 17 Dùng input() để nhận bốn giá trị và in type() ngay sau khi nhập
ma_may = input("Nhập mã máy: ")
cong_suat_str = input("Nhập công suất W: ")
so_phut_str = input("Nhập số phút sử dụng: ")
don_gia_str = input("Nhập đơn giá điện/kWh: ")
print("\n--- Kieu du lieu input() ---")
print(f"Mã máy: {ma_may} - Kiểu: {type(ma_may)}")
print(f"Công suất: {cong_suat_str} - Kiểu: {type(cong_suat_str)}")
print(f"Số phút: {so_phut_str} - Kiểu: {type(so_phut_str)}")
print(f"Đơn giá: {don_gia_str} - Kiểu: {type(don_gia_str)}")
# 18Chuyển công suất sang float, số phút sang int và đơn giá sang float
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)
# 19Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("\n--- KẾT QUẢ SAU KHI CHUYỂN ĐỔI KIỂU ---")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh")
print(f"Chi phí điện: {chi_phi} VNĐ")