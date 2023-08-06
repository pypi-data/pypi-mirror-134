use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

use squall_router::SquallRouter;

#[pyclass]
pub struct Router {
    router: SquallRouter,
}

#[pymethods]
impl Router {
    #[new]
    fn new() -> Self {
        Router { router: SquallRouter::new() }
    }

    pub fn set_ignore_trailing_slashes(&mut self) -> PyResult<()> {
        self.router.set_ignore_trailing_slashes();
        Ok(())
    }

    pub fn add_route(&mut self, method: String, path: String, handler_id: i32) -> PyResult<()> {
        if let Err(e) = self.router.add_route(method, path, handler_id) {
            return Err(PyValueError::new_err(e.to_string()));
        }
        Ok(())
    }

    pub fn add_location(&mut self, method: String, path: String, handler_id: i32) -> PyResult<()> {
        Ok(self.router.add_location(method, path, handler_id))
    }

    pub fn resolve<'a>(
        &'a self,
        method: &str,
        path: &'a str,
    ) -> PyResult<Option<(i32, Vec<(&str, &'a str)>)>> {
        if let Some(result) = self.router.resolve(method, path) {
            return Ok(Some(result));
        }
        Ok(None)
    }

    pub fn add_validator(&mut self, alias: String, regex: String) -> PyResult<()> {
        match self.router.add_validator(alias, regex) {
            Ok(v) => Ok(v),
            Err(e) => Err(PyValueError::new_err(e.to_string())),
        }
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn squall_router(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Router>()?;
    Ok(())
}
