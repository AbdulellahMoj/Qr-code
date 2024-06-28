# QR Code Generator

A versatile QR Code Generator built using Python and Flask. This project includes multiple versions with various functionalities, allowing users to generate QR codes in different formats and with customizable colors.

## Overview

This repository contains three versions of a QR Code Generator, each progressively adding more features. The goal of this project is to provide a simple yet powerful tool for creating QR codes that can be customized in terms of format and color. The final version includes a full-featured web application with a user-friendly interface.

## Features

- **Multiple Formats:** Generate QR codes in PNG and SVG formats.
- **Customization:** Customize the fill and background colors of the QR code.
- **Web Interface:** User-friendly web interface for generating and downloading QR codes.
- **Docker Support:** Easily containerize the application for deployment.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/qr-code-generator.git
    cd qr-code-generator
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Flask Application

1. **Navigate to the project directory:**
    ```sh
    cd qr-code-generator
    ```

2. **Run the Flask application:**
    ```sh
    python main.py
    ```

3. **Open your web browser and go to `http://127.0.0.1:5000` to use the QR Code Generator.**

Alternatively, you can use the deployed version of the application available at [this link](https://p01--qrcodegen--tq6n2bpmjsfv.code.run/generate).

## Versions

### Version 1
- **Description:** Generates a QR code directly in PNG format with predefined colors.
- **Functionality:** Simple script to generate and save the QR code as a PNG file.

### Version 2
- **Description:** Generates QR codes in both PNG and SVG formats, with customizable colors.
- **Functionality:** Command-line interface prompts the user for input to generate the QR code accordingly.

### Version 3 (Main Version)
- **Description:** Full web application using Flask, providing a user-friendly interface to input data, choose colors, and select the file format.
- **Functionality:** Displays the generated QR code on the web page and allows users to download it directly.
- **Components:**
  - `main.py`: Handles the Flask application logic.
  - `index.html`: HTML template for the web interface.
  - `Dockerfile`: Configuration for containerizing the application.
