

function _gitinit(){
        console.log("Initializing");
           $.ajax({
    url: "../test.py",
    type:'POST',
    context: document.body
  }).done(function() {
      console.log('Done');
  });
        };

        function _gitcommit(){

        };

 