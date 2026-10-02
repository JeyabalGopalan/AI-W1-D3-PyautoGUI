import pyautogui
import pyperclip
import time
import re


# ==========================================
# STEP 1: GET URL FROM TERMINAL
# ==========================================

url = input("Enter Instagram Profile URL: ")

print("\nStarting automation...")
time.sleep(1)


# ==========================================
# STEP 2: OPEN GOOGLE CHROME
# ==========================================

print("Opening Google Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(5)


# ==========================================
# STEP 3: SELECT CHROME ACCOUNT
# ==========================================

print("Selecting Chrome account...")

# Change these coordinates according to your screen
pyautogui.moveTo(1129, 619, duration=0.5)
pyautogui.click()

time.sleep(5)


# ==========================================
# STEP 4: OPEN NEW TAB
# ==========================================

print("Opening new tab...")

pyautogui.hotkey("ctrl", "t")
time.sleep(2)


# ==========================================
# STEP 5: OPEN INSTAGRAM URL
# ==========================================

print("Opening Instagram profile...")

pyautogui.hotkey("ctrl", "l")

# Copy URL to clipboard
pyperclip.copy(url)

# Paste URL
pyautogui.hotkey("ctrl", "v")

# Open URL
pyautogui.press("enter")

# Wait for Instagram profile to load
time.sleep(7)


# ==========================================
# STEP 6: COPY PROFILE INFORMATION
# ==========================================

print("Copying profile information...")

# Select all visible webpage text
pyautogui.hotkey("ctrl", "a")

time.sleep(1)

# Copy selected text
pyautogui.hotkey("ctrl", "c")

time.sleep(2)


# Get copied text from clipboard
page_text = pyperclip.paste()


# ==========================================
# STEP 7: EXTRACT REQUIRED INFORMATION
# ==========================================

# Split the copied text into individual lines
lines = page_text.splitlines()

# Remove empty lines and unnecessary spaces
lines = [line.strip() for line in lines if line.strip()]


# ==========================================
# FIND ACCOUNT NAME
# ==========================================

# In your output:
# r4consulting_india
# R4consultingindia
#
# The first one is the Instagram username.

account_name = None

for line in lines:
    if line.startswith("r4consulting_india"):
        account_name = line
        break


# ==========================================
# FIND POSTS, FOLLOWERS AND FOLLOWING
# ==========================================

posts = None
followers = None
following = None

for line in lines:

    # Example:
    # "350 posts"
    if "posts" in line:
        posts = line.replace(" posts", "")

    # Example:
    # "317 followers"
    elif "followers" in line:
        followers = line.replace(" followers", "")

    # Example:
    # "466 following"
    elif "following" in line:
        following = line.replace(" following", "")


# ==========================================
# FIND BIO
# ==========================================

bio = None

bio_start = (
    "Boost Your Business with Expert Business Consultancy, "
    "Lead Generation & Brand Building | R4Consulting India"
)

for line in lines:
    if "Boost Your Business" in line:
        bio = line
        break


# ==========================================
# FIND LINK IN BIO
# ==========================================

link = None

for line in lines:
    if line.startswith("www.") or line.startswith("http"):
        link = line
        break


# ==========================================
# DISPLAY FINAL RESULT
# ==========================================

print("\n====================================")
print("       INSTAGRAM PROFILE DATA")
print("====================================")

print(f"Account Name : {account_name}")
print(f"Posts        : {posts}")
print(f"Followers    : {followers}")
print(f"Following    : {following}")
print(f"Bio          : {bio}")
print(f"Link in Bio  : {link}")

print("====================================")

# ==========================================
# STEP 8: OPEN MICROSOFT EXCEL
# ==========================================

print("\nOpening Microsoft Excel...")

# Open Windows Run
pyautogui.hotkey("win", "r")
time.sleep(1)

# Type Excel
pyautogui.write("excel")

# Press Enter
pyautogui.press("enter")

# Wait for Excel start screen
time.sleep(7)


# ==========================================
# STEP 9: CLICK BLANK WORKBOOK
# ==========================================

print("Selecting Blank Workbook...")

# Click the "Blank workbook" tile
# Based on your current screen resolution
pyautogui.click(370, 270)

# Wait for the workbook to open
time.sleep(5)


# ==========================================
# STEP 10: GO TO CELL A1
# ==========================================

print("Preparing Excel...")

pyautogui.hotkey("ctrl", "home")

time.sleep(1)


# ==========================================
# STEP 11: PREPARE HEADINGS + DATA
# ==========================================

headers = [
    "Account Name",
    "Posts",
    "Followers",
    "Following",
    "Bio",
    "Link in Bio"
]

values = [
    account_name,
    posts,
    followers,
    following,
    bio,
    link
]


# ==========================================
# STEP 12: CREATE EXCEL TABLE
# ==========================================

# \t = next column
# \n = next row

excel_data = (
    "\t".join(headers)
    + "\n"
    + "\t".join(str(value) for value in values)
)


# ==========================================
# STEP 13: COPY TABLE
# ==========================================

pyperclip.copy(excel_data)

time.sleep(1)


# ==========================================
# STEP 14: PASTE INTO EXCEL
# ==========================================

print("Storing data in Excel...")

# Make sure A1 is selected
pyautogui.hotkey("ctrl", "home")

time.sleep(1)

# Paste complete table
pyautogui.hotkey("ctrl", "v")

time.sleep(3)

# ==========================================
# STEP 15: SAVE EXCEL FILE
# ==========================================

print("\nStarting Save As process...")

# ------------------------------------------
# 1. Open File menu
# ------------------------------------------

pyautogui.hotkey("alt", "f")

time.sleep(2)


# ------------------------------------------
# 2. Select Save As
# ------------------------------------------

# Press A for Save As
pyautogui.press("a")

time.sleep(3)


# ------------------------------------------
# 3. Click Browse
# ------------------------------------------

print("Opening Browse...")

# IMPORTANT:
# This coordinate is for the Excel screen
# shown in your screenshot.
#
# If Browse appears in a different location
# on your computer, we can adjust it.

pyautogui.click(300, 500)

time.sleep(3)


# ==========================================
# STEP 16: ENTER SAVE LOCATION
# ==========================================

print("Selecting save location...")

# The Windows Save As dialog should now be open.
#
# Click the File name box near the bottom.

pyautogui.click(500, 760)

time.sleep(1)


# ==========================================
# STEP 17: ENTER FILE PATH + FILE NAME
# ==========================================

save_path = r"C:\Users\jeyaj\OneDrive\Desktop\AI\W1 D3\Final_Insta_Tracker\Page-Data.xlsx"

# Copy complete path
pyperclip.copy(save_path)

# Paste path into File name
pyautogui.hotkey("ctrl", "v")

time.sleep(1)


# ==========================================
# STEP 18: SAVE
# ==========================================

print("Saving Page-Data.xlsx...")

pyautogui.press("enter")

time.sleep(5)


# ==========================================
# STEP 19: HANDLE FORMAT WARNING
# ==========================================

# If Excel asks:
# "This document may contain features..."
#
# Press Enter to accept the default option.

pyautogui.press("enter")

time.sleep(3)


print("\n====================================")
print("       FILE SAVED SUCCESSFULLY")
print("====================================")

print("File Name : Page-Data.xlsx")
print("Location  :")
print(r"C:\Users\jeyaj\OneDrive\Desktop\AI\W1 D3\Final_Insta_Tracker")