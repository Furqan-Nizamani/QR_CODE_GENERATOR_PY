import streamlit as st
import qrcode
from PIL import Image
import io

# /// app title ///
st.title("QR Code GENERATOR")

# /// USER INPUT ///
data = st.text_input("ENTER YOUR URL TO GENERATE THE QR CODE:")

# /// BUTTON TO GENERATE QR CODE ///
if st.button("GENERATE QR CODE"):
    if data.strip() == "":
        st.warning("NO TEXT URL ENTERED")
    else:
        # /// generate qr code ///
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4  
        )
        qr.add_data(data)
        qr.make(fit=True)

        # /// create an image of the qr code
        img = qr.make_image(fill_color="black", back_color="white")

        # /// Convert PIL image to BytesIO object
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)

        # /// DISPLAY QR CODE ///
        st.image(img_byte_array, caption="YOUR QR CODE", use_container_width=True)

        # /// Save the image to a file
        img.save("qr_code.png")

        # /// Download the image
        with open("qr_code.png", "rb") as file:
            st.download_button(
                label="Download QR Code",
                data=file,
                file_name="qr_code.png",
                mime="image/png"
            )
