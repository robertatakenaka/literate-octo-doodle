# literate-octo-doodle

## Installation

### Download the source code

```console
git clone https://github.com/robertatakenaka/literate-octo-doodle

```

### Create a virtual environment

```console
python3 -m venv virtualenv_dir
```

### Activate the virtual environment

**Windows**

```console
virtualenv_dir\Scripts\activate.bat
```

**Linux like**

```console
source virtualenv_dir/bin/activate
```

### Install the requirements

```console
pip install -r requirements.txt
```

### Install the application

```console
python setup.py install
```


## Configuration

Set the environment variables SERVER (CouchDB location) and DATABASE (Database name)

**Example**

```console
export SERVER="http://couchdb.domain.org:5984"
export DATABASE=database_name
```


## Usage

To get a CSV file with books data, run the command extract, where `/path/books.csv` is the CSV file path resulting of the command execution.

**Example**

```console
extract books /path/books.csv
```

To get a CSV file with chapters data, run the command extract, where `/path/chapters.csv` is the CSV file path resulting of the command execution.

**Example**

```console
extract chapters /path/chapters.csv
```