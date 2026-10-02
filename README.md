# 📊 Instagram Profile Data Tracker using PyAutoGUI

A Python-based desktop automation project that uses **PyAutoGUI** to automate the process of collecting Instagram profile information and storing it in an Excel file.

The bot interacts with the browser and Microsoft Excel just like a human user by using mouse movements, keyboard actions, copy/paste operations, and screen-based automation.

---

## 📌 Project Overview

This project automates the collection of basic Instagram profile information.

The user enters an Instagram profile URL in the terminal. The bot then:

             START
                │
                ▼
       Enter Instagram URL
                │
                ▼
          Open Chrome
                │
                ▼
       Select Chrome Account
                │
                ▼
      Open Instagram Profile
                │
                ▼
        Copy Profile Text
                │
                ▼
       Extract Profile Data
                │
        ┌───────┴────────┐
        ▼                ▼
               START
                │
                ▼
       Enter Instagram URL
                │
                ▼
          Open Chrome
                │
                ▼
       Select Chrome Account
                │
                ▼
      Open Instagram Profile
                │
                ▼
        Copy Profile Text
                │
                ▼
       Extract Profile Data
                │
        ┌───────┴────────┐
        ▼                ▼
     Account Name        Posts
     Followers           Following
     Bio                 Link
                │
                ▼
          Open Excel
   
                │
                ▼
       Open Blank Workbook
                │
                ▼
       Store Profile Data
                │
                ▼
          Save Excel
                │
                ▼
              END

---

## 🎯 Objective

The main objective of this project is to demonstrate how **Python desktop automation** can be used in a Digital Marketing workflow.

Instead of manually copying Instagram profile information into Excel, the bot performs the repetitive task automatically.

---

## 📋 Data Collected

The bot extracts the following information:

| Field | Description |
|---|---|
| Account Name | Instagram username |
| Posts | Number of posts |
| Followers | Number of followers |
| Following | Number of accounts followed |
| Bio | Instagram profile bio |
| Link in Bio | Website/link available in the profile |

---

## 🛠️ Technologies Used

### Python

Python is used as the main programming language for building the automation.

### PyAutoGUI

PyAutoGUI is used to control the computer using:

- Mouse movement
- Mouse clicks
- Keyboard input
- Keyboard shortcuts
- Browser interaction
- Excel interaction

### Pyperclip

Pyperclip is used to:

- Copy text to the clipboard
- Read copied webpage information
- Paste URLs
- Transfer data into Excel

### Microsoft Excel

Excel is used to store the extracted Instagram profile information.

### Google Chrome

Chrome is used to access the Instagram profile.

---

Library	Purpose

* pyautogui	-> Mouse and keyboard automation
* pyperclip	-> Clipboard copy and paste
* time	-> Add delays and wait for applications
* re	-> Extract specific information using patterns
