fetch('https://fudpkbqlpl.execute-api.us-east-1.amazonaws.com/Prod/resume-site')
    .then(res => res.json())
    .then((data) => {document.getElementById('count').innerText = data})
