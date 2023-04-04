<h1>Todo Project</h1>
    <p>
      This project is a simple todo list web application built with <a href="https://fastapi.tiangolo.com/">FastAPI</a> and a SQLite database. It allows users to create, update and delete tasks.
    </p>
    <h2>Installation</h2>
    <ol>
      <li>Clone the repository: <code>git clone https://github.com/KLYMENKORUS/Todo_App_FastAPI.git</code></li>
      <li>Install the dependencies: <code>pip install -r requirements.txt</code></li>
    </ol>
    <h2>Usage</h2>
    <ol>
      <li>Start the application: <code>uvicorn run:app --reload</code></li>
      <li>Open your browser and go to <a href="http://localhost:8000/">http://localhost:8000/</a></li>
      <li>Add new tasks by entering the title and clicking "Add Task".</li>
      <li>Mark tasks as complete by clicking the checkbox next to the task.</li>
      <li>Delete tasks by clicking the "Delete" button next to the task.</li>
    </ol>
    <h2>API Endpoints</h2>
    <p>The following API endpoints are available:</p>
    <ul>
      <li><code>GET /</code> - Returns a list of all tasks.</li>
      <li><code>POST /add</code> - Adds a new task.</li>
      <li><code>GET /update/{todo_id}</code> - Updates a task.</li>
      <li><code>GET /delete/{todo_id}</code> - Deletes a task.</li>
    </ul>
