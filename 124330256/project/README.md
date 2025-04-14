# Task Management App

# Description:

### The Task Management Application is a Python-based command-line tool that allows users to manage their tasks. It provides basic functionality for adding, listing, and removing tasks, along with tracking their completion status. Tasks are stored in a JSON file (tasks.json), making it easy to load and save data between sessions. This simple tool aims to help users stay organized by managing tasks efficiently.

### File Structure: project.py

### This file contains the core logic for managing tasks:

### main(): The entry point, which displays a menu and handles user input.
### add_task(description): Adds a task with the given description.
### remove_task(task_id): Removes a task by its ID.
### list_tasks(): Lists all tasks with their completion status.

## test_project.py
### This file includes test functions to ensure the application works as expected:
### test_add_task(): Validates task addition.
### test_remove_task(): Validates task removal.
### test_list_tasks(): Ensures tasks are listed correctly.

## requirements.txt
### Lists dependencies for the project. It includes pytest for testing purposes.

## tasks.json
### A JSON file that stores tasks with their descriptions and completion statuses.

## Design Choices
### I chose to store task data in a JSON file for simplicity. This allows easy modification and retrieval of task data without needing a complex database. The task statuses are represented using boolean values (True for completed, False for pending), keeping the design straightforward.

### For testing, I used pytest to create clear and automated tests for the core functions, ensuring reliability and ease of maintenance.

## Future Improvements
### Adding a graphical user interface (GUI) for a more user-friendly experience.
### Implementing task prioritization and due dates for better task management.
### Adding notifications to remind users of tasks nearing their due dates.
