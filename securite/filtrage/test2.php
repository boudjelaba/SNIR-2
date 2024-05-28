<?php
$e1 = $_POST["entree"];
echo "e1 :";
echo $e1;
echo "<br>";

// filter_var()
$y2 = filter_var($e1, FILTER_SANITIZE_STRING);
echo "y2 :";
echo $y2;
echo "<br>";

$y3 = strip_tags($y2);
echo "y3 :";
echo $y3;
echo "<br>";

?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<form method="POST">
		<input type="text" id="entree" name="entree" required />
		<input type="submit" value="Submit">
	</form>
</body>
</html>