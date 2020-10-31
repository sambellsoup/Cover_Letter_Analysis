var request = new XMLHttpRequest();

request.open('GET', 'https://private-anon-951fd0fd5c-jobspikr.apiary-mock.com/v2/data');

request.setRequestHeader('Content-Type', 'application/json');
request.setRequestHeader('client_id', 'rooki_jp_sandbox_e7fea44cf2');
request.setRequestHeader('client_auth_key', 't2PM7wVV5Ij2wyJ-caRNuQEB6JsFImTjitzX60UElyY');

request.onreadystatechange = function () {
  if (this.readyState === 4 && this.status == 200) {
    console.log('Status:', this.status);
    console.log('Headers:', this.getAllResponseHeaders());
    console.log('this is the response', this.responseText);


    var myJSON = this.responseText;
    // myJSON = JSON.stringify(myJSON);
    // let regex = /\,(?!\s*?[\{\[\"\'\w])/g;
    // let correct = myJSON.replace(regex, '');
    // var myObj = JSON.stringify(myJSON);
    var myObj = JSON.parse(myJSON);
    document.getElementById("demob" + x).innerHTML = myObj.job_title;
    console.log('the type of response is', typeof myJSON)
    console.log(body)
    // var sampleObject = { name: "John", age: 31, city: "New York" };
    // var sampleJSON = JSON.stringify(sampleObject);
    // console.log("sampleJSON is a", typeof(sampleJSON))
    // console.log("sampleObject is a", typeof(sampleObject))
    x +++ 1
  }
};

    var body = {
      'size': 10,
      'cursor': 1549411216369936,
      'format': 'json',
      'search_query_json': {
        'query_string': {
          'default_field': 'job_title',
          'query': q
        }
      }
    };

    request.send(JSON.stringify(body));
