const queryForm = document.getElementById('queryForm');
const queryInput = document.getElementById('queryInput');
const resultDisplay = document.getElementById('resultDisplay');
const uploadBtn = document.getElementById('uploadBtn');
const documentInput = document.getElementById('documentInput');
const uploadMessage = document.getElementById('uploadMessage');
const queryError = document.getElementById('queryError');
const uploadError = document.getElementById('uploadError');

queryForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const query = queryInput.value.trim();
  if (!query) {
    queryError.textContent = 'Please enter a query.';
    return;
  }
  queryError.textContent = '';
  try {
    const res = await fetch('http://localhost:8000/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    resultDisplay.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    queryError.textContent = 'Failed to fetch response from backend.';
  }
});

uploadBtn.addEventListener('click', async () => {
  const file = documentInput.files[0];
  if (!file) {
    uploadError.textContent = 'Please select a file.';
    return;
  }
  uploadError.textContent = '';
  const formData = new FormData();
  formData.append('file', file);
  try {
    const res = await fetch('http://localhost:8000/documents/upload', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    uploadMessage.textContent = data.message || 'Upload successful';
  } catch (error) {
    uploadError.textContent = 'Failed to upload document.';
  }
});
