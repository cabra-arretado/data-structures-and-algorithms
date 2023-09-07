#[derive(Debug)]
pub struct ArrayList<T> {
    length: usize,
    capacity: usize,
    array: *mut T,
}

impl<T> ArrayList<T> {
    pub fn new(capacity: usize) -> Self {
        Self {
            length: 0,
            capacity,
            array: std::ptr::null_mut(),
        }
    }
    pub fn get(&self, index: usize) -> Option<&T> {
        if index >= self.length {
            return None;
        }
        unsafe { self.array.add(index).as_ref() }
    }
}
