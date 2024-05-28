<?php

include "../../_private/private_data.php";

function connect(){
	try{
		$conn = mysqli_connect(hostname: HOST, username: USER, password: PASS, database: DB);
		if($conn){
			echo "<h2>connecté</h2>";
			return $conn;
		}else{
			throw new Exception(message: "<h2>Connexion impossible</h2>");
			
		}
	}catch (Exception $e){
		echo "<h2>Erreur inconnue.</h2>";
		echo "<h2>Erreur" . $e->getMessage() . "</h2>";
	}
	return null;
}

$db = connect();
?>