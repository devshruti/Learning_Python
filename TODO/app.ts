// app.ts
class Todo {
    constructor(public id: number, public content: string, public completed: boolean = false) {}
}

class TodoList {
    private tasks: Todo[] = [];

    addTask(content: string) {
        const newTask = new Todo(Date.now(), content);
        this.tasks.push(newTask);
        return newTask;
    }

     // Method to get the list of tasks
     getTasks(): Todo[] {
        return this.tasks;
    }

    // Method to delete a task by ID
    deleteTask(taskId: number) {
        const taskIndex = this.tasks.findIndex((task) => task.id === taskId);
        if (taskIndex !== -1) {
            this.tasks.splice(taskIndex, 1);
        }
    }

    // Method to mark a task as completed or not
    markTaskAsCompleted(taskId: number, completed: boolean) {
        const task = this.tasks.find((task) => task.id === taskId);
        if (task) {
            task.completed = completed;
        }
    }
}


// Get DOM elements
const taskInput = document.getElementById('taskInput') as HTMLInputElement;
const addTaskButton = document.getElementById('addTaskButton') || "";
const taskList = document.getElementById('taskList') || "";

// Event listener for adding tasks
// Create an instance of TodoList
const todoList = new TodoList();

// Event listener for adding tasks
if (addTaskButton) {
    addTaskButton.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        console.log('Clicked Add Task Button'); 
        console.log('Task Text:', taskText);
        if (taskText !== '') {
            const newTask = todoList.addTask(taskText);
            renderTask(newTask);
            taskInput.value = '';
        }
    });
} else {
    console.error("Element with ID 'addTaskButton' not found.");
}

// Function to render a task
function renderTask(task: Todo) {
    const taskItem = document.createElement('li');
    taskItem.innerHTML = `
        <div class="flex items-center justify-between py-2 border-b">
            <span class="${task.completed ? 'line-through' : ''}">${task.content}</span>
            <button class="text-red-600 delete-btn">Delete</button>
        </div>
    `;

    // Event listener for deleting tasks
    const deleteButton = taskItem.querySelector('.delete-btn') as HTMLElement;
    if (deleteButton) {
        deleteButton.addEventListener('click', () => {
            // Implement logic to delete the task from the TodoList and remove it from the UI
            const taskId = task.id; // Get the task's ID
            todoList.deleteTask(taskId); // Use the TodoList method to delete the task
            taskItem.remove(); // Remove the task item from the UI
        });
    }

    // Event listener for marking tasks as completed
    const taskText = taskItem.querySelector('span') as HTMLElement;
    taskText.addEventListener('click', () => {
        // Implement logic to toggle the completed status of the task
        const taskId = task.id; // Get the task's ID
        const completed = !task.completed; // Toggle completed status
        todoList.markTaskAsCompleted(taskId, completed); // Use the TodoList method to update completed status
        task.completed = completed; // Update the task object
        taskText.classList.toggle('line-through'); // Update UI to show completed status
    });

    if (taskList) {
        taskList.appendChild(taskItem);
    } else {
        console.error("Element with ID 'taskList' not found.");
    }
}

// Function to save tasks to localStorage
function saveTasksToLocalStorage() {
    localStorage.setItem('tasks', JSON.stringify(todoList.getTasks()));
}

// Function to load tasks from localStorage
function loadTasksFromLocalStorage() {
    const savedTasks = localStorage.getItem('tasks');
    if (savedTasks) {
        const tasks = JSON.parse(savedTasks);
        tasks.forEach((task: Todo) => {
            todoList.addTask(task.content);
        });
    }
}

// Load tasks from localStorage when the page loads
document.addEventListener('DOMContentLoaded', () => {
    loadTasksFromLocalStorage();
    // Render the loaded tasks to update the UI
    todoList.getTasks().forEach((task) => {
        renderTask(task);
    });
});

// Event listener for adding, deleting, or marking tasks as completed
// Update localStorage whenever a task changes
taskList?.addEventListener('click', () => {
    saveTasksToLocalStorage();
});
