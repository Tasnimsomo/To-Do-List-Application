# Task Management API Documentation

This document provides details about the API endpoints for the Task Management application.

## Base URL
The base URL for all endpoints is `http://<host>:<port>` (e.g., `http://127.0.0.1:5000`).

---

## Endpoints

### 1. List All Tasks
**Endpoint:** `/`  
**Method:** `GET`  
**Description:** Retrieves a list of all tasks.

- **Response:**
  - Renders the `index.html` template with a list of tasks.


### 2. Add a New Task
**Endpoint:** `/add`  
**Method:** `POST`  
**Description:** Adds a new task to the task list.

- **Request Parameters:**
  - `title` (string): The title of the task (from form data).

- **Response:**
  - Redirects to the `/` route to display the updated task list.

---


### 3. Delete a Task
**Endpoint:** `/delete/<int:id>`  
**Method:** `DELETE`  
**Description:** Deletes a specific task by its ID.

- **Path Parameter:**
  - `id` (integer): The ID of the task to delete.

- **Response:**
  - Redirects to the `/` route to display the updated task list.
---
### 4. Update a Task
**Endpoint:** `/update/<int:id>`  
**Method:** `POST`  
**Description:** Updates the title of a specific task by its ID.

- **Path Parameter:**
  - `id` (integer): The ID of the task to update.

- **Request Parameters:**
  - `title` (string): The new title for the task (from form data).

- **Response:**
  - Redirects to the `/` route to display the updated task list.

---
### 5. Mark a Task as Completed
**Endpoint:** `/complete_task/<int:id>`  
**Method:** `POST`  
**Description:** Marks a specific task as completed.

- **Path Parameter:**
  - `id` (integer): The ID of the task to mark as completed.

- **Response:**
  - Redirects to the `/` route to display the updated task list.

---

### 6. Mark a Task as Incomplete
**Endpoint:** `/incomplete_task/<int:id>`  
**Method:** `POST`  
**Description:** Marks a specific task as incomplete.

- **Path Parameter:**
  - `id` (integer): The ID of the task to mark as incomplete.

- **Response:**
  - Redirects to the `/` route to display the updated task list.

---

## Notes
1. Ensure the database connection is properly configured in the `database.py` file and the `Task` model is defined in `models.py`.
2. The `render_template` function expects templates in the `templates` directory.
3. Adjust HTTP methods or error handling as necessary for production use.

## Example Workflow
1. Access `/` to view all tasks.
2. Use `/add` to create a new task by submitting a form.
3. Interact with `/update/<id>`, `/complete_task/<id>`, or `/incomplete_task/<id>` to modify tasks.
4. Remove tasks via `/delete/<id>`.

