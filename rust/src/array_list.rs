
#[derive(Debug)]
pub struct ArrayList<T> {
    length: usize,
    capacity: usize,
    array: *mut T,
}

impl<T> ArrayList<T> {
    pub fn new() -> Self {
        ArrayList {
            length: 0,
            capacity: 0,
            array: std::ptr::null_mut(),
        }
    }
}
