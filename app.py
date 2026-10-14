import streamlit as st

# Cấu hình giao diện ứng dụng
st.set_page_config(page_title="Tính Chỉ Số DTI", page_icon="🏦", layout="centered")

st.title("🏦 Tính Chỉ Số DTI & Thẩm Định Vay")
st.write("Nhập thông tin bên dưới để tính chỉ số DTI (Debt-to-Income):")

# Các ô nhập dữ liệu đầu vào
STV = st.number_input("Số tiền vay (VNĐ)", min_value=0, value=800_000_000, step=10_000_000)
THV = st.number_input("Thời hạn vay (năm)", min_value=1, value=5, step=1)
LS_percent = st.number_input("Lãi suất vay (%/năm)", min_value=0.0, value=12.0, step=0.1)
TN = st.number_input("Thu nhập hàng tháng (VNĐ)", min_value=0, value=45_000_000, step=1_000_000)
NC = st.number_input("Nợ cũ hàng tháng (VNĐ)", min_value=0, value=10_000_000, step=1_000_000)
CPSH = st.number_input("Chi phí sinh hoạt / 1 người (VNĐ)", min_value=0, value=4_000_000, step=500_000)
SN = st.number_input("Số người trong gia đình", min_value=1, value=3, step=1)

# Đổi lãi suất phần trăm sang dạng thập phân
LS = LS_percent / 100

# Nút tính toán
if st.button("Tính DTI", type="primary"):
    thu_nhap_rong = TN - (CPSH * SN)
    
    if thu_nhap_rong <= 0:
        st.error("Thu nhập ròng (Thu nhập - Chi phí sinh hoạt) phải lớn hơn 0!")
    else:
        # Công thức tính DTI theo đúng đoạn code mẫu của bạn
        goc_lai_thang = (STV / (THV * 12)) + (STV * (LS / 12))
        DTI = (goc_lai_thang + NC) / thu_nhap_rong
        DTI_percent = DTI * 100

        st.subheader("Kết quả:")
        st.write(f"- **Chỉ số DTI:** `{DTI_percent:.2f}%`")

        # Đánh giá điều kiện vay: DTI < 70% (0.7) là ĐƯỢC VAY theo đúng code gốc
        if DTI < 0.7:
            st.success("✅ **KẾT LUẬN: ĐƯỢC VAY** (DTI < 70%, nằm trong ngưỡng an toàn)")
        else:
            st.error("❌ **KẾT LUẬN: KHÔNG ĐƯỢC VAY** (DTI ≥ 70%, vượt quá ngưỡng an toàn)")
