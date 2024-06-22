# Pomodoro Technique Timer with Pygame

This repository contains an implementation of the Pomodoro Technique Timer using Tkinter in Python. The Pomodoro Technique is a time management method where work is divided into intervals (usually 25 minutes) separated by short breaks.

## Features

- **Work and Break Intervals**: The timer supports configurable work intervals (25 minutes), short breaks (5 minutes), and long breaks (20 minutes).
- **Visual Timer**: A graphical representation of the timer is displayed inside a tomato image.
- **Automatic Transitions**: The timer transitions automatically between work and break intervals.
- **Progress Checkmarks**: After each work interval, a checkmark is added to indicate progress.
- **Sound Notification**: A beep sound is played when each interval ends.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. **Install dependencies**:
   Ensure you have Python installed. You can install the required libraries using pip:
   ```sh
   pip install tkinter winsound
   ```

3. **Run the program**:
   ```sh
   python pomodoro_timer.py
   ```

## Usage

### Start the Timer

Click the "Start" button to begin the timer. The timer will start counting down from 25 minutes (default work interval).

### Reset the Timer

Click the "Reset" button to reset the timer. This will stop the current countdown and reset the timer display to "00:00".

### Checkmarks

After each work interval, a checkmark (✔) will appear below the timer to indicate progress. Every two intervals will be followed by a short break, and every four intervals will be followed by a long break.

## Customization

You can customize various aspects of the timer, including:

- **Work Interval**: Change the `WORK_MIN` constant to adjust the work interval duration.
- **Short Break Interval**: Change the `SHORT_BREAK_MIN` constant to adjust the short break duration.
- **Long Break Interval**: Change the `LONG_BREAK_MIN` constant to adjust the long break duration.
- **Colors and Fonts**: Customize the appearance by changing the color and font constants.

## Code Overview

### Constants

- **Colors**: PINK, RED, GREEN, YELLOW
- **Font**: FONT_NAME
- **Intervals**: WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN

### Main Components

- **Timer Reset**: `reset_timer()` function resets the timer to its initial state.
- **Timer Mechanism**: `start_timer()` function starts the timer and manages the transitions between work and break intervals.
- **Countdown Mechanism**: `count_down(count)` function manages the countdown for each interval.
- **UI Setup**: The Tkinter window is set up with labels, buttons, and a canvas for the graphical timer.

### Key Functions

- **reset_timer()**: Stops the timer and resets the display and progress checkmarks.
- **start_timer()**: Starts the timer and transitions between work and break intervals.
- **count_down(count)**: Manages the countdown and updates the timer display every second.

## Future Improvements

- **Customizable Intervals**: Allow users to set custom durations for work and break intervals.
- **User Notifications**: Add visual or audio notifications for interval transitions.
- **Data Persistence**: Save and display historical data on work sessions and breaks.



---

Enjoy using the Pomodoro Technique Timer! If you have any questions or feedback, please don't hesitate to reach out.