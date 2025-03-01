# Simple Firebase Database Entry

Use this basic programming language to teach young kids computational thinking of basic order.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Install Python 3.8.1: https://www.python.org/ftp/python/3.8.1/python-3.8.1-amd64.exe
```

### Usage

Connect to the database
```python

from firebase_simple import database_fire

database = database_fire.Db("database.io.url", "secure.key.path")
```

Add values to the database
```python
# To access the root directory, leave the path parameter blank
database.update("/path/", {"value": 1, "array": [1, 2, 3, 4]})
```

Save data with unique key
```python
database.save({"value": 1, "value1": [1, 2, 3, 4]}, path = "/path/", ret=True)
```

Load data
```python
# To access the root directory, leave the path parameter blank
data = database.load("/path/")  # This is a dictionary
print(data["value"])  # This outputs: int 1
```

## Deployment

This will tell you how to get the development env running
Run this command into the CMD when python is installed

```
python -m pip install firebase_admin
```

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Morgan West** - *Core Development* - [morganz13](https://github.com/morganzwest)

## License and Code of Conduct

This project is licensed under the Creative Commons Zero v1.0 Universal License - see the [LICENSE.md](LICENSE.md) file for details.
This project uses a custom Code Of Conduct Distrobution - see the [CODE OF CONDUCT.md](docs/CODE_OF_CONDUCT.md) file for details.
This project requests all pull requests are written from our template - see the [PULL REQUEST TEMPLATE.md](docs/pull_request_template.md) for details.

This project requests all feature request (issues) are written with our template - see the [FEATURE REQUEST.md](.github/ISSUE_TEMPLATE/feature_request.md) file for details.
This project requests all bug reports (issues) are written with our template - see the [BUG REPORT.md](.github/ISSUE_TEMPLATE/bug_report.md) for details.
