# django-learning
Learning Django, to get prepared to be able to build a web application developed as part of my NBCC Core Research Assistant position.
This project explores foundational web development using Django, focusing on routing, views, templates, and HTTP handling.
It supports research into accessibility, clean architecture, and rapid prototyping for inclusive digital solutions.

I’m also using this framework  to simulate and analyze common CTF (Capture The Flag) attack vectors — such as URL manipulation, query/header/cookie injection, and session hijacking.
I am participating in the 2025 Target/ Women in Cybersecurity Challenge 
<p></p>
<img width="707" height="471" alt="image" src="https://github.com/user-attachments/assets/5aa995ee-b198-46c4-92b5-d6438dc47e1e" />

<img width="370" height="387" alt="image" src="https://github.com/user-attachments/assets/71a0b90b-4ef9-429c-a83c-82faddbb180b" />

# Django Access Lab

## Features
- Basic Django routing
- HTTP parameter testing
- CTF vulnerability simulations

## Setup
1. Clone the repo 
2. Create a virtualenv

I used Python’s built-in venv module to isolate the dependencies for this project.
Using a virtual environment ensures that:

🧼 Clean Environment
Each project maintains its own dependencies and versions (e.g., Django), avoiding global package conflicts.

🧪 Reproducibility
The environment can be recreated using requirements.txt, making it easier to collaborate and deploy.

🔒 Safety
Installing packages globally can break other Python projects. venv keeps things isolated.

Tooling Compatibility
Tools like django-admin and linters use the venv-scoped environment, ensuring predictable behavior.
"Activated env" 
.\venv\Scripts\Activate.ps1

3. Install Django  ---  python -m pip install Django
4. Start the Django project:

    django-admin startproject mysite .
5. Run the server
    python manage.py runserver
## Future Work
- Add authentication
- Simulate session hijacking
- Add test API routes
