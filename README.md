# 🐍 Terminal Snake

**A fun snake game for your terminal - perfect for quick breaks while waiting for builds, deployments, or long-running processes!**

![Terminal Snake Demo](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20unix-lightgrey)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎮 Features

- **🚀 Quick to start** - Just run `snake` in your terminal
- **🎯 Classic gameplay** - Eat food, grow your snake, avoid walls and yourself
- **🌈 Colorful interface** - Green snake, red food, yellow score (if your terminal supports colors)
- **⌨️ Simple controls** - Arrow keys to move, 'Q' to quit
- **📱 Responsive** - Adapts to your terminal size
- **💻 Cross-platform** - Works on Linux, macOS, and Unix systems
- **🔧 No dependencies** - Uses Python's built-in `curses` library

## 🚀 Installation

### From PyPI (Recommended)

```bash
pip install terminal-snake
```

### From Source

```bash
git clone https://github.com/fdnthecoder/terminal-snake.git
cd terminal-snake
pip install .
```

## 🎯 Usage

After installation, you can start the game with either:

```bash
snake
```

or

```bash
terminal-snake
```

### As a Python Module

```python
from terminal_snake import play

# Start the game
play()
```

## 🎮 How to Play

1. **Move the snake** using arrow keys (↑ ↓ ← →)
2. **Eat the red food** (*) to grow your snake and increase your score
3. **Avoid hitting** the walls or your own body
4. **Press 'Q'** to quit anytime

### Controls

- `↑` - Move up
- `↓` - Move down
- `←` - Move left
- `→` - Move right
- `Q` - Quit game

## 🔧 Requirements

- **Python 3.6+**
- **Terminal with curses support** (most Linux/macOS terminals)
- **Minimum terminal size**: 20x10 characters

## 🎯 Perfect For

- 🏗️ **Waiting for builds** to complete
- 🚀 **Deployment downtime** 
- 🧪 **Test suite runs**
- ☕ **Coffee breaks**
- 🤔 **Thinking breaks** during coding
- 😴 **Any boring waiting period**

## 🎨 Screenshots

```
┌─ Score: 5 ──────────────── Arrows: move, Q: quit ─┐
│                                                   │
│           *                                       │
│                                                   │
│                    @##                           │
│                                                   │
│                                                   │
│                                                   │
│                                                   │
└───────────────────────────────────────────────────┘
```

## 🛠️ Development

### Local Development

```bash
# Clone the repository
git clone https://github.com/fdnthecoder/terminal-snake.git
cd terminal-snake

# Install in development mode
pip install -e .

# Run the game
snake
```

### Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests (if you add them)
pytest

# Format code
black terminal_snake/

# Lint code
flake8 terminal_snake/
```

### Building and Publishing

```bash
# Build the package
python setup.py sdist bdist_wheel

# Upload to PyPI (requires account and twine)
twine upload dist/*
```

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- 🎵 Add sound effects (terminal beeps)
- 🏆 High score tracking
- 🎨 Different snake themes
- 🎮 Different game modes (speed variations, obstacles)
- 📊 Game statistics
- 🐛 Bug fixes and improvements

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the classic Snake game
- Built with Python's `curses` library
- Perfect for procrastination during development 😄

## 📞 Support

If you encounter any issues:

1. Check that your terminal supports curses
2. Ensure your terminal is at least 20x10 characters
3. Make sure you're using Python 3.6+
4. [Open an issue](https://github.com/fdnthecoder/terminal-snake/issues) on GitHub

---

**Made with ❤️ for developers who need a quick break!**

*Happy coding and happy playing! 🐍🎮*

