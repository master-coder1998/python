# 🔐 CAPTCHA Verification System

A Python-based CAPTCHA image generator and verification system using Tkinter GUI.

## 📋 Description

This project generates random CAPTCHA images and provides a graphical user interface for verifying user input against the generated CAPTCHA. It uses the `captcha` library to create images with random 6-digit codes.

## ✨ Features

- **Random CAPTCHA Generation** - Creates unique 6-digit CAPTCHA images
- **GUI Interface** - User-friendly Tkinter-based interface
- **Verification System** - Checks if user input matches the generated CAPTCHA
- **Refresh Functionality** - Generate new CAPTCHA on demand
- **Visual Feedback** - Message boxes for success/failure notifications

## 🛠 Prerequisites

```bash
pip install captcha pillow
```

## 📦 Installation

1. Install required dependencies:
```bash
pip install captcha
```

2. Download fonts and update paths in the code:
   - Download TrueType font files (.ttf)
   - Update the font paths in `Captcha.py`:
   ```python
   image = ImageCaptcha(fonts=['path/to/font1.ttf', 'path/to/font2.ttf'])
   ```

## 🚀 Usage

```bash
python Captcha.py
```

The application window will display:
- CAPTCHA image at the top
- Text input field for user verification
- Submit button to check the answer
- Refresh button to generate a new CAPTCHA

## 📁 Files

- `Captcha.py` - Main application file with Tkinter GUI implementation

## 🔧 Key Components

### ImageCaptcha
- Generates CAPTCHA images with random 6-digit numbers
- Uses specified TrueType fonts for text rendering
- Saves images as PNG files

### Tkinter GUI
- `Label` - Displays CAPTCHA image
- `Text` - Input field for user verification
- `Button` - Submit and Refresh buttons
- `messagebox` - Shows verification results

## 💡 Learning Concepts

- **GUI Development** - Tkinter framework basics
- **Image Generation** - Using PyCAP TCHA library
- **Event Handling** - Button clicks and user interaction
- **File I/O** - Saving and loading image files
- **String Comparison** - Verifying user input

## 📝 Notes

- The CAPTCHA image is saved as `out.png` in the current directory
- Each refresh generates a new random 6-digit code
- Case-sensitive verification

## 🌟 Potential Enhancements

- [ ] Add difficulty levels (more digits, distortion)
- [ ] Implement timeout for CAPTCHA expiration
- [ ] Add audio CAPTCHA for accessibility
- [ ] Save verification attempts log
- [ ] Customize fonts and styling
- [ ] Add security features (rate limiting)

## 📚 Related Topics

- Python GUI Development with Tkinter
- Image Processing
- Random Number Generation
- Event-Driven Programming
