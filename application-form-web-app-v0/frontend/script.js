const form = document.getElementById('userForm');
const userList = document.getElementById('userList');

async function loadUsers() {
  const res = await fetch('http://localhost:5000/api/users');
  const users = await res.json();
  userList.innerHTML = users.map(u => `<li>${u.name} (${u.email})</li>`).join('');
}

form.addEventListener('submit', async e => {
  e.preventDefault();
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  await fetch('http://localhost:5000/api/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, email })
  });
  form.reset();
  loadUsers();
});

loadUsers();
