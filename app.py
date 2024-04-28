import streamlit as st
from newspaper import Article
from summary import abstract
import requests
from checkURL import checkURL


def main():
    st.title("Tóm tắt bài báo")
    # Input the url of text
    url = st.text_input("Nhập đường dẫn/URL bài báo của bạn")

    # Guidelines
    st.subheader("Lưu ý khi sử dụng:")
    st.write("1. Copy đường dẫn/ link bài báo bỏ vào sẽ chạy")
    st.write("2. Web hiện chỉ chạy được những link bài báo như vnexpress, Tuổi trẻ, thanh niên,...")
    st.write("""3. Web được xây dựng cho vui, nên link nếu k dùng được thì thôi, 
             Đừng có feedback chi, tại hông có sửa web đâu, vậy ha =))))
             """)
    st.write('4. Có 1 số trường hợp bấm 1 sẽ báo lỗi link, thì bấm lần 2, lỗi nữa thì đổi link nhé :)))')


    if st.button("Tóm tắt"):
        # if checkURL(url) == False:
        #     st.error("Link này tui vô hông được, thử cái khác xem :V", icon="🚨")
        try:
            with st.spinner("Đợi tí, đang đọc nè :V"):
                summary = abstract(url)
                st.success("Đọc xong rồi nè =)))")
                st.markdown("Okey, đây")
                st.text_area("Tóm tắt lại:", value=summary, height=500)
        except:
            st.error("Link này tui vô hông được, thử cái khác xem :V", icon="🚨")


if __name__ == "__main__":
    main()
