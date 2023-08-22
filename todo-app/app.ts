class Todo {
    id: number;
    content: string;
    completed: boolean;

    constructor(id: number, content: string, completed: boolean = false) {
        this.id = id;
        this.content = content;
        this.completed = completed;
    }
}
class TodoList {
    private tasks: Todo[] = [];
    private taskIdCounter: number = 1;

    addTask(content: string) {
        const newTask = new Todo(this.taskIdCounter++, content);
        this.tasks.push(newTask);
        return newTask;
    }

    deleteTask(id: number) {
        const taskIndex = this.tasks.findIndex(task => task.id === id);
        if (taskIndex !== -1) {
            this.tasks.splice(taskIndex, 1);
        }
    }

    markTaskAsCompleted(id: number) {
        const task = this.tasks.find(task => task.id === id);
        if (task) {
            task.completed = true;
        }
    }

    getAllTasks() {
        return this.tasks;
    }
}


// Create an instance of the TodoList class
const todoList = new TodoList();

// Function to render tasks in the UI
function renderTasks() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';

    todoList.getAllTasks().forEach(task => {
        // Create HTML elements to display each task
        const listItem = document.createElement('li');
        listItem.className = 'flex justify-between items-center';

        const taskText = document.createElement('span');
        taskText.innerText = task.content;

        const completeButton = document.createElement('button');
        completeButton.innerText = 'Complete';
        completeButton.addEventListener('click', () => {
            // Handle task completion here
            todoList.markTaskAsCompleted(task.id);
            renderTasks(); // Update the UI
        });

        const deleteButton = document.createElement('button');
        deleteButton.innerText = 'Delete';
        deleteButton.addEventListener('click', () => {
            // Handle task deletion here
            todoList.deleteTask(task.id);
            renderTasks(); // Update the UI
        });

        listItem.appendChild(taskText);
        listItem.appendChild(completeButton);
        listItem.appendChild(deleteButton);

        taskList.appendChild(listItem);
    });
}

// Add task when the "Add" button is clicked
const addTaskButton = document.getElementById('addTaskBtn');
addTaskButton.addEventListener('click', () => {
    const taskInput = <HTMLInputElement>document.getElementById('taskInput');
    const content = taskInput.value.trim();

    if (content) {
        // Add a new task to the TodoList
        todoList.addTask(content);

        // Clear the input field
        taskInput.value = '';

        // Update the UI to display the added task
        renderTasks();
    }
});

// Initial rendering of tasks
renderTasks();
// Inside your `renderTasks` function, modify the taskText element like this:
const taskText = document.createElement('span');
taskText.innerText = task.content;
taskText.style.textDecoration = task.completed ? 'line-through' : 'none';

const completeCheckbox = document.createElement('input');
completeCheckbox.type = 'checkbox';
completeCheckbox.checked = task.completed;
completeCheckbox.addEventListener('change', () => {
    // Handle task completion here
    todoList.markTaskAsCompleted(task.id);
    renderTasks(); // Update the UI
});

// Replace the completeButton with the completeCheckbox in the listItem
listItem.appendChild(completeCheckbox);
// In your `renderTasks` function, add a delete button:
const deleteButton = document.createElement('button');
deleteButton.innerText = 'Delete';
deleteButton.addEventListener('click', () => {
    // Handle task deletion here
    todoList.deleteTask(task.id);
    renderTasks(); // Update the UI
});

// Add the deleteButton to the listItem
listItem.appendChild(deleteButton);
// Function to save tasks to localStorage
function saveTasksToLocalStorage() {
    localStorage.setItem('tasks', JSON.stringify(todoList.getAllTasks()));
}

// Function to load tasks from localStorage
function loadTasksFromLocalStorage() {
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
        const tasks = JSON.parse(storedTasks);
        tasks.forEach((task: Todo) => {
            todoList.addTask(task.content);
            if (task.completed) {
                todoList.markTaskAsCompleted(task.id);
            }
        });
        renderTasks();
    }
}

// Call loadTasksFromLocalStorage when the app starts to load previously saved tasks
loadTasksFromLocalStorage();

// Add event listeners to save tasks when tasks change
addEventListener('unload', () => {
    saveTasksToLocalStorage();
});
