#!/usr/bin/env python3
"""
Command Line Interface for Terminal Snake Game
"""

import argparse
import sys
from .game import play
from . import __version__


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="🐍 Terminal Snake Game - A fun break while waiting for builds!",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Controls:
  Arrow Keys  - Move the snake
  Q           - Quit the game

Objective:
  Eat the red food (*) to grow your snake and increase your score.
  Avoid hitting the walls or your own body!

Perfect for taking a quick break during:
  • Long build times
  • Deployment waits
  • Test suite runs
  • Any boring waiting period!

Enjoy! 🎮
        """
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"Terminal Snake {__version__}"
    )
    
    args = parser.parse_args()
    
    # Start the game
    print("🐍 Starting Terminal Snake Game...")
    print("📏 Make sure your terminal is at least 20x10 characters!")
    print("⌨️  Use arrow keys to move, 'Q' to quit.")
    print("\nPress Enter to start or Ctrl+C to cancel...")
    
    try:
        input()  # Wait for user to press Enter
        play()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()

