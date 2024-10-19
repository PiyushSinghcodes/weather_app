# Weather App

A simple weather application built with Flask, allowing users to retrieve and visualize weather data.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- **Python**: Programming language used for backend development.
- **Flask**: Web framework used to build the web application.
- **Pandas**: Data manipulation and analysis library.
- **SQLite**: Lightweight database for storing weather data.
- **Matplotlib**: Library for creating static, animated, and interactive visualizations.
- **Requests**: Library for making HTTP requests to external APIs.
- **Docker**: Containerization tool to package the application.

## Features

- Retrieve and process weather data.
- Daily summary of weather conditions.
- Alert notifications for extreme weather conditions.
- Visualize weather data using charts.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Docker (for containerization)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/PiyushSinghcodes/weather_app.git
   cd weather_app
   ```

2. **Create a Virtual Environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   - Ensure `requirements.txt` is populated with the necessary packages. If it's empty, you can manually add the following lines:
     ```plaintext
     Flask
     pandas
     requests
     matplotlib
     ```
   - Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   - To run the application locally, use:
   ```bash
   python app.py
   ```

5. **Docker Installation (Optional)**
   - Build the Docker image:
   ```bash
   sudo docker build -t weather_app .
   ```
   - Run the Docker container:
   ```bash
   sudo docker run -p 8080:8080 weather_app
   ```

## Usage

- After running the app, open your browser and go to `http://127.0.0.1:8080` to access the weather app.
- Follow the prompts to retrieve and visualize the weather data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

Feel free to share.

Project By - Piyush Singh(https://www.linkedin.com/in/piyush-singh908?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app) 
