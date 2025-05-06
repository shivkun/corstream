<p align="center">
  <a href="" rel="noopener">
 <img src="https://4jvunv3uhj.ufs.sh/f/j3njteUqvFKuYLYN4feQPcuZI9TeKXw4Cvol0qBhSHkiFJxN" alt="CorStream Logo"></a>
</p>

<h3 align="center">CorStream</h3>

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Last Commit](https://img.shields.io/github/last-commit/shivkun/corstream/main)]()
[![Contributors](https://img.shields.io/github/contributors/shivkun/corstream)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)


</div>

---

<p align="center">
    A coroutine composition framework for Python that enables declarative, streaming-style async pipelines.
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

**CorStream** is a Python library that lets you build elegant, composable pipelines using asynchronous iterables and coroutine-based operators. Think of it like a blend of `asyncio`, `RxPy`, and Unix pipes — but designed for readability, type safety, and modern Python development.

With CorStream, you can easily:
- Transform and filter async data flows
- Batch, throttle, or log stream data
- Apply async functions with concurrency control
- Collect or reduce outputs with simple syntax

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You’ll need Python 3.9 or higher and [Poetry](https://python-poetry.org/) installed:

```
python3 --version
# Should be 3.9+

curl -sSL https://install.python-poetry.org | python3 -
```

### Installing

Clone the repo and install dependencies with Poetry:

```
git clone https://github.com/shivkun/corstream.git
cd corstream
poetry install
```

CorStream is also published on PyPI, you can install it directly with:

```
pip install corstream
# or use Poetry
poetry add corstream
```

You can now run tests, examples, or start building pipelines!

## 🔧 Running the tests <a name = "tests"></a>

To run all tests:

```
poetry run pytest
```

### Break down into end-to-end tests

Each operator and sink has its own test file under `tests/`.

Example:

```
tests/test_map.py          # Tests for .map()
tests/test_batch.py        # Tests for .batch()
tests/test_to_list.py      # Tests for .to_list()
```

### And coding style tests

CorStream follows strict linting and formatting with `black`, `mypy`, and `ruff`:

```
poetry run black corstream/
poetry run ruff check corstream/
poetry run mypy corstream/
```

## 🎈 Usage <a name="usage"></a>

Here's a simple pipeline:

```python
from corstream import Stream

async def get_email(user_id: int) -> str:
    return f"user{user_id}@example.com"

async def send_batch(batch: list[str]):
    print("Sending:", batch)

await (
    Stream
    .from_iterable(range(1, 11))
    .filter(lambda x: x % 2 == 0)
    .map_async(get_email, max_concurrency=3)
    .batch(5)
    .log("batch")
    .for_each(send_batch)
)
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python 3.9+](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [AsyncIO](https://docs.python.org/3/library/asyncio.html)
- [Pytest](https://docs.pytest.org/)

## ✍️ Authors <a name = "authors"></a>

- [@shivkun](https://github.com/shivkun) — Design & Implementation

See also the list of [contributors](https://github.com/shivkun/corstream/contributors).

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Inspiration from functional programming and reactive streams
- Thanks to the maintainers of `asyncio`, `RxPy`, and `toolz`
