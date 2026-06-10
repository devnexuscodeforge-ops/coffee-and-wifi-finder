# coffee-and-wifi-finder
# Coffee & Wifi Finder

A simple Flask web application that helps users find cafes with good coffee, WiFi, and power socket availability. Users can also add new cafes through a form, and the data is saved into a CSV file.

## 📌 Project Name

**Coffee & Wifi Finder**

## 🚀 Features

* View a list of cafes
* Add a new cafe
* Save cafe data into a CSV file
* Validate Google Maps location URLs
* Show an error message when the URL is invalid
* Display cafe ratings for:

  * Coffee
  * WiFi strength
  * Power socket availability
* Simple and clean Bootstrap design

## 🛠️ Technologies Used

* Python
* Flask
* Flask-WTF
* WTForms
* HTML
* CSS
* Bootstrap
* CSV file storage

## 📁 Project Structure

```text
coffee-and-wifi-finder/
│
├── main.py
├── cafe-data.csv
│
├── static/
│   └── css/
│       └── styles.css
│
└── templates/
    ├── index.html
    ├── add.html
    └── cafes.html
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/coffee-and-wifi-finder.git
```

Go into the project folder:

```bash
cd coffee-and-wifi-finder
```

Install the required packages:

```bash
pip install flask flask-wtf
```

Run the project:

```bash
python3 main.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

## 🧪 How It Works

The home page lets users go to the cafe list or add a new cafe.

When a user adds a cafe, the app checks if the location is a valid URL. If the URL is wrong, the form shows:

```text
Invalid URL.
```

If the form is valid, the cafe information is saved into `cafe-data.csv`. Then the user is redirected to the cafes page, where the new cafe appears in the table.

## 📄 CSV Data Format

Cafe data is stored in `cafe-data.csv` using this format:

```csv
Cafe Name,Location,Open,Close,Coffee,Wifi,Power
```

Example:

```csv
Lighthaus,https://www.google.com/maps/place/Lighthaus+Cafe,11AM,3:30PM,☕☕☕☕,💪💪,🔌🔌🔌
```

## ✅ URL Validation

This project uses WTForms URL validation to make sure the cafe location is a real URL.

Example valid URL:

```text
https://www.google.com/maps
```

Example invalid URL:

```text
sdfsdf
```

## 📸 Screenshots

You can add your project screenshots here later.

```md
![Home Page](screenshots/home.png)
![Add Cafe Page](screenshots/add-cafe.png)
![Cafes Page](screenshots/cafes.png)
```

## 📚 What I Learned

While building this project, I practiced:

* Creating routes in Flask
* Rendering HTML templates
* Working with forms
* Using Flask-WTF and WTForms
* Validating user input
* Reading and writing CSV files
* Using Bootstrap for styling
* Building a small full-stack web app with Python

## 🔮 Future Improvements

* Add a database instead of CSV
* Add delete and edit cafe features
* Add user login
* Add search and filter options
* Improve mobile design
* Add real Google Maps integration

## 👨‍💻 Author

Created by **khsn**

## 📜 License

This project is open source and free to use for learning purposes.
