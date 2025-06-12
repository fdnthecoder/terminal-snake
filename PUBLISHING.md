# 🚀 Publishing Terminal Snake to PyPI

This guide explains how to publish your snake game to PyPI so developers worldwide can install it with `pip install terminal-snake`.

## 📋 Prerequisites

1. **PyPI Account**: Create accounts on both:
   - [PyPI](https://pypi.org/account/register/) (production)
   - [TestPyPI](https://test.pypi.org/account/register/) (testing)

2. **API Tokens**: Generate API tokens for both accounts:
   - Go to Account Settings → API tokens → Add API token
   - Save these tokens securely!

3. **Install Publishing Tools**:
   ```bash
   pip install twine
   ```

## 🧪 Test on TestPyPI First

1. **Build the package**:
   ```bash
   cd terminal-snake
   python setup.py sdist bdist_wheel
   ```

2. **Upload to TestPyPI**:
   ```bash
   twine upload --repository testpypi dist/*
   ```
   - Enter your TestPyPI username and API token when prompted

3. **Test installation from TestPyPI**:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ terminal-snake
   snake  # Test the command
   ```

## 🌍 Publish to PyPI (Production)

1. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```
   - Enter your PyPI username and API token when prompted

2. **Verify installation**:
   ```bash
   pip install terminal-snake
   snake
   ```

## 🎯 After Publishing

Developers can now install your game with:

```bash
# Install the game
pip install terminal-snake

# Run it
snake
# or
terminal-snake

# Use in Python
from terminal_snake import play
play()
```

## 📈 Marketing Your Package

1. **Update your README** with installation badges
2. **Share on social media** with hashtags: #python #gamedev #terminal
3. **Post on Reddit**: r/python, r/commandline, r/gamedev
4. **Developer communities**: Dev.to, Hacker News, Python Discord

## 🔄 Updating the Package

1. **Update version** in `terminal_snake/__init__.py`
2. **Update CHANGELOG** if you have one
3. **Rebuild and republish**:
   ```bash
   # Clean old builds
   rm -rf build/ dist/ *.egg-info/
   
   # Build new version
   python setup.py sdist bdist_wheel
   
   # Upload
   twine upload dist/*
   ```

## 🎮 Usage Examples for Developers

**Perfect for build scripts**:
```bash
#!/bin/bash
echo "Starting long build process..."
make build &
BUILD_PID=$!

echo "🐍 Play snake while you wait!"
snake

wait $BUILD_PID
echo "Build complete!"
```

**In Python projects**:
```python
# In your development environment
def take_break():
    """Take a quick game break during development"""
    try:
        from terminal_snake import play
        print("🎮 Time for a quick break!")
        play()
    except ImportError:
        print("Install terminal-snake for quick game breaks: pip install terminal-snake")
```

## 📊 Package Statistics

After publishing, monitor your package:
- **Download stats**: https://pypistats.org/packages/terminal-snake
- **PyPI page**: https://pypi.org/project/terminal-snake/
- **Issues**: GitHub issues for bug reports and feature requests

---

**🎉 Congratulations! Your snake game is now available to developers worldwide!**

