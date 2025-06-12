# Terminal Snake

A classic snake game for your terminal. Perfect for quick breaks during development.

![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20unix-lightgrey)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- Classic snake gameplay in the terminal
- Colorful interface (green snake, red food, yellow score)
- Arrow key controls, 'Q' to quit
- Adapts to terminal size
- Cross-platform (Linux, macOS, Unix)
- No external dependencies (uses Python's built-in `curses`)

## Installation

```bash
pip install terminal-snake
```

Or from source:
```bash
git clone https://github.com/fdnthecoder/terminal-snake.git
cd terminal-snake
pip install .
```

## Usage

```bash
snake
```

Or as a Python module:
```python
from terminal_snake import play
play()
```

## How to Play

- Use arrow keys to move the snake
- Eat the red food (*) to grow and increase your score
- Avoid hitting walls or your own body
- Press 'Q' to quit

## Requirements

- Python 3.6+
- Terminal with curses support
- Minimum terminal size: 20x10 characters

## Development

```bash
git clone https://github.com/fdnthecoder/terminal-snake.git
cd terminal-snake
pip install -e .
```

## Contributing

Contributions are welcome! Some ideas:

- Add sound effects (terminal beeps)
- High score tracking
- Different game modes
- Bug fixes and improvements

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter issues:

1. Check that your terminal supports curses
2. Ensure your terminal is at least 20x10 characters
3. Make sure you're using Python 3.6+
4. [Open an issue](https://github.com/fdnthecoder/terminal-snake/issues) on GitHub

