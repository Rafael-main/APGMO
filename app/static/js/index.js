document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('generate_my_pass')
  .addEventListener('submit', handleForm)
})

async function handleForm(ev) {
  ev.preventDefault();

  let myForm = ev.target;
  let fd = new FormData(myForm);

  fd.append('api-key', 'myApiKey');

  for (let key of fd.keys()) {
    console.log(key, fd.get(key));
  }

  let json_data = await convert2JSON(fd);

  let url = 'http://localhost:5000/generate';
  let h = new Headers();
  h.append('Content-type', 'application/json');
  let req = new Request(url, {
    headers: h,
    body: json_data,
    method: 'post'
  });

  fetch(req)
    .then((res) => res.json())
    .then((data) => {
      console.log('Response from server');
      console.log(data);
      document.getElementById('password').value = data.password
    })
    .catch(console.warn)
}

function convert2JSON (formData) {
  obj = {};
  for (let key of formData.keys()) {
    obj[key] =  formData.get(key);
  }
  return JSON.stringify(obj);
}

function clickFunction() {
  var copyText = document.getElementById("password");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
};