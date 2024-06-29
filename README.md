Here's the updated `README.md` file with your GitHub repository URL:

# WiFi Password Viewer

This Streamlit application displays the SSIDs and passwords of all saved WiFi profiles on your Windows device. It provides the following features:

## Features

1. **Export to File**: Download the list of WiFi profiles and their details as a CSV file.
2. **Graphical Visualization**: Visualize the most frequently connected WiFi networks using a bar chart.
3. **Additional WiFi Details**: View extra information such as authentication type and encryption method for each WiFi profile.
4. **Filter and Search**: Filter WiFi profiles by most recently used or those with available passwords, and search for specific SSIDs.

## Installation

To run this application, you need to have Python installed. Follow these steps to install the required dependencies:

1. Clone this repository:

    ```bash
    git clone https://github.com/dearcoder03/Wifi-Password-Viewer.git
    cd Wifi-Password-Viewer
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the Streamlit app, run the following command:

```bash
streamlit run wifi_password_viewer.py
```

This will start a local web server and open the app in your default web browser.

## Note

- This application works only on Windows.
- You must have the necessary permissions to access WiFi profiles on your device.

## Dependencies

The required dependencies are listed in the `requirements.txt` file:
- streamlit
- pandas
- matplotlib

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Thanks to the Streamlit community for providing excellent documentation and support.

This `README.md` file provides a comprehensive overview of the project, including features, installation instructions, usage, and other relevant details.
