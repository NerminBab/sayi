import streamlit as st
import random

st.title("🎯 Sayı Tahmin Oyunu")
st.write("1 ile 10 arasında bir sayı tuttum. Bakalım bulabilecek misin?")

# Oturum durumu (session state) kullanarak sayıyı ve hakkı saklıyoruz
if "dogru_sayi" not in st.session_state:
    st.session_state.dogru_sayi = random.randint(1, 10)
    st.session_state.hak = 3
    st.session_state.mesaj = ""

# Kullanıcıdan tahmin al
tahmin = st.number_input("Tahminini gir:", min_value=1, max_value=10, step=1)

# Tahmini gönder butonu
if st.button("Tahmin Et"):
    if st.session_state.hak > 0:
        if tahmin == st.session_state.dogru_sayi:
            st.session_state.mesaj = "🎉 Tebrikler! Doğru bildin!"
        elif tahmin > st.session_state.dogru_sayi:
            st.session_state.hak -= 1
            st.session_state.mesaj = f"⬇️ Daha küçük bir sayı dene. Kalan hakkın: {st.session_state.hak}"
        else:
            st.session_state.hak -= 1
            st.session_state.mesaj = f"⬆️ Daha büyük bir sayı dene. Kalan hakkın: {st.session_state.hak}"
    if st.session_state.hak == 0 and tahmin != st.session_state.dogru_sayi:
        st.session_state.mesaj = f"😢 Hakkın bitti! Doğru sayı {st.session_state.dogru_sayi} idi."

st.write(st.session_state.mesaj)

# Yeniden başlat butonu
if st.button("🔄 Oyunu Yeniden Başlat"):
    st.balloons()
    st.session_state.dogru_sayi = random.randint(1, 10)
    st.session_state.hak = 3
    st.session_state.mesaj = ""
    st.rerun()
