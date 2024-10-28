# GPU Info
Simple Django web app to display the GPU information of on a host with NVIDIA GPUs
## Steps to Run the Code

1. **Create a virtual environment**

    ```bash
    virtualenv . --python=python3
    ```

2. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

3. **Generate a secret key**

    i. Open a Python shell in your project directory and run the following command:

    ```bash
    python3 manage.py shell
    ```

    ii. In the shell window, type:

    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```

    iii. Copy the generated key and add it to the `SECRET_KEY` field in the `server_monitor/settings.py` file.

4. **Start the web server**

    ```bash
    python manage.py runserver
    ```

    The web server will start at `localhost:8080`.
