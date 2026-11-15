import streamlit as st
from generator import generate_ad

st.set_page_config(page_title="AI Marketing & Ad Campaign Generator", page_icon="📢")

# دعم العرض من اليمين لليسار للعربي
st.markdown(
    """
    <style>
    .stApp { direction: rtl; text-align: right; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📢 مولّد الحملات الإعلانية بالذكاء الاصطناعي")

product = st.text_input("اسم المنتج", placeholder="مثال: عطر ليالي بغداد")
description = st.text_area("وصف المنتج", placeholder="مثال: عطر شرقي فاخر برائحة العود والورد")
audience = st.text_input("الجمهور المستهدف", placeholder="مثال: نساء ورجال من 25 إلى 45 سنة")
platform = st.selectbox("المنصة", ["انستغرام", "فيسبوك", "تيك توك", "تويتر (X)", "لينكدإن"])
tone = st.selectbox("نبرة الإعلان", ["فخم وأنيق", "مرح وخفيف", "رسمي", "عاطفي", "حماسي"])

if st.button("ولّد الإعلان"):
    if not product or not description or not audience:
        st.warning("عبّي كل الحقول أولاً")
    else:
        with st.spinner("جاري توليد الإعلان..."):
            try:
                result = generate_ad(product, description, audience, platform, tone)
                st.markdown(result)
            except Exception as e:
                st.error(f"صار خطأ: {e}")