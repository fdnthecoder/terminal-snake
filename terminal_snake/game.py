#!/usr/bin/env python3
"""
Terminal Snake Game

A classic snake game that runs in your terminal. Perfect for taking a break
while waiting for builds, deployments, or long-running processes!

Controls:
- Arrow keys: Move the snake
- 'q': Quit the game

Objective:
- Eat the red food (*) to grow your snake and increase your score
- Avoid hitting the walls or your own body

Author: Amadou x Warp
"""

import curses
import random
import sys


class SnakeGame:
    """Main Snake Game class."""
    
    def __init__(self, height, width):
        """Initialize the snake game.
        
        Args:
            height (int): Terminal height
            width (int): Terminal width
        """
        self.height = height
        self.width = width
        
        # Start snake in the middle of the screen
        start_y = height // 2
        start_x = width // 2
        self.snake = [(start_y, start_x), (start_y, start_x-1), (start_y, start_x-2)]
        self.direction = (0, 1)  # Initial direction (right)
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        
    def generate_food(self):
        """Generate food at a random position not occupied by the snake.
        
        Returns:
            tuple: (y, x) coordinates of the food
        """
        while True:
            food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
            if food not in self.snake:
                return food
    
    def move_snake(self):
        """Move the snake in the current direction and handle collisions."""
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.height - 1 or
            new_head[1] <= 0 or new_head[1] >= self.width - 1):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 1
            self.food = self.generate_food()
        else:
            self.snake.pop()  # Remove tail if no food eaten
    
    def change_direction(self, new_direction):
        """Change snake direction, preventing reversing into itself.
        
        Args:
            new_direction (tuple): (dy, dx) direction tuple
        """
        # Prevent moving in opposite direction
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction


def main(stdscr=None):
    """Main game function that can be called directly or with curses wrapper.
    
    Args:
        stdscr: Curses screen object (optional, will be created if None)
    """
    if stdscr is None:
        # If called without stdscr, use curses wrapper
        return curses.wrapper(main)
    
    # Check minimum terminal size
    height, width = stdscr.getmaxyx()
    if height < 10 or width < 20:
        stdscr.addstr(0, 0, "Terminal too small! Minimum size: 20x10")
        stdscr.addstr(1, 0, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()
        return
    
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)  # Non-blocking input
    stdscr.timeout(150)  # Game speed (milliseconds)
    
    # Initialize colors if available
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Snake
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # Food
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Score
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Instructions
    
    # Initialize game
    game = SnakeGame(height, width)
    
    # Game loop
    while not game.game_over:
        # Clear screen
        stdscr.clear()
        
        # Draw borders
        stdscr.border()
        
        # Handle input
        key = stdscr.getch()
        if key == curses.KEY_UP:
            game.change_direction((-1, 0))
        elif key == curses.KEY_DOWN:
            game.change_direction((1, 0))
        elif key == curses.KEY_LEFT:
            game.change_direction((0, -1))
        elif key == curses.KEY_RIGHT:
            game.change_direction((0, 1))
        elif key == ord('q') or key == ord('Q'):
            break
        
        # Move snake
        game.move_snake()
        
        # Draw snake
        for i, segment in enumerate(game.snake):
            try:
                if i == 0:  # Head
                    char = '@'
                    attr = curses.color_pair(1) | curses.A_BOLD if curses.has_colors() else curses.A_BOLD
                else:  # Body
                    char = '#'
                    attr = curses.color_pair(1) if curses.has_colors() else 0
                stdscr.addch(segment[0], segment[1], char, attr)
            except curses.error:
                # Handle edge case where drawing goes out of bounds
                pass
        
        # Draw food
        try:
            food_attr = curses.color_pair(2) | curses.A_BOLD if curses.has_colors() else curses.A_BOLD
            stdscr.addch(game.food[0], game.food[1], '*', food_attr)
        except curses.error:
            pass
        
        # Draw score
        score_text = f"Score: {game.score}"
        score_attr = curses.color_pair(3) | curses.A_BOLD if curses.has_colors() else curses.A_BOLD
        try:
            stdscr.addstr(0, 2, score_text, score_attr)
        except curses.error:
            pass
        
        # Draw instructions
        if width > 30:  # Only show if screen is wide enough
            try:
                instr_attr = curses.color_pair(4) if curses.has_colors() else 0
                stdscr.addstr(0, width - 25, "Arrows: move, Q: quit", instr_attr)
            except curses.error:
                pass
        
        # Refresh screen
        stdscr.refresh()
    
    # Game over screen
    stdscr.clear()
    stdscr.border()
    
    game_over_text = "GAME OVER!"
    final_score_text = f"Final Score: {game.score}"
    restart_text = "Press any key to exit"
    
    # Center the text
    h, w = stdscr.getmaxyx()
    try:
        game_over_attr = curses.color_pair(2) | curses.A_BOLD if curses.has_colors() else curses.A_BOLD
        score_attr = curses.color_pair(3) | curses.A_BOLD if curses.has_colors() else curses.A_BOLD
        exit_attr = curses.color_pair(4) if curses.has_colors() else 0
        
        stdscr.addstr(h//2 - 1, (w - len(game_over_text))//2, game_over_text, game_over_attr)
        stdscr.addstr(h//2, (w - len(final_score_text))//2, final_score_text, score_attr)
        stdscr.addstr(h//2 + 2, (w - len(restart_text))//2, restart_text, exit_attr)
    except curses.error:
        # Fallback for very small terminals
        stdscr.addstr(1, 1, "Game Over!")
        stdscr.addstr(2, 1, f"Score: {game.score}")
    
    stdscr.refresh()
    stdscr.nodelay(False)  # Wait for input
    stdscr.getch()


def play():
    """Entry point for the game - handles errors gracefully."""
    try:
        main()
    except KeyboardInterrupt:
        print("\n🐍 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Make sure your terminal supports curses and has sufficient size.")
    finally:
        print("\n🎮 Thanks for playing Terminal Snake!")


if __name__ == "__main__":
    play()

