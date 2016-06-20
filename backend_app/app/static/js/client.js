function _gitinit(){
  console.log("Initializing");
    var request = new XMLHttpRequest();
request.open('GET', 'init', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};
/*


   
      function _gitinit(){
        console.log("Initializing");
           $.ajax({
    url: "init",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        
        };

  */

function _gitadd(){
  console.log("Adding");
    var request = new XMLHttpRequest();
request.open('GET', 'add', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};

/*

        function _gitadd(){
            console.log("Adding");
           $.ajax({
    url: "add",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  }).error(function(response){
    console.log(response);
  });


        };

*/

function _gitstatus(){
  console.log("Getting Status");
    var request = new XMLHttpRequest();
request.open('GET', 'status', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};

/*


        function _gitstatus(){
console.log("Getting Status");
           $.ajax({
    url: "status",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        };

        */


    function _gitcommit(){
  console.log("Commiting");
    var request = new XMLHttpRequest();
request.open('GET', 'commit', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};

/*

             function _gitcommit(){
console.log("Commiting");

           $.ajax({
    url: "commit",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        };
    */


    function _gitcommithistory(){
  console.log("Getting Status");
    var request = new XMLHttpRequest();
request.open('GET', 'commithistory', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};

/*

                     function _gitcommithistory(){
console.log("Showing Commit History");
           $.ajax({
    url: "commithistory",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        };

      */

function _gitcommitlogs(){
  console.log("Showing Commit Logs:");
    var request = new XMLHttpRequest();
request.open('GET', 'commitlogs', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};

/*


                     function _gitcommitlogs(){
console.log("Showing Commit Logs : ");
           $.ajax({
    url: "commitlogs",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        };

      */

function _gitloadrepo(){
  console.log("Loading a new repo/file");
    var request = new XMLHttpRequest();
request.open('GET', 'loadrepo', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};

/*

      function _gitloadrepo(){
console.log("Showing Commit Logs : ");
           $.ajax({
    url: "loadrepo",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        };

*/


function _gitdeff(){
  console.log("Showing diff of 2 commits");
    var request = new XMLHttpRequest();
request.open('GET', 'difftree', true);

request.onload = function() {
  if (request.status >= 200 && request.status < 400) {
    // Success!
    var resp = request.responseText;
    console.log(resp);
  } else {
    // We reached our target server, but it returned an error

  }
};

request.onerror = function() {
  // There was a connection error of some sort
};
request.send();
};


/*

              function _gitdiff(){
console.log("Showing Diff between 2 commits : ");
           $.ajax({
    url: "difftree",
    type:'GET',
    context: document.body
  }).done(function(response) {
      console.log(response);
  });
        };

        */