# Filesystem python wrapper
Filesystem wrapper for python developers

# Install

```
pip install filesystem
```
[https://pypi.python.org/pypi/filesystem/](https://pypi.python.org/pypi/filesystem/)


# Usage
```python
import filesystem
# Using the glob syntax
pointers = filesystem.glob("filesystem/*")

# Walk recursively a directory
tree = [x for x in filesystem.walk("filesystem")]

print pointers 
```

```
# [{'name': '__init__.py', 'created': 1429784337.4815214, 'abspath': '/home/oskar/github/oskarnyqvist/python/filesystem/filesystem/__init__.py', 'modified': 1429784141.817514, 'access': 1429784337.4815214, 'ext': 'py', 'is_link': False, 'is_file': True, 'is_dir': False, 'dirname': 'filesystem', 'size': 1119}, {'name': '__init__.pyc', 'created': 1429784169.241515, 'abspath': '/home/oskar/github/oskarnyqvist/python/filesystem/filesystem/__init__.pyc', 'modified': 1429784169.241515, 'access': 1429784337.3615215, 'ext': 'pyc', 'is_link': False, 'is_file': True, 'is_dir': False, 'dirname': 'filesystem', 'size': 1902}]

```

``` python
py_files = [x for x in pointers if x["ext"] == "py"]
print py_files

```

```
# [{'name': '__init__.py', 'created': 1429784337.4815214, 'abspath': '/home/oskar/github/oskarnyqvist/python/filesystem/filesystem/__init__.py', 'modified': 1429784141.817514, 'access': 1429784337.4815214, 'ext': 'py', 'is_link': False, 'is_file': True, 'is_dir': False, 'dirname': 'filesystem', 'size': 1119}]

```
```python
print [x["name"] for x in py_files]
```

```
# ['__init__.py']
```
