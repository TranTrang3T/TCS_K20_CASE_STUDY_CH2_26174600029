# Cho trước
tong_phut = 135
cong_suat_w = 250

# 9Dùng // và % để tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"9. Tổng {tong_phut} phút = {so_gio} giờ {so_phut_du} phút")
# 10Tạo biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print(f"10. Sử dụng lâu hơn 60 phút (su_dung_lau): {su_dung_lau}")
# 11Tạo biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print(f"11. Dữ liệu hợp lệ (du_lieu_hop_le): {du_lieu_hop_le}")
# 12Dự đoán và kiểm chứng hai biểu thức ưu tiên toán tử: 100 + 20 * 3 và (100 + 20) * 3
kq_1 = 100 + 20 * 3       
 # Phép nhân thực hiện trước: 100 + 60 = 160
kq_2 = (100 + 20) * 3    
 # Phép trong ngoặc thực hiện trước: 120 * 3 = 360
print("12. Dự đoán & kiểm chứng biểu thức:")
print(f"   - 100 + 20 * 3 = {kq_1}")
print(f"   - (100 + 20) * 3 = {kq_2}")