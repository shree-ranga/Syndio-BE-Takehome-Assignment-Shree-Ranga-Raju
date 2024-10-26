# Syndio Backend Takehome Assignment

## Steps to run the project

### Project setup

1. Open your terminal
2. Clone the repository:

```bash
   git clone https://github.com/shree-ranga/Syndio-BE-Takehome-Assignment-Shree-Ranga-Raju
```

3. Navigate to the cloned project directory:

```bash
   cd Syndio-BE-Takehome-Assignment-Shree-Ranga-Raju
```

### Setup virtual environment

1. Create virtual environment:

```bash
   python3 -m venv venv
```

2. Activate the virtual environment:

```bash
   source venv/bin/activate
```

### Install Python dependencies

```bash
pip install -r requirements.txt
```

### Run server

1. Set the desired server port:

```bash
   export DJANGO_PORT=5000 #replace with your desired port
```

2. Start the server:

```bash
   sh run.sh
```

3. Navigate to `127.0.0.1:5000/pvalue?department=Engineering` to see the results!
