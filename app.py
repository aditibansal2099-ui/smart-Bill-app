import streamlit as st
import pandas as pd

# ----------------------------
# APP SETTINGS
# ----------------------------
st.set_page_config(page_title="Smart Bill", page_icon="💖", layout="centered")
PASSWORD = "1234"  # change to your secret password

# ----------------------------
# CUSTOM STYLING
# ----------------------------
page_bg = """
<style>
body {
    background: linear-gradient(135deg, #ffc0cb 0%, #dda0dd 100%);
    color: #4b004b;
    font-family: 'Poppins', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    color: #800080;
}
.stButton>button {
    background-color: #ff69b4;
    color: white;
    border-radius: 12px;
    padding: 8px 20px;
    font-weight: bold;
    border: none;
}
.stButton>button:hover {
    background-color: #d63384;
    color: #fff;
}
div[data-testid="stMarkdownContainer"] {
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------------------
# HEADER & LOGO
# ----------------------------
st.markdown("<h1>💖 SMART BILL 💖</h1>", unsafe_allow_html=True)
st.image("smartbill_logo.jpg", use_column_width=True)

# ----------------------------
# PASSWORD PROTECTION
# ----------------------------
password = calculate("🔒 Enter Password to Access", type="password")
if password != PASSWORD:
    st.warning("Please enter the correct password to continue.")
    st.stop()

# ----------------------------
# MAIN BILLING AREA
# ----------------------------
st.markdown("<h3>Enter Item Details</h3>", unsafe_allow_html=True)
item_count = st.number_input("🧾 How many items do you want to add?", min_value=1, max_value=50, value=1, step=1)

data = []
for i in range(int(item_count)):
    st.subheader(f"✨ Item {i+1}")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(f"Item Name {i+1}")
        qty = st.number_input(f"Quantity {i+1}", min_value=1.0, step=1.0)
    with col2:
        price = st.number_input(f"Price per item {i+1}", min_value=0.0, step=0.5)
        gst = st.number_input(f"GST (%) for Item {i+1}", min_value=0.0, step=0.5)

    discount = st.slider(f"Discount (%) for Item {i+1}", 0, 100, 0)

    # calculations
    rate = qty * price
    gst_amt = gst / 100 * rate
    total = rate + gst_amt
    dis = total * discount / 100
    final_amt = total - dis

    data.append([name, qty, price, gst, discount, round(final_amt, 2)])

# ----------------------------
# DISPLAY BILL SUMMARY
# ----------------------------
if st.button("💫 Generate Bill"):
    df = pd.DataFrame(data, columns=["Item Name", "Quantity", "Price", "GST (%)", "Discount (%)", "Final Amount (₹)"])
    total_amount = df["Final Amount (₹)"].sum()

    st.markdown("<h3 style='color:#4B0082;'>🧾 BILL SUMMARY</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown(f"<h2 style='color:#ff1493;'>💰 Grand Total: ₹ {total_amount:.2f}</h2>", unsafe_allow_html=True)
    st.success("🎉 Bill Generated Successfully!")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2025 Smart Bill | Made with 💕 using Python & Streamlit")
