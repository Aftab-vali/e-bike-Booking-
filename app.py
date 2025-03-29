from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# Path to save the booking details
CSV_FILE = 'booking_details.csv'


# Function to save booking details to CSV
def save_booking_details(data):
    file_exists = os.path.isfile(CSV_FILE)

    # Define the header fields
    header = ['Name', 'Phone', 'Email', 'State', 'Password']

    # Open the CSV file in append mode
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write the header if the file is new
        if not file_exists:
            writer.writerow(header)

        # Write the booking details
        writer.writerow(data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        state = request.form.get('state')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Simple password match check
        if password != confirm_password:
            return render_template('book.html', error="Passwords do not match. Please try again.")

        # Save the booking details in the CSV file
        save_booking_details([name, phone, email, state, password])

        return redirect(url_for('success'))

    return render_template('book.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
