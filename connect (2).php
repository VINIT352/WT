<?php
  $Username = $_POST['Username'];
  $Mobile_no = $_POST['Mobile_no'];
  $Email = $_POST['Email'];
  $Age = $_POST['Age'];
  $position = $_POST['position'];

  $conn = new mysqli('localhost','root','','test');
  if($conn->connect_error){
    die('connection failed :'.$conn->connect_error);
  }else{
    $stmt = $conn->prepare("insert into registration(Username, Mobile_no, Email, Age, position)
    values(?, ?, ?, ?, ?)");
    $stmt->bind_param("sisis" ,$Username,$Mobile_no, $Email, $Age, $position);
    $stmt->execute();
    echo"REGISTRATION SUCESSFULL!!!!...";
    $stmt->close();
    $conn->close();
  }
?>
<html>
<title>Cricket Trial Regirstration</title>
<head>
      <style>
         body{
            background-image: url('cricket-bat-ball-26560801.jpg');
            background-repeat: no-repeat;
           background-attachment: fixed;
           background-size: cover;
       
         }
      </style>
    </head>
<body>

<br><br><br>Welcome <br>
Your Entered name is:<?php echo $_POST["Username"]; ?><br>
Your Entered Email address is: <?php echo $_POST["Email"]; ?><br>
Your Entered Mobile number is: <?php echo $_POST["Mobile_no"]; ?><br>
Your Entered Age is: <?php echo $_POST["Age"]; ?><br>
Your Selected Position is: <?php echo $_POST["position"]; ?><br>
<a href="test2.html" target="_self"><p>Home Page</p></a>

</body>
</html>