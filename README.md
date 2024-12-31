
# Phishing Simulation Project

This project simulates a phishing attack for educational purposes, with a focus on enhancing awareness of phishing threats.

## Project Overview

### `send_mail.py`
- Script for sending phishing email alerts using the SMTP protocol.
- Sends an HTML email with a phishing link.
- When the link is clicked it will redirect to a fake facebook login page.
- After the victim press 'login' he will be redirected to a page where it says 'You have fallen for a phishing attack and guidance to avoid phishing mail's               in future'.

### `app.py`
- A Flask-based web application that logs user credentials into a SQLite database (`phishing_log.db`).
- Implements routes:
  - `/`: Serves the login page (`login_page.html`).
  - `/submit`: Captures credentials and logs them into the database.
  - `/educate`: Displays an educational page (`educate.html`) with phishing awareness tips.

### `phishing_log.db`
- It is a database that is created automatically when 'app.py' is run, it storing captured credentials.
- There will be a `log` table with columns for `username`, `password`, and `timestamp`.


## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2.**Send Emails**:
   Modify email credentials in `send_mail.py` and run the script to send phishing emails.
   ```bash
     python send_mail.py
   ```   
3. **Run the Application**:
   ```bash
   python app.py
   ```
   Access the application at `http://localhost:5000/`.

4. **Accessing Database**:
   When we run the `app.py` file it  create the `phishing_log.db` automatically and set up the `log` table.
   Here we see the people who has fallen victim to phishing stimulation.

## Warning
This project is intended solely for educational purposes and raising awareness. Unauthorized use of this tool for malicious purposes is illegal and unethical.
