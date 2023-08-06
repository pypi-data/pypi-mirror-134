use pyo3::exceptions::{PyOSError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::PyBytes;

use ravif::{encode_rgba, Config};
use std::fs;
use std::path::Path;

mod utils;

fn get_config(quality: Option<f32>) -> Config {
    let quality = match quality {
        Some(q) => q,
        None => 80.0,
    };
    let alpha_quality = ((quality + 100.) / 2.).min(quality + quality / 4. + 2.);
    Config {
        quality: quality,
        speed: 4,
        alpha_quality: alpha_quality,
        premultiplied_alpha: false,
        color_space: ravif::ColorSpace::YCbCr,
        threads: 0,
    }
}

fn convert_result(result: PyResult<Vec<u8>>, py: Python) -> PyResult<PyObject> {
    match result {
        Ok(res) => Ok(PyBytes::new(py, &res).into()),
        Err(err) => Err(err),
    }
}

fn convert_to_avif_from_path_internal(path: &Path, config: Config) -> PyResult<Vec<u8>> {
    let data = fs::read(&path).map_err(|e| {
        PyOSError::new_err(format!(
            "Unable to read input image {}: {}",
            path.display(),
            e
        ))
    })?;
    convert_to_avif_from_bytes_internal(&data, config)
}

fn convert_to_avif_from_bytes_internal(data: &Vec<u8>, config: Config) -> PyResult<Vec<u8>> {
    let img = utils::load_rgba(data)
        .map_err(|e| PyValueError::new_err(format!("Unable to decode image to rgba: {}", e)))?;
    let (out_data, _color_size, _alpha_size) = encode_rgba(img.as_ref(), &config)
        .map_err(|e| PyValueError::new_err(format!("Unable to encode image to avif: {}", e)))?;
    Ok(out_data)
}

#[pyfunction]
#[pyo3(text_signature = "(path, quality=80)")]
fn convert_to_avif_from_path(path: String, quality: Option<f32>, py: Python) -> PyResult<PyObject> {
    let config = get_config(quality);
    let result = convert_to_avif_from_path_internal(Path::new(&path), config);
    convert_result(result, py)
}

#[pyfunction]
#[pyo3(text_signature = "(image_bytes, quality=80)")]
fn convert_to_avif_from_bytes(
    image_bytes: Vec<u8>,
    quality: Option<f32>,
    py: Python,
) -> PyResult<PyObject> {
    let config = get_config(quality);
    let result = convert_to_avif_from_bytes_internal(&image_bytes, config);
    convert_result(result, py)
}

#[pymodule]
fn py_ravif(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(convert_to_avif_from_path, m)?)?;
    m.add_function(wrap_pyfunction!(convert_to_avif_from_bytes, m)?)?;
    Ok(())
}
