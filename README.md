
# Alarm Clock

This repository contains a Python-based alarm clock application built using Tkinter for the GUI and Pygame for playing alarm tones. The application allows users to set an alarm, choose an alarm tone, and use a snooze function.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Set an alarm for a specific time (HH:MM:SS).
- Select an alarm tone (mp3 file) as per your choice.
- Snooze functionality with user-defined snooze time.

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/kunal654/alarm-clock.git
cd alarm-clock
```

### Install Dependencies

Install the necessary Python libraries using pip:

```bash
pip install pygame
```

## Usage

### Define Your Alarm Time and Tone

1. Launch the application by running the `alarm.py` file.
2. Enter the alarm time in the format HH:MM:SS.
3. Click the "Browse" button to select an mp3 file for the alarm tone.
4. Enter the snooze time in seconds.
5. Click the "Set Alarm" button to start the alarm.

### Run the Script

Execute the script to start the application:

```bash
python alarm_clock.py
```

## Script Overview

### `set_alarm(alarm_time, alarm_tone, snooze_time)`

This function performs the following tasks:

- Sets and checks the alarm time.
- Plays the alarm tone when the set time is reached.
- Handles the snooze functionality based on user input.

### `start_alarm()`

Starts the alarm in a separate thread to ensure the GUI remains responsive.

### `browse_file()`

Opens a file dialog to select an alarm tone file.

## Customization

### Modify Alarm Time Format

Adjust the format of the alarm time in the `time_entry` widget if needed.

### Change the Snooze Logic

Customize the snooze functionality by modifying the `set_alarm` function.

## Dependencies

- `pygame`: For playing the alarm tones.
- `tkinter`: For creating the GUI (usually comes pre-installed with Python).

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub or contact me directly at [kunalgautam489@gmail.com](mailto:kunalgautam489@gmail.com).

