
const keywords = document.currentScript.getAttribute('keywords')
const websites = document.currentScript.getAttribute('websites')

const data = {
  'keywords' : keywords,
  'websites' : websites
}

const Url = "http://127.0.0.1:5000/hello_world"


const postParams = {
  method:"POST",
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data)
}

fetch(Url,postParams)
  .then(data=>{return data.json()})
  .then(res=>{console.log(res)})
