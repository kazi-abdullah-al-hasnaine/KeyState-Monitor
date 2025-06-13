# 🔐 KeyState Monitor v1.1

A modern, lightweight Windows desktop application that provides real-time visual monitoring of your keyboard lock keys (Caps Lock, Num Lock, and Scroll Lock) with an elegant, professional interface.

![KeyState Monitor](https://img.shields.io/badge/Platform-Windows-blue) ![Version](https://img.shields.io/badge/Version-1.1-green) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Size](https://img.shields.io/badge/Size-~10MB-orange)

## 📋 Overview

KeyState Monitor is a standalone desktop utility designed for users who need instant visual feedback about their keyboard's lock key states. Perfect for accessibility, productivity, and system monitoring, this application runs independently without requiring Python or any additional software installations.

### ✨ Key Features

- **🔄 Real-Time Monitoring**: Continuously tracks lock key states with smooth 200ms refresh intervals
- **🎨 Modern Interface**: Sleek dark theme with animated status indicators and professional styling
- **💡 Visual Feedback**: Color-coded glowing circles (Green=ON, Red=OFF) for instant recognition
- **📊 Smart Status Bar**: Live counter showing active keys and system status
- **⚡ Lightweight**: Minimal system resource usage (~10MB executable)
- **🖥️ Native Integration**: Direct Windows API integration for accurate, lag-free detection
- **🚀 Portable**: Single executable file - no installation required

## 🎯 Perfect For

- **Accessibility Users**: Visual confirmation when keyboard LEDs aren't visible or present
- **Remote Workers**: Monitor key states on external keyboards without built-in indicators  
- **Gamers**: Quick glance at lock states during gameplay without keyboard distractions
- **Content Creators**: Avoid typing errors during streaming, recording, or presentations
- **Office Workers**: Prevent accidental caps lock mishaps in professional communications
- **System Administrators**: Monitor keyboard states during remote sessions or troubleshooting

## 🖼️ Interface Preview

The application features three distinct visual states:
- **🟢 Active Keys**: Bright teal indicators with inner glow effects
- **🔴 Inactive Keys**: Coral red indicators for clear OFF status  
- **✨ State Changes**: Smooth background animations when keys toggle
- **📋 Status Bar**: Real-time active key counter with professional styling

## 🚀 Getting Started

### 📥 Download & Run (Recommended)

1. **Download the latest release**:
   - Navigate to `Releases/` → `Release 1.1/`
   - Download `KeyState Monitor.exe`

2. **Run immediately**:
   - Double-click the executable file
   - No installation, setup, or additional software required
   - Works on Windows 7, 8, 10, and 11

3. **Optional - Create Desktop Shortcut**:
   - Right-click `KeyState Monitor.exe`
   - Select "Create shortcut"
   - Move shortcut to Desktop for easy access

### 📁 File Structure
```
KeyState-Monitor/
├── Release/
│   └── Release 1.1/
│       └── KeyState Monitor.exe    ← Download this file
├── keystate_monitor.py             ← Source code
└── README.md                       ← This documentation
```

## 🛠️ Development & Source Code

### 🔧 For Developers & Customization

If you want to modify the source code, add features, or contribute:

#### **Clone Repository**
```bash
git clone https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor.git
cd keystate-monitor
```

#### **Prerequisites for Development**
- Python 3.6 or higher
- tkinter (included with Python)
- Windows OS for testing

#### **Run from Source**
```bash
python keystate_monitor.py
```

#### **Build Your Own Executable**
```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed --name "KeyState Monitor" keystate_monitor.py

# Find built executable in dist/ folder
```

### 🔨 Customization Options

The source code allows easy customization of:
- **Colors & Themes**: Modify the color scheme variables
- **Polling Rate**: Adjust monitoring frequency (default: 200ms)
- **Window Size**: Change dimensions and layout
- **Animations**: Customize transition effects and timing
- **Additional Keys**: Extend monitoring to other keyboard states

## ⚙️ Technical Specifications

### **System Requirements**
- **OS**: Windows 7/8/10/11 (32-bit or 64-bit)
- **RAM**: ~5MB runtime memory usage
- **Storage**: ~10MB disk space
- **Permissions**: Standard user privileges (no admin required)

### **Architecture Details**
- **Framework**: Python tkinter with Windows API integration
- **Key Detection**: Direct `ctypes.windll.user32.GetKeyState()` calls
- **Virtual Key Codes**: 
  - Caps Lock: `0x14`
  - Num Lock: `0x90`
  - Scroll Lock: `0x91`
- **Threading**: Non-blocking UI updates with efficient polling
- **Performance**: Optimized for minimal CPU usage

### **Security & Privacy**
- **No Internet Connection**: Completely offline application
- **No Data Collection**: Zero telemetry or user data gathering
- **Local Processing**: All operations performed on local machine
- **Open Source**: Full transparency with public source code

## 🐛 Troubleshooting

### Common Issues & Solutions

**Application won't start:**
- Ensure Windows Defender/antivirus isn't blocking the executable
- Try running as administrator if permission issues occur
- Check Windows version compatibility (Windows 7+)

**Key states not updating:**
- Restart the application
- Ensure no other software is interfering with keyboard monitoring
- Check if Windows accessibility features are conflicting

**Performance issues:**
- Close other resource-intensive applications
- The app uses minimal resources (~0.1% CPU typical usage)

**Display problems:**
- Update graphics drivers
- Check display scaling settings in Windows
- Try running in compatibility mode for older Windows versions

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### **Quick Contributions**
1. **Report Issues**: Use GitHub Issues for bugs or feature requests
2. **Suggest Features**: Share ideas for improvements
3. **Share Feedback**: Let us know how you use the application

### **Code Contributions**
1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/keystate-monitor.git
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-new-feature
   ```
4. **Make** your changes and test thoroughly
5. **Commit** with clear messages:
   ```bash
   git commit -m "Add amazing new feature with detailed description"
   ```
6. **Push** to your fork:
   ```bash
   git push origin feature/amazing-new-feature
   ```
7. **Submit** a Pull Request with detailed description

### **Development Guidelines**
- Follow existing code style and structure
- Test on multiple Windows versions when possible
- Update documentation for new features
- Keep the application lightweight and fast

## 📜 Version History

### **v1.1 (Current)**
- Modern GUI with dark theme and animations
- Improved visual indicators with glowing effects  
- Enhanced status bar with active key counter
- Optimized performance and reduced resource usage
- Added developer credit and GitHub integration

### **Previous Versions**
- v1.0: Initial release with basic functionality

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

**Summary**: Free to use, modify, and distribute for personal and commercial purposes.

## 🙏 Acknowledgments

- **Windows API**: For reliable system-level key state access
- **Python tkinter**: Cross-platform GUI framework
- **Open Source Community**: For inspiration and best practices
- **User Feedback**: Driving continuous improvement and feature development

## 📞 Contact & Support

**Kazi Abdullah Al Hasnaine**
- 🐙 **GitHub**: [@kazi-abdullah-al-hasnaine](https://github.com/kazi-abdullah-al-hasnaine)
- 📧 **Issues**: [Report bugs or request features](https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor/issues)
- 🌟 **Project**: [KeyState Monitor Repository](https://github.com/kazi-abdullah-al-hasnaine/keystate-monitor)

---

## 🚀 Quick Start Summary

1. **Download**: `Release/Release 1.1/KeyState Monitor.exe`
2. **Run**: Double-click the executable
3. **Enjoy**: Real-time keyboard lock key monitoring!

---

⭐ **If you find KeyState Monitor helpful, please star the repository!** ⭐

*Making keyboard state monitoring simple, elegant, and accessible for everyone.*
