![Tests](https://github.com/estafons/boilerplate/actions/workflows/ci.yml/badge.svg)

# Boilerplate

Boilerplate is a simple python cli tool to create boiler plate code from jinja templates. It acts as a thin layer to Jinja. Its sole purpose is to help standarize aspects of boilerplate code writting. See the example usecase bellow and then try it out!

# Installation

TODO

## Example Usacase

Assume you want to create an application that is capable of *handling multiple file types* and then *return the text* that it read. This application could potentialy read text from: docx, pdf, images etc.


The data sources can be multiple and even more can be neccessary in the future. For each case, you will probably want to write a test case that tests that the data read are indeed correct.

So far you would probably copy-paste and change the code appropriately each time you created a new text-reader interface or rewrite a test from scratch.

With boilerplate you can create templates that you can use to generate your boilerplate code each time it is needed.

## Now lets Code it!

Assume a function that read text from a `.txt` file:

```python
def read_txt(file_path: str) -> str:
    pass
```

Now we will write a test that tests this functionality:

```python
def test_read_txt():
    txt_expected_file = Path(os.path.abspath(__file__)).parent.parent / "data/test_data.txt"
    txt_file = Path(os.path.abspath(__file__)).parent.parent / "data/test_data.txt"
    text_read = read_txt(txt_file)
    with open(txt_expected) as f:
       text_expected = f.read()
    assert text_read == text_expected
```

Now Suppose we want to write a function that reads from an image. We assume the same function signature:

```python
def read_from_image(file_path: str) -> str:
    pass
```

Our test will be something like the one bellow:

```python
def test_read_from_image():
    txt_expected_file = Path(os.path.abspath(__file__)).parent.parent / "data/expected_data.txt"
    image_file = Path(os.path.abspath(__file__)).parent.parent / "data/test_data.jpg"
    text_read = read_from_image(image_file)
    with open(txt_expected) as f:
       text_expected = f.read()
    assert text_read == text_expected
```

Well..

This is indeed pretty similar! What if we automated that? Lets try that out!

## Writting a simple template

```python
def test_read_from{{ source_name }}():
    expected_txt_file = Path(os.path.abspath(__file__)).parent.parent /"data/{{ expected_data_file_name }}"
    input_file = Path(os.path.abspath(__file__)).parent.parent / "data/{{ input_file_name }}"
    text_read = read_from_{{ source_name }}(input_file)
    with open(expected_txt_file) as f:
         text_expected = f.read()
    assert text_read == text_expected
```

With variables each time:
```yaml
source_name: txt | image
expected_data_file_name: some_file_name
input_file_name: some_other_file_name
```

Ok now we wrote our test for both cases!

What we achieved?
1. Wrote one test that we will use for most cases that are similar!
2. Enforced uniformity of code thus improving readability among developers.
3. You test both your function but the function interface too! If a function that reads from a source cannot be tested from this template then we may have broken a convention and we should always be aware when doing that.


[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
