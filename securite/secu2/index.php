<?php
// ********************
// A commenter 1 ou 2 lignes pour rendre
// l'en-tête ou le pieds de page inaccessible
define('en_tete', TRUE);
define('pieds', TRUE);
// ********************
require('header.php');
echo "<br>Corps du site<br>";
require('footer.php');
?>