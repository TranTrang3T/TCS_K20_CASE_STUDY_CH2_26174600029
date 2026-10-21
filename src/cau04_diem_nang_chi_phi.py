# Cho trước
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
# 13Tính điện năng tiêu thụ và chi phí điện
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("--- KẾT QUẢ KHI so_phut = 90 ---")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh")
print(f"Chi phí điện: {chi_phi} VNĐ")
# 14 In cả giá trị và kiểu dữ liệu của hai kết quả
print(f"Kiểu của dien_nang_kwh: {type(dien_nang_kwh)}")
print(f"Kiểu của chi_phi: {type(chi_phi)}")
# 15 Dự đoán kết quả trước khi chạy:
# dien_nang_kwh = 250 * 90 / 60 / 1000 = 0.375 kWh
# chi_phi = 0.375 * 3000 = 1125.0 VNĐ
# 16Thay so_phut bằng 60 rồi chạy lại và so sánh
print(" Kêt quả so_phut = 60")
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Điện năng tiêu thụ mới: {dien_nang_kwh} kWh")
print(f"Chi phí điện mới: {chi_phi} VNĐ")
print("So sánh: Khi thời gian giảm từ 90 phút xuống 60 phút, điện năng tiêu thụ và chi phí giảm tương ứng theo tỉ lệ thời gian.")