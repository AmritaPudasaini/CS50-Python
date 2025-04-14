import pytest
import os
import json
from project import add_task, list_tasks, complete_task, delete_task, load_tasks, save_tasks

TASKS_FILE = "tasks.json"

# Helper function to reset the tasks file before each test
@pytest.fixture
def reset_tasks_file():
    """Reset tasks.json before each test to ensure a clean slate."""
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)
    yield
    # Cleanup after each test
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)

def test_add_task(reset_tasks_file):
    """Test adding a task to the task list."""
    add_task("Test Task 1")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test Task 1"
    assert tasks[0]["status"] == "incomplete"

def test_list_tasks(reset_tasks_file):
    """Test listing all tasks."""
    add_task("Test Task 1")
    add_task("Test Task 2")
    tasks = load_tasks()
    # Capture output and check if it contains the task descriptions
    output = list_tasks()
    assert "Test Task 1" in output
    assert "Test Task 2" in output

def test_complete_task(reset_tasks_file):
    """Test completing a task."""
    add_task("Test Task 1")
    tasks = load_tasks()
    assert tasks[0]["status"] == "incomplete"

    complete_task(1)

    tasks = load_tasks()
    assert tasks[0]["status"] == "complete"

def test_delete_task(reset_tasks_file):
    """Test deleting a task."""
    add_task("Test Task 1")
    add_task("Test Task 2")
    tasks = load_tasks()
    assert len(tasks) == 2

    delete_task(1)

    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test Task 2"

def test_invalid_task_number(reset_tasks_file):
    """Test completing or deleting a task with an invalid task number."""
    add_task("Test Task 1")
    tasks = load_tasks()
    assert len(tasks) == 1

    # Test completing with an invalid task number
    complete_task(2)  # Invalid task number
    tasks = load_tasks()
    assert tasks[0]["status"] == "incomplete"

    # Test deleting with an invalid task number
    delete_task(2)  # Invalid task number
    tasks = load_tasks()
    assert len(tasks) == 1
