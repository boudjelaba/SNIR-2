<?php
$e1 = $_POST["entree"];
echo "e1 :";
echo $e1;
echo "<br>";

$e2 = htmlspecialchars($e1);
echo "e2 :";
echo $e2;
echo "<br>";

$e3 = htmlentities($e2);
echo "e3 :";
echo $e3;
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