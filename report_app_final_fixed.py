import streamlit as st

st.set_page_config(page_title="نموذج التقرير", layout="centered")

# عرض عنوان للتأكيد أن التطبيق يعمل
st.title("📋 نموذج التقرير الميداني")

# بيانات دخول بسيطة للتجربة
المستخدمون = {
    "admin": "1234",
    "test": "test"
}

if "auth" not in st.session_state:
    with st.form("login"):
        st.subheader("🔐 تسجيل الدخول")
        username = st.text_input("اسم المستخدم")
        password = st.text_input("كلمة المرور", type="password")
        submit = st.form_submit_button("دخول")
        if submit:
            if username in المستخدمون and المستخدمون[username] == password:
                st.session_state.auth = username
                st.success(f"تم تسجيل الدخول كـ {username}")
                st.rerun()
            else:
                st.error("❌ بيانات الدخول غير صحيحة")
    st.stop()

st.success(f"مرحبًا بك، {st.session_state.auth} 👋")
st.write("هذا هو النموذج التجريبي لتأكيد عمل التطبيق.")