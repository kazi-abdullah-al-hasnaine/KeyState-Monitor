# 🔐 KeyState Monitor

A modern, real-time Windows application that monitors the state of your keyboard lock keys (Caps Lock, Num Lock, and Scroll Lock) with a sleek, professional GUI.

![KeyState Monitor](https://img.shields.io/badge/Platform-Windows-blue) ![Python](https://img.shields.io/badge/Python-3.6+-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Description

KeyState Monitor is a lightweight desktop utility that provides real-time visual feedback for your keyboard's lock key states. With its modern dark theme and intuitive interface, you can instantly see whether Caps Lock, Num Lock, or Scroll Lock are active without having to check your keyboard indicators.

### ✨ Key Features

- **Real-time Monitoring**: Continuously tracks lock key states with 200ms refresh rate
- **Modern UI**: Clean, dark-themed interface with smooth animations
- **Visual Indicators**: Glowing status circles with color-coded feedback
- **Status Counter**: Shows how many keys are currently active
- **Lightweight**: Minimal system resources usage
- **Windows Integration**: Uses native Windows API for accurate key state detection

## 🎯 Use Cases

- **Accessibility**: Visual confirmation for users who can't see keyboard LEDs
- **Remote Work**: Monitor key states when using external keyboards without indicators
- **Gaming**: Quick glance at lock key states during gameplay
- **Productivity**: Avoid typing errors due to unexpected Caps Lock activation
- **System Monitoring**: Keep track of keyboard state during presentations or screen sharing

## 🖥️ Screenshots

The application features:
- **Green indicators** for active (ON) keys
- **Red indicators** for inactive (OFF) keys
- **Smooth animations** when key states change
- **Professional status bar** showing active key count

## 🚀 Installation & Usage

### Prerequisites
- Windows OS (7/8/10/11)
- Python 3.6 or higher
- tkinter (usually comes with Python)

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor.git
   cd keystate-monitor
   ```

2. **Run the application**:
   ```bash
   python keystate_monitor.py
   ```

3. **Or create an executable** (optional):
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --windowed keystate_monitor.py
   ```

### No Installation Required
Simply download the Python file and run it directly - no additional dependencies needed!

## 🛠️ Technical Details

### Architecture
- **GUI Framework**: tkinter (native Python GUI)
- **Windows API**: ctypes.windll for key state detection
- **Animation System**: Custom animation handlers for smooth transitions
- **Threading**: Non-blocking UI updates

### Key Components
- **ModernKeyFrame**: Custom widget for each lock key display
- **KeySentinelApp**: Main application controller
- **Windows API Integration**: Direct system calls for accurate key state reading

### Virtual Key Codes Used
- `0x14` - Caps Lock
- `0x90` - Num Lock  
- `0x91` - Scroll Lock

## 🎨 Customization

The application uses a carefully designed color scheme:
- **Background**: `#1e1e2f` (Dark blue-gray)
- **Cards**: `#363950` (Medium gray)
- **Active State**: `#4ecdc4` (Teal)
- **Inactive State**: `#ff6b6b` (Coral red)
- **Text**: `#ffffff` / `#e6e6e6` (White/Light gray)

You can easily modify colors, fonts, and animations by editing the respective variables in the code.

## 🔧 Configuration

### Polling Rate
Default: 200ms (5 times per second)
```python
self.root.after(200, self.update_status)  # Change 200 to desired milliseconds
```

### Window Size
Default: 400x320 pixels
```python
self.root.geometry("400x320")  # Modify as needed
```

## 🐛 Troubleshooting

### Common Issues

**Application doesn't start**:
- Ensure Python 3.6+ is installed
- Check if tkinter is available: `python -c "import tkinter"`

**Key states not updating**:
- Run as administrator (some systems require elevated privileges)
- Check if Windows API calls are blocked by security software

**Display issues**:
- Update graphics drivers
- Try running with `--disable-gpu` flag if using compiled version

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
git clone https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor.git
cd keystate-monitor
# Make your changes
python keystate_monitor.py  # Test your changes
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's tkinter for cross-platform compatibility
- Uses Windows API for reliable key state detection
- Inspired by the need for better keyboard state visibility

## 📧 Contact

**Kazi Abdullah Al Hasnaine**
- GitHub: [@kazi-abdullah-al-hasnaine](https://github.com/kazi-abdullah-al-hasnaine)
- Project Link: [https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor](https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor)

---

⭐ **Star this repository if you find it helpful!** ⭐

*KeyState Monitor - Making keyboard state monitoring simple and elegant.*
