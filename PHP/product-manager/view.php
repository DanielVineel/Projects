<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Products</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="main">
        <div class="table-container">
            <h2>Product List</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Status</th>
                        <th>Image</th>
                    </tr>
                </thead>
                <tbody>
                <?php
                    $db = mysqli_connect('localhost', 'root', '', 'product_db');
                    $data = mysqli_query($db, 'SELECT * FROM list');

                    while ($row = mysqli_fetch_assoc($data)) {
                        echo "<tr>
                                <td>{$row['id']}</td>
                                <td>{$row['name']}</td>
                                <td>{$row['status']}</td>
                                <td><img src='{$row['url']}' alt='Image' style='max-width:100px;'></td>
                              </tr>";
                    }
                ?>
                </tbody>
            </table>
            <button onclick="window.location.href='formCreate.php'">Back to Add</button>
        </div>
    </div>
</body>
</html>
