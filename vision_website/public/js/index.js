// Your web app's Firebase configuration
var firebaseConfig = {
    // firebase config details
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  firebase.auth.Auth.Persistence.LOCAL;


  //Signup backend
  $("#btn-signup").click(function() {
        var email = $('#email').val();
        var pass = $('#pass').val();
        var cpass = $('#cpass').val();
        if(email != "" && pass != "" && cpass != "") {
            if (pass == cpass) {
                var res = firebase.auth().createUserWithEmailAndPassword(email, pass)
                res.catch(function (error) {
                var errCode = error.code;
                var errMsg = error.message;
                console.log(errMsg)
                window.alert("Message :" + errMsg)
                });
            }
            else {
                window.alert("The Passoword and Confirmation Password are Different")
            }
        }   
        else {
            window.alert('Please fill all fields');
        }
    });
    
  //Signin backend
  $("#btn-signin").click(function() {
      var email = $('#email').val();
      var pass = $('#pass').val();
      if(email != "" && pass != "") {
          var res = firebase.auth().signInWithEmailAndPassword(email, pass)
          res.catch(function (error) {
              var errCode = error.code;
              var errMsg = error.message;
              console.log(errMsg)
              window.alert("Message :" + errMsg)
          }
          );
      }
      else {
          window.alert('Please fill all fields');
      }
  });

  //Forget Password backend
  $("#btn-forgetPass").click(function() {
      var auth = firebase.auth()
      var email = $('#email').val()

      if (email != "") {
          auth.sendPasswordResetEmail(email).then(function () {
              window.alert("E-Mail has been sent to the specified e-mail address. Please check and verify.")
          }).catch(function (error) {
                var errCode = error.code;
                var errMsg = error.message;
                console.log(errMsg)
                window.alert("Message :" + errMsg)
          })
      }
      else {
          window.alert("Please fill in the email field")
      }
    });

  //Logout backend
  $("#btn-logout").click(function() {
      firebase.auth().signOut();
  });
  
  //Account Settings
  $("#btn-accounts").click(function() {
      var fname = $('#fname').val()
      var lname = $('#lname').val()

      var rootRef = firebase.database().ref().child('Users')
      var uid = firebase.auth().currentUser.uid
      var userRef = rootRef.child(uid)
      if (fname != "") {
          if (lname != "") {
              var userData = {
                  "firstName" : fname,
                  "lastName" : lname,
              }
          }
          else if(lname == "") {
            var userData = {
                "firstName" : fname,
            }
          }

          userRef.set(userData, (error) => {
              if (error) {
                var errCode = error.code;
                var errMsg = error.message;
    
                console.log(errCode)
                console.log(errMsg)
                
                window.alert("Message :" + errMsg)
              }
              else {
                window.location.href = "/home"
              }
          })
      }
  });