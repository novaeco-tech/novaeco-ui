# 🎨 NovaEco UI

**The Shared UI Library for the NovaEco System-of-Systems.**
This library provides standardized templates, CSS, and macros (like the Mission Control Launchpad) to ensure a consistent user experience across all vertical sectors (Agro, Trade, etc.).

---

## 📦 Installation

Since this is an internal library, install it directly from GitHub using `pip`.

**For Production (Pinned Version):**
Add this to your `requirements.txt`:
```text
git+https://github.com/novaeco-tech/novaeco-ui.git@v0.1.0#egg=novaeco-ui
````

**For Local Development (Editable):**

```bash
# Clone the repo first
git clone https://github.com/novaeco-tech/novaeco-ui.git

# Install in editable mode
pip install -e ./novaeco-ui
```

-----

## 🚀 Usage

### 1\. Register the Blueprint

In your Flask application (`app.py` or `create_app`), register the blueprint to expose the static assets and templates.

```python
from flask import Flask
from novaeco_ui import novaeco_ui_bp

app = Flask(__name__)

# Register the blueprint
# This makes templates available under 'novaeco_ui/' 
# and static files under '/static/novaeco_ui/'
app.register_blueprint(novaeco_ui_bp)
```

### 2\. Use the Launchpad

The library provides a Jinja2 macro to render the global navigation bar. You must pass the service URLs dynamically to ensure it works in both Local Dev and Production.

**In your base template (e.g., `base.html`):**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="{{ url_for('novaeco_ui.static', filename='css/launchpad.css') }}">
</head>
<body>

    {% from 'novaeco_ui/launchpad.html' import render_launchpad %}

    {{ render_launchpad(
         user=current_user, 
         active_app='agro',
         urls={
           'app': config.get('APP_URL'),
           'agro': config.get('AGRO_URL'),
           'trade': config.get('TRADE_URL'),
           'auth_logout': config.get('AUTH_LOGOUT_URL')
         }
       ) 
    }}

    <main>
        {% block content %}{% endblock %}
    </main>

</body>
</html>
```

-----

## 🛠️ Development & Release

### Versioning strategy

This repository uses a **`VERSION` file** as the single source of truth.
We do not use `git push` tags manually. We use the **NovaEco CLI** and GitHub Actions.

### How to release a new version

1.  **Make your changes** (CSS/HTML).

2.  **Bump the version** using the CLI (requires `novaeco-devtools`):

    ```bash
    # Bumps VERSION from 0.1.0 -> 0.1.1
    novaeco version patch ui
    ```

3.  **Push to main:**

    ```bash
    git add VERSION
    git commit -m "chore(release): bump to 0.1.1"
    git push
    ```

4.  **Wait for CI:**

      * The GitHub Action will detect the change in `VERSION`.
      * It will auto-tag the commit as `v0.1.1`.
      * It will create a GitHub Release.

5.  **Update Consumers:**

      * Go to `novaeco` (Core) or other sector repos.
      * Update their `requirements.txt` to the new tag.
