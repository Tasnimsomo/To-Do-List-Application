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

