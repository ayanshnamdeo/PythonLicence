# import csv
# import cv2
# import pytesseract
# import sqlite3

# # Initialize the Tesseract OCR engine
# pytesseract.pytesseract.tesseract_cmd = 'C:/Users/ayanshnamdeo/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

# # Open a video file
# video_path = 'model/newSample.mp4'
# cap = cv2.VideoCapture(video_path)
# def save_to_csv(license_plate_text):
#     # Save the data to a CSV file
#     with open('license_plate_data.csv', 'a', newline='') as csvfile:
#         fieldnames = ['License Plate']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         # Write the header only if the file is empty
#         if csvfile.tell() == 0:
#             writer.writeheader()

#         # Write the data
#         writer.writerow({'License Plate': license_plate_text})
        
# def extract_license_plate_from_frame(frame):
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Use Tesseract to perform OCR on the grayscale image
#     license_plate_text = pytesseract.image_to_string(gray, config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

#     # Print the extracted license plate text
#     print("Detected License Plate:", license_plate_text)

#     # Store the data in a CSV file
#     save_to_csv(license_plate_text)

#     return frame

    

# # Connect to a SQLite database
# conn = sqlite3.connect('plate_numbers.db')
# cursor = conn.cursor()

# # Create a table to store plate numbers
# cursor.execute('''CREATE TABLE IF NOT EXISTS plates
#                   (id INTEGER PRIMARY KEY,
#                    plate_number TEXT,
#                    timestamp DATETIME)''')
# conn.commit()

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break


 
    
#     # Convert the frame to grayscale for better OCR results
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Use Tesseract to perform OCR on the grayscale frame
#     plate_number = pytesseract.image_to_string(gray)
    
#     # Clean up the recognized text (you may need to adapt this based on your data)
#     plate_number = ''.join(e for e in plate_number if e.isalnum())
    
#     if plate_number:
#         # Store the recognized plate number in the database along with a timestamp
#         cursor.execute('INSERT INTO plates (plate_number, timestamp) VALUES (?, CURRENT_TIMESTAMP)', (plate_number,))
#         conn.commit()
    
#     # Call the function to extract the license plate from the frame
#         processed_frame = extract_license_plate_from_frame(frame)

#         # Display the frame with the detected license plate
#         cv2.imshow('Detected License Plate', processed_frame)
#     cv2.imshow('Video', frame)
    
#     if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
#         break

# cap.release()
# cv2.destroyAllWindows()
# conn.close()


#new





# \

# import cv2
# import pytesseract
# import sqlite3

# # Set the path to the Tesseract OCR executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ayanshnamdeo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# # Initialize SQLite database
# conn = sqlite3.connect('license_plate_data.db')
# cursor = conn.cursor()

# # Create a table to store license plate data if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS license_plates (
#         id INTEGER PRIMARY KEY,
#         plate_number TEXT
#     )
# ''')
# conn.commit()

# def extract_license_plate_from_frame(frame):
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Use Tesseract to perform OCR on the grayscale image
#     license_plate_text = pytesseract.image_to_string(
#         gray, config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     )

#     # Print the extracted license plate text
#     print("Detected License Plate:", license_plate_text)

#     # Store the data in the SQLite database
#     save_to_database(license_plate_text)

#     return frame

# def save_to_database(license_plate_text):
#     # Save the data to the SQLite database
#     cursor.execute("INSERT INTO license_plates (plate_number) VALUES (?)", (license_plate_text,))
#     conn.commit()

# if __name__ == "__main__":
#     # Specify the path to the video file you want to process
#     video_path = 'model/newSample.mp4'

#     # Open the video file
#     cap = cv2.VideoCapture(video_path)

#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Call the function to extract the license plate from the frame
#         processed_frame = extract_license_plate_from_frame(frame)

#         # Display the frame with the detected license plate
#         cv2.imshow('Detected License Plate', processed_frame)

#         # Press 'q' to exit the loop
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close the OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()

#     # Close the SQLite database connection
#     conn.close()


#newww

# import cv2
# import pytesseract
# import sqlite3

# # Set the path to the Tesseract OCR executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ayanshnamdeo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# # Initialize SQLite database
# conn = sqlite3.connect('license_plate_data.db')
# cursor = conn.cursor()

# # Create a table to store license plate data if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS license_plates (
#         id INTEGER PRIMARY KEY,
#         plate_number TEXT
#     )
# ''')
# conn.commit()

# def extract_license_plate_from_frame(frame):
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Use Tesseract to perform OCR on the grayscale image
#     license_plate_text = pytesseract.image_to_string(
#         gray, config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
#     )

#     # Print the extracted license plate text
#     print("Detected License Plate:", license_plate_text)

#     # Store the data in the SQLite database
#     save_to_database(license_plate_text)

#     return frame

# def save_to_database(license_plate_text):
#     # Save the data to the SQLite database
#     cursor.execute("INSERT INTO license_plates (plate_number) VALUES (?)", (license_plate_text,))
#     conn.commit()

# def retrieve_and_print_license_plate_numbers():
#     # Retrieve license plate numbers from the database
#     cursor.execute("SELECT plate_number FROM license_plates")
#     plate_numbers = cursor.fetchall()

#     # Extract the license plate numbers from the result
#     license_plate_numbers = [row[0] for row in plate_numbers]

#     # Close the database connection
#     conn.close()

#     # Display the retrieved license plate numbers
#     for plate_number in license_plate_numbers:
#         print(plate_number)

# if __name__ == "__main__":
#     # Specify the path to the video file you want to process
#     video_path = 'model/newSample.mp4'

#     # Open the video file
#     cap = cv2.VideoCapture(video_path)

#     while cap.isOpened():
#         ret, frame = cap.read()

#         if not ret:
#             break

#         # Call the function to extract the license plate from the frame
#         processed_frame = extract_license_plate_from_frame(frame)

#         # Display the frame with the detected license plate
#         cv2.imshow('Detected License Plate', processed_frame)

#         # Press 'q' to exit the loop
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video capture object and close the OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()

#     # Retrieve and print the license plate numbers
#     retrieve_and_print_license_plate_numbers()

import cv2
import pytesseract
import re
import sqlite3

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ayanshnamdeo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Initialize SQLite database
conn = sqlite3.connect('license_plate_data.db')
cursor = conn.cursor()

# Create a table to store license plate data if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS license_plates (
        id INTEGER PRIMARY KEY,
        plate_number TEXT
    )
''')
conn.commit()

# Define a pattern for the HSRP format (customize this according to your region)
hsrp_pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'

def extract_license_plate_from_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to perform OCR on the grayscale image
    license_plate_text = pytesseract.image_to_string(
        gray, config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    )

    # Clean up the recognized text (remove non-alphanumeric characters)
    clean_plate_text = re.sub(r'[^A-Z0-9]', '', license_plate_text)

    # Check if the recognized text matches the HSRP pattern
    if re.match(hsrp_pattern, clean_plate_text):
        # Print the extracted license plate text
        print("Detected License Plate:", clean_plate_text)

        # Store the data in the SQLite database
        save_to_database(clean_plate_text)

    return frame

def save_to_database(license_plate_text):
    # Save the data to the SQLite database
    cursor.execute("INSERT INTO license_plates (plate_number) VALUES (?)", (license_plate_text,))
    conn.commit()

def retrieve_and_print_license_plate_numbers():
    # Retrieve license plate numbers from the database
    cursor.execute("SELECT plate_number FROM license_plates")
    plate_numbers = cursor.fetchall()

    # Extract the license plate numbers from the result
    license_plate_numbers = [row[0] for row in plate_numbers]

    # Close the database connection
    conn.close()

    # Display the retrieved license plate numbers
    for plate_number in license_plate_numbers:
        print("Retrieved License Plate:", plate_number)

if __name__ == "__main__":
    # Specify the path to the video file you want to process
    video_path = 'model/SampleData.mp4'

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Call the function to extract the license plate from the frame
        processed_frame = extract_license_plate_from_frame(frame)

        # Display the frame with the detected license plate
        cv2.imshow('Detected License Plate', processed_frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Retrieve and print the license plate numbers
    retrieve_and_print_license_plate_numbers()
