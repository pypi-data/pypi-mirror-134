use crate::qubit_backend::circuit::Circuit;
use pyo3::prelude::*;

#[pymethods]
impl Circuit {
    pub fn compute_expressivity() {
        for node in 0..self.num_nodes() {
        self.num_amplitudes
        // let KL_divergence = P * (P/Q).log().iter().sum();
        }
    }
}
