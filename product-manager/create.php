<?php 
$pName = $_GET['productName'];
$pID = $_GET['productID'];
$qStatus = $_GET['qualityStatus'];
$url = $_GET['pic']; // Using the URL input only

$db = mysqli_connect('localhost', 'root', '', 'product_db');

if (!$db) {
    die("Database connection failed: " . mysqli_connect_error());
}

$query = "INSERT INTO list (name, id, status, url) VALUES ('$pName', $pID, '$qStatus', '$url')";

if (mysqli_query($db, $query)) {
    echo 'Inserted successfully';
} else {
    echo 'Error: ' . mysqli_error($db);
}

// Redirect after insert
header('Location: formCreate.php');
exit;
?>
