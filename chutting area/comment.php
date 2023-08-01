<?php
// Retrieve the submitted form data
$name = $_POST['name'];
$email = $_POST['email'];
$comment = $_POST['comment'];

// You can store the data in a database or perform any other processing here

// Display the results on a webpage
?>

<!DOCTYPE html>
<html>
<head>
  <title>Comment Submission</title>
</head>
<body>
  <h1>Thank you for your comment!</h1>

  <p>Name: <?php echo $name; ?></p>
  <p>Email: <?php echo $email; ?></p>
  <p>Comment: <?php echo $comment; ?></p>
</body>
</html>