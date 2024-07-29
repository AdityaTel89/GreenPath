# GreenPath
Green Path (Traffic sign Classification)


# Traffic Sign Detection and Reporting System

This project aims to enhance road safety by using a Convolutional Neural Network (CNN) model for real-time traffic sign detection with 97.94% accuracy. It includes a user reporting system for reporting locations and incidents with detailed descriptions and integrates the traffic sign detection model into a responsive web application. Additionally, it provides a comprehensive learning page for users to study all traffic signs.

## Features

- **Real-time Traffic Sign Detection**: Utilizes a CNN model to accurately detect and classify traffic signs.
- **User Reporting System**: Allows users to report locations and incidents with detailed descriptions.
- **Responsive Web Application**: Ensures compatibility across various devices.
- **Learning Page**: A comprehensive section for users to study traffic signs, enhancing knowledge and safety.

## Installation

### Prerequisites

- Python 3.6 or higher
- Git
- Virtualenv

### Clone the Repository

```bash
git clone https://github.com/yourusername/traffic-sign-detection.git
cd traffic-sign-detection
```

### Create and Activate a Virtual Environment

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up the Application

1. **Database Setup**: Configure your database settings in the `config.py` file.
2. **Model Weights**: Download the pre-trained CNN model weights and place them in the `models/` directory.
3. **Environment Variables**: Create a `.env` file in the root directory and set up necessary environment variables (e.g., API keys, database URL).

### Run the Application

```bash
python app.py
```

### Access the Web Application

Open your browser and go to `http://localhost:5001`.

## Usage

- **Real-time Detection**: Upload images or use the live camera feed to detect traffic signs.
- **Reporting**: Submit reports about traffic incidents with location and description details.
- **Learning Page**: Browse and learn about various traffic signs.

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

---

## Python Installation Steps

1. **Download Python**: Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python for your operating system.

2. **Install Python**:
   - **Windows**: Run the downloaded executable file and follow the installation prompts. Make sure to check the box that says "Add Python to PATH".
   - **macOS**: Open the downloaded `.pkg` file and follow the installation instructions.
   - **Linux**: Use the package manager for your distribution (e.g., `sudo apt-get install python3`).

3. **Verify Installation**:
   - Open a terminal (Command Prompt on Windows) and run:
     ```bash
     python --version
     ```

4. **Install Pip**:
   - Pip is the package installer for Python. It is included by default with Python 3.4 and later. To ensure you have it installed, run:
     ```bash
     python -m ensurepip --upgrade
     ```

5. **Install Virtualenv**:
   - Virtualenv helps to create isolated Python environments. Install it using pip:
     ```bash
     pip install virtualenv
     ```
