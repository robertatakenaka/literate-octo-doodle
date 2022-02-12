# literate-octo-doodle

Utilitary to extract data from CouchDB database, only fields at the top level.


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


## Optional Configuration

By default, it extracts:

for books:

* _id
* title
* is_comercial
* isbn
* eisbn
* doi_number
* use_licence
* publisher
* language

For a different set of attributes, configure the environment variable `BOOK_FIELDS`:

*WINDOWS*

```console

SET BOOK_FIELDS="_id,title,is_comercial,isbn,eisbn,doi_number,use_licence,publisher,language"
```

*LINUX*

```console

export BOOK_FIELDS="_id,title,is_comercial,isbn,eisbn,doi_number,use_licence,publisher,language"
```

for chapters:

* _id
* monograph_title
* title
* order
* monograph
* descriptive_information

For a different set of attributes, configure the environment variable `CHAPTER_FIELDS`:

*WINDOWS*

```console

SET CHAPTER_FIELDS="_id,monograph_title,title,order,monograph,descriptive_information"
```

*LINUX*

```console

export CHAPTER_FIELDS="_id,monograph_title,title,order,monograph,descriptive_information"
```


## Mandatory Configuration

Set the environment variables:

* SERVER (CouchDB location)
* DATABASE (Database name)


**Example**

*Windows*

```console
set SERVER="http://couchdb.domain.org:5984"
set DATABASE=database_name
```

*Linux*

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