# 🔐 Password Checker & Generator

This is a password strength checker and generator application built using Python and Streamlit. It helps users evaluate the strength of their passwords and provides suggestions for improving them. Additionally, it can generate strong passwords that meet modern security standards.

## Features

- **Password Strength Checker**: Checks the strength of your password based on length, complexity, and character variety (uppercase, lowercase, digits, special characters).
- **Common Weak Password Blacklist**: Rejects commonly used passwords like "password123", "123456", etc., and suggests stronger alternatives.
- **Custom Scoring Weights**: Passwords are scored on a scale from "Weak" to "Strong", with different weights given to factors such as length and complexity.
- **Password History**: Stores your last 10 strong passwords for reference, while also ensuring that newly created passwords are not similar to the last 3.
- **Password Suggestion**: Generates a random, strong password based on secure practices.
  
## Installation

To run the password checker app on your local machine, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/password-checker.git
    ```

2. Navigate to the project directory:
    ```bash
    cd password-checker
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. The app will open in your browser, and you can start using the password checker!

## Usage

1. **Enter a Password**: Type or paste your password into the input field. The app will evaluate its strength and provide feedback.
2. **Suggestions**: If your password is weak, the app will suggest improvements such as adding uppercase letters, digits, or special characters.
3. **Generate a Strong Password**: Click the "Suggest a Strong Password" button to receive a secure, randomly generated password.
4. **View Last 10 Passwords**: The app saves your last 10 strong passwords for reference. You can view them by expanding the "View Last 10 Passwords" section.

## Scoring System

- **Weak**: Score ≤ 3 - Your password is weak and needs improvements.
- **Moderate**: Score 4-5 - Your password is moderate but can be made stronger.
- **Strong**: Score 6-7 - Your password is strong and secure.

## Requirements

- Python 3.6+
- Streamlit
- `re` (regular expressions module)

### Example of a Strong Password:
A strong password should meet the following criteria:
- At least 12 characters long
- Contains a mix of uppercase and lowercase letters
- Includes at least one digit (0-9)
- Contains at least one special character (e.g., !@#$%^&*)

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Enjoy creating strong and secure passwords! 🔐

