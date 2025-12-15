# Sheet2DB

### Install and Configuration

1. Clone the repository:
```bash
git clone git@github.com:ViniciusSonntagDorow/Sheet2DB.git
cd Sheet2DB
```

2. Configure the correct Python version with `Pyenv`:
```bash
pyenv install 3.13
pyenv local 3.13
```

3. Create and activate virtual environment:
```bash
python -m venv .venv
# Mac and Linux
source .venv/bin/activate
# Windows
.venv/scripts/activate
```

4. Install the dependencies:
```bash
pip install -e .
```

5. Configure environment variables:
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your database credentials
```

### Running the Application

```bash
streamlit run src/main.py
```

### Running Tests

```bash
pytest tests/ -v
```