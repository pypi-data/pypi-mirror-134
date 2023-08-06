<p align="center">
    <a href="https://github.com/mtag-dev/squall/">
        <img src="https://github.com/mtag-dev/squall/raw/master/docs/assets/squall-logo.png" alt="Squall" width="300"/>
    </a>
</p>
<p align="center">
    <em>Squall routing subsystem. Python binding for the <a href="https://crates.io/crates/squall-router">Rust Squall router</a> </em>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPi](https://img.shields.io/pypi/v/squall-router?color=%2334D058&label=pypi%20package)](https://pypi.org/project/squall-router/)
[![PyVersions](https://img.shields.io/pypi/pyversions/squall-router.svg?color=%2334D058)](https://pypi.org/project/squall-router/)


[Rust Squall router]: https://crates.io/crates/squall-router

### Installation

```shell
pip3 install squall-router
```

### Usage

```python
from squall_router import Router

router = Router()
router.add_validator("int", r"^[0-9]+$")
router.add_validator("uuid", r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

router.add_route("GET", "/repo/{repo_name}", 0)
router.add_route("GET", "/user/{user_id:int}", 1)
router.add_route("GET", "/event/{event_id:uuid}", 2)
router.add_location("GET", "/static", 3)

assert router.resolve("GET", "/repo/squall") == (0, [("repo_name", "squall")])
assert router.resolve("GET", "/user/123") == (1, [("user_id", "123")])
assert router.resolve("GET", "/user/user") is None

event_id = "6d1a7b12-f2de-4ba7-b3c5-a4af3cab757d"
assert router.resolve("GET", f"/event/{event_id}") == (2, [("event_id", event_id)])
assert router.resolve("GET", f"/event/123432") is None

assert router.resolve("GET", f"/static/css/style.css") == (3, [])
```

### Ignore trailing slashes mode

`set_ignore_trailing_slashes` - Allows to put the router in a mode where all trailing slashes will be ignored on both, route registration and resolving stages

```python
from squall_router import Router

router = Router()
router.set_ignore_trailing_slashes()
router.add_validator("int", r"^[0-9]+$")
router.add_validator("uuid", r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

router.add_route("GET", "/repo/{repo_name}/", 0)
router.add_route("GET", "/user/{user_id:int}/", 1)
router.add_route("GET", "/event/{event_id:uuid}", 2)
router.add_location("GET", "/static", 3)

assert router.resolve("GET", "/repo/squall") == (0, [("repo_name", "squall")])
assert router.resolve("GET", "/user/123") == (1, [("user_id", "123")])
assert router.resolve("GET", "/user/user") is None

event_id = "6d1a7b12-f2de-4ba7-b3c5-a4af3cab757d"
assert router.resolve("GET", f"/event/{event_id}/") == (2, [("event_id", event_id)])
assert router.resolve("GET", f"/event/123432/") is None

assert router.resolve("GET", f"/static/css/style.css") == (3, [])
```
