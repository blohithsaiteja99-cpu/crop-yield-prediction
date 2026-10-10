import os
import sys

# Ensure root directory and crop_project directory are in sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

CROP_PROJECT_DIR = os.path.join(ROOT_DIR, "crop_project")
if os.path.exists(CROP_PROJECT_DIR) and CROP_PROJECT_DIR not in sys.path:
    sys.path.insert(0, CROP_PROJECT_DIR)

# Import the Flask application instance
try:
    from crop_project.crop_app import app
except ImportError:
    from crop_app import app

# Expose app for Vercel WSGI
application = app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
