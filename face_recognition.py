import streamlit as st
import json
import os
import subprocess

# JSON file to store face data
JSON_FILE = "input.json"
UPLOAD_DIR = "uploads"

# Ensure the JSON file exists
if not os.path.exists(JSON_FILE):
    with open(JSON_FILE, "w") as f:
        json.dump({"faces": [{}]}, f, indent=4)

# Ensure the 'uploads' directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Load existing data from JSON
with open(JSON_FILE, "r") as f:
    data = json.load(f)

face_db = data["faces"]  # Reference to face data

def save_to_json():
    """Save face_db list to JSON file."""
    with open(JSON_FILE, "w") as f:
        json.dump({"faces": face_db}, f, indent=4)

def call_addface():
    """Call the addface_.py script whenever JSON is updated."""
    subprocess.run(["python", "addface_.py"], check=True)

def app():
    st.title("Face Recognition System")

    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add Face", "📋 List Faces", "🔍 Recognize Face", "🗑️ Delete Face"])

    # 🔹 Add Face Tab
    with tab1:
        st.header("Add a New Face")

        # Input fields
        name = st.text_input("Enter Name", key="add_name")
        email = st.text_input("Enter Email ID", key="add_email")
        image = st.file_uploader("Upload Face Image", type=["jpg", "jpeg", "png"], key="add_image")

        if st.button("Save Face", key="save_face"):
            if name and email and image:
                image_url = os.path.join(UPLOAD_DIR, f"{name}_{email}.png")  # Define image storage path
                with open(image_url, "wb") as img_file:
                    img_file.write(image.getbuffer())  # Save the uploaded image

                # Always replace the single stored entry
                face_db.clear()
                face_db.append({"name": name, "mail_id": email, "image_url": image_url})
                
                save_to_json()  # Update JSON file
                call_addface()  # Call addface_.py after updating JSON

                st.success(f"✅ Face for {name} has been added/updated successfully!")
                st.write(f"📧 Email: {email}")
                st.write(f"🖼️ Image saved at: {image_url}")
            else:
                st.error("⚠️ Please fill all details and upload an image.")

    # 🔹 List Faces Tab
    with tab2:
        st.header("List Faces")
        
        if st.button("Show Faces", key="show_faces"):
            if face_db:
                for person in face_db:
                    st.write(f"🧑 Name: {person['name']}")
                    st.write(f"📧 Email: {person['mail_id']}")
                    st.write(f"🖼️ Image Path: {person['image_url']}")
                    st.write("---")
            else:
                st.warning("⚠️ No records found!")

if __name__ == "__main__":
    app()
    
    # # 🔹 List Faces Tab
    # with tab2:
    #     st.header("List Faces")

    #     list_name = st.text_input("Enter Name to List", key="list_name")
    #     list_email = st.text_input("Enter Email ID", key="list_email")

    #     if st.button("Show Faces", key="show_faces"):
    #         filtered_faces = [person for person in face_db if person["name"] == list_name and person["email"] == list_email]

    #         if filtered_faces:
    #             st.success(f"✅ Found {len(filtered_faces)} record(s) for {list_name}")
    #             for person in filtered_faces:
    #                 st.write(f"🧑 Name: {person['name']}")
    #                 st.write(f"📧 Email: {person['email']}")
    #                 st.write("---")
    #         else:
    #             st.warning("⚠️ No matching records found!")

    # # 🔹 Recognize Face Tab
    # with tab3:
    #     st.header("Recognize a Face")

    #     recog_name = st.text_input("Enter Name", key="recognize_name")
    #     recog_email = st.text_input("Enter Email ID", key="recognize_email")
    #     image = st.file_uploader("Upload an Image for Recognition", type=["jpg", "jpeg", "png"], key="recognize_image")

    #     if st.button("Recognize Face", key="recognize_face"):
    #         if recog_name and recog_email and image:
    #             matched_faces = [person for person in face_db if person["name"] == recog_name and person["email"] == recog_email]

    #             if matched_faces:
    #                 person = matched_faces[0]  # Simulated recognition logic
    #                 st.success(f"✅ Face recognized: {person['name']}")
    #                 st.write(f"📧 Email: {person['email']}")
    #             else:
    #                 st.warning("⚠️ No matching record found.")
    #         else:
    #             st.error("⚠️ Please enter Name, Email ID, and upload an image.")

    # # 🔹 Delete Face Tab
    # with tab4:
    #     st.header("Delete a Face Record")
    #     name_to_delete = st.text_input("Enter Name", key="delete_name")
    #     email_to_delete = st.text_input("Enter Email ID", key="delete_email")
    #     phone_to_delete = st.text_input("Enter Phone Number", key="delete_phone")

    #     if st.button("Delete Face", key="delete_face"):
    #         if name_to_delete and email_to_delete and phone_to_delete:
    #             new_db = [person for person in face_db if not (person["name"] == name_to_delete and person["email"] == email_to_delete and person["phone"] == phone_to_delete)]
                
    #             if len(new_db) < len(face_db):  # Check if deletion happened
    #                 face_db[:] = new_db
    #                 st.warning(f"⚠️ Face record for {name_to_delete} has been deleted!")
    #             else:
    #                 st.warning("⚠️ No matching record found to delete!")
    #         else:
    #             st.error("⚠️ Please enter Name, Email, and Phone Number to delete.")

 
