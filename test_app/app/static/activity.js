  $(document).ready(function() {
        
            // run an AJAX get request to the route you setup above...
            // respect the cross-domain policy by using the same domain
            // you used to access your index.html file!
           $.ajax({
    url: "/gitlet/git_init.js",
    type:'GET',
    context: document.body
  }).done(function() {
      console.log('Done');
  });   
    });




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