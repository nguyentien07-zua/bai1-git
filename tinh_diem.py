def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    return (diem_toan + diem_ly + diem_hoa) / 3

def xep_loai(diem_tb):
    if diem_tb >= 8:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

def main():
    print("=== CHƯƠNG TRÌNH TÍNH ĐIỂM TRUNG BÌNH ===")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))

    for diem in [diem_toan, diem_ly, diem_hoa]:
        if diem < 0 or diem > 10:
            print("Điểm không hợp lệ! Vui lòng nhập từ 0 đến 10.")
            return

    diem_tb = tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa)
    ket_qua = xep_loai(diem_tb)

    print(f"\nĐiểm trung bình: {diem_tb:.2f}")
    print(f"Xếp loại: {ket_qua}")

if __name__ == "__main__":
    main()